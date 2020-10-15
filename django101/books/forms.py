from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all()

    def add_form_control_class_to_all(self):
        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_pages(self):
        pages = self.cleaned_data['pages']
        if pages <= 0:
            raise ValidationError(f'Pages should be a positive number, now they are {pages}')
        return pages

    class Meta:
        model = Book
        fields = '__all__'
