from allauth.account.forms import SignupForm
from django import forms

from .models import Player

SEX = (
    ("male", "Băiat"),
    ("female", "Fată"),
)


class PlayerSignupForm(SignupForm):
    """
    Form that will be rendered on a user sign up section/screen.
    Default fields will be added automatically.
    Check UserSocialSignupForm for accounts created from social.
    """

    address_line1 = forms.CharField(max_length=180, label="Adresa 1")
    address_line2 = forms.CharField(max_length=180, label="Adresa 2")
    city = forms.CharField(max_length=40, label="Oraș")
    district_county = forms.CharField(max_length=20, label="Sector/Județ")

    parent1 = forms.CharField(max_length=20, label="Părinte")
    parent2 = forms.CharField(max_length=20, label="Părinte")
    mobile1 = forms.CharField(max_length=20, label="Telefon mobil 1")
    mobile2 = forms.CharField(max_length=20, label="Telefon mobil 2")
    email = forms.EmailField(max_length=20, label="Email")

    height = forms.IntegerField(label="Înălțiime")
    weight = forms.IntegerField(label="Greutate")
    sex = forms.ChoiceField(choices=SEX)
    dob = forms.DateField(label="Data nașterii")

    def save(self, request):
        user = super().save(request)
        user.address_line1 = self.cleaned_data["address_line1"]
        user.address_line2 = self.cleaned_data["address_line2"]
        user.city = self.cleaned_data["city"]
        user.district_county = self.cleaned_data["district_county"]

        user.parent1 = self.cleaned_data["parent1"]
        user.parent2 = self.cleaned_data["parent2"]
        user.mobile1 = self.cleaned_data["mobile1"]
        user.mobile2 = self.cleaned_data["mobile2"]
        user.email = self.cleaned_data["email"]

        user.height = self.cleaned_data["height"]
        user.weight = self.cleaned_data["weight"]
        user.sex = self.cleaned_data["sex"]
        user.dob = self.cleaned_data["dob"]

        user.save()

        Player.objects.create(
            user=user,
            address_line1=self.cleaned_data["address_line1"],
            address_line2=self.cleaned_data["address_line2"],
            city=self.cleaned_data["city"],
            district_county=self.cleaned_data["district_county"],
            parent1=self.cleaned_data["parent1"],
            parent2=self.cleaned_data["parent2"],
            mobile1=self.cleaned_data["mobile1"],
            mobile2=self.cleaned_data["mobile2"],
            email=self.cleaned_data["email"],
            height=self.cleaned_data["height"],
            weight=self.cleaned_data["weight"],
            sex=self.cleaned_data["sex"],
            dob=self.cleaned_data["dob"],
        )
        return user
