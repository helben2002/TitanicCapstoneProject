# TitanicCapstoneProject

Project in ML in a course from Lexicon

Project Structure

titanic-project/
│
├── ml/ # Machine learning development
│ ├── data/ # Raw and processed Titanic data
│ ├── notebooks/ # Experimentation
│ ├── features.py # Feature engineering logic
│ ├── pipeline.py # Preprocessing and model pipeline
│ ├── train.py # Model training and evaluation
│ └── model.pkl # Saved trained pipeline
│
├── django_app/ # Django web application
│ ├── manage.py
│ │
│ ├── config/ # Django project configuration
│ │ ├── settings.py
│ │ ├── urls.py
│ │ ├── asgi.py
│ │ └── wsgi.py
│ │
│ ├── predictor/ # Django app
│ │ ├── models.py # Database models for inputs and predictions
│ │ ├── views.py # Request handling and result rendering
│ │ ├── forms.py # Input validation
│ │ ├── ml_service.py # Loads and runs the ML model
│ │ ├── urls.py # App-specific routing
│ │ └── templates/
│ │ └── predictor/
│ │ ├── home.html
│ │ ├── form.html
│ │ ├── result.html
│ │ └── history.html
│
├── docs/ # Project documentation
│ ├── architecture.md # System architecture overview
│ ├── ml_decisions.md # ML design and feature choices
│ └── scrum_notes.md # Scrum process and reflections
│
├── README.md # Project overview and instructions
├── requirements.txt # Python dependencies
└── .gitignore
