import os
import datetime
import pandas as pd

URLS = {
    "t300_e": "https://www.pmel.noaa.gov/tao/wwv/data/t300_east.dat",
    "t300_w": "https://www.pmel.noaa.gov/tao/wwv/data/t300_west.dat",
    "t300_c": "https://www.pmel.noaa.gov/tao/wwv/data/t300.dat",
    "wwv_e": "https://www.pmel.noaa.gov/tao/wwv/data/wwv_east.dat",
    "wwv_w": "https://www.pmel.noaa.gov/tao/wwv/data/wwv_west.dat",
    "wwv_c": "https://www.pmel.noaa.gov/tao/wwv/data/wwv.dat",
    "u850_e": "https://www.cpc.ncep.noaa.gov/data/indices/epac850",
    "u850_w": "https://www.cpc.ncep.noaa.gov/data/indices/wpac850",
    "u850_c": "https://www.cpc.ncep.noaa.gov/data/indices/cpac850",
    "olr": "https://www.cpc.ncep.noaa.gov/data/indices/olr",
    "nino": "https://www.cpc.ncep.noaa.gov/data/indices/sstoi.indices",
}


def process_3in1(key):
    df = pd.read_fwf(
        URLS[key],
        widths=[4] + [6] * 12,
        delimiter="\s+",
        skiprows=[0, 1, 2, 3, 54, 55, 56, 57, 58, 108, 109, 110, 111, 1112],
        header=None,
        names=["year"] + list(range(1, 13)),
        na_values=-999.9,
    )

    indices = [0] + list(df.loc[df["year"] == 2023].index)
    labels = ["", "_anom", "_norm"]
    dfs = []
    for i, index in enumerate(indices):
        sub_df = (
            df[index : indices[i + 1]]
            .melt("year", var_name="month")
            .rename(columns={"value": f"{key}{labels[i]}"})
            .dropna()
        )
        sub_df.index = pd.to_datetime(
            sub_df["year"].astype(str) + sub_df["month"].astype(str).str.zfill(2),
            format="%Y%m",
        )
        dfs.append(sub_df.drop(columns=["year", "month"]))
        if i == 2:
            break
    return pd.concat(dfs, axis=1)


def process_ewc(key):
    return pd.concat(
        [
            pd.read_csv(
                URLS[key],
                skiprows=6,
                delimiter="\s+",
                names=["time", key, f"{key}_anom"],
                date_parser=lambda x: datetime.datetime.strptime(x, "%Y%m"),
                parse_dates=True,
                index_col="time",
            )
            for key in [f"{key}_e", f"{key}_w", f"{key}_c"]
        ],
        axis=1,
    )


t300_df = process_ewc("t300")
wwv_df = process_ewc("wwv")
olr_df = process_3in1("olr")
u850_df = pd.concat([process_3in1(f"u850_{ewc}") for ewc in "ewc"], axis=1)
nino_df = pd.read_csv(
    URLS["nino"], delimiter="\s+", parse_dates={"time": ["YR", "MON"]}
).set_index("time")
nino_df.columns = [
    col.lower() if i % 2 == 0 else f"{nino_df.columns[i - 1].lower()}_anom"
    for i, col in enumerate(nino_df.columns)
]

df = pd.concat(
    [
        df.loc[~df.index.duplicated(keep="last")]
        for df in [t300_df, wwv_df, olr_df, u850_df, nino_df]
    ],
    axis=1,
)
df.to_csv("nino_ml.csv")
