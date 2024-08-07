from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False

    start_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )
    sort_by = forms.ChoiceField(
        choices=[
            ('date_asc', 'Date Ascending'),
            ('date_desc', 'Date Descending'),
            ('category_asc', 'Category Ascending'),
            ('category_desc', 'Category Descending'),
        ],
        required=False
    )
