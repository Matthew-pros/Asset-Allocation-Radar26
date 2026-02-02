import matplotlib.pyplot as plt
import numpy as np

def plot_radar(z_scores):
    labels = list(z_scores.keys())
    values = list(z_scores.values())
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)
    values += values[:1]
    angles = list(angles) + [angles[0]]

    fig, ax = plt.subplots(subplot_kw=dict(polar=True))
    ax.plot(angles, [v+3 for v in values])
    ax.fill(angles, [v+3 for v in values], alpha=0.3)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)
    plt.show()
