# TitanicCapstoneProject

Project in ML in a course from Lexicon

Project Structure

titanic-project/
│
├── ml/                         # Machine learning development (offline)
│   ├── data/
│   │   └── raw/                # Original Kaggle Titanic dataset
│   ├── notebooks/              # EDA and experimentation
│   ├── features.py             # Feature engineering logic
│   ├── pipeline.py             # Preprocessing and model pipeline
│   ├── train.py                # Model training and evaluation
│   └── model.pkl               # Saved trained pipeline
│
├── django_app/                 # Django web application
│   ├── manage.py
│   │
│   ├── config/                 # Django project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   ├── prediction/             # Django app for model inference
│   │   ├── migrations/
│   │   ├── models.py           # Database models for predictions
│   │   ├── views.py            # Request handling and result rendering
│   │   ├── forms.py            # Input validation
│   │   ├── ml_service.py       # Loads and runs the ML model
│   │   ├── urls.py             # App-specific routing
│   │   └── templates/
│   │       └── prediction/
│   │           ├── home.html
│   │           ├── form.html
│   │           ├── result.html
│   │           └── history.html
│
├── docs/                       # Project documentation
│   ├── architecture.md         # System architecture overview
│   ├── ml_decisions.md         # ML design and feature choices
│   └── scrum_notes.md          # Scrum process and reflections
│
├── README.md                   # Project overview and setup instructions
├── requirements.txt            # Python dependencies
└── .gitignore

