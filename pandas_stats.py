# NOTE: Before running this script, update the file paths in the pd.read_csv() calls
# to match the location of your Dataset_Election folder.
# Example: Change 'data/Dataset_Election/...' to your actual path if needed.

# Aditya Deshmukh
# SUID: 668192355

# This script contains three separate pandas-based analysis scripts for:
#   1. Facebook Ads dataset
#   2. Twitter Posts dataset
#   3. Facebook Posts dataset
#
# Each section:
#   - Loads and cleans the dataset
#   - Computes descriptive statistics (numeric & categorical)
#   - Groups stats by relevant columns
#   - Writes a full report to a text file
# To run a specific analysis, comment/uncomment the relevant main() call at the bottom.

import pandas as pd

# ----------------------------------------------------------------------------
# 1. FACEBOOK ADS DATASET ANALYSIS
# ----------------------------------------------------------------------------

def load_and_clean_fb_ads(path):
    """
    Load and clean the Facebook Ads dataset.
    - Replaces empty/whitespace cells with NaN
    - Drops rows that are entirely NaN
    """
    df = pd.read_csv(path, encoding='utf-8')
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    df = df.dropna(how='all')
    return df

def overall_stats_fb_ads(df, out):
    # Write overall numeric and categorical stats for the Facebook Ads dataset.
    out.write('='*60 + '\n')
    out.write('OVERALL DATASET SUMMARY (Pandas)\n')
    out.write('='*60 + '\n')

    # Numeric columns summary
    out.write('Numeric columns (describe):\n')
    desc = df.describe().T.to_string()
    out.write(desc + '\n\n')

    # Categorical columns summary
    out.write('Categorical columns (unique / top values):\n')
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        out.write(f"-- {col} --\n")
        out.write(f"Unique: {df[col].nunique(dropna=True)}\n")
        vc = df[col].value_counts(dropna=True).head(5)
        out.write(vc.to_string() + '\n\n')

def grouped_stats_fb_ads(df, keys, out):
    # Write grouped numeric and categorical stats for the Facebook Ads dataset.
    group_name = ', '.join(keys)
    out.write('='*60 + '\n')
    out.write(f'STATS GROUPED BY ({group_name})\n')
    out.write('='*60 + '\n')

    grouped = df.groupby(keys)
    for name, grp in grouped:
        out.write(f"Group = {name}\n")
        # Numeric
        desc = grp.describe().T.to_string()
        out.write(desc + '\n')
        # Categorical
        cat_cols = grp.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            out.write(f"  {col} - Unique: {grp[col].nunique(dropna=True)} | Top 5:\n")
            vc = grp[col].value_counts(dropna=True).head(5)
            out.write('    ' + vc.to_string().replace('\n', '\n    ') + '\n')
        out.write('\n')

def main_fb_ads():
    
    # Main function for Facebook Ads analysis.
    
    data_path = (
        'data/2024_fb_ads_president_scored_anon.csv'
    )
    df = load_and_clean_fb_ads(data_path)

    report_path = 'fb_ads_pandas_report.txt'
    print(f"Generating pandas report -> {report_path}")

    with open(report_path, 'w', encoding='utf-8') as out:
        overall_stats_fb_ads(df, out)
        grouped_stats_fb_ads(df, ['page_id'], out)
        grouped_stats_fb_ads(df, ['page_id', 'ad_id'], out)

    print("Done! Check fb_ads_pandas_report.txt for the pandas analysis.")

# ----------------------------------------------------------------------------
# 2. TWITTER POSTS DATASET ANALYSIS
# ----------------------------------------------------------------------------

def load_and_clean_twitter(path):
    """
    Load and clean the Twitter Posts dataset.
    - Replaces empty/whitespace cells with NaN
    - Drops rows that are entirely NaN
    """
    df = pd.read_csv(path)
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    df = df.dropna(how='all')
    return df

def write_overall_stats_twitter(df, out):
    # Write overall numeric and categorical stats for the Twitter Posts dataset.
    out.write('='*60 + '\n')
    out.write('TWITTER POSTS DATASET - OVERALL SUMMARY\n')
    out.write('='*60 + '\n')

    # Numeric columns
    out.write('\nNumeric columns:\n')
    num_stats = df.describe().T.round(4)
    out.write(num_stats.to_string() + '\n')

    # Categorical columns
    out.write('\nCategorical columns:\n')
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        out.write(f"\nColumn: {col}\n")
        out.write(f"  - Unique values: {df[col].nunique(dropna=True)}\n")
        top5 = df[col].value_counts(dropna=True).head(5)
        out.write("  - Top 5 values:\n")
        out.write(top5.to_string().replace('\n', '\n    ') + '\n')

