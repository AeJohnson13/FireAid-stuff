# !/usr/bin/env python3
# correlation.py
# Alex Johnson
# 2025-10-07

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from operator import itemgetter

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn import metrics
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.neural_network import MLPClassifier

input_file = "Mini Project Dataset Narrowed.csv"
fireData = pd.DataFrame()
fireData = pd.read_csv(input_file)

