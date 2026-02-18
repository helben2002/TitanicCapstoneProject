# TitanicCapstoneProject

## Project Overview and Purpose

The Titanic++ Capstone Project is a machine learning and web application project to predict the likelihood of survival for passengers aboard the Titanic. It combines data preprocessing, feature engineering, and predictive modeling with a Django web interface for user input and a database for storing predictions.

### Project Goals
**1. Data Analysis and Feature Engineering**  
    - Clean and preprocess raw Titanic dataset from Kaggle  
    - Engineer features such as `age_group`, `fare_group`, `title`, `family_group` and `is_female`  
    - Encode categorical variables  
**2. Machine Learning Model Development**  
    - Train different models using the preprocessed data  
    - Evaluate performancy using accuracy, confusion matrix, classification report, and cross-validation  
    - Select a model  
    - Save the trained model  
**3. Web Application for Predictions**  
    - Build a Django web app with a home page, a prediction page, and a history page, where users can input passenger information to predict their likelihood of survival  
    - Use a prediction service to map user input to the ML model schema and return predictions  
    - Saven predictions, probabilities, and input data in a database  

## Project Structure

<pre> 
titanic-project/
│  
├── ml/  
│   ├── data/  
│   │   ├── raw/  
│   │   │   ├── test.csv   
│   │   │   ├── train.csv
│   │   │   
│   │   ├── processed/  
│   │   │   ├── test_cleaned.csv   
│   │   │   ├── train_cleaned.csv       
│   ├── models/  
│   │   └── titanic_model.pkl  
│   ├── notebooks/  
│   ├── submissions/       
│   ├── predict_service.py  
│   ├── predict.py  
│   ├── titanic_features.py  
│   ├── titanic_pipeline.py  
│   └── titanic_train.py  
│  
├── django_app/  
│   ├── manage.py  
│   ├── config/  
│   │   ├── settings.py  
│   │   ├── urls.py  
│   │   ├── asgi.py  
│   │   └── wsgi.py  
│   │  
│   └── predictor/
│       ├── migrations/
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       ├── ml_service.py
│       ├── urls.py
├── templates/
│   └── predictor/
│       ├── base.html
│       ├── history.html
│       ├── home.html
│       └── predict.html
├── static/
│   ├── images/ 
│   ├── css/    
│
├── README.md
├── requirements.txt
└── .gitignore
</pre>

## How to setup and run the Project locally

### Prerequisites

#### Make sure you have the following installed:

- Git
- Python 3.x
- pip

### 1. Clone the repository
```git clone https://github.com/helben2002/TitanicCapstoneProject.git```
```cd TitanicCapstoneProject```


### 2. Create and activate virtual Environment
Windows
```python -m venv .venv```
```source .venv/bin/activate```


### 3. Install dependencies
```pip install -r requirements.txt```


### 4. Run database migrations
```python manage.py migrate```


### Optional: Seed prediction data
#### If you want example prediction data for testing or demo purposes, run:
```python manage.py seed_predictions```


### 5. Run the development server
```python manage.py runserver```


### 6. Open the application
Go to:
```http://127.0.0.1:8000/```



