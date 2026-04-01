import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Data
# -----------------------------
categories = [
    "Direct Construction",
    "Indirect",
    "Engineering \& Design",
    "Overhead",
    "Profit",
    "Contingency"
]

values = [
    210062.44,
    28500.00,
    28000.00,
    16699.37,
    16699.37,
    23856.24
]

# -----------------------------
# LaTeX-style font settings
# -----------------------------
plt.rcParams.update({
    "text.usetex": True,  # requires LaTeX installed
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 16
})

# -----------------------------
# Plot
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.bar(categories, values, edgecolor="black")

# Rotate labels for readability
plt.xticks(rotation=25, ha='right')

# -----------------------------
# Annotate bars
# -----------------------------
for bar in bars:
    height = bar.get_height()
    ax.annotate(
        rf"\${height:,.0f}",
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 5),
        textcoords="offset points",
        ha='center',
        va='bottom'
    )

# -----------------------------
# Labels and title
# -----------------------------
ax.set_ylim(0, max(values) * 1.09)
ax.set_ylabel(r"Cost (\$)")
# ax.set_title(r"Comparison of Major Cost Components")

# Optional: add grid for readability
ax.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
fig.savefig("costing.png", dpi=900)
