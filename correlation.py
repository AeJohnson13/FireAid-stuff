# !/usr/bin/env python3
# correlation.py
# Alex Johnson
# 2025-10-07

import pandas as pd
import numpy as np

input_file = "Mini Project Dataset Narrowed.csv"
fireData = pd.DataFrame()
fireData = pd.read_csv(input_file)


# Continuous Variables
Acres = fireData.ESTIMATEDTOTALACRES.to_numpy()

# Discrete Ranges
Slope = fireData.ORIGINSLOPE.to_numpy()
Aspect = fireData.ORIGINASPECT.to_numpy()
Elevation = fireData.ORIGINELEVATION.to_numpy()

# Fuel/Vegetation Bools
Spruce = fireData.SPRUCE.to_numpy()
Tundra = fireData.MUNDRA.to_numpy() # moss and tundra included
Grass = fireData.GRASS.to_numpy()
Brush = fireData.BRUSH.to_numpy()
Hardwood = fireData.HARD.to_numpy()
Leaf = fireData.LEAF.to_numpy()
Unknown = fireData.UNKNOWN.to_numpy()
Other = fireData.OTHER.to_numpy()

from sklearn.linear_model import SGDRegressor
