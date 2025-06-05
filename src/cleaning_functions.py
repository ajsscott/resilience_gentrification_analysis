# cleaning_functions.py
# Utility functions for cleaning dfs


def preview_df(df):
    print("Shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
    print("\nMissing values (%):\n", (df.isna().mean() * 100).round(2))
    print(df.head())
