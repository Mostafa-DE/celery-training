from re import A
from django import forms


class ReviewForm(forms.Form):
    name = forms.CharField(
        label="First Name",
        max_length=50,
        min_length=4,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "placeholder": "First Name",
                "id": "form-firstname"
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        max_length=100,
        min_length=10,
        attrs={
            "class": "form-control mb-3",
            "placeholder": "Email",
            "id": "form-email"
        }
    )

    review = forms.CharField(
        label="Review",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": "5"
            }
        )
    )

    def send_email(self):
        send_review_email_task.delay(
            self.cleaned_data["name"], self.cleaned_data["email"], self.cleaned_data["review"]
        )
