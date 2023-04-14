import pandas as pd

df = pd.read_csv('https://www.cpc.ncep.noaa.gov/data/indices/oni.ascii.txt',
                 delimiter='\s+')
df.columns = ['season', 'year', 'sst_c', 'anom_c']

# classify whether below, between, or above the 0.5 threshold
df['threshold'] = 'between'
df.loc[df['anom_c'] <= -0.5, 'threshold'] = 'below'
df.loc[df['anom_c'] >= 0.5, 'threshold'] = 'above'

# cumulatively count how many months stay in same threshold before changing
df['threshold_group'] = (df['threshold'] != df['threshold'].shift(1)).cumsum()
df['cumulative'] = df.groupby('threshold_group', group_keys=False)['anom_c'].apply(
    lambda col: (col ** 0).cumsum()).astype(int)

# classify it's a warm (el nino) or cold period (la_nina) based on
# threshold for at least 5 consecutive overlapping seasons
df_class = df.groupby('threshold_group').agg(
    {'threshold': 'first', 'anom_c': 'count'})
df_class = df_class.rename(columns={'anom_c': 'ntotal'})
df_class['oni'] = 'neutral'
la_nina_cond = (df_class['ntotal'] >= 5) & (df_class['threshold'] == 'below')
el_nino_cond = (df_class['ntotal'] >= 5) & (df_class['threshold'] == 'above')
df_class.loc[la_nina_cond, 'oni'] = 'la_nina'
df_class.loc[el_nino_cond, 'oni'] = 'el_nino'
df = df.join(df_class[['ntotal', 'oni']], on='threshold_group').drop(
    'threshold_group', axis=1)
df.to_csv('oni.csv', index=False)

# mimic the format of https://origin.cpc.ncep.noaa.gov/products/analysis_monitoring/ensostuff/ONI_v5.php
pivot_df = df[['season', 'year', 'oni']].pivot(index='year', columns='season', values='oni')
pivot_df = pivot_df[['DJF', 'JFM', 'FMA', 'MAM', 'AMJ', 'MJJ',
                     'JJA', 'JAS', 'ASO', 'SON', 'OND', 'NDJ']]
pivot_df.to_csv('oni_cpc_table.csv')
