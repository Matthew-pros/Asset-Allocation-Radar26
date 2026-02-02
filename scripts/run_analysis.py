from asset_radar.config import ASSETS
from asset_radar.data_loader import fetch_prices
from asset_radar.analytics import calculate_z_scores
from asset_radar.visualization import plot_radar

data = fetch_prices(ASSETS.keys(), years=5)
z = calculate_z_scores(data)
plot_radar(z)
