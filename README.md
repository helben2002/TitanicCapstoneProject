# TitanicCapstoneProject

Project in ML in a course from Lexicon

## Project Structure

```text
titanic-project/
│
├── ml/
│   ├── data/
│   │   └── raw/
│   ├── models/
│   │   └── titanic_model.pkl
│   ├── notebooks/
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
│       └── templates/
│           └── predictor/
│               ├── home.html
│               ├── form.html
│               ├── result.html
│               └── history.html
│
├── docs/
│   ├── architecture.md
│   ├── ml_decisions.md
│   └── scrum_notes.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

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



