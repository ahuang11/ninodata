# Oceanic Niño Index (ONI)

### Overview
Match the color coding of the Climate Prediction Center's Oceanic Niño Index, convert into a tidy dataframe, and make it directly readable from online. https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php

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

### CSV Columns' Descriptions
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

### Notes
Data used to classify ONI is read from https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt which rounds to the hundreth place, not https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php which rounds to the tenth place. Thus, there will be minor differences in edge cases between this repo's computed ONI and the color coded ONI on the latter webpage.

One discrepancy was found between AMJ 2011 and JJA 2011; the former webpage lists the SST anomalies as -0.47 and -0.46 respectively which is not less than or equal to the -0.5 threshold, but the latter webpage lists the SST anomalies both as -0.5 which is less than or equal to the -0.5 threshold.
