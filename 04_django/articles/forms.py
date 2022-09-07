from cProfile import label
from tkinter import Widget
from django import forms
from .models import Article
from articles.models import Article

# class ArticleForm(forms.Form):
    # NATION_A ='kr'
    # NATION_B ='ch'
    # NATION_C ='jp'
    # NATIONS_CHOICES = [
    #     (NATION_A, '한국'),
    #     (NATION_B, '중국'),
    #     (NATION_C, '일본'),
    # ]
    # title = forms.CharField(max_length = 10)
    # content = forms.CharField(widget=forms.Textarea)
    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder' : 'Enter the title',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder' : 'Enter the title',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={
            'required' : 'Please enter your content',
        }
    )
    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)  