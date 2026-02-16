from django import forms

class PassengerForm(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder" : "e.g. Mr. Owen Harris"
    }))
    Pclass = forms.IntegerField()
    Sex = forms.ChoiceField(choices=[("male", "Male"), ("female", "Female")])
    Age = forms.FloatField()
    SibSp = forms.IntegerField()
    Parch = forms.IntegerField()
    Fare = forms.FloatField()
    Embarked = forms.ChoiceField(
        choices=[("S","Southampton"), ("C","Cherbourg"), ("Q","Queenstown")]
    )
