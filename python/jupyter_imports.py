# Load with Jupyter magic %load \..\..
% matplotlib inline

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
from IPython.core.interactiveshell import InteractiveShell

%config InlineBackend.figure_format = "retina"  # Higher resolution plots
InteractiveShell.ast_node_interactivity = "all"  # Multiple outputs
plt.style.use('..\..\material_theme_light.mplstyle')  # My Matplotlib style

# Plot references
# plt.axhline(0, c='#9E9E9E', zorder=1) Origin line
# plt.title('Lorep ipsum', loc='left') Title
# plt.legend(bbox_to_anchor=(1,1), loc='upper left') Legend
# plt.scatter(x, y, alpha=0.5, label='Lorep', s=100, linewidths=0, zorder=2) Scatter
# plt.tick_params(bottom=True) Bottom ticks min, max = ax.get_ylim() or ax.set_ylim() can help
