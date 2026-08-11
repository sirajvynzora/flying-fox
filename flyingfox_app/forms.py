

from django import forms
from .models import Offer, Testimonial


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ["name", "image", "review"]




from django import forms

from .models import ContactEnquiry


class ContactEnquiryForm(forms.ModelForm):

    class Meta:

        model = ContactEnquiry

        fields = [
            "name",
            "email",
            "subject",
            "message",
        ]


    def clean_name(self):

        name = self.cleaned_data.get(
            "name",
            ""
        ).strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "Please enter a valid name."
            )

        return name


    def clean_subject(self):

        subject = self.cleaned_data.get(
            "subject",
            ""
        ).strip()

        if len(subject) < 3:
            raise forms.ValidationError(
                "Please enter a valid subject."
            )

        return subject


    def clean_message(self):

        message = self.cleaned_data.get(
            "message",
            ""
        ).strip()

        if len(message) < 10:
            raise forms.ValidationError(
                "Please enter a little more information."
            )

        return message



class OfferForm(forms.ModelForm):

    class Meta:
        model = Offer
        fields = [
            "title",
            "description",
            "banner_image",
            "rides",
            "discount_type",
            "discount_value",
            "start_date",
            "end_date",
            "is_active",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Offer title"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "banner_image": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),
            "rides": forms.CheckboxSelectMultiple(),
            "discount_type": forms.Select(
                attrs={"class": "form-control"}
            ),
            "discount_value": forms.NumberInput(
                attrs={"class": "form-control", "step": "0.01"}
            ),
            "start_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "end_date": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "is_active": forms.CheckboxInput(
                attrs={"class": "toggle-switch-input"}
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError(
                "Start date cannot be after end date."
            )

        return cleaned_data
    
