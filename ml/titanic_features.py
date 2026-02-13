import pandas as pd

#--------------------------------------------------------------------------

# Rename columns
def rename_columns(df):
    df = df.copy()
    df.columns = df.columns.str.lower()

    rename_map = {
        'passengerid': 'passenger_id',
        'pclass': 'passenger_class',
        'sibsp': 'sibling_spouse_count',
        'parch': 'parent_child_count',
        'ticket': 'ticket_number',
        'embarked': 'embarked_port'
    }

    return df.rename(columns=rename_map)
#--------------------------------------------------------------------------

# Handle missing values
def impute_missing(df):
    df = df.copy()

    df["embarked_port"] = df["embarked_port"].fillna(df["embarked_port"].mode()[0])

    df["age"] = df["age"].fillna(
        df.groupby(["passenger_class", "sibling_spouse_count", "parent_child_count"])["age"]
        .transform("median")
    )

    df["age"] = df["age"].fillna(df["age"].median())

    return df
#--------------------------------------------------------------------------

# Feature engineering
AGE_BINS = [0, 13, 18, 30, 50, 100]
AGE_LABELS = ['child', 'teenager', 'young_adult', 'adult', 'senior']

FARE_BINS = [0, 16, 30, 1000]
FARE_LABELS = ['low', 'medium', 'high']

FAMILY_SIZE_BINS = [0, 1, 4, 20]
FAMILY_SIZE_LABELS = ['alone', 'small', 'large']


def extract_title(name):
    title = name.str.extract(r',\s*([^\.]+)\.')
    title_map = {'Mlle': 'Miss', 'Ms': 'Miss', 'Mme': 'Mrs'}
    title = title.replace(title_map)

    rare = ['Lady','the Countess','Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona']
    title = title.replace(rare, 'other')

    return title


def feature_engineer(df):
    df = df.copy()

    df["age_group"] = pd.cut(df["age"], AGE_BINS, labels=AGE_LABELS)
    df["fare_group"] = pd.cut(df["fare"], FARE_BINS, labels=FARE_LABELS)

    df["family_size"] = df["sibling_spouse_count"] + df["parent_child_count"] + 1
    df["family_group"] = pd.cut(df["family_size"], FAMILY_SIZE_BINS, labels=FAMILY_SIZE_LABELS)

    df["title"] = extract_title(df["name"])

    df["is_female"] = df["sex"].map({"male":0, "female":1})

    return df
#--------------------------------------------------------------------------

# Encoding
def encode_features(df):
    cols = ['title','age_group','fare_group','family_group','embarked_port']

    return pd.get_dummies(df, columns=cols, dtype=int)