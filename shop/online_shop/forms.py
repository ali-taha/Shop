from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Store, Product, Basket


User = get_user_model()

class RegisterSeller(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username", "email", "password", "phone_number",]

        widgets = {"password": (forms.PasswordInput)}

        labels = {
            "username": ("username"),
            "password": ("password"),
            "email": ("email"),
            "phone_number": ("phone_number"),
        }

        def clean_repeat_password(self):
            repeat_password = self.cleaned_data["repeat_password"]
            new_password = self.cleaned_data["new_password"]
            if new_password != repeat_password:
                raise ValidationError("password and repeat password must be same")
            return repeat_password



class SelllerLoginForm(forms.Form):
    username = forms.CharField(max_length=120, label="username")
    password = forms.CharField(
        max_length=120, widget=forms.PasswordInput, label="password"
    )            

class CreateStoreForm(forms.ModelForm):

    class Meta:
        model = Store
        fields = ["title", "description", "type", "location_lat","location_lng"]

class AddProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['store'].queryset = Store.alive.filter(owner=self.request.user)
    store = forms.ModelChoiceField(queryset = Store.alive.filter())
    

    class Meta:
        model = Product 
        fields = ["store", "category", "title", "tag", "stock", "image", "description", "price"]      

class UpdateBasketForm(forms.ModelForm):

    class Meta:
        model = Basket
        fields = ["status"]
