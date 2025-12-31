# Trader Sentiment Analysis

This project analyzes the relationship between cryptocurrency market sentiment
(Fear & Greed Index) and trader behavior using historical trade data.

The objective is to understand how sentiment impacts trading performance,
risk-taking behavior, and profitability.

## Key Highlights
- Cleaned and standardized raw trading data
- Merged market sentiment with trade-level data
- Analyzed PnL behavior across sentiment phases
- Built reproducible and modular analysis pipeline

## Tech Stack
- Python
- Pandas
- Matplotlib
- Jupyter / Script-based workflow

## How to Run
```bash
pip install pandas matplotlib
python trader_sentiment_analysis.py

trader_sentiment_analysis/
│
├── data/
│   ├── raw/
│   │   ├── fear_greed_index.csv
│   │   └── historical_data.csv
│
├── notebooks/
│   └── trader_sentiment_analysis.py
│
├── README.md
