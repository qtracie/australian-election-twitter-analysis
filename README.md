# Australian Election 2019 Tweets Analysis

This repository contains a text mining and time-series-style social media analysis project for **OPIM 5671: Data Mining and Time Series Forecasting** at the University of Connecticut.

The project analyzes more than 180,000 tweets related to the **2019 Australian Federal Election** collected from Kaggle between **May 10 and May 20, 2019**. The analysis combines classical NLP, sentiment and emotion mining, topic modeling, predictive modeling, and transformer-based evaluation.

## Project Overview

The goal of this project is to understand public discourse around the 2019 Australian election by answering questions such as:

- What were the dominant themes in election-related tweets?
- How did sentiment and emotion change before, during, and after Election Day?
- Which tweet features were associated with higher retweets and favorites?
- Do emotional tweets receive more engagement than neutral tweets?
- How do classical NLP models compare with transformer-based approaches?

## Repository Structure

```text
.
├── notebooks/
│   └── australian_election_twitter_analysis.ipynb
├── presentation/
│   └── australian_election_twitter_analysis_presentation.pptx
├── src/
│   └── text_processing.py
├── data/
│   └── README.md
├── outputs/
│   └── figures/
├── docs/
│   └── project_summary.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The notebook downloads the dataset directly from Kaggle using `kagglehub`:

**Dataset:** Australian Election 2019 Tweets  
**Source:** Kaggle  
**Approximate size:** 183,379 tweets  
**Date range:** May 10–20, 2019  
**Primary text column:** `full_text`

Because the dataset is publicly available and may be large, the raw CSV file is not included in this repository. Re-run the notebook to download the data automatically.

## Methods Used

### 1. Data Processing

- Parsed tweet timestamps
- Handled missing values while preserving valid tweet text
- Cleaned tweet text using lowercase conversion, tokenization, stopword removal, special-character filtering, and lemmatization
- Added domain-specific stopwords such as election hashtags and Twitter noise terms

### 2. Feature Engineering

Created features including:

- TextBlob sentiment polarity and subjectivity
- NRC emotion scores: joy, trust, fear, surprise, sadness, disgust, anger, and anticipation
- Positive and negative valence scores
- Word count, character count, lexical diversity, and readability
- Hashtag, mention, and URL indicators
- Popularity score = retweet count + favorite count

### 3. Exploratory Data Analysis

- Word frequency analysis
- Word clouds for tweet content and user profiles
- Daily and hourly tweet activity patterns
- Hashtag and mention analysis
- Influential user analysis using total engagement

### 4. Sentiment and Emotion Analysis

- Sentiment category distribution: positive, neutral, and negative
- Daily sentiment trend around Election Day
- NRC emotion profile analysis
- Engagement comparison across sentiment groups

### 5. Topic Modeling

- Built LDA topic models using Gensim
- Evaluated topic coherence across different numbers of topics
- Interpreted five major topic groups:
  - Election day culture and democracy sausage
  - Political leaders and controversies
  - Voting activity and public participation
  - Policy debate: climate, tax, and government
  - Party competition and voter support

### 6. Predictive Modeling

- Linear regression models for sentiment, positivity, retweets, and favorites
- Log transformations for skewed engagement variables
- Feature groups included sentiment, emotion, text structure, and topic indicators
- Compared train/test performance using R² and error metrics

### 7. Transformer Models

- Benchmarked a classical TF-IDF + Logistic Regression pipeline
- Explored transformer-based sentiment classification approaches
- Discussed limitations of evaluating transformer models against rule-based silver labels

## Key Findings

- Tweet volume peaked sharply on **May 18, 2019**, Election Day.
- Sentiment was mostly neutral to slightly positive overall.
- Negative and positive tweets tended to receive more engagement than neutral informational tweets.
- Hashtags, URLs, and mentions were stronger engagement predictors than sentiment or emotion.
- Emotion scores had very weak correlation with retweets and favorites.
- Topic-level emotion analysis revealed more nuance than aggregate sentiment analysis.
- Evaluation against TextBlob labels can reward models for mimicking rule-based sentiment rather than capturing human nuance.

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/australian-election-twitter-analysis.git
cd australian-election-twitter-analysis
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
# .venv\Scripts\activate       # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Open the notebook:

```bash
jupyter notebook notebooks/australian_election_twitter_analysis.ipynb
```

5. Run the notebook from top to bottom.

## Notes

- Some cells may take time because the notebook processes a large tweet dataset.
- Transformer-related cells may require more memory and are best run in Google Colab or an environment with GPU support.
- If Kaggle authentication is required, configure your Kaggle credentials before running the dataset download step.

## Course Context

**Course:** OPIM 5671 — Data Mining and Time Series Forecasting  
**Institution:** University of Connecticut  
**Term:** Spring 2026  
**Project Type:** Term Project #2 — Text Mining and NLP Analysis

## Author

Quynh Trang Le and project team  
MS in Business Analytics and Project Management  
University of Connecticut
