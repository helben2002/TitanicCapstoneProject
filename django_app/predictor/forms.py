from django import forms

class PassengerForm(forms.Form):
    Name = forms.CharField(
        label="Passenger Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "e.g. Mr. Owen Harris",
            "class": "form-control"
        })
    )

    Pclass = forms.IntegerField(
        label="Passenger Class",
        min_value=1,
        max_value=3,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    Sex = forms.ChoiceField(
        label="Sex",
        choices=[("male", "Male"), ("female", "Female")],
        widget=forms.Select(attrs={"class": "form-control"})
    )

    Age = forms.FloatField(
        label="Age",
        min_value=0,
        max_value=120,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    SibSp = forms.IntegerField(
        label="Siblings / Spouses aboard",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    Parch = forms.IntegerField(
        label="Parents / Children aboard",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    Fare = forms.FloatField(
        label="Ticket Fare",
        min_value=0,
        widget=forms.NumberInput(attrs={"class": "form-control"})
    )

    Embarked = forms.ChoiceField(
        label="Port of Embarkation",
        choices=[
            ("S", "Southampton"),
            ("C", "Cherbourg"),
            ("Q", "Queenstown")
        ],
        widget=forms.Select(attrs={"class": "form-control"})
    )
