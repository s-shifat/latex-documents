import numpy as np
import matplotlib.pyplot as plt

labels = ["Contractor Overhead", "Contractor Profit", "Contingency"]
values = [16699.37, 16699.37, 23856.24]

total = 238562.44
percentages = [v / total * 100 for v in values]

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "font.size": 16
})

fig, ax = plt.subplots(figsize=(8, 8))

wedges, _ = ax.pie(
    values,
    startangle=90,
    wedgeprops={"edgecolor": "black", "linewidth": 1.0}
)

for i, w in enumerate(wedges):
    angle = (w.theta1 + w.theta2) / 2
    angle_rad = np.deg2rad(angle)

    x_arrow = 0.9 * np.cos(angle_rad)
    y_arrow = 0.9 * np.sin(angle_rad)

    x_text = 1.25 * np.cos(angle_rad)
    y_text = 1.25 * np.sin(angle_rad)

    annotation = (
        rf"{labels[i]}" "\n"
        rf"\${values[i]:,.2f}" "\n"
        rf"({percentages[i]:.1f}\%)"
    )

    ax.annotate(
        annotation,
        xy=(x_arrow, y_arrow),
        xytext=(x_text, y_text),
        ha="center",
        va="center",
        arrowprops=dict(arrowstyle="-", lw=1.0)
    )

# ax.set_title(r"Distribution of Cost Adders", fontsize=16)
ax.axis("equal")
plt.tight_layout()
fig.savefig("adders.png", dpi=900)
