from django import forms

from .models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = [
            "name", "email", "phone", "message"
        ]

        widgets = {

            "name": forms.TextInput(attrs={
                "class": "form-control",
                # "id": "name",
                "type": "text",
                "placeholder":"Name",
                "required": "required",
                "data-validation-required-message":"Please enter your name."

            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",                
                # "id": "email",
                "type": "email",
                "placeholder":"Email Address",
                "required": "required",
                "data-validation-required-message":"Please enter your email address."
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                # "id": "phone",
                # "type": "tel",
                "placeholder":"Phone Number",
                "required": "required",
                "data-validation-required-message":"Please enter your phone number."
            }),
            "message": forms.Textarea(attrs={
                "class": "form-control",
                # "id": "message",
                "placeholder":"Message",
                "required": "required",
                "data-validation-required-message":"Please enter a message."
            })

        }
        
      