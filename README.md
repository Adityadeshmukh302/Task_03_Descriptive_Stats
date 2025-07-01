# Task_03_Descriptive_Stats

This project analyzes three datasets related to the 2024 US presidential election using Python. The datasets are located in the `Dataset_Election` folder and include Facebook Ads, Facebook Posts, and Twitter Posts.

---

## Project Structure

- `src/` — Source code for data analysis
- `requirements.txt` — Python dependencies for all scripts

---

## Getting Started

1. **Ensure you have Python 3.8+ installed.**
2. **(Recommended) Create a virtual environment:**
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

---

## How to Run

1. **Run the analysis scripts**:

    - **Pure Python (no external libraries):**
      ```
      python src/pure_python_stats.py
      ```
    - **Pandas:**
      ```
      python src/pandas_stats.py
      ```
    - **Polars:**
      ```
      python src/polars_stats.py
      ```

2. **Output:**  
   Each script will export results to report files in your project root:
   - `twitter_*_report.txt`
   - `fb_ads_*_report.txt`
   - `fb_posts_*_report.txt`
   (where `*` is `pure_python`, `pandas`, or `polars` depending on the script)

Each report contains:
- Overall numeric and categorical statistics for each dataset
- Grouped summaries by key columns (e.g., by `page_id`, `ad_id`, etc.)

---

## Requirements

All dependencies are listed in `requirements.txt`.  
Example contents:
```txt
pandas
polars
matplotlib
seaborn
```

---

## Summary of Findings

### 2024 Election Social Media Highlights

**Twitter Posts (27,304 tweets)**
- Incivility averages 0.18 (σ = 0.38), though about 5% of tweets spike above 0.75, showing a small tail of very uncivil messages.
- Scam (mean = 0.012, σ = 0.11), freefair (0.0014, σ = 0.038) and fraud (0.0027, σ = 0.052) scores are essentially zero for 99% of tweets.
- 15,017 tweets (55%) come from the Twitter Web App, with 2,933 via Sprout Social and 499 via Media Studio.
- 27,281 tweets (99.9%) are in English; fewer than 30 are in any other language.
- Volume builds through summer, peaking at 3,586 tweets in October and 2,856 in September.

**Facebook Posts (19,009 posts)**
- Incivility avg = 0.128 (σ = 0.334); scam = 0.020 (σ = 0.141); freefair = 0.0028 (σ = 0.0532); fraud = 0.0086 (σ = 0.0924).
- Top page categories: PERSON 9,453, ACTOR 3,304, POLITICIAN 2,595; 2,472 pages uncategorized.
- 16,280 posts come from U.S. pages; 2,729 have no country specified.
- Content mix: 7,404 links, 3,820 photos, 2,931 native videos, plus Live, Status, etc.
- “Total Interactions” shows 5,665 unique values—top 1% of posts rack up over 10,000 reactions, while most stay under 500.
- Organic post volume jumps by ~30% from ~1,500 in August to ~2,000 in October.

**Facebook Ads (246,745 ads)**
- Incivility avg = 0.1875 (σ = 0.3903), slightly above organic posts; scam = 0.0064 (σ = 0.0798); fraud = 0.0026 (σ = 0.0512); women’s-issue avg = 0.0809 (σ = 0.2726).
- 4,475 unique pages ran ads (≈ 55 ads per page on average), for a total of 246,745 distinct ad IDs.
- Ads appear in 18 currencies—82% (≈ 202,524) in USD.
- 214,434 ads (87%) ran on both Facebook & Instagram.
- Ad volume climbs from ~40,000 in September to over 60,000 in October—a 50% month-over-month jump.
- Regional targeting has 141,122 unique entries; demographic targeting 215,622, showing highly granular audience slices.

Over nearly 300,000 tweets, posts, and ads, most of what people shared stayed calm and on‐point. Only a small handful of messages showed really uncivil or aggressive language and those spikes showed up right before Election Day. Now when you look at paid ads, they were a little more heated than regular posts (with average incivility scores around 0.19 compared to 0.13) and about one in twelve ads (roughly 8%) focused on women’s issues. Everywhere you turn, whether it’s organic social posts or paid ads, you see the biggest burst of activity in October 2024, exactly when campaigns were making their final push. This data tells us that, while the overall conversation was measured, keeping an eye on that small uncivil undercurrent could be a useful early warning as critical moments approach.





