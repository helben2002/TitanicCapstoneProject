import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from pathlib import Path

from titanic_features import (
    rename_columns,
    impute_missing,
    feature_engineer,
    encode_features,
)

#--------------------------------------------------------------------------

# Select model columns
def prepare_model_data(df):
    keep = ['survived','passenger_class','is_female']

    keep += [c for c in df.columns if c.startswith((
        'title_','fare_group_','age_group_','family_group_','embarked_port_'
    ))]

    df_model = df[keep].copy()

    X = df_model.drop('survived', axis=1)
    y = df_model['survived']

    return X, y
#--------------------------------------------------------------------------

# Prepare data 
def prepare_training_data(df):
    df = rename_columns(df)
    df = impute_missing(df)
    df = feature_engineer(df)
    df = encode_features(df)

    X, y = prepare_model_data(df)

    return X, y
