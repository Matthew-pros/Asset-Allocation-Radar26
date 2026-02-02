import pandas as pd

def calculate_z_scores(data, window=252):
    z_scores = {}
    for col in data.columns:
        prices = data[col].dropna()
        if len(prices) < window:
            continue
        mean = prices.rolling(window).mean()
        std = prices.rolling(window).std()
        z_scores[col] = (prices.iloc[-1] - mean.iloc[-1]) / std.iloc[-1]
    return z_scores
