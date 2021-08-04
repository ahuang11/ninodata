# ninodata

### Overview

Make data relevant to Nino indices directly accessible with `pandas.read_csv`.

### Motivation

Trying to set up a machine learning model, but the data is so inconsistent and dirty from all sources... so I tidied up the data and shared it, hoping that it can help you too.

### Usage

```
df = pd.read_csv('https://raw.githubusercontent.com/ahuang11/oni/master/oni.csv')
print(df.head(15))

# output

   season  year  sst_c  anom_c threshold  cumulative  ntotal      oni
0     DJF  1950  24.72   -1.53     below           1       7  la_nina
1     JFM  1950  25.17   -1.34     below           2       7  la_nina
2     FMA  1950  25.75   -1.16     below           3       7  la_nina
3     MAM  1950  26.12   -1.18     below           4       7  la_nina
4     AMJ  1950  26.32   -1.07     below           5       7  la_nina
5     MJJ  1950  26.31   -0.85     below           6       7  la_nina
6     JJA  1950  26.21   -0.54     below           7       7  la_nina
7     JAS  1950  25.96   -0.42   between           1       3  neutral
8     ASO  1950  25.76   -0.39   between           2       3  neutral
9     SON  1950  25.63   -0.44   between           3       3  neutral
10    OND  1950  25.48   -0.60     below           1       4  neutral
11    NDJ  1950  25.34   -0.80     below           2       4  neutral
12    DJF  1951  25.42   -0.82     below           3       4  neutral
13    JFM  1951  25.96   -0.54     below           4       4  neutral
14    FMA  1951  26.74   -0.17   between           1       3  neutral
```

OR

```
df = pd.read_csv('https://raw.githubusercontent.com/ahuang11/oni/master/nino_ml.csv', index_col=0, parse_dates=True)
print(df.dropna().head(15))

# output
              t300_e  t300_e_anom    t300_w  t300_w_anom    t300_c  \
1982-01-01  17.07052     0.096138  21.00096     0.130941  19.12099   
1982-02-01  16.94978     0.174458  21.08333     0.201464  19.10621   
1982-03-01  16.83664     0.216805  21.10322     0.173842  19.06247   
1982-04-01  16.90166     0.328028  21.08463     0.168816  19.08388   
1982-05-01  16.95667     0.365135  20.96281     0.143486  19.04663   
1982-06-01  16.83508     0.212471  20.77251     0.090977  18.88920   
1982-07-01  16.76243     0.120325  20.66742     0.091255  18.79963   
1982-08-01  17.12920     0.440733  20.63754     0.064568  18.95947   
1982-09-01  17.72200     0.945202  20.65966    -0.017754  19.25455   
1982-10-01  17.98471     1.120775  20.69530    -0.150160  19.39880   
1982-11-01  18.13777     1.179571  20.49180    -0.475876  19.36584   
1982-12-01  18.25919     1.241333  20.07812    -0.869966  19.20811   
1983-01-01  17.98178     1.007391  19.85376    -1.016256  18.95837   
1983-02-01  17.66729     0.891973  19.88024    -1.001623  18.82177   
1983-03-01  17.66997     1.050129  19.98756    -0.941820  18.87903   

            t300_c_anom         wwv_e    wwv_e_anom         wwv_w  \
1982-01-01     0.114294  8.545323e+14  2.747840e+13  1.744721e+15   
1982-02-01     0.188547  8.115376e+14  3.110805e+13  1.763667e+15   
1982-03-01     0.194391  7.747996e+14  3.949504e+13  1.767636e+15   
1982-04-01     0.244970  7.790038e+14  6.740944e+13  1.750226e+15   
1982-05-01     0.249504  7.957734e+14  8.451127e+13  1.708836e+15   
1982-06-01     0.149088  7.894133e+14  6.630369e+13  1.673828e+15   
1982-07-01     0.105160  7.844379e+14  4.782815e+13  1.669973e+15   
1982-08-01     0.244492  8.415854e+14  8.775772e+13  1.677114e+15   
1982-09-01     0.442837  9.267273e+14  1.499622e+14  1.678117e+15   
1982-10-01     0.457739  9.696770e+14  1.718459e+14  1.676370e+15   
1982-11-01     0.315941  1.012769e+15  1.939457e+14  1.642149e+15   
1982-12-01     0.139889  1.060189e+15  2.245316e+14  1.566682e+15   
1983-01-01    -0.048326  9.958760e+14  1.688221e+14  1.530633e+15   
1983-02-01    -0.095898  9.124297e+14  1.320001e+14  1.535820e+15   
1983-03-01     0.010950  8.741457e+14  1.388411e+14  1.549613e+15   

              wwv_w_anom  ...  u850_c_anom  u850_c_norm  nino1+2  \
1982-01-01  4.294444e+13  ...          0.8          0.3    24.29   
1982-02-01  4.971143e+13  ...         -0.8         -0.3    25.49   
1982-03-01  4.128443e+13  ...         -0.9         -0.3    25.21   
1982-04-01  3.365966e+13  ...         -1.5         -0.6    24.50   
1982-05-01  2.045545e+13  ...         -2.1         -0.8    23.97   
1982-06-01  1.552993e+13  ...         -1.6         -0.6    22.89   
1982-07-01  3.009752e+13  ...         -1.6         -0.6    22.47   
1982-08-01  3.685176e+13  ...         -1.9         -0.8    21.75   
1982-09-01  2.177387e+13  ...         -5.0         -2.0    21.80   
1982-10-01 -7.667053e+12  ...         -6.4         -2.5    22.94   
1982-11-01 -6.597432e+13  ...         -8.5         -3.4    24.59   
1982-12-01 -1.425945e+14  ...         -8.1         -3.2    26.13   
1983-01-01 -1.711438e+14  ...         -7.4         -2.9    27.42   
1983-02-01 -1.781358e+14  ...         -6.7         -2.6    28.09   
1983-03-01 -1.767383e+14  ...         -8.6         -3.4    28.68   

            nino1+2_anom  nino3  nino3_anom  nino4  nino4_anom  nino3.4  \
1982-01-01         -0.17  25.87        0.24  28.30        0.00    26.72   
1982-02-01         -0.58  26.38        0.01  28.21        0.11    26.70   
1982-03-01         -1.31  26.98       -0.16  28.41        0.22    27.20   
1982-04-01         -0.97  27.68        0.18  28.92        0.42    28.02   
1982-05-01         -0.23  27.79        0.71  29.49        0.70    28.54   
1982-06-01          0.07  27.46        1.03  29.76        0.92    28.75   
1982-07-01          0.87  26.44        0.82  29.38        0.58    28.10   
1982-08-01          1.10  26.15        1.16  29.04        0.36    27.93   
1982-09-01          1.44  26.52        1.67  29.16        0.47    28.11   
1982-10-01          2.12  27.11        2.19  29.38        0.72    28.64   
1982-11-01          3.00  27.62        2.64  29.23        0.60    28.81   
1982-12-01          3.34  28.39        3.25  29.15        0.66    29.21   
1983-01-01          2.96  28.92        3.29  29.00        0.70    29.36   
1983-02-01          2.02  28.92        2.55  28.79        0.69    29.13   
1983-03-01          2.16  29.10        1.96  28.76        0.57    29.03   

            nino3.4_anom  
1982-01-01          0.15  
1982-02-01         -0.02  
1982-03-01         -0.02  
1982-04-01          0.24  
1982-05-01          0.69  
1982-06-01          1.10  
1982-07-01          0.88  
1982-08-01          1.11  
1982-09-01          1.39  
1982-10-01          1.95  
1982-11-01          2.16  
1982-12-01          2.64  
1983-01-01          2.79  
1983-02-01          2.41  
1983-03-01          1.81  

[15 rows x 32 columns]
```

