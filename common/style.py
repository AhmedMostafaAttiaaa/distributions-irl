"""Shared look for every notebook: a colorblind-safe palette and matplotlib settings.

This file holds only colors and plot settings. All teaching code stays in the notebooks.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

# Okabe-Ito palette: distinguishable under the common forms of color blindness.
PALETTE = {
    "blue": "#0072B2",
    "orange": "#E69F00",
    "green": "#009E73",
    "red": "#D55E00",
    "sky": "#56B4E9",
    "pink": "#CC79A7",
    "yellow": "#F0E442",
    "black": "#000000",
}

# Ordered list, handy for parameter sweeps (several curves on one axis).
COLORS = [PALETTE[name] for name in ("blue", "orange", "green", "red", "sky", "pink")]

# Roles used consistently across lessons.
MAIN = PALETTE["blue"]        # theoretical curve
SIM = PALETTE["orange"]       # simulation / samples
HIGHLIGHT = PALETTE["red"]    # shaded region, answer annotation
NEUTRAL = "#666666"           # mean lines, guides


def apply_style():
    """Apply the shared matplotlib settings."""
    mpl.rcParams.update({
        "figure.figsize": (8, 4.5),
        "figure.dpi": 100,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "legend.fontsize": 11,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": plt.cycler(color=COLORS),
    })
