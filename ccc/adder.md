# adder.py

學習 n 位數加法，格式如 8550531 代表 85+50=135 (其中 135 表達格式反過來，變成 531， kaparthy 說這樣比較好讓 GPT 學)


```
    Creates n-digit addition problems. For example, if n=2, then an example
    addition problem would be to add 85 + 50 = 135. This problem would be
    represented as the following string for the GPT:

    "8550531"

    This is because:
    - we are discarding the + and =, which are not necessary. We just encode the digits
      of the input numbers concatenated together.
    - the result 135 is encoded backwards to make the addition easier to learn for the
      GPT model, because of how the addition algorithm works.

    As one more example, the problem 6 + 39 = 45 would be encoded as:

    "0639054"

    where you will notice that we are padding with zeros to make sure that we always
    produce strings of the exact same size: n + n + (n + 1). When n=2, this is 7.
    At test time, we will feed in an addition problem by giving the first 2n digits,
    and hoping that the GPT model completes the sequence with the next (n+1) digits
    correctly.
```

## 執行結果

```
$ python adder.py
system:
    seed: 3407
    work_dir: ./out/adder
data:
    ndigit: 2
model:
    model_type: gpt-nano
    n_layer: None
    n_head: None
    n_embd: None
    vocab_size: None
    block_size: None
    embd_pdrop: 0.1
    resid_pdrop: 0.1
    attn_pdrop: 0.1
trainer:
    device: auto
    num_workers: 4
    max_iters: None
    batch_size: 64
    learning_rate: 0.0005
    betas: (0.9, 0.95)
    weight_decay: 0.1
    grad_norm_clip: 1.0

number of parameters: 0.09M
running on device cpu
ccc: trainer running ....
iter_dt 0.00ms; iter 0: train loss 2.31638
GPT claims that 99 + 32 = 122 but gt is 131
GPT claims that 56 + 21 = 25 but gt is 77
GPT claims that 55 + 3 = 3 but gt is 58
GPT claims that 38 + 62 = 122 but gt is 100
GPT claims that 99 + 5 = 5 but gt is 104
train final score: 12/9500 = 0.13% correct
GPT claims that 74 + 15 = 25 but gt is 89
GPT claims that 77 + 27 = 0 but gt is 104
GPT claims that 88 + 28 = 3 but gt is 116
GPT claims that 10 + 2 = 22 but gt is 12
GPT claims that 23 + 7 = 3 but gt is 30
test final score: 0/500 = 0.00% correct
saving model with new top score of 12.0
iter_dt 78.12ms; iter 10: train loss 2.11295
iter_dt 113.30ms; iter 20: train loss 1.99540
iter_dt 93.75ms; iter 30: train loss 1.91904
iter_dt 78.12ms; iter 40: train loss 1.86133
iter_dt 93.75ms; iter 50: train loss 1.80097
iter_dt 78.13ms; iter 60: train loss 1.76190
iter_dt 78.13ms; iter 70: train loss 1.71448
iter_dt 109.38ms; iter 80: train loss 1.67259
iter_dt 109.38ms; iter 90: train loss 1.63653
iter_dt 125.00ms; iter 100: train loss 1.63268
iter_dt 78.12ms; iter 110: train loss 1.60675
iter_dt 93.75ms; iter 120: train loss 1.64297
iter_dt 127.00ms; iter 130: train loss 1.58015
iter_dt 137.58ms; iter 140: train loss 1.57161
iter_dt 93.75ms; iter 150: train loss 1.57671
iter_dt 93.75ms; iter 160: train loss 1.57750
iter_dt 95.75ms; iter 170: train loss 1.55459
iter_dt 93.75ms; iter 180: train loss 1.55171
iter_dt 109.38ms; iter 190: train loss 1.55128
iter_dt 125.01ms; iter 200: train loss 1.54185
iter_dt 128.01ms; iter 210: train loss 1.53900
iter_dt 132.01ms; iter 220: train loss 1.55610
iter_dt 149.01ms; iter 230: train loss 1.54526
iter_dt 190.01ms; iter 240: train loss 1.55012
iter_dt 130.01ms; iter 250: train loss 1.52256
iter_dt 93.75ms; iter 260: train loss 1.54641
iter_dt 112.77ms; iter 270: train loss 1.54045
iter_dt 93.75ms; iter 280: train loss 1.54621
iter_dt 109.37ms; iter 290: train loss 1.54574
iter_dt 100.71ms; iter 300: train loss 1.53262
iter_dt 140.62ms; iter 310: train loss 1.55578
iter_dt 93.75ms; iter 320: train loss 1.52418
iter_dt 93.75ms; iter 330: train loss 1.54038
iter_dt 78.13ms; iter 340: train loss 1.52488
iter_dt 101.74ms; iter 350: train loss 1.52616
iter_dt 93.75ms; iter 360: train loss 1.50668
iter_dt 98.20ms; iter 370: train loss 1.48661
iter_dt 109.38ms; iter 380: train loss 1.48263
iter_dt 93.75ms; iter 390: train loss 1.47087
iter_dt 133.72ms; iter 400: train loss 1.48830
iter_dt 109.38ms; iter 410: train loss 1.47406
iter_dt 79.60ms; iter 420: train loss 1.51491
iter_dt 89.09ms; iter 430: train loss 1.44892
iter_dt 78.12ms; iter 440: train loss 1.40866
iter_dt 93.75ms; iter 450: train loss 1.31425
iter_dt 82.45ms; iter 460: train loss 1.38047
iter_dt 93.75ms; iter 470: train loss 1.32637
iter_dt 93.75ms; iter 480: train loss 1.36430
iter_dt 93.75ms; iter 490: train loss 1.33740
iter_dt 78.12ms; iter 500: train loss 1.32524
GPT claims that 99 + 32 = 110 but gt is 131
GPT claims that 56 + 21 = 67 but gt is 77
GPT claims that 55 + 3 = 74 but gt is 58
GPT claims that 38 + 62 = 110 but gt is 100
GPT claims that 99 + 5 = 114 but gt is 104
train final score: 556/9500 = 5.85% correct
GPT claims that 74 + 15 = 99 but gt is 89
GPT claims that 77 + 27 = 117 but gt is 104
GPT claims that 88 + 28 = 117 but gt is 116
GPT claims that 10 + 2 = 9 but gt is 12
GPT claims that 23 + 7 = 11 but gt is 30
test final score: 29/500 = 5.80% correct
saving model with new top score of 585.0
iter_dt 156.01ms; iter 510: train loss 1.30597
iter_dt 94.70ms; iter 520: train loss 1.29637
iter_dt 83.59ms; iter 530: train loss 1.21291
iter_dt 93.75ms; iter 540: train loss 1.18682
iter_dt 93.75ms; iter 550: train loss 1.17514
iter_dt 116.01ms; iter 560: train loss 1.20741
iter_dt 101.70ms; iter 570: train loss 1.18084
iter_dt 78.13ms; iter 580: train loss 1.23697
iter_dt 93.75ms; iter 590: train loss 1.14956
iter_dt 126.47ms; iter 600: train loss 1.15870
iter_dt 78.12ms; iter 610: train loss 1.11332
iter_dt 93.75ms; iter 620: train loss 1.14188
iter_dt 93.75ms; iter 630: train loss 1.01487
iter_dt 78.13ms; iter 640: train loss 1.09797
iter_dt 78.12ms; iter 650: train loss 1.05196
iter_dt 78.12ms; iter 660: train loss 1.08967
iter_dt 78.12ms; iter 670: train loss 0.99406
iter_dt 109.73ms; iter 680: train loss 1.04309
iter_dt 93.75ms; iter 690: train loss 1.03132
iter_dt 106.01ms; iter 700: train loss 1.01585
iter_dt 93.75ms; iter 710: train loss 0.94242
iter_dt 79.77ms; iter 720: train loss 0.96692
iter_dt 78.12ms; iter 730: train loss 0.96309
iter_dt 93.75ms; iter 740: train loss 0.86324
iter_dt 89.92ms; iter 750: train loss 0.89530
iter_dt 93.75ms; iter 760: train loss 0.91291
iter_dt 90.04ms; iter 770: train loss 0.85752
iter_dt 95.27ms; iter 780: train loss 0.83805
iter_dt 78.13ms; iter 790: train loss 0.90640
iter_dt 96.97ms; iter 800: train loss 0.82929
iter_dt 93.75ms; iter 810: train loss 0.86478
iter_dt 80.67ms; iter 820: train loss 0.77797
iter_dt 93.75ms; iter 830: train loss 0.85105
iter_dt 85.85ms; iter 840: train loss 0.80400
iter_dt 105.41ms; iter 850: train loss 0.77763
iter_dt 79.58ms; iter 860: train loss 0.72661
iter_dt 93.75ms; iter 870: train loss 0.80811
iter_dt 93.75ms; iter 880: train loss 0.82757
iter_dt 79.67ms; iter 890: train loss 0.78332
iter_dt 93.75ms; iter 900: train loss 0.68360
iter_dt 93.75ms; iter 910: train loss 0.77852
iter_dt 93.75ms; iter 920: train loss 0.72706
iter_dt 95.55ms; iter 930: train loss 0.66349
iter_dt 94.95ms; iter 940: train loss 0.71811
iter_dt 105.56ms; iter 950: train loss 0.71086
iter_dt 90.99ms; iter 960: train loss 0.65842
iter_dt 80.57ms; iter 970: train loss 0.68273
iter_dt 79.64ms; iter 980: train loss 0.66183
iter_dt 93.75ms; iter 990: train loss 0.66593
iter_dt 125.00ms; iter 1000: train loss 0.62973
GPT claims that 99 + 5 = 94 but gt is 104
GPT claims that 96 + 20 = 126 but gt is 116
GPT claims that 52 + 69 = 111 but gt is 121
GPT claims that 79 + 29 = 98 but gt is 108
GPT claims that 33 + 17 = 40 but gt is 50
train final score: 4839/9500 = 50.94% correct
GPT claims that 77 + 27 = 94 but gt is 104
GPT claims that 88 + 28 = 106 but gt is 116
GPT claims that 10 + 2 = 11 but gt is 12
GPT claims that 23 + 7 = 20 but gt is 30
GPT claims that 5 + 98 = 93 but gt is 103
test final score: 254/500 = 50.80% correct
saving model with new top score of 5093.0
iter_dt 84.57ms; iter 1010: train loss 0.59089
iter_dt 78.13ms; iter 1020: train loss 0.65254
iter_dt 78.13ms; iter 1030: train loss 0.59603
iter_dt 93.75ms; iter 1040: train loss 0.66563
iter_dt 93.75ms; iter 1050: train loss 0.57807
iter_dt 86.97ms; iter 1060: train loss 0.56578
iter_dt 78.13ms; iter 1070: train loss 0.62336
iter_dt 76.56ms; iter 1080: train loss 0.51491
iter_dt 78.12ms; iter 1090: train loss 0.56762
iter_dt 79.56ms; iter 1100: train loss 0.51768
iter_dt 95.27ms; iter 1110: train loss 0.52200
iter_dt 86.65ms; iter 1120: train loss 0.51638
iter_dt 99.01ms; iter 1130: train loss 0.52968
iter_dt 109.01ms; iter 1140: train loss 0.57174
iter_dt 101.13ms; iter 1150: train loss 0.51491
iter_dt 78.13ms; iter 1160: train loss 0.52642
iter_dt 78.13ms; iter 1170: train loss 0.51875
iter_dt 93.75ms; iter 1180: train loss 0.46740
iter_dt 113.33ms; iter 1190: train loss 0.45916
iter_dt 93.75ms; iter 1200: train loss 0.46326
iter_dt 78.12ms; iter 1210: train loss 0.49658
iter_dt 78.12ms; iter 1220: train loss 0.44731
iter_dt 128.01ms; iter 1230: train loss 0.41931
iter_dt 93.75ms; iter 1240: train loss 0.41770
iter_dt 78.12ms; iter 1250: train loss 0.40500
iter_dt 93.75ms; iter 1260: train loss 0.49146
iter_dt 92.33ms; iter 1270: train loss 0.41973
iter_dt 93.75ms; iter 1280: train loss 0.37697
iter_dt 93.75ms; iter 1290: train loss 0.37440
iter_dt 78.13ms; iter 1300: train loss 0.42253
iter_dt 93.75ms; iter 1310: train loss 0.34133
iter_dt 93.75ms; iter 1320: train loss 0.34752
iter_dt 78.12ms; iter 1330: train loss 0.45639
iter_dt 93.75ms; iter 1340: train loss 0.37109
iter_dt 89.44ms; iter 1350: train loss 0.47023
iter_dt 78.12ms; iter 1360: train loss 0.38458
iter_dt 93.75ms; iter 1370: train loss 0.37544
iter_dt 93.75ms; iter 1380: train loss 0.35630
iter_dt 78.13ms; iter 1390: train loss 0.36620
iter_dt 93.75ms; iter 1400: train loss 0.29998
iter_dt 93.56ms; iter 1410: train loss 0.31551
iter_dt 93.75ms; iter 1420: train loss 0.29671
iter_dt 93.75ms; iter 1430: train loss 0.31640
iter_dt 109.38ms; iter 1440: train loss 0.39569
iter_dt 93.75ms; iter 1450: train loss 0.30033
iter_dt 115.41ms; iter 1460: train loss 0.30161
iter_dt 218.22ms; iter 1470: train loss 0.32158
iter_dt 111.40ms; iter 1480: train loss 0.27380
iter_dt 93.75ms; iter 1490: train loss 0.32554
iter_dt 78.12ms; iter 1500: train loss 0.25572
GPT claims that 38 + 62 = 90 but gt is 100
GPT claims that 97 + 79 = 166 but gt is 176
GPT claims that 66 + 89 = 145 but gt is 155
GPT claims that 29 + 10 = 49 but gt is 39
GPT claims that 49 + 68 = 107 but gt is 117
train final score: 9216/9500 = 97.01% correct
GPT claims that 56 + 45 = 91 but gt is 101
GPT claims that 89 + 67 = 146 but gt is 156
GPT claims that 36 + 66 = 92 but gt is 102
GPT claims that 49 + 51 = 90 but gt is 100
GPT claims that 78 + 78 = 146 but gt is 156
test final score: 485/500 = 97.00% correct
saving model with new top score of 9701.0
iter_dt 138.01ms; iter 1510: train loss 0.34399
iter_dt 124.01ms; iter 1520: train loss 0.36643
iter_dt 87.46ms; iter 1530: train loss 0.29542
iter_dt 99.95ms; iter 1540: train loss 0.23638
iter_dt 93.75ms; iter 1550: train loss 0.33336
iter_dt 78.13ms; iter 1560: train loss 0.27076
iter_dt 78.13ms; iter 1570: train loss 0.22642
iter_dt 93.75ms; iter 1580: train loss 0.28436
iter_dt 187.01ms; iter 1590: train loss 0.25968
iter_dt 93.75ms; iter 1600: train loss 0.27403
iter_dt 84.99ms; iter 1610: train loss 0.30768
iter_dt 110.80ms; iter 1620: train loss 0.32491
iter_dt 93.75ms; iter 1630: train loss 0.28655
iter_dt 93.75ms; iter 1640: train loss 0.31148
iter_dt 88.84ms; iter 1650: train loss 0.32381
iter_dt 93.75ms; iter 1660: train loss 0.25071
iter_dt 98.46ms; iter 1670: train loss 0.27372
iter_dt 78.13ms; iter 1680: train loss 0.23467
iter_dt 78.12ms; iter 1690: train loss 0.25026
iter_dt 85.20ms; iter 1700: train loss 0.23554
iter_dt 83.42ms; iter 1710: train loss 0.23321
iter_dt 93.75ms; iter 1720: train loss 0.29537
iter_dt 78.12ms; iter 1730: train loss 0.23742
iter_dt 95.16ms; iter 1740: train loss 0.22388
iter_dt 78.12ms; iter 1750: train loss 0.22410
iter_dt 84.15ms; iter 1760: train loss 0.30951
iter_dt 91.90ms; iter 1770: train loss 0.24145
iter_dt 126.29ms; iter 1780: train loss 0.24496
iter_dt 95.56ms; iter 1790: train loss 0.24143
iter_dt 79.50ms; iter 1800: train loss 0.30907
iter_dt 78.13ms; iter 1810: train loss 0.22948
iter_dt 78.12ms; iter 1820: train loss 0.25664
iter_dt 93.75ms; iter 1830: train loss 0.19517
iter_dt 93.75ms; iter 1840: train loss 0.23098
iter_dt 109.01ms; iter 1850: train loss 0.17151
iter_dt 86.95ms; iter 1860: train loss 0.20929
iter_dt 78.13ms; iter 1870: train loss 0.26307
iter_dt 93.75ms; iter 1880: train loss 0.18567
iter_dt 95.51ms; iter 1890: train loss 0.22272
iter_dt 78.13ms; iter 1900: train loss 0.22547
iter_dt 93.75ms; iter 1910: train loss 0.16552
iter_dt 99.06ms; iter 1920: train loss 0.21711
iter_dt 93.75ms; iter 1930: train loss 0.19345
iter_dt 79.61ms; iter 1940: train loss 0.17743
iter_dt 113.01ms; iter 1950: train loss 0.19215
iter_dt 93.75ms; iter 1960: train loss 0.15691
iter_dt 78.13ms; iter 1970: train loss 0.17783
iter_dt 75.96ms; iter 1980: train loss 0.19171
iter_dt 72.60ms; iter 1990: train loss 0.14473
iter_dt 97.73ms; iter 2000: train loss 0.21612
GPT claims that 80 + 90 = 180 but gt is 170
GPT claims that 79 + 39 = 108 but gt is 118
GPT claims that 89 + 51 = 130 but gt is 140
GPT claims that 87 + 57 = 134 but gt is 144
GPT claims that 80 + 0 = 90 but gt is 80
train final score: 9444/9500 = 99.41% correct
GPT claims that 12 + 29 = 31 but gt is 41
GPT claims that 21 + 29 = 40 but gt is 50
GPT claims that 88 + 57 = 135 but gt is 145
test final score: 497/500 = 99.40% correct
saving model with new top score of 9941.0
iter_dt 79.56ms; iter 2010: train loss 0.14617
iter_dt 87.36ms; iter 2020: train loss 0.17185
iter_dt 85.88ms; iter 2030: train loss 0.20251
iter_dt 100.00ms; iter 2040: train loss 0.14769
iter_dt 102.11ms; iter 2050: train loss 0.18194
iter_dt 93.06ms; iter 2060: train loss 0.22908
iter_dt 76.95ms; iter 2070: train loss 0.13382
iter_dt 97.01ms; iter 2080: train loss 0.11185
iter_dt 95.14ms; iter 2090: train loss 0.11884
iter_dt 93.75ms; iter 2100: train loss 0.18312
iter_dt 92.64ms; iter 2110: train loss 0.14437
iter_dt 101.75ms; iter 2120: train loss 0.12824
iter_dt 83.97ms; iter 2130: train loss 0.16926
iter_dt 93.75ms; iter 2140: train loss 0.10485
iter_dt 95.18ms; iter 2150: train loss 0.15536
iter_dt 79.98ms; iter 2160: train loss 0.15206
iter_dt 93.58ms; iter 2170: train loss 0.11600
iter_dt 149.01ms; iter 2180: train loss 0.15721
iter_dt 78.12ms; iter 2190: train loss 0.11873
iter_dt 112.00ms; iter 2200: train loss 0.10617
iter_dt 93.75ms; iter 2210: train loss 0.18747
iter_dt 78.13ms; iter 2220: train loss 0.13524
iter_dt 80.37ms; iter 2230: train loss 0.12195
iter_dt 95.01ms; iter 2240: train loss 0.17157
iter_dt 99.01ms; iter 2250: train loss 0.12308
iter_dt 93.69ms; iter 2260: train loss 0.13880
iter_dt 102.01ms; iter 2270: train loss 0.12094
iter_dt 78.12ms; iter 2280: train loss 0.15843
iter_dt 97.01ms; iter 2290: train loss 0.14392
iter_dt 132.01ms; iter 2300: train loss 0.19432
iter_dt 129.01ms; iter 2310: train loss 0.11553
iter_dt 98.44ms; iter 2320: train loss 0.09520
iter_dt 96.14ms; iter 2330: train loss 0.16911
iter_dt 101.72ms; iter 2340: train loss 0.13024
iter_dt 122.48ms; iter 2350: train loss 0.10567
iter_dt 96.01ms; iter 2360: train loss 0.08651
iter_dt 92.66ms; iter 2370: train loss 0.11243
iter_dt 125.01ms; iter 2380: train loss 0.19281
iter_dt 143.92ms; iter 2390: train loss 0.08740
iter_dt 88.34ms; iter 2400: train loss 0.17504
iter_dt 89.18ms; iter 2410: train loss 0.12555
iter_dt 127.62ms; iter 2420: train loss 0.15936
iter_dt 136.01ms; iter 2430: train loss 0.13942
iter_dt 107.09ms; iter 2440: train loss 0.12105
iter_dt 94.01ms; iter 2450: train loss 0.08969
iter_dt 83.98ms; iter 2460: train loss 0.15089
iter_dt 421.03ms; iter 2470: train loss 0.09619
iter_dt 92.10ms; iter 2480: train loss 0.10217
iter_dt 93.04ms; iter 2490: train loss 0.16331
iter_dt 99.03ms; iter 2500: train loss 0.14393
GPT claims that 50 + 50 = 110 but gt is 100
GPT claims that 56 + 50 = 116 but gt is 106
GPT claims that 86 + 16 = 92 but gt is 102
GPT claims that 57 + 50 = 117 but gt is 107
train final score: 9496/9500 = 99.96% correct
test final score: 500/500 = 100.00% correct
saving model with new top score of 9996.0
iter_dt 91.45ms; iter 2510: train loss 0.13034
iter_dt 108.21ms; iter 2520: train loss 0.14321
iter_dt 91.48ms; iter 2530: train loss 0.10184
iter_dt 90.65ms; iter 2540: train loss 0.13224
iter_dt 84.46ms; iter 2550: train loss 0.17450
iter_dt 72.59ms; iter 2560: train loss 0.10096
iter_dt 77.96ms; iter 2570: train loss 0.08858
iter_dt 83.21ms; iter 2580: train loss 0.13343
iter_dt 78.13ms; iter 2590: train loss 0.11788
iter_dt 79.57ms; iter 2600: train loss 0.09665
iter_dt 93.75ms; iter 2610: train loss 0.10982
iter_dt 122.01ms; iter 2620: train loss 0.08911
iter_dt 88.05ms; iter 2630: train loss 0.11789
iter_dt 152.21ms; iter 2640: train loss 0.07900
iter_dt 199.91ms; iter 2650: train loss 0.10303
iter_dt 136.09ms; iter 2660: train loss 0.08702
iter_dt 477.03ms; iter 2670: train loss 0.13690
iter_dt 104.40ms; iter 2680: train loss 0.07189
iter_dt 78.13ms; iter 2690: train loss 0.06462
iter_dt 99.76ms; iter 2700: train loss 0.09322
iter_dt 79.42ms; iter 2710: train loss 0.08504
iter_dt 109.00ms; iter 2720: train loss 0.09370
iter_dt 124.95ms; iter 2730: train loss 0.05533
iter_dt 134.33ms; iter 2740: train loss 0.06555
iter_dt 93.69ms; iter 2750: train loss 0.15509
iter_dt 126.32ms; iter 2760: train loss 0.16152
iter_dt 118.01ms; iter 2770: train loss 0.06202
iter_dt 111.66ms; iter 2780: train loss 0.06237
iter_dt 129.79ms; iter 2790: train loss 0.10509
iter_dt 102.13ms; iter 2800: train loss 0.13094
iter_dt 95.06ms; iter 2810: train loss 0.11350
iter_dt 127.01ms; iter 2820: train loss 0.10824
iter_dt 100.70ms; iter 2830: train loss 0.09200
iter_dt 93.75ms; iter 2840: train loss 0.14601
iter_dt 84.32ms; iter 2850: train loss 0.09866
iter_dt 78.13ms; iter 2860: train loss 0.07083
iter_dt 77.95ms; iter 2870: train loss 0.09324
iter_dt 95.64ms; iter 2880: train loss 0.09494
iter_dt 93.75ms; iter 2890: train loss 0.06882
iter_dt 78.13ms; iter 2900: train loss 0.10926
iter_dt 105.05ms; iter 2910: train loss 0.06880
iter_dt 93.75ms; iter 2920: train loss 0.07234
iter_dt 126.45ms; iter 2930: train loss 0.05460
iter_dt 93.75ms; iter 2940: train loss 0.08312
iter_dt 78.13ms; iter 2950: train loss 0.06341
iter_dt 95.49ms; iter 2960: train loss 0.06946
iter_dt 93.75ms; iter 2970: train loss 0.13818
iter_dt 78.12ms; iter 2980: train loss 0.12696
iter_dt 93.75ms; iter 2990: train loss 0.08148
iter_dt 99.32ms; iter 3000: train loss 0.09389
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
saving model with new top score of 10000.0
iter_dt 93.75ms; iter 3010: train loss 0.06687
iter_dt 93.75ms; iter 3020: train loss 0.05426
iter_dt 93.75ms; iter 3030: train loss 0.09911
iter_dt 93.75ms; iter 3040: train loss 0.04762
iter_dt 95.16ms; iter 3050: train loss 0.11495
iter_dt 93.75ms; iter 3060: train loss 0.07137
iter_dt 78.13ms; iter 3070: train loss 0.05012
iter_dt 93.75ms; iter 3080: train loss 0.13542
iter_dt 93.75ms; iter 3090: train loss 0.05090
iter_dt 73.78ms; iter 3100: train loss 0.06384
iter_dt 78.12ms; iter 3110: train loss 0.05857
iter_dt 87.19ms; iter 3120: train loss 0.08495
iter_dt 109.38ms; iter 3130: train loss 0.08790
iter_dt 93.75ms; iter 3140: train loss 0.11438
iter_dt 78.13ms; iter 3150: train loss 0.04521
iter_dt 78.13ms; iter 3160: train loss 0.08625
iter_dt 93.75ms; iter 3170: train loss 0.06468
iter_dt 93.75ms; iter 3180: train loss 0.04193
iter_dt 95.30ms; iter 3190: train loss 0.09145
iter_dt 78.13ms; iter 3200: train loss 0.03651
iter_dt 87.86ms; iter 3210: train loss 0.06591
iter_dt 78.12ms; iter 3220: train loss 0.04434
iter_dt 93.75ms; iter 3230: train loss 0.07653
iter_dt 79.95ms; iter 3240: train loss 0.05930
iter_dt 93.75ms; iter 3250: train loss 0.06308
iter_dt 93.75ms; iter 3260: train loss 0.03513
iter_dt 93.75ms; iter 3270: train loss 0.07078
iter_dt 78.12ms; iter 3280: train loss 0.04112
iter_dt 93.75ms; iter 3290: train loss 0.11880
iter_dt 146.69ms; iter 3300: train loss 0.07557
iter_dt 76.56ms; iter 3310: train loss 0.03399
iter_dt 93.75ms; iter 3320: train loss 0.12261
iter_dt 94.89ms; iter 3330: train loss 0.07186
iter_dt 93.75ms; iter 3340: train loss 0.03516
iter_dt 91.36ms; iter 3350: train loss 0.08994
iter_dt 95.26ms; iter 3360: train loss 0.06177
iter_dt 93.75ms; iter 3370: train loss 0.06039
iter_dt 93.75ms; iter 3380: train loss 0.09601
iter_dt 78.12ms; iter 3390: train loss 0.06704
iter_dt 93.75ms; iter 3400: train loss 0.04884
iter_dt 78.12ms; iter 3410: train loss 0.06048
iter_dt 93.75ms; iter 3420: train loss 0.07105
iter_dt 88.35ms; iter 3430: train loss 0.04955
iter_dt 78.13ms; iter 3440: train loss 0.06911
iter_dt 93.75ms; iter 3450: train loss 0.06714
iter_dt 78.13ms; iter 3460: train loss 0.03906
iter_dt 93.75ms; iter 3470: train loss 0.07050
iter_dt 96.01ms; iter 3480: train loss 0.09359
iter_dt 93.75ms; iter 3490: train loss 0.07778
iter_dt 118.33ms; iter 3500: train loss 0.05254
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 92.35ms; iter 3510: train loss 0.04565
iter_dt 100.30ms; iter 3520: train loss 0.05861
iter_dt 78.13ms; iter 3530: train loss 0.04078
iter_dt 99.19ms; iter 3540: train loss 0.03834
iter_dt 93.97ms; iter 3550: train loss 0.04378
iter_dt 82.69ms; iter 3560: train loss 0.07814
iter_dt 90.78ms; iter 3570: train loss 0.05525
iter_dt 87.95ms; iter 3580: train loss 0.09319
iter_dt 95.05ms; iter 3590: train loss 0.04723
iter_dt 108.14ms; iter 3600: train loss 0.07101
iter_dt 93.75ms; iter 3610: train loss 0.05483
iter_dt 99.11ms; iter 3620: train loss 0.04797
iter_dt 89.24ms; iter 3630: train loss 0.05056
iter_dt 78.13ms; iter 3640: train loss 0.02592
iter_dt 76.94ms; iter 3650: train loss 0.07788
iter_dt 88.56ms; iter 3660: train loss 0.07870
iter_dt 83.20ms; iter 3670: train loss 0.06536
iter_dt 116.01ms; iter 3680: train loss 0.03334
iter_dt 98.37ms; iter 3690: train loss 0.05505
iter_dt 94.57ms; iter 3700: train loss 0.05442
iter_dt 93.75ms; iter 3710: train loss 0.03412
iter_dt 99.31ms; iter 3720: train loss 0.05391
iter_dt 104.10ms; iter 3730: train loss 0.04140
iter_dt 79.81ms; iter 3740: train loss 0.03362
iter_dt 78.01ms; iter 3750: train loss 0.07167
iter_dt 85.58ms; iter 3760: train loss 0.04209
iter_dt 93.75ms; iter 3770: train loss 0.05922
iter_dt 81.58ms; iter 3780: train loss 0.04983
iter_dt 93.41ms; iter 3790: train loss 0.05592
iter_dt 93.75ms; iter 3800: train loss 0.04696
iter_dt 78.12ms; iter 3810: train loss 0.05087
iter_dt 97.01ms; iter 3820: train loss 0.03486
iter_dt 147.37ms; iter 3830: train loss 0.06132
iter_dt 72.32ms; iter 3840: train loss 0.04383
iter_dt 93.75ms; iter 3850: train loss 0.04906
iter_dt 90.22ms; iter 3860: train loss 0.03652
iter_dt 91.34ms; iter 3870: train loss 0.06342
iter_dt 88.45ms; iter 3880: train loss 0.05932
iter_dt 93.75ms; iter 3890: train loss 0.03410
iter_dt 87.38ms; iter 3900: train loss 0.08786
iter_dt 84.57ms; iter 3910: train loss 0.05092
iter_dt 79.95ms; iter 3920: train loss 0.04283
iter_dt 78.12ms; iter 3930: train loss 0.02651
iter_dt 93.75ms; iter 3940: train loss 0.03009
iter_dt 108.86ms; iter 3950: train loss 0.02443
iter_dt 114.08ms; iter 3960: train loss 0.02875
iter_dt 90.77ms; iter 3970: train loss 0.07154
iter_dt 147.00ms; iter 3980: train loss 0.03815
iter_dt 115.03ms; iter 3990: train loss 0.03083
iter_dt 142.97ms; iter 4000: train loss 0.03637
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 100.01ms; iter 4010: train loss 0.06628
iter_dt 129.01ms; iter 4020: train loss 0.06193
iter_dt 108.33ms; iter 4030: train loss 0.05253
iter_dt 94.23ms; iter 4040: train loss 0.09106
iter_dt 78.13ms; iter 4050: train loss 0.04322
iter_dt 93.75ms; iter 4060: train loss 0.06273
iter_dt 87.08ms; iter 4070: train loss 0.03871
iter_dt 109.01ms; iter 4080: train loss 0.02993
iter_dt 109.38ms; iter 4090: train loss 0.03896
iter_dt 93.75ms; iter 4100: train loss 0.07508
iter_dt 96.88ms; iter 4110: train loss 0.06005
iter_dt 88.43ms; iter 4120: train loss 0.04289
iter_dt 117.01ms; iter 4130: train loss 0.03670
iter_dt 96.88ms; iter 4140: train loss 0.08593
iter_dt 92.20ms; iter 4150: train loss 0.04719
iter_dt 93.75ms; iter 4160: train loss 0.10326
iter_dt 121.01ms; iter 4170: train loss 0.05862
iter_dt 93.75ms; iter 4180: train loss 0.02275
iter_dt 78.13ms; iter 4190: train loss 0.05487
iter_dt 78.13ms; iter 4200: train loss 0.05547
iter_dt 79.68ms; iter 4210: train loss 0.06911
iter_dt 113.37ms; iter 4220: train loss 0.03785
iter_dt 94.32ms; iter 4230: train loss 0.05640
iter_dt 99.71ms; iter 4240: train loss 0.04952
iter_dt 116.01ms; iter 4250: train loss 0.06524
iter_dt 93.07ms; iter 4260: train loss 0.02686
iter_dt 101.01ms; iter 4270: train loss 0.01866
iter_dt 98.00ms; iter 4280: train loss 0.04611
iter_dt 93.96ms; iter 4290: train loss 0.02235
iter_dt 82.80ms; iter 4300: train loss 0.06901
iter_dt 110.90ms; iter 4310: train loss 0.06675
iter_dt 109.38ms; iter 4320: train loss 0.04456
iter_dt 114.81ms; iter 4330: train loss 0.03250
iter_dt 92.96ms; iter 4340: train loss 0.03817
iter_dt 102.20ms; iter 4350: train loss 0.02485
iter_dt 93.75ms; iter 4360: train loss 0.04544
iter_dt 93.75ms; iter 4370: train loss 0.07889
iter_dt 86.57ms; iter 4380: train loss 0.01915
iter_dt 109.12ms; iter 4390: train loss 0.01986
iter_dt 93.75ms; iter 4400: train loss 0.01588
iter_dt 91.47ms; iter 4410: train loss 0.03631
iter_dt 78.13ms; iter 4420: train loss 0.04002
iter_dt 93.75ms; iter 4430: train loss 0.03929
iter_dt 83.86ms; iter 4440: train loss 0.04220
iter_dt 93.75ms; iter 4450: train loss 0.01355
iter_dt 92.30ms; iter 4460: train loss 0.02474
iter_dt 74.37ms; iter 4470: train loss 0.06596
iter_dt 91.01ms; iter 4480: train loss 0.04693
iter_dt 90.62ms; iter 4490: train loss 0.06210
iter_dt 78.13ms; iter 4500: train loss 0.02417
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 97.01ms; iter 4510: train loss 0.13434
iter_dt 97.62ms; iter 4520: train loss 0.03150
iter_dt 78.12ms; iter 4530: train loss 0.02762
iter_dt 77.58ms; iter 4540: train loss 0.03569
iter_dt 96.12ms; iter 4550: train loss 0.00818
iter_dt 93.75ms; iter 4560: train loss 0.08760
iter_dt 78.13ms; iter 4570: train loss 0.04513
iter_dt 92.20ms; iter 4580: train loss 0.01726
iter_dt 77.97ms; iter 4590: train loss 0.07774
iter_dt 78.12ms; iter 4600: train loss 0.06691
iter_dt 89.56ms; iter 4610: train loss 0.02171
iter_dt 78.12ms; iter 4620: train loss 0.08311
iter_dt 78.12ms; iter 4630: train loss 0.01841
iter_dt 79.96ms; iter 4640: train loss 0.02997
iter_dt 98.07ms; iter 4650: train loss 0.05106
iter_dt 93.75ms; iter 4660: train loss 0.03457
iter_dt 78.12ms; iter 4670: train loss 0.02881
iter_dt 100.16ms; iter 4680: train loss 0.03024
iter_dt 74.33ms; iter 4690: train loss 0.05073
iter_dt 93.75ms; iter 4700: train loss 0.05676
iter_dt 89.93ms; iter 4710: train loss 0.00779
iter_dt 78.14ms; iter 4720: train loss 0.01446
iter_dt 102.01ms; iter 4730: train loss 0.02666
iter_dt 127.16ms; iter 4740: train loss 0.02160
iter_dt 78.13ms; iter 4750: train loss 0.02839
iter_dt 82.68ms; iter 4760: train loss 0.04082
iter_dt 78.12ms; iter 4770: train loss 0.03141
iter_dt 94.00ms; iter 4780: train loss 0.03060
iter_dt 93.75ms; iter 4790: train loss 0.04694
iter_dt 93.75ms; iter 4800: train loss 0.02542
iter_dt 88.60ms; iter 4810: train loss 0.04130
iter_dt 93.75ms; iter 4820: train loss 0.05722
iter_dt 80.97ms; iter 4830: train loss 0.05029
iter_dt 86.99ms; iter 4840: train loss 0.03670
iter_dt 78.13ms; iter 4850: train loss 0.10149
iter_dt 93.75ms; iter 4860: train loss 0.01509
iter_dt 79.40ms; iter 4870: train loss 0.02182
iter_dt 86.96ms; iter 4880: train loss 0.01623
iter_dt 105.18ms; iter 4890: train loss 0.05555
iter_dt 93.75ms; iter 4900: train loss 0.04578
iter_dt 96.38ms; iter 4910: train loss 0.02341
iter_dt 100.86ms; iter 4920: train loss 0.04322
iter_dt 78.12ms; iter 4930: train loss 0.01890
iter_dt 84.72ms; iter 4940: train loss 0.05311
iter_dt 83.62ms; iter 4950: train loss 0.03730
iter_dt 95.56ms; iter 4960: train loss 0.03699
iter_dt 93.75ms; iter 4970: train loss 0.01277
iter_dt 104.08ms; iter 4980: train loss 0.04977
iter_dt 99.01ms; iter 4990: train loss 0.03591
iter_dt 89.91ms; iter 5000: train loss 0.05552
GPT claims that 56 + 36 = 82 but gt is 92
GPT claims that 59 + 39 = 88 but gt is 98
GPT claims that 55 + 36 = 81 but gt is 91
GPT claims that 55 + 35 = 80 but gt is 90
GPT claims that 56 + 35 = 81 but gt is 91
train final score: 9495/9500 = 99.95% correct
test final score: 500/500 = 100.00% correct
iter_dt 80.96ms; iter 5010: train loss 0.05481
iter_dt 84.22ms; iter 5020: train loss 0.06394
iter_dt 82.70ms; iter 5030: train loss 0.04460
iter_dt 142.96ms; iter 5040: train loss 0.04708
iter_dt 105.20ms; iter 5050: train loss 0.05909
iter_dt 93.34ms; iter 5060: train loss 0.02054
iter_dt 93.75ms; iter 5070: train loss 0.04763
iter_dt 78.12ms; iter 5080: train loss 0.17778
iter_dt 92.39ms; iter 5090: train loss 0.02715
iter_dt 93.75ms; iter 5100: train loss 0.07712
iter_dt 319.05ms; iter 5110: train loss 0.01059
iter_dt 104.67ms; iter 5120: train loss 0.04752
iter_dt 93.75ms; iter 5130: train loss 0.10096
iter_dt 118.01ms; iter 5140: train loss 0.03038
iter_dt 113.76ms; iter 5150: train loss 0.05481
iter_dt 126.01ms; iter 5160: train loss 0.03083
iter_dt 93.75ms; iter 5170: train loss 0.02957
iter_dt 109.95ms; iter 5180: train loss 0.05142
iter_dt 100.35ms; iter 5190: train loss 0.01449
iter_dt 128.61ms; iter 5200: train loss 0.03494
iter_dt 177.01ms; iter 5210: train loss 0.02046
iter_dt 147.46ms; iter 5220: train loss 0.06008
iter_dt 117.85ms; iter 5230: train loss 0.03534
iter_dt 125.00ms; iter 5240: train loss 0.01807
iter_dt 170.14ms; iter 5250: train loss 0.04290
iter_dt 204.01ms; iter 5260: train loss 0.03757
iter_dt 163.04ms; iter 5270: train loss 0.01535
iter_dt 125.00ms; iter 5280: train loss 0.06389
iter_dt 107.45ms; iter 5290: train loss 0.03272
iter_dt 95.24ms; iter 5300: train loss 0.04209
iter_dt 122.01ms; iter 5310: train loss 0.01835
iter_dt 137.01ms; iter 5320: train loss 0.01586
iter_dt 214.34ms; iter 5330: train loss 0.05286
iter_dt 149.08ms; iter 5340: train loss 0.02080
iter_dt 164.01ms; iter 5350: train loss 0.06981
iter_dt 113.55ms; iter 5360: train loss 0.02925
iter_dt 159.01ms; iter 5370: train loss 0.03538
iter_dt 93.75ms; iter 5380: train loss 0.02819
iter_dt 100.01ms; iter 5390: train loss 0.00977
iter_dt 90.77ms; iter 5400: train loss 0.09095
iter_dt 93.15ms; iter 5410: train loss 0.02144
iter_dt 111.01ms; iter 5420: train loss 0.00588
iter_dt 112.01ms; iter 5430: train loss 0.02227
iter_dt 93.75ms; iter 5440: train loss 0.04230
iter_dt 78.13ms; iter 5450: train loss 0.00680
iter_dt 103.75ms; iter 5460: train loss 0.00994
iter_dt 83.60ms; iter 5470: train loss 0.02384
iter_dt 108.03ms; iter 5480: train loss 0.03679
iter_dt 92.53ms; iter 5490: train loss 0.05084
iter_dt 109.36ms; iter 5500: train loss 0.01980
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 101.40ms; iter 5510: train loss 0.04513
iter_dt 78.13ms; iter 5520: train loss 0.01127
iter_dt 127.00ms; iter 5530: train loss 0.02978
iter_dt 86.26ms; iter 5540: train loss 0.01189
iter_dt 76.57ms; iter 5550: train loss 0.01360
iter_dt 90.85ms; iter 5560: train loss 0.06091
iter_dt 103.07ms; iter 5570: train loss 0.07272
iter_dt 89.55ms; iter 5580: train loss 0.11071
iter_dt 85.20ms; iter 5590: train loss 0.01200
iter_dt 93.75ms; iter 5600: train loss 0.02548
iter_dt 93.75ms; iter 5610: train loss 0.02322
iter_dt 89.41ms; iter 5620: train loss 0.08786
iter_dt 71.60ms; iter 5630: train loss 0.01617
iter_dt 98.22ms; iter 5640: train loss 0.02664
iter_dt 101.79ms; iter 5650: train loss 0.02590
iter_dt 95.89ms; iter 5660: train loss 0.06481
iter_dt 94.02ms; iter 5670: train loss 0.06840
iter_dt 78.13ms; iter 5680: train loss 0.02725
iter_dt 87.94ms; iter 5690: train loss 0.01627
iter_dt 82.86ms; iter 5700: train loss 0.05316
iter_dt 100.19ms; iter 5710: train loss 0.07126
iter_dt 111.39ms; iter 5720: train loss 0.01556
iter_dt 85.35ms; iter 5730: train loss 0.02031
iter_dt 88.47ms; iter 5740: train loss 0.03391
iter_dt 93.75ms; iter 5750: train loss 0.02890
iter_dt 93.75ms; iter 5760: train loss 0.02488
iter_dt 97.26ms; iter 5770: train loss 0.01183
iter_dt 99.49ms; iter 5780: train loss 0.05403
iter_dt 176.01ms; iter 5790: train loss 0.04298
iter_dt 78.98ms; iter 5800: train loss 0.02799
iter_dt 91.83ms; iter 5810: train loss 0.01906
iter_dt 112.19ms; iter 5820: train loss 0.01163
iter_dt 101.51ms; iter 5830: train loss 0.06064
iter_dt 78.13ms; iter 5840: train loss 0.00774
iter_dt 79.95ms; iter 5850: train loss 0.05579
iter_dt 81.98ms; iter 5860: train loss 0.01613
iter_dt 98.11ms; iter 5870: train loss 0.04749
iter_dt 118.89ms; iter 5880: train loss 0.02736
iter_dt 90.74ms; iter 5890: train loss 0.04487
iter_dt 135.01ms; iter 5900: train loss 0.05623
iter_dt 91.32ms; iter 5910: train loss 0.02460
iter_dt 122.00ms; iter 5920: train loss 0.03338
iter_dt 103.93ms; iter 5930: train loss 0.04641
iter_dt 98.00ms; iter 5940: train loss 0.06651
iter_dt 117.72ms; iter 5950: train loss 0.01736
iter_dt 100.86ms; iter 5960: train loss 0.03796
iter_dt 78.13ms; iter 5970: train loss 0.03266
iter_dt 93.75ms; iter 5980: train loss 0.06516
iter_dt 103.48ms; iter 5990: train loss 0.01624
iter_dt 95.95ms; iter 6000: train loss 0.02070
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 78.12ms; iter 6010: train loss 0.00873
iter_dt 86.20ms; iter 6020: train loss 0.06186
iter_dt 100.19ms; iter 6030: train loss 0.01725
iter_dt 98.27ms; iter 6040: train loss 0.01400
iter_dt 93.75ms; iter 6050: train loss 0.02474
iter_dt 94.01ms; iter 6060: train loss 0.02678
iter_dt 79.79ms; iter 6070: train loss 0.04105
iter_dt 87.52ms; iter 6080: train loss 0.05198
iter_dt 83.89ms; iter 6090: train loss 0.04252
iter_dt 93.75ms; iter 6100: train loss 0.05298
iter_dt 78.13ms; iter 6110: train loss 0.02798
iter_dt 73.57ms; iter 6120: train loss 0.02565
iter_dt 92.89ms; iter 6130: train loss 0.04452
iter_dt 100.24ms; iter 6140: train loss 0.02054
iter_dt 88.45ms; iter 6150: train loss 0.01707
iter_dt 76.94ms; iter 6160: train loss 0.02915
iter_dt 78.12ms; iter 6170: train loss 0.01129
iter_dt 79.89ms; iter 6180: train loss 0.03607
iter_dt 102.01ms; iter 6190: train loss 0.01141
iter_dt 98.16ms; iter 6200: train loss 0.00602
iter_dt 113.43ms; iter 6210: train loss 0.04154
iter_dt 78.12ms; iter 6220: train loss 0.02195
iter_dt 78.12ms; iter 6230: train loss 0.01064
iter_dt 99.01ms; iter 6240: train loss 0.01092
iter_dt 119.01ms; iter 6250: train loss 0.01573
iter_dt 122.01ms; iter 6260: train loss 0.01532
iter_dt 96.01ms; iter 6270: train loss 0.03476
iter_dt 80.25ms; iter 6280: train loss 0.03662
iter_dt 78.13ms; iter 6290: train loss 0.04832
iter_dt 92.03ms; iter 6300: train loss 0.01290
iter_dt 119.00ms; iter 6310: train loss 0.01976
iter_dt 132.01ms; iter 6320: train loss 0.02207
iter_dt 125.01ms; iter 6330: train loss 0.02494
iter_dt 103.01ms; iter 6340: train loss 0.02688
iter_dt 104.01ms; iter 6350: train loss 0.01681
iter_dt 93.75ms; iter 6360: train loss 0.01648
iter_dt 100.01ms; iter 6370: train loss 0.00942
iter_dt 82.73ms; iter 6380: train loss 0.02592
iter_dt 93.75ms; iter 6390: train loss 0.00812
iter_dt 126.01ms; iter 6400: train loss 0.01999
iter_dt 99.01ms; iter 6410: train loss 0.01075
iter_dt 100.01ms; iter 6420: train loss 0.02314
iter_dt 73.32ms; iter 6430: train loss 0.00587
iter_dt 100.95ms; iter 6440: train loss 0.02305
iter_dt 89.30ms; iter 6450: train loss 0.00963
iter_dt 110.32ms; iter 6460: train loss 0.06277
iter_dt 196.45ms; iter 6470: train loss 0.10918
iter_dt 104.61ms; iter 6480: train loss 0.10309
iter_dt 142.07ms; iter 6490: train loss 0.02583
iter_dt 110.01ms; iter 6500: train loss 0.04944
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 92.18ms; iter 6510: train loss 0.01097
iter_dt 90.07ms; iter 6520: train loss 0.05550
iter_dt 114.10ms; iter 6530: train loss 0.02273
iter_dt 329.86ms; iter 6540: train loss 0.02520
iter_dt 94.32ms; iter 6550: train loss 0.01994
iter_dt 98.69ms; iter 6560: train loss 0.08573
iter_dt 78.13ms; iter 6570: train loss 0.03734
iter_dt 86.98ms; iter 6580: train loss 0.02935
iter_dt 76.38ms; iter 6590: train loss 0.03026
iter_dt 93.11ms; iter 6600: train loss 0.03617
iter_dt 98.60ms; iter 6610: train loss 0.03890
iter_dt 95.11ms; iter 6620: train loss 0.00717
iter_dt 96.09ms; iter 6630: train loss 0.01522
iter_dt 98.30ms; iter 6640: train loss 0.04372
iter_dt 84.70ms; iter 6650: train loss 0.01631
iter_dt 113.76ms; iter 6660: train loss 0.04181
iter_dt 141.49ms; iter 6670: train loss 0.02263
iter_dt 99.19ms; iter 6680: train loss 0.06601
iter_dt 78.13ms; iter 6690: train loss 0.03775
iter_dt 94.87ms; iter 6700: train loss 0.02263
iter_dt 78.12ms; iter 6710: train loss 0.02924
iter_dt 102.01ms; iter 6720: train loss 0.05093
iter_dt 101.45ms; iter 6730: train loss 0.02732
iter_dt 88.51ms; iter 6740: train loss 0.09599
iter_dt 78.13ms; iter 6750: train loss 0.02499
iter_dt 85.35ms; iter 6760: train loss 0.04721
iter_dt 113.64ms; iter 6770: train loss 0.00602
iter_dt 129.42ms; iter 6780: train loss 0.01655
iter_dt 71.73ms; iter 6790: train loss 0.07379
iter_dt 69.32ms; iter 6800: train loss 0.01556
iter_dt 76.58ms; iter 6810: train loss 0.02799
iter_dt 81.05ms; iter 6820: train loss 0.04689
iter_dt 78.12ms; iter 6830: train loss 0.00489
iter_dt 78.12ms; iter 6840: train loss 0.02052
iter_dt 71.32ms; iter 6850: train loss 0.01280
iter_dt 99.73ms; iter 6860: train loss 0.01597
iter_dt 104.27ms; iter 6870: train loss 0.02445
iter_dt 97.73ms; iter 6880: train loss 0.01751
iter_dt 98.77ms; iter 6890: train loss 0.01165
iter_dt 124.42ms; iter 6900: train loss 0.01252
iter_dt 138.01ms; iter 6910: train loss 0.07703
iter_dt 84.86ms; iter 6920: train loss 0.02645
iter_dt 89.21ms; iter 6930: train loss 0.02214
iter_dt 78.12ms; iter 6940: train loss 0.08255
iter_dt 78.12ms; iter 6950: train loss 0.00925
iter_dt 80.33ms; iter 6960: train loss 0.01910
iter_dt 83.62ms; iter 6970: train loss 0.02798
iter_dt 78.12ms; iter 6980: train loss 0.01249
iter_dt 78.12ms; iter 6990: train loss 0.06060
iter_dt 82.01ms; iter 7000: train loss 0.02032
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 93.75ms; iter 7010: train loss 0.02206
iter_dt 102.57ms; iter 7020: train loss 0.01680
iter_dt 66.19ms; iter 7030: train loss 0.01570
iter_dt 78.12ms; iter 7040: train loss 0.01909
iter_dt 137.14ms; iter 7050: train loss 0.03165
iter_dt 97.59ms; iter 7060: train loss 0.00995
iter_dt 70.08ms; iter 7070: train loss 0.01339
iter_dt 86.72ms; iter 7080: train loss 0.00663
iter_dt 82.61ms; iter 7090: train loss 0.01860
iter_dt 80.72ms; iter 7100: train loss 0.04572
iter_dt 72.17ms; iter 7110: train loss 0.03662
iter_dt 78.12ms; iter 7120: train loss 0.01360
iter_dt 96.00ms; iter 7130: train loss 0.08472
iter_dt 97.01ms; iter 7140: train loss 0.01108
iter_dt 72.89ms; iter 7150: train loss 0.00728
iter_dt 96.41ms; iter 7160: train loss 0.01716
iter_dt 78.13ms; iter 7170: train loss 0.02931
iter_dt 93.75ms; iter 7180: train loss 0.01350
iter_dt 112.01ms; iter 7190: train loss 0.04743
iter_dt 76.98ms; iter 7200: train loss 0.00515
iter_dt 78.13ms; iter 7210: train loss 0.01593
iter_dt 82.00ms; iter 7220: train loss 0.03144
iter_dt 78.12ms; iter 7230: train loss 0.06286
iter_dt 85.48ms; iter 7240: train loss 0.01035
iter_dt 82.82ms; iter 7250: train loss 0.01323
iter_dt 78.12ms; iter 7260: train loss 0.01302
iter_dt 78.12ms; iter 7270: train loss 0.01662
iter_dt 93.09ms; iter 7280: train loss 0.01070
iter_dt 110.01ms; iter 7290: train loss 0.03253
iter_dt 170.01ms; iter 7300: train loss 0.01719
iter_dt 78.13ms; iter 7310: train loss 0.04353
iter_dt 108.96ms; iter 7320: train loss 0.06804
iter_dt 98.00ms; iter 7330: train loss 0.00898
iter_dt 93.96ms; iter 7340: train loss 0.01524
iter_dt 67.63ms; iter 7350: train loss 0.05089
iter_dt 78.13ms; iter 7360: train loss 0.00782
iter_dt 128.01ms; iter 7370: train loss 0.01558
iter_dt 87.01ms; iter 7380: train loss 0.00812
iter_dt 100.01ms; iter 7390: train loss 0.01789
iter_dt 93.01ms; iter 7400: train loss 0.00936
iter_dt 109.38ms; iter 7410: train loss 0.00883
iter_dt 110.01ms; iter 7420: train loss 0.04394
iter_dt 77.57ms; iter 7430: train loss 0.02522
iter_dt 83.86ms; iter 7440: train loss 0.04086
iter_dt 78.12ms; iter 7450: train loss 0.08304
iter_dt 103.01ms; iter 7460: train loss 0.00746
iter_dt 118.01ms; iter 7470: train loss 0.03960
iter_dt 78.12ms; iter 7480: train loss 0.01577
iter_dt 80.55ms; iter 7490: train loss 0.01055
iter_dt 249.34ms; iter 7500: train loss 0.00937
train final score: 9500/9500 = 100.00% correct
test final score: 500/500 = 100.00% correct
iter_dt 109.01ms; iter 7510: train loss 0.02678
iter_dt 138.01ms; iter 7520: train loss 0.00390
iter_dt 125.35ms; iter 7530: train loss 0.00500
iter_dt 93.75ms; iter 7540: train loss 0.02905
iter_dt 82.89ms; iter 7550: train loss 0.02909
iter_dt 90.77ms; iter 7560: train loss 0.01715
iter_dt 92.01ms; iter 7570: train loss 0.00933
iter_dt 123.01ms; iter 7580: train loss 0.03755
iter_dt 113.01ms; iter 7590: train loss 0.03579
iter_dt 125.75ms; iter 7600: train loss 0.15076
iter_dt 255.02ms; iter 7610: train loss 0.01270
iter_dt 225.01ms; iter 7620: train loss 0.01962
iter_dt 353.02ms; iter 7630: train loss 0.00670
iter_dt 152.50ms; iter 7640: train loss 0.00591
iter_dt 133.81ms; iter 7650: train loss 0.00745
iter_dt 106.80ms; iter 7660: train loss 0.00984
iter_dt 133.01ms; iter 7670: train loss 0.01349
iter_dt 98.07ms; iter 7680: train loss 0.06097
iter_dt 239.02ms; iter 7690: train loss 0.01403
iter_dt 94.60ms; iter 7700: train loss 0.01672
iter_dt 89.60ms; iter 7710: train loss 0.01021
iter_dt 109.38ms; iter 7720: train loss 0.04145
iter_dt 212.01ms; iter 7730: train loss 0.00464
iter_dt 113.31ms; iter 7740: train loss 0.14863
iter_dt 134.21ms; iter 7750: train loss 0.03630
iter_dt 99.21ms; iter 7760: train loss 0.01396
iter_dt 109.37ms; iter 7770: train loss 0.00747
iter_dt 115.81ms; iter 7780: train loss 0.00690
iter_dt 109.38ms; iter 7790: train loss 0.06718
iter_dt 109.38ms; iter 7800: train loss 0.00467
iter_dt 100.31ms; iter 7810: train loss 0.02743
iter_dt 110.06ms; iter 7820: train loss 0.02669
```