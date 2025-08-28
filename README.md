# Myntra Women’s Dresses – Data Analysis Task  

## Project Overview  
This repository contains my work for the Datahut Internship task. The dataset provided consisted of information about women’s dresses listed on Myntra. The objective was to clean the dataset, perform exploratory data analysis (EDA), and summarize the findings.  
The focus of the task was not on building an app but on working with the data to extract useful insights.  

---

## Files in this Repository  
- **Datahut Internship.ipynb** – Jupyter Notebook containing the cleaning and analysis steps.  
- **myntra_womens_dresses_clean.csv** – Cleaned version of the dataset.
- **visualizations** – Images of visualizations
- **report.pdf** – Short summary report (2–3 pages) highlighting the process, findings, and challenges.  
- **README.md** – This file.  

---

## Steps Performed  
1. **Data Cleaning**  
   - Removed duplicate entries based on product URL.  
   - Standardized brand names for consistency.  
   - Converted price, discount, and ratings into numeric formats.  
   - Added a new column for discount percentage.  

2. **Exploratory Data Analysis (EDA)**  
   - Looked at the most popular brands by count.  
   - Analyzed pricing patterns and distribution.  
   - Studied discounts and their variation across brands.  
   - Checked product ratings and reviews.  
   - Created visualizations to summarize these findings.  

---

## Key Insights  
- A few brands dominate the product listings, while many brands have very few items.  
- Discounts are common, with some brands offering higher average discounts than others.  
- Most products fall within a mid-range price bracket, with a small number of very high-priced outliers.  
- Many products have no ratings or reviews, which can affect customer trust.  

---

## Challenges Faced  
- **Inconsistent formatting** in brand and price columns, which required cleaning.  
- **Missing data** in ratings and reviews. I chose to leave them as missing instead of filling them artificially.  
- **Outliers** in price values. These were handled carefully while plotting distributions.  

---

## Tools Used  
- **Python** – Data cleaning and analysis  
- **Pandas** – Data manipulation  
- **Matplotlib & Seaborn** – Visualization  
- **Jupyter Notebook** – For documentation and workflow  

---


## Conclusion
This task helped me practice real-world data cleaning and exploratory analysis. It showed how data can be messy and inconsistent, and how careful preprocessing is important before deriving insights.
The final cleaned dataset and the report provide a clear summary of the main patterns in the Myntra women’s dresses data.
