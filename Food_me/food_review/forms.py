from food_review.models import TypeOfFood, Tag
from django import forms


class AddRestaurant(forms.Form):
    """Add a restaurant"""

    resturant_name = forms.CharField(label="Restaurant Name", max_length=255,
                                     widget=forms.TextInput(attrs={'class': "w3-input"}))
    address = forms.CharField(label="Street Address", max_length=255,
                              widget=forms.TextInput(attrs={'class': "w3-input"}))
    city = forms.CharField(label="City", max_length=100,
                           widget=forms.TextInput(attrs={'class': "w3-input"}))
    state = forms.CharField(label="State", max_length=50,
                            widget=forms.TextInput(attrs={'class': "w3-input"}))
    zip_code = forms.CharField(label="Zip Code", max_length=5,
                               widget=forms.TextInput(attrs={'class': "w3-input"}))
    phone_number = forms.CharField(label="Phone Number", max_length=10,
                                   widget=forms.TextInput(attrs={'class': "w3-input"}))

    type_food = forms.ChoiceField(
        choices=[(tq.pk, tq.__str__()) for tq in TypeOfFood.objects.all()])


class AddRestaurantTags(forms.Form):
    tag = forms.MultipleChoiceField(choices=[(tq.pk, tq.__str__()) for tq in Tag.objects.all()],
                                    widget=forms.CheckboxSelectMultiple())


class AddRestaurantReview(forms.Form):
    rating = forms.IntegerField(
        label="How would you rate this restaurant?", max_value=5)
    review = forms.CharField(label="Your review", max_length=500)
