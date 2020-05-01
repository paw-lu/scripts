# Fonts

# If font issues, check out paths in ~/.matplotlib/fontlist-v310.json
# Can also manually remove ~/.matplotlib/tex.cache

# Rebuild font cache

import matplotlib

matplotlib.font_manager._rebuild()

# -----------------------------------------------------------------------------

# Jupyter


%matplotlib inline  # Inline notebook plots
%config InlineBackend.figure_format = "retina"  # Higher resolution plots

# -----------------------------------------------------------------------------
# Plot snippets

fig = plt.figure(figsize=(9, 5))  # Figure size
plt.axhline(0, c="#757575", zorder=1, linewidth=1.2)  # Origin line
plt.title("Lorep ipsum")  # Title
plt.legend(bbox_to_anchor=(1,1), loc="upper left")  # Right vertical legend
plt.legend(bbox_to_anchor=(0, -0.2, 1, 0), ncol=5, loc="upper left", mode="expand")  # Bottom horizonal legend
plt.scatter(x, y, alpha=0.5, label='Lorep', s=100, linewidths=0, zorder=2)  # Scatter
plt.tick_params(bottom=True)  # Bottom ticks min, max = ax.get_ylim() or ax.set_ylim() can help
