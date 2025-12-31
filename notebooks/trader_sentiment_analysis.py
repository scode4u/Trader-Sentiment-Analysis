import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

fear_greed_path = os.path.join(BASE_DIR, "data", "raw", "fear_greed_index.csv")
trades_path = os.path.join(BASE_DIR, "data", "raw", "historical_data.csv")


fear_greed = pd.read_csv(fear_greed_path)
trades = pd.read_csv(trades_path)


fear_greed.columns = fear_greed.columns.str.lower()
trades.columns = trades.columns.str.lower()


trades = trades.rename(columns={
    'account': 'account',
    'coin': 'symbol',
    'execution price': 'execution_price',
    'size tokens': 'size',
    'side': 'side',
    'closed pnl': 'closedpnl',
    'timestamp': 'time'
})


trades['time'] = pd.to_datetime(trades['time'])
trades['date'] = trades['time'].dt.date

fear_greed['date'] = pd.to_datetime(fear_greed['date']).dt.date


merged = trades.merge(fear_greed, on='date', how='left')


merged['is_profitable'] = merged['closedpnl'] > 0

summary = merged.groupby('classification').agg(
    avg_pnl=('closedpnl', 'mean'),
    total_trades=('closedpnl', 'count'),
    win_rate=('is_profitable', 'mean')
).reset_index()

plt.figure(figsize=(8, 5))
plt.bar(summary['classification'], summary['avg_pnl'])
plt.xlabel("Market Sentiment")
plt.ylabel("Average PnL")
plt.title("Average PnL by Market Sentiment")
plt.tight_layout()
plt.show()

print("Script executed successfully!")
