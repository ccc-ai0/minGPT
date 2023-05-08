"""
Full definition of a GPT Language Model, all of it in this single file.
(在此單一文件中，完整定義了 GPT 語言模型。)

References: (參考資料)
1) the official GPT-2 TensorFlow implementation released by OpenAI: (在此單一文件中，完整定義了 GPT 語言模型。)
https://github.com/openai/gpt-2/blob/master/src/model.py
2) huggingface/transformers PyTorch implementation: (huggingface/transformers 的 PyTorch 實現：)
https://github.com/huggingface/transformers/blob/main/src/transformers/models/gpt2/modeling_gpt2.py
"""

import math

import torch
import torch.nn as nn
from torch.nn import functional as F

from mingpt.utils import CfgNode as CN

# -----------------------------------------------------------------------------

class NewGELU(nn.Module):
    """
    Implementation of the GELU activation function currently in Google BERT repo (identical to OpenAI GPT).
    Reference: Gaussian Error Linear Units (GELU) paper: https://arxiv.org/abs/1606.08415
    """
    def forward(self, x):
        return 0.5 * x * (1.0 + torch.tanh(math.sqrt(2.0 / math.pi) * (x + 0.044715 * torch.pow(x, 3.0))))


class CausalSelfAttention(nn.Module):
    """
    A vanilla multi-head masked self-attention layer with a projection at the end.
    It is possible to use torch.nn.MultiheadAttention here but I am including an
    explicit implementation here to show that there is nothing too scary here.
    """
    """
    CausalSelfAttention 是一個多頭自注意力機制，這裡使用的是一個基本的線性轉換矩陣 (self.c_attn) 
    來得到 query, key, value 三個向量，然後將他們分割為多個頭，並進行矩陣運算來獲得多頭的輸出。
    具體來說，該模型在執行過程中，將輸入 x 進行線性轉換，分成 query, key, value 三個向量，
    再將它們分割成多個頭。然後，它使用遮罩來確保在計算注意力時，只會關注當前位置之前的部分。
    該模型計算出注意力值，並將注意力值乘以 value，這樣就得到了經過注意力機制後的輸出。最後，
    將這些輸出聚合在一起，再進行一個線性轉換，最終得到模型的輸出。值得注意的是，該模型在計算
    過程中使用了一些 dropout 正則化手段。
    """
    def __init__(self, config):
        super().__init__()
        assert config.n_embd % config.n_head == 0
        # key, query, value projections for all heads, but in a batch
        self.c_attn = nn.Linear(config.n_embd, 3 * config.n_embd)
        # output projection
        self.c_proj = nn.Linear(config.n_embd, config.n_embd)
        # regularization
        self.attn_dropout = nn.Dropout(config.attn_pdrop)
        self.resid_dropout = nn.Dropout(config.resid_pdrop)
        # causal mask to ensure that attention is only applied to the left in the input sequence
        self.register_buffer("bias", torch.tril(torch.ones(config.block_size, config.block_size))
                                     .view(1, 1, config.block_size, config.block_size))
        self.n_head = config.n_head
        self.n_embd = config.n_embd

    def forward(self, x):
        """
        這是一個執行自注意力機制（self-attention mechanism）的函數，
        用於一個 GPT 模型的一個子模塊中。

        輸入 x 是一個形狀為 (batch_size, sequence_length, embedding_dimensionality) 
        的張量，代表一個批次的序列，其中 embedding_dimensionality 是嵌入層的維度。
        這個函數將使用自注意力機制來為這些嵌入向量中的每個位置生成一個新的嵌入向量。

        這個函數首先使用一個線性變換 self.c_attn 將 x 轉換為一個形狀為 (batch_size, 
        sequence_length, 3 * embedding_dimensionality) 的張量。然後這個張量被拆分為
        三個形狀為 (batch_size, sequence_length, embedding_dimensionality) 
        的張量 q、k 和 v，代表自注意力機制中的查詢、鍵和值。

        接下來，這些張量 q、k 和 v 被切片並重新組合成多頭自注意力的形式，即分成 
        self.n_head 個頭，每個頭的嵌入向量維度為 C // self.n_head。這樣，每個頭
        都可以獨立地進行自注意力計算，然後將計算出的嵌入向量再次組合在一起。

        然後，函數計算自注意力矩陣 att，用於在所有位置之間計算注意力分數。注意力
        分數與鍵向量和查詢向量相乘後，經過緩慢的軟化函數（softmax）進行歸一化。
        然後使用這些注意力分數加權鍵向量，得到新的值向量。最後，函數使用線性變換
          self.c_proj 將新的值向量映射回原始嵌入維度，最終返回一個形狀為 
          (batch_size, sequence_length, embedding_dimensionality) 的張量。        
        """
        B, T, C = x.size() # batch size, sequence length, embedding dimensionality (n_embd)

        # calculate query, key, values for all heads in batch and move head forward to be the batch dim
        q, k ,v  = self.c_attn(x).split(self.n_embd, dim=2)
        k = k.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
        q = q.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)
        v = v.view(B, T, self.n_head, C // self.n_head).transpose(1, 2) # (B, nh, T, hs)

        # causal self-attention; Self-attend: (B, nh, T, hs) x (B, nh, hs, T) -> (B, nh, T, T)
        att = (q @ k.transpose(-2, -1)) * (1.0 / math.sqrt(k.size(-1)))
        att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf'))
        att = F.softmax(att, dim=-1)
        att = self.attn_dropout(att)
        y = att @ v # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
        y = y.transpose(1, 2).contiguous().view(B, T, C) # re-assemble all head outputs side by side

        # output projection
        y = self.resid_dropout(self.c_proj(y))
        return y

class Block(nn.Module):
    """ an unassuming Transformer block """

    """
    這是一個 Transformer block，由 self-attention 和 MLP 組成。在 forward 的時候，
    會先將輸入的 x 經過 LayerNorm 後，再經過 CausalSelfAttention。接著，再加上 x，
    再經過另一個 LayerNorm 後，再經過一個由 Linear、GELU 和 Dropout 組成的 MLP。
    最後，再加上原本的 x 後，就是這個 block 的輸出。其中，config.n_embd 是 
    embedding 的維度，config.resid_pdrop 是 dropout 的比例。
    """
    def __init__(self, config):
        super().__init__()
        self.ln_1 = nn.LayerNorm(config.n_embd)
        self.attn = CausalSelfAttention(config)
        self.ln_2 = nn.LayerNorm(config.n_embd)
        self.mlp = nn.ModuleDict(dict(
            c_fc    = nn.Linear(config.n_embd, 4 * config.n_embd),
            c_proj  = nn.Linear(4 * config.n_embd, config.n_embd),
            act     = NewGELU(),
            dropout = nn.Dropout(config.resid_pdrop),
        ))
        m = self.mlp
        self.mlpf = lambda x: m.dropout(m.c_proj(m.act(m.c_fc(x)))) # MLP forward

    def forward(self, x):
        x = x + self.attn(self.ln_1(x))
        x = x + self.mlpf(self.ln_2(x))
        return x


class GPT(nn.Module):
    """ GPT Language Model """

    """
    這是一個 PyTorch 的 GPT 語言模型，用於自然語言處理的應用。：

    1. get_default_config(): 回傳一個字典，包含這個模型預設的參數。
    2. __init__(self, config): 建立模型。輸入的 config 包含模型的參數，其中 vocab_size 和 block_size 是必要的參數。這個方法建立一個 Transformer 的網路結構，並且有一個 linear layer (lm_head) 做為輸出，用來預測下一個字。
    3. from_pretrained(cls, model_type): 載入已經訓練好的 GPT 模型，並且使用載入的參數初始化新的模型。該方法呼叫 huggingface/transformers 的函式，從事載入、初始化的工作。
    """
    @staticmethod
    def get_default_config():
        C = CN()
        # either model_type or (n_layer, n_head, n_embd) must be given in the config
        C.model_type = 'gpt'
        C.n_layer = None
        C.n_head = None
        C.n_embd =  None
        # these options must be filled in externally
        C.vocab_size = None
        C.block_size = None
        # dropout hyperparameters
        C.embd_pdrop = 0.1
        C.resid_pdrop = 0.1
        C.attn_pdrop = 0.1
        return C

    def __init__(self, config):
        super().__init__()
        assert config.vocab_size is not None
        assert config.block_size is not None
        self.block_size = config.block_size

        type_given = config.model_type is not None
        params_given = all([config.n_layer is not None, config.n_head is not None, config.n_embd is not None])
        assert type_given ^ params_given # exactly one of these (XOR)
        if type_given:
            # translate from model_type to detailed configuration
            config.merge_from_dict({
                # names follow the huggingface naming conventions
                # GPT-1
                'openai-gpt':   dict(n_layer=12, n_head=12, n_embd=768),  # 117M params
                # GPT-2 configs
                'gpt2':         dict(n_layer=12, n_head=12, n_embd=768),  # 124M params
                'gpt2-medium':  dict(n_layer=24, n_head=16, n_embd=1024), # 350M params
                'gpt2-large':   dict(n_layer=36, n_head=20, n_embd=1280), # 774M params
                'gpt2-xl':      dict(n_layer=48, n_head=25, n_embd=1600), # 1558M params
                # Gophers
                'gopher-44m':   dict(n_layer=8, n_head=16, n_embd=512),
                # (there are a number more...)
                # I made these tiny models up
                'gpt-mini':     dict(n_layer=6, n_head=6, n_embd=192),
                'gpt-micro':    dict(n_layer=4, n_head=4, n_embd=128),
                'gpt-nano':     dict(n_layer=3, n_head=3, n_embd=48),
            }[config.model_type])

        self.transformer = nn.ModuleDict(dict(
            wte = nn.Embedding(config.vocab_size, config.n_embd),
            wpe = nn.Embedding(config.block_size, config.n_embd),
            drop = nn.Dropout(config.embd_pdrop),
            h = nn.ModuleList([Block(config) for _ in range(config.n_layer)]),
            ln_f = nn.LayerNorm(config.n_embd),
        ))
        self.lm_head = nn.Linear(config.n_embd, config.vocab_size, bias=False)

        # init all weights, and apply a special scaled init to the residual projections, per GPT-2 paper
        self.apply(self._init_weights)
        for pn, p in self.named_parameters():
            if pn.endswith('c_proj.weight'):
                torch.nn.init.normal_(p, mean=0.0, std=0.02/math.sqrt(2 * config.n_layer))

        # report number of parameters (note we don't count the decoder parameters in lm_head)
        n_params = sum(p.numel() for p in self.transformer.parameters())
        print("number of parameters: %.2fM" % (n_params/1e6,))

    def _init_weights(self, module):
        if isinstance(module, nn.Linear):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
            if module.bias is not None:
                torch.nn.init.zeros_(module.bias)
        elif isinstance(module, nn.Embedding):
            torch.nn.init.normal_(module.weight, mean=0.0, std=0.02)
        elif isinstance(module, nn.LayerNorm):
            torch.nn.init.zeros_(module.bias)
            torch.nn.init.ones_(module.weight)

    @classmethod
    def from_pretrained(cls, model_type):
        """
        Initialize a pretrained GPT model by copying over the weights
        from a huggingface/transformers checkpoint.
        """
        assert model_type in {'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'}
        from transformers import GPT2LMHeadModel

        # create a from-scratch initialized minGPT model
        config = cls.get_default_config()
        config.model_type = model_type
        config.vocab_size = 50257 # openai's model vocabulary
        config.block_size = 1024  # openai's model block_size
        model = GPT(config)
        sd = model.state_dict()

        # init a huggingface/transformers model
        model_hf = GPT2LMHeadModel.from_pretrained(model_type)
        sd_hf = model_hf.state_dict()

        # copy while ensuring all of the parameters are aligned and match in names and shapes
        keys = [k for k in sd_hf if not k.endswith('attn.masked_bias')] # ignore these
        transposed = ['attn.c_attn.weight', 'attn.c_proj.weight', 'mlp.c_fc.weight', 'mlp.c_proj.weight']
        # basically the openai checkpoints use a "Conv1D" module, but we only want to use a vanilla nn.Linear.
        # this means that we have to transpose these weights when we import them
        assert len(keys) == len(sd)
        for k in keys:
            if any(k.endswith(w) for w in transposed):
                # special treatment for the Conv1D weights we need to transpose
                assert sd_hf[k].shape[::-1] == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k].t())
            else:
                # vanilla copy over the other parameters
                assert sd_hf[k].shape == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k])

        return model

    def configure_optimizers(self, train_config):
        """
        This long function is unfortunately doing something very simple and is being very defensive:
        We are separating out all parameters of the model into two buckets: those that will experience
        weight decay for regularization and those that won't (biases, and layernorm/embedding weights).
        We are then returning the PyTorch optimizer object.

        
        此函數將模型的所有參數分成兩個桶：一個桶會經歷權重衰減(weight decay)進行正則化，另一個桶不會
        (包括偏置和層規範化/嵌入權重)。然後，它將返回 PyTorch 優化器物件。函數內容包含以下幾個步驟：

        首先，它通過遍歷模型的每個模塊及其參數，將所有參數分成兩個集合：需要權重衰減的參數集合和不需要
        權重衰減的參數集合。
        
        接下來，它驗證是否考慮了每個參數，並確保沒有參數同時在兩個集合中出現。
        
        最後，它使用這些集合中的參數，創建一個 PyTorch 優化器物件(AdamW)，其中需要權重衰減的參數使用
        weight_decay參數進行正則化，不需要權重衰減的參數設置 weight_decay 參數為 0。

        此函數使用了PyTorch深度學習框架的常用優化技巧，可以通過對權重的調節來進行正則化，進而提高模型
        的泛化性能。
        """

        # separate out all parameters to those that will and won't experience regularizing weight decay
        decay = set()
        no_decay = set()
        whitelist_weight_modules = (torch.nn.Linear, )
        blacklist_weight_modules = (torch.nn.LayerNorm, torch.nn.Embedding)
        for mn, m in self.named_modules():
            for pn, p in m.named_parameters():
                fpn = '%s.%s' % (mn, pn) if mn else pn # full param name
                # random note: because named_modules and named_parameters are recursive
                # we will see the same tensors p many many times. but doing it this way
                # allows us to know which parent module any tensor p belongs to...
                if pn.endswith('bias'):
                    # all biases will not be decayed
                    no_decay.add(fpn)
                elif pn.endswith('weight') and isinstance(m, whitelist_weight_modules):
                    # weights of whitelist modules will be weight decayed
                    decay.add(fpn)
                elif pn.endswith('weight') and isinstance(m, blacklist_weight_modules):
                    # weights of blacklist modules will NOT be weight decayed
                    no_decay.add(fpn)

        # validate that we considered every parameter
        param_dict = {pn: p for pn, p in self.named_parameters()}
        inter_params = decay & no_decay
        union_params = decay | no_decay
        assert len(inter_params) == 0, "parameters %s made it into both decay/no_decay sets!" % (str(inter_params), )
        assert len(param_dict.keys() - union_params) == 0, "parameters %s were not separated into either decay/no_decay set!" \
                                                    % (str(param_dict.keys() - union_params), )

        # create the pytorch optimizer object
        optim_groups = [
            {"params": [param_dict[pn] for pn in sorted(list(decay))], "weight_decay": train_config.weight_decay},
            {"params": [param_dict[pn] for pn in sorted(list(no_decay))], "weight_decay": 0.0},
        ]
        optimizer = torch.optim.AdamW(optim_groups, lr=train_config.learning_rate, betas=train_config.betas)
        return optimizer


    def forward(self, idx, targets=None):
        """
        這段程式是一個 PyTorch 模型的前向傳播函式，該模型使用 GPT (Generative Pre-trained Transformer) 
        的架構。此函式的輸入是一個由整數索引構成的張量 idx，形狀為 (b, t)，其中 b 是批次大小，t 是每個
        序列的長度。如果給定了 targets 張量，代表需要計算損失，否則只回傳 logits 張量。程式中會先檢查 t 
        是否超過預設的 block_size，如果是就會拋出例外。然後會計算位置編碼的張量 pos，與 token embedding 
        張量 tok_emb 和位置 embedding 張量 pos_emb 相加後，經過經過一些 Transformer block，最後輸出 
        logits 張量。如果有 targets 張量，則會使用 F.cross_entropy 函式計算交叉熵損失。最後回傳 logits 
        張量和 loss 張量。
        """
        device = idx.device
        b, t = idx.size()
        assert t <= self.block_size, f"Cannot forward sequence of length {t}, block size is only {self.block_size}"
        pos = torch.arange(0, t, dtype=torch.long, device=device).unsqueeze(0) # shape (1, t)

        # forward the GPT model itself
        tok_emb = self.transformer.wte(idx) # token embeddings of shape (b, t, n_embd)
        pos_emb = self.transformer.wpe(pos) # position embeddings of shape (1, t, n_embd)
        x = self.transformer.drop(tok_emb + pos_emb)
        for block in self.transformer.h:
            x = block(x)
        x = self.transformer.ln_f(x)
        logits = self.lm_head(x)

        # if we are given some desired targets also calculate the loss
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1), ignore_index=-1)

        return logits, loss

    @torch.no_grad()
    def generate(self, idx, max_new_tokens, temperature=1.0, do_sample=False, top_k=None):
        """
        Take a conditioning sequence of indices idx (LongTensor of shape (b,t)) and complete
        the sequence max_new_tokens times, feeding the predictions back into the model each time.
        Most likely you'll want to make sure to be in model.eval() mode of operation for this.

        这是一个用于生成文本的函数，它采用了GPT模型的输出来生成新的token序列。该函数采用一个已知的
        token序列idx，然后在其中添加max_new_tokens个新的token，直到生成的新token序列的长度达到指定
        的max_new_tokens。函数的主要参数包括temperature、do_sample和top_k，这些参数控制了如何从
        GPT模型的输出中采样token，以及采样的数量。temperature控制了token采样时所使用的温度值，
        它可以控制token的随机性和多样性。do_sample参数控制是否使用采样的方式获取下一个token，
        如果为False，则使用概率最大的token。top_k参数控制从模型的输出中选择概率最大的k个token。
        函数的输出是一个新的token序列。
        """
        for _ in range(max_new_tokens):
            # if the sequence context is growing too long we must crop it at block_size
            idx_cond = idx if idx.size(1) <= self.block_size else idx[:, -self.block_size:]
            # forward the model to get the logits for the index in the sequence
            logits, _ = self(idx_cond)
            # pluck the logits at the final step and scale by desired temperature
            logits = logits[:, -1, :] / temperature
            # optionally crop the logits to only the top k options
            if top_k is not None:
                v, _ = torch.topk(logits, top_k)
                logits[logits < v[:, [-1]]] = -float('Inf')
            # apply softmax to convert logits to (normalized) probabilities
            probs = F.softmax(logits, dim=-1)
            # either sample from the distribution or take the most likely element
            if do_sample:
                idx_next = torch.multinomial(probs, num_samples=1)
            else:
                _, idx_next = torch.topk(probs, k=1, dim=-1)
            # append sampled index to the running sequence and continue
            idx = torch.cat((idx, idx_next), dim=1)

        return idx
