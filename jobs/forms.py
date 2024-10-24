from django import forms
from .models import Application
from ckeditor.fields import RichTextFormField


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["name", "email", "phone_number", "cover_letter", "resume"]

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control p-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control p-3"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control p-3"}),
            "cover_letter": RichTextFormField(),
            "resume": forms.FileInput(attrs={"class": "form-control p-3"}),
        }


class JobSearchForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        label="keyword",
        widget=forms.TextInput(
            attrs={
                "type": "search",
                "class": "form-control border-0 rounded-0 customer-input",
                "placeholder": "Search job title or keyword",
                "aria-label": "Search jot title or keyword",
                "aria-describedby": "basic-addon1",
            }
        ),
    )
    location = forms.CharField(
        required=False,
        label="location",
        widget=forms.TextInput(
            attrs={
                "type": "search",
                "class": "form-control border-0 rounded-0 customer-input",
                "placeholder": "Country or timezone",
                "aria-label": "Country or timezone",
                "aria-describedby": "basic-addon1",
            }
        ),
    )