### CSV Columns' Descriptions

For oni.csv
* `season` - `DJF`: Dec, Jan, Feb; `JFM`: Jan, Feb, Mar; `FMA`: Feb, Mar, Apr, etc
* `sst_c` - ERSST.v5 sea surface temperatures in Celsius bounded within the Niño 3.4 region (5N-5S, 120-170W)
* `anom_c` - the three month running mean of `sst_c`
* `threshold` - classification of `anom_c`
    * if `sst_c` is less than or equal to -0.5, set `threshold` to `below`
    * if `sst_c` is between -0.5 and 0.5, set `threshold` to `between`
    * if `sst_c` is greater than or equal to 0.5, set `threshold` to `above`
* `cumulative` - the cumulative count of overlapping `season`s at the same `threshold`
* `ntotal` - the total count of overlapping `season`s at the same `threshold`
* `oni` - the Oceanic Nino Index
    * if `ntotal` is greater than or equal to 5 and `threshold` is `below`, set `oni` to `la_nina`
    * if `ntotal` is greater than or equal to 5 and `threshold` is `above`, set `oni` to `el_nino`
    * else all other cases set `oni` to `neutral`

For nino.csv
* `t300` - depth averaged temps up from 0 to 300m
* `wwv` - warm water volume
* `u850` - 850 mb trade wind index
* `*_e` - east
* `*_w` - west
* `*_c` - central
* `*_anom` - anomaly
* `*_norm` - standardized
* Check out the URLs listed in process_nino_ml.csv

### Notes

For oni.csv

Data used to classify ONI is read from https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt which rounds to the hundreth place, not https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php which rounds to the tenth place. Thus, there will be minor differences in edge cases between this repo's computed ONI and the color coded ONI on the latter webpage.

One discrepancy was found between AMJ 2011 and JJA 2011; the former webpage lists the SST anomalies as -0.47 and -0.46 respectively which is not less than or equal to the -0.5 threshold, but the latter webpage lists the SST anomalies both as -0.5 which is less than or equal to the -0.5 threshold.

Please report bugs under GitHub issues!
