from django import forms


class QuestionForm(forms.Form):

    name_attrs = {'placeholder': 'Имя', 'class': 'input-contacts'}
    phone_attrs = {'placeholder': 'Телефон', 'class': 'input-contacts'}
    question_attrs = {'placeholder': 'Комментарий', 'class': 'input-contacts'}

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=name_attrs))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs=phone_attrs))
    question = forms.CharField(max_length=255, widget=forms.TextInput(attrs=question_attrs), required=False)
