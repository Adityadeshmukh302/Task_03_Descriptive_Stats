# Aditya Deshmukh
# SUID : 668192355


#This script uses Polars to load, clean, and analyze the Twitter posts dataset:
# - Reads the CSV into a Polars DataFrame
# - Drops fully blank rows
# - Prints overall descriptive statistics via DataFrame.describe()
# - For categorical columns: prints value_counts() and n_unique()
# - Computes grouped summaries by keys using group_by().agg()



import polars as pl

# Function to load and clean a CSV file using Polars
def load_and_clean(path: str) -> pl.DataFrame:
    # Read CSV file
    df = pl.read_csv(path, infer_schema_length=1000)
    # For each string column, trim whitespace and set empty strings to null
    for col, dtype in zip(df.columns, df.dtypes):
        if dtype == pl.Utf8:
            df = df.with_columns(
                pl.when(pl.col(col).str.strip_chars() == "")
                  .then(None)
                  .otherwise(pl.col(col).str.strip_chars())
                  .alias(col)
            )
    # Drop rows where all columns are null
    df = df.filter(
        pl.fold(
            acc=pl.lit(False),
            function=lambda acc, s: acc | s.is_not_null(),
            exprs=[pl.col(c) for c in df.columns]
        )
    )
    return df

# Function to write overall statistics to a file
def overall_stats(df: pl.DataFrame, out) -> None:
    out.write("--- Overall Numeric Summary ---\n")
    out.write(str(df.describe()) + "\n\n")
    # For each string column, write categorical stats
    for col in df.columns:
        if df[col].dtype == pl.Utf8:
            out.write(f"\n--- Categorical summary for '{col}' ---\n")
            vc = df[col].value_counts()
            out.write(str(vc) + "\n")
            out.write(f"Unique values in '{col}': {df[col].n_unique()}\n\n")

# Function to write grouped statistics to a file
def group_stats(df: pl.DataFrame, keys: list[str], out) -> None:
    out.write(f"\n--- Grouped Summary by {keys} ---\n")
    # Find numeric columns
    numeric_types = (pl.Float64, pl.Int64, pl.UInt64, pl.Float32, pl.Int32, pl.UInt32)
    numeric_cols = [col for col, dtype in zip(df.columns, df.dtypes) if dtype in numeric_types]
    if not numeric_cols:
        out.write("No numeric columns to summarize.\n")
        return
    # Prepare aggregation expressions for each numeric column
    agg_exprs = []
    for col in numeric_cols:
        agg_exprs.extend([
            pl.col(col).mean().alias(f"{col}_mean"),
            pl.col(col).std().alias(f"{col}_std"),
            pl.col(col).min().alias(f"{col}_min"),
            pl.col(col).max().alias(f"{col}_max"),
        ])
    # Group by keys and aggregate
    summary = df.group_by(keys).agg(agg_exprs)
    out.write(str(summary) + "\n")

# Analyze Twitter posts and write results to a file
def analyze_twitter(path: str, out) -> None:
    out.write("=== Analyzing Twitter Posts ===\n")
    df = load_and_clean(path)
    overall_stats(df, out)
    for keys in [["id"], ["id", "url"]]:
        group_stats(df, keys, out)

# Analyze Facebook Ads and write results to a file
def analyze_fb_ads(path: str, out) -> None:
    out.write("=== Analyzing Facebook Ads ===\n")
    df = load_and_clean(path)
    overall_stats(df, out)
    group_stats(df, ["page_id"], out)
    group_stats(df, ["page_id", "ad_id"], out)

# Analyze Facebook Posts and write results to a file
def analyze_fb_posts(path: str, out) -> None:
    out.write("=== Analyzing Facebook Posts ===\n")
    df = load_and_clean(path)
    overall_stats(df, out)
    group_stats(df, ["Facebook_Id"], out)
    group_stats(df, ["Facebook_Id", "post_id"], out)

if __name__ == '__main__':
    # Analyze Twitter posts and export to file
    twitter_path = (
        '/Users/adityadeshmukh/Downloads/OPT_project/Dataset_Election/'
        '2024_tw_posts_president_scored_anon.csv'
    )
    with open("twitter_polars_report.txt", "w", encoding="utf-8") as out:
        analyze_twitter(twitter_path, out)

    # Analyze Facebook ads and export to file
    fb_ads_path = (
        '/Users/adityadeshmukh/Downloads/OPT_project/Dataset_Election/'
        '2024_fb_ads_president_scored_anon.csv'
    )
    with open("fb_ads_polars_report.txt", "w", encoding="utf-8") as out:
        analyze_fb_ads(fb_ads_path, out)

    # Analyze Facebook posts and export to file
    fb_posts_path = (
        '/Users/adityadeshmukh/Downloads/OPT_project/Dataset_Election/'
        '2024_fb_posts_president_scored_anon.csv'
    )
    with open("fb_posts_polars_report.txt", "w", encoding="utf-8") as out:
        analyze_fb_posts(fb_posts_path, out)

    print("\nAnalysis complete. Results exported to report files.")
