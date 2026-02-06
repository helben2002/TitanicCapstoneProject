# TitanicCapstoneProject

Project in ML in a course from Lexicon

## Project Structure

```text
titanic-project/
│
├── ml/
│   ├── data/
│   │   └── raw/
│   ├── notebooks/
│   ├── features.py
│   ├── pipeline.py
│   ├── train.py
│   └── model.pkl
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


