# NOTE: Before running this script, update the file paths in the pd.read_csv() calls
# to match the location of your Dataset_Election folder.
# Example: Change 'data/Dataset_Election/...' to your actual path if needed.

# Aditya Deshmukh 
# SUID : 668192355


#This script contains three pure Python data analytics scripts for three different datasets:
# 1. Twitter posts dataset
# 2. Facebook posts dataset
# 3. Facebook ads dataset

#Each script:
# - Loads the dataset from CSV (no pandas)
# - Cleans and summarizes data (numeric and categorical columns)
# - Computes overall and grouped statistics
# - Writes a full report to a text file
# Uncomment the function call for the dataset you want to analyze,
#at the bottom of the script.

import csv
import math
from collections import Counter, defaultdict

# =========================
# Utility Functions
# =========================

def is_number(val):
    """Check if a string can be converted to a float."""
    try:
        float(val)
        return True
    except ValueError:
        return False

def stats_numeric(vals):
    
# Compute statistics for numeric columns: count, mean, min, max, std deviation
  
    nums = [float(x) for x in vals]
    n = len(nums)
    mean = sum(nums) / n if n else 0
    mn = min(nums) if nums else 0
    mx = max(nums) if nums else 0
    var = sum((x - mean) ** 2 for x in nums) / n if n else 0
    std = math.sqrt(var)
    return {
        'count': n,
        'mean': round(mean, 4),
        'min': mn,
        'max': mx,
        'std': round(std, 4)
    }

def stats_categorical(vals):
  
    # Compute statistics for categorical columns:
    # count, unique values, most frequent value, frequency of most frequent
    # and ignores blank values.
    
    cleaned = [v for v in vals if v.strip()]
    ctr = Counter(cleaned)
    count = sum(ctr.values())
    unique = len(ctr)
    top, freq = ctr.most_common(1)[0] if ctr else (None, 0)
    return {
        'count': count,
        'unique': unique,
        'top': top,
        'freq': freq
    }

def summarize_column(col_vals):
   
    # Decide whether to use numeric or categorical stats for a column.
    
    non_blank = [v for v in col_vals if v.strip()]
    if non_blank and all(is_number(v) for v in non_blank):
        return stats_numeric(non_blank)
    return stats_categorical(col_vals)

def load_csv(path):
    
    # Load a CSV file, dropping rows where every cell is blank.
    # Returns header and list of rows.

    with open(path, encoding='utf-8', newline='') as fh:
        reader = csv.reader(fh)
        header = next(reader)
        rows = [row for row in reader if any(cell.strip() for cell in row)]
    return header, rows

def overall_summary(header, rows):
    
    # Compute summary statistics for all columns in the dataset.
    # Returns a dictionary: column name -> stats dict.
    
    cols = list(zip(*rows))
    return {name: summarize_column(vals) for name, vals in zip(header, cols)}

def grouped_summary(header, rows, keys):
    
    # Group rows by specified column or columns (e.g., ['Facebook_Id'], ['Facebook_Id','post_id']),
    # then calculate descriptive stats for each group.
    # The result maps each unique key tuple to its stats dictionary.
    
    idxs = [header.index(k) for k in keys]
    buckets = defaultdict(list)
    for row in rows:
        key = tuple(row[i] for i in idxs)
        buckets[key].append(row)
    return {key: overall_summary(header, grp_rows) for key, grp_rows in buckets.items()}


# =========================
# 1. Twitter Posts Dataset
# =========================

def analyze_twitter_posts():
    
    # Analyze the Twitter posts dataset and write a full report.
    
    data_path = (
        'data/2024_tw_posts_president_scored_anon.csv'
    )
    header, rows = load_csv(data_path)
    sep = '=' * 60
    report_path = 'twitter_full_report.txt'

    print(f"Generating full report -> {report_path}")

    with open(report_path, 'w', encoding='utf-8') as out:
        # Overall stats
        out.write(sep + '\n')
        out.write('TWITTER POSTS DATASET - OVERALL SUMMARY\n')
        out.write(sep + '\n')
        overall = overall_summary(header, rows)
        for col, stats in overall.items():
            out.write(f"Column: {col}\n")
            for metric, val in stats.items():
                out.write(f"  - {metric}: {val}\n")
            out.write('\n')

        # Group by 'id'
        out.write(sep + '\n')
        out.write("SUMMARY BY 'id'\n")
        out.write(sep + '\n')
        by_id = grouped_summary(header, rows, ['id'])
        for (id_val,), stats in by_id.items():
            out.write(f"id = {id_val}\n")
            for col, col_stats in stats.items():
                out.write(f"  Column: {col}\n")
                for m, v in col_stats.items():
                    out.write(f"    - {m}: {v}\n")
            out.write('\n')

        # Group by ('id', 'url')
        out.write(sep + '\n')
        out.write("SUMMARY BY (id, url)\n")
        out.write(sep + '\n')
        by_combo = grouped_summary(header, rows, ['id', 'url'])
        for (id_val, url_val), stats in by_combo.items():
            out.write(f"id = {id_val}, url = {url_val}\n")
            for col, col_stats in stats.items():
                out.write(f"  Column: {col}\n")
                for m, v in col_stats.items():
                    out.write(f"    - {m}: {v}\n")
            out.write('\n')

    print("Done! Check twitter_full_report.txt for the report.")

