# NOTE: Before running this script, update the file paths in the pd.read_csv() calls
# to match the location of your Dataset_Election folder.
# Example: Change 'data/Dataset_Election/...' to your actual path if needed.

#Aditya Deshmukh 
# SUID: 668192355
# Following code visualizes the Twitter, Facebook posts, and Facebook ads datasets for the 2024 US Presidential Election.
# This script generates various plots to analyze the distribution of civic scores, sources, languages, and other relevant metrics.
# It uses pandas for data manipulation and matplotlib for plotting.


import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Twitter Posts Visualizations
# -------------------------------

def visualize_twitter():
    # Columns to load from Twitter dataset
    cols = [
        'incivility_illuminating',
        'scam_illuminating',
        'freefair_illuminating',
        'fraud_illuminating',
        'source',
        'lang',
        'month_year'
    ]
    # Load data
    df = pd.read_csv(
        'data/Dataset_Election/2024_tw_posts_president_scored_anon.csv',  # <-- Update this path if needed
        usecols=cols,
        dtype=str
    ).dropna(how='all')

    # Convert score columns to numeric
    score_cols = cols[:4]
    for c in score_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    # Plot histogram for incivility score
    plt.figure()
    df['incivility_illuminating'].hist(bins=20)
    plt.title('Incivility Score Distribution (Twitter)')
    plt.xlabel('incivility_illuminating')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

    # Boxplot for all score columns
    plt.figure()
    df[score_cols].boxplot()
    plt.title('Boxplot of Civic-Score Metrics (Twitter)')
    plt.tight_layout()
    plt.show()

    # Top-10 Tweet sources
    plt.figure()
    df['source'].value_counts().nlargest(10).plot(kind='bar')
    plt.title('Top 10 Tweet Sources')
    plt.xlabel('Source')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Language distribution
    plt.figure()
    df['lang'].value_counts().plot(kind='bar')
    plt.title('Language Distribution')
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

    # Tweets by month-year
    plt.figure()
    df['month_year'].value_counts().sort_index().plot(kind='bar')
    plt.title('Tweets per Month–Year')
    plt.xlabel('Month–Year')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# -------------------------------
# Facebook Posts Visualizations
# -------------------------------

def visualize_fb_posts():
    # Columns to load from Facebook Posts dataset
    cols = [
        'incivility_illuminating',
        'scam_illuminating',
        'freefair_illuminating',
        'fraud_illuminating',
        'page_category',
        'admin_country',
        'type',
        'month_year'
    ]
    # Load data
    df = pd.read_csv(
        'data/Dataset_Election/2024_fb_posts_president_scored_anon.csv',  # <-- Update this path if needed
        usecols=cols,
        dtype=str
    ).dropna(how='all')

    # Convert score columns to numeric
    score_cols = cols[:4]
    for c in score_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    # Histogram for score columns
    plt.figure(figsize=(12,4))
    df[score_cols].hist(bins=20, layout=(1, len(score_cols)), edgecolor='black')
    plt.suptitle('Facebook Posts — Score Distributions')
    plt.tight_layout(rect=[0,0.03,1,0.95])
    plt.show()

    # Boxplot for score columns
    plt.figure()
    df[score_cols].boxplot()
    plt.title('Facebook Posts — Score Boxplots')
    plt.tight_layout()
    plt.show()

    # Top 10 for categorical columns
    for col in ['page_category','admin_country','type','month_year']:
        if col in df.columns:
            plt.figure()
            df[col].value_counts().nlargest(10).plot(kind='bar')
            plt.title(f'Facebook Posts — Top 10 {col}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

# -------------------------------
# Facebook Ads Visualizations
# -------------------------------

def visualize_fb_ads():
    # Columns to load from Facebook Ads dataset
    cols = [
        'incivility_illuminating',
        'scam_illuminating',
        'freefair_illuminating',
        'fraud_illuminating',
        'womens_issue_topic_illuminating',
        'currency',
        'delivery_platform',
        'month_year'
    ]
    # Load data
    df = pd.read_csv(
        'data/Dataset_Election/2024_fb_ads_president_scored_anon.csv',  # <-- Update this path if needed
        usecols=cols,
        dtype=str
    ).dropna(how='all')

    # Convert score columns to numeric
    score_cols = cols[:4]
    for c in score_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    # Histogram for score columns
    plt.figure(figsize=(12,4))
    df[score_cols].hist(bins=20, layout=(1, len(score_cols)), edgecolor='black')
    plt.suptitle('Facebook Ads — Score Distributions')
    plt.tight_layout(rect=[0,0.03,1,0.95])
    plt.show()

    # Boxplot for score columns
    plt.figure()
    df[score_cols].boxplot()
    plt.title('Facebook Ads — Score Boxplots')
    plt.tight_layout()
    plt.show()

    # Top 10 for categorical columns
    for col in ['currency','delivery_platform','month_year']:
        if col in df.columns:
            plt.figure()
            df[col].value_counts().nlargest(10).plot(kind='bar')
            plt.title(f'Facebook Ads — Top 10 {col}')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()

# -------------------------------
# Main: Run all visualizations
# -------------------------------

if __name__ == '__main__':
    # Visualize Twitter posts
    visualize_twitter()
    # Visualize Facebook posts
    visualize_fb_posts()
    # Visualize Facebook ads
    visualize_fb_ads()