def write_group_stats_twitter(df, keys, out):
    # Write grouped numeric and categorical stats for the Twitter Posts dataset.
    name = ', '.join(keys)
    out.write('\n' + '='*60 + '\n')
    out.write(f'STATS GROUPED BY ({name})\n')
    out.write('='*60 + '\n')

    for key_vals, group in df.groupby(keys):
        out.write(f"\nGroup = {key_vals}\n")
        # Numeric summary
        num_stats = group.describe().T.round(4)
        out.write(num_stats.to_string() + '\n')
        # Categorical summary
        cat_cols = group.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            out.write(f"\nColumn: {col}\n")
            out.write(f"  - Unique values: {group[col].nunique(dropna=True)}\n")
            top5 = group[col].value_counts(dropna=True).head(5)
            out.write("  - Top 5 values:\n")
            out.write(top5.to_string().replace('\n', '\n    ') + '\n')

def main_twitter():
    # Main function for Twitter Posts analysis.
    data_path = (
        'data/2024_tw_posts_president_scored_anon.csv'
    )
    report_path = 'twitter_pandas_report.txt'

    print(f"Loading and cleaning data from {data_path}")
    df = load_and_clean_twitter(data_path)

    print(f"Writing full report to {report_path}")
    with open(report_path, 'w', encoding='utf-8') as out:
        write_overall_stats_twitter(df, out)
        write_group_stats_twitter(df, ['id'], out)
        write_group_stats_twitter(df, ['id', 'url'], out)

    print("Done! Check twitter_pandas_report.txt for the report.")

# ----------------------------------------------------------------------------
# 3. FACEBOOK POSTS DATASET ANALYSIS
# ----------------------------------------------------------------------------

def load_and_clean_fb_posts(path):
    """
    Load and clean the Facebook Posts dataset.
    - Replaces empty/whitespace cells with NaN
    - Drops rows that are entirely NaN
    """
    df = pd.read_csv(path)
    df = df.replace(r'^\s*$', pd.NA, regex=True)
    df = df.dropna(how='all')
    return df

def write_overall_stats_fb_posts(df, out):
    # Write overall numeric and categorical stats for the Facebook Posts dataset.
    out.write('='*60 + '\n')
    out.write('FACEBOOK POSTS DATASET - OVERALL SUMMARY\n')
    out.write('='*60 + '\n')

    # Numeric columns
    out.write('\nNumeric columns:\n')
    num_stats = df.describe().T.round(4)
    out.write(num_stats.to_string() + '\n')

    # Categorical columns
    out.write('\nCategorical columns:\n')
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in cat_cols:
        out.write(f"\nColumn: {col}\n")
        out.write(f"  - Unique values: {df[col].nunique(dropna=True)}\n")
        top5 = df[col].value_counts(dropna=True).head(5)
        out.write("  - Top 5 values:\n")
        out.write(top5.to_string().replace('\n', '\n    ') + '\n')

def write_group_stats_fb_posts(df, keys, out):
    # Write grouped numeric and categorical stats for the Facebook Posts dataset.
    name = ', '.join(keys)
    out.write('\n' + '='*60 + '\n')
    out.write(f'STATS GROUPED BY ({name})\n')
    out.write('='*60 + '\n')

    for key_vals, group in df.groupby(keys):
        out.write(f"\nGroup = {key_vals}\n")
        # Numeric summary
        num_stats = group.describe().T.round(4)
        out.write(num_stats.to_string() + '\n')
        # Categorical summary
        cat_cols = group.select_dtypes(include=['object', 'category']).columns
        for col in cat_cols:
            out.write(f"\nColumn: {col}\n")
            out.write(f"  - Unique values: {group[col].nunique(dropna=True)}\n")
            top5 = group[col].value_counts(dropna=True).head(5)
            out.write("  - Top 5 values:\n")
            out.write(top5.to_string().replace('\n', '\n    ') + '\n')

def main_fb_posts():
    # Main function for Facebook Posts analysis.
    data_path = (
        'data/2024_fb_posts_president_scored_anon.csv'
    )
    df = load_and_clean_fb_posts(data_path)

    report_path = 'fb_posts_pandas_report.txt'
    print(f"Generating pandas report -> {report_path}")

    with open(report_path, 'w', encoding='utf-8') as out:
        write_overall_stats_fb_posts(df, out)
        write_group_stats_fb_posts(df, ['Facebook_Id'], out)
        write_group_stats_fb_posts(df, ['Facebook_Id', 'post_id'], out)

    print("Done! Check fb_posts_pandas_report.txt for the pandas analysis.")

# Uncomment the desired main function to run the analysis for that dataset

# main_fb_ads()
# main_twitter()
main_fb_posts()