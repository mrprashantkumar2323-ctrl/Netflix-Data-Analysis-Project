# Netflix Data Analysis — Python EDA Project

## Project Overview
An end-to-end Exploratory Data Analysis (EDA) project on Netflix Movies and TV Shows. The project cleans the dataset, analyzes content distribution, release trends, genres, countries, ratings and movie durations, and converts the findings into business-style insights.

### Resume-ready description
**Netflix Data Analysis | Python, Pandas, Matplotlib, Seaborn**
- Performed exploratory data analysis on Netflix's content catalog to understand content distribution, ratings, genres, countries and release trends.
- Cleaned missing values, converted date fields, engineered year/month features and standardized duration fields.
- Created visualizations to identify content trends and translated findings into actionable insights.

## Business Questions
1. How many Movies and TV Shows are available?
2. How has Netflix content changed over release years?
3. Which countries contribute the most titles?
4. What are the most common genres?
5. Which ratings dominate the catalog?
6. How do movie durations vary?
7. Which years saw the largest volume of content added to Netflix?
8. What practical insights can a content analyst derive?

## Dataset
The notebook uses the commonly used `netflix_titles.csv` dataset. If the CSV is not present locally, the notebook downloads a public GitHub mirror at runtime.

Expected columns:
`show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description`

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure
```text
netflix-data-analysis/
├── Netflix_Data_Analysis.ipynb
├── netflix_analysis.py
├── requirements.txt
├── README.md
└── data/
    └── netflix_titles.csv   # optional local copy
```

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook Netflix_Data_Analysis.ipynb
```

Or:
```bash
python netflix_analysis.py
```

## Portfolio Tips
For GitHub, add 3–5 exported charts to an `images/` folder and place them in the README. For LinkedIn, post the dashboard/charts plus 3 concise insights rather than only uploading the notebook.
