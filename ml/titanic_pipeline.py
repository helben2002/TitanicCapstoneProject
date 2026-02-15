from ml.titanic_features import (
    rename_columns,
    impute_missing,
    feature_engineer,
    encode_features,
)

#--------------------------------------------------------------------------

MODEL_FEATURES = [
    'passenger_class', 
    'is_female', 
    'title_Master', 
    'title_Miss', 
    'title_Mr', 
    'title_Mrs', 
    'title_Sir', 
    'title_other', 
    'age_group_child', 
    'age_group_teenager', 
    'age_group_young_adult', 
    'age_group_adult', 
    'age_group_senior', 
    'fare_group_low', 
    'fare_group_medium', 
    'fare_group_high', 
    'family_group_alone', 
    'family_group_small', 
    'family_group_large', 
    'embarked_port_C', 
    'embarked_port_Q', 
    'embarked_port_S'
]
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

    # Ensure correct column order for modeling
    X = X[MODEL_FEATURES]  

    return X, y