# =========================
# 2. Facebook Posts Dataset
# =========================

def analyze_facebook_posts():
    
   # Analyze the Facebook posts dataset and write a full report.
    
    data_path = (
        'data/2024_fb_posts_president_scored_anon.csv'
    )
    header, rows = load_csv(data_path)
    sep = '=' * 60
    report_file = 'fb_posts_full_report.txt'

    print(f"Generating Facebook Posts full report -> {report_file}")
    with open(report_file, 'w', encoding='utf-8') as out:
        # Overall Summary
        out.write(sep + '\n')
        out.write('FACEBOOK POSTS DATASET - OVERALL SUMMARY\n')
        out.write(sep + '\n')
        overall = overall_summary(header, rows)
        for col, stats in overall.items():
            out.write(f"Column: {col}\n")
            for metric, val in stats.items():
                out.write(f"  - {metric}: {val}\n")
            out.write('\n')

        # Summary by Facebook_Id
        out.write(sep + '\n')
        out.write("SUMMARY BY 'Facebook_Id'\n")
        out.write(sep + '\n')
        by_fb = grouped_summary(header, rows, ['Facebook_Id'])
        for (fb_id,), stats in by_fb.items():
            out.write(f"Facebook_Id = {fb_id}\n")
            for col, col_stats in stats.items():
                out.write(f"  Column: {col}\n")
                for m, v in col_stats.items():
                    out.write(f"    - {m}: {v}\n")
            out.write('\n')

        # Summary by (Facebook_Id, post_id)
        out.write(sep + '\n')
        out.write("SUMMARY BY (Facebook_Id, post_id)\n")
        out.write(sep + '\n')
        by_combo = grouped_summary(header, rows, ['Facebook_Id', 'post_id'])
        for (fb_id, post_id), stats in by_combo.items():
            out.write(f"Facebook_Id = {fb_id}, post_id = {post_id}\n")
            for col, col_stats in stats.items():
                out.write(f"  Column: {col}\n")
                for m, v in col_stats.items():
                    out.write(f"    - {m}: {v}\n")
            out.write('\n')

    print("Done! Check fb_posts_full_report.txt for the complete report.")


# =========================
# 3. Facebook Ads Dataset
# =========================

def analyze_facebook_ads():
    
    # Analyze the Facebook ads dataset and write a full report.
    
    data_path = (
        'data/2024_fb_ads_president_scored_anon.csv'
    )

    # load and clean data
    header, rows = load_csv(data_path)

    # file to write the full report
    report_path = 'fb_ads_president_full_report.txt'
    sep = '=' * 60

    print(f"Starting report generation of: {report_path}")

    with open(report_path, 'w', encoding='utf-8') as report:
        # Overall stats
        report.write(sep + '\n')
        report.write('OVERALL DATASET SUMMARY\n')
        report.write(sep + '\n')
        overall_stats = overall_summary(header, rows)
        for col, stats in overall_stats.items():
            report.write(f"Column: {col}\n")
            for metric, val in stats.items():
                report.write(f"  - {metric}: {val}\n")
            report.write('\n')

        # Stats by page_id
        report.write(sep + '\n')
        report.write('SUMMARY BY PAGE_ID\n')
        report.write(sep + '\n')
        page_stats = grouped_summary(header, rows, ['page_id'])
        for (page_id,), stats in page_stats.items():
            report.write(f"PAGE_ID = {page_id}\n")
            for col, col_stats in stats.items():
                report.write(f"  Column: {col}\n")
                for metric, val in col_stats.items():
                    report.write(f"    - {metric}: {val}\n")
            report.write('\n')

        # Stats by (page_id, ad_id)
        report.write(sep + '\n')
        report.write('SUMMARY BY (PAGE_ID, AD_ID)\n')
        report.write(sep + '\n')
        combo_stats = grouped_summary(header, rows, ['page_id', 'ad_id'])
        for (page_id, ad_id), stats in combo_stats.items():
            report.write(f"PAGE_ID = {page_id}, AD_ID = {ad_id}\n")
            for col, col_stats in stats.items():
                report.write(f"  Column: {col}\n")
                for metric, val in col_stats.items():
                    report.write(f"    - {metric}: {val}\n")
            report.write('\n')

    print("Report generated successfully!")

# =========================
# Main Entry Point
# =========================

if __name__ == '__main__':
    # Uncomment the function for the dataset you want to analyze
    # The Default is Facebook Ads
   
    # analyze_twitter_posts()
    # analyze_facebook_posts() 
    analyze_facebook_ads()
