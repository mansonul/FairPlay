from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
User = get_user_model()
SEX = (
    ("male", "Băiat"),
    ("female", "Fată"),
)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="staff")
    photo = models.ImageField(null=True, blank=True, upload_to="images/staff")
    dob = models.DateField(auto_now=False, auto_now_add=False)

    # Address
    address_line1 = models.CharField(max_length=180, null=False, blank=False)
    address_line2 = models.CharField(max_length=180, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    district_county = models.CharField(max_length=20, null=False, blank=False)

    # Contact
    mobile1 = models.CharField(max_length=15, null=False, blank=False)
    mobile2 = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=70, null=False, blank=False)

    def __str__(self):
        return str(self.user)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="player")

    # Address
    address_line1 = models.CharField(max_length=180, null=False, blank=False)
    address_line2 = models.CharField(max_length=180, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    district_county = models.CharField(max_length=20, null=False, blank=False)

    # Contact
    parent1 = models.CharField(max_length=180, null=False, blank=False)
    parent2 = models.CharField(max_length=180, null=True, blank=True)
    mobile1 = models.CharField(max_length=15, null=False, blank=False)
    mobile2 = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=70, null=False, blank=False)

    # Bio
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sex = models.CharField(max_length=10, choices=SEX)
    photo = models.ImageField(null=True, blank=True, upload_to="images/player")
    dob = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return str(self.user)
