from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField()

class CitySearch(forms.Form):
    city = forms.CharField(label='City', max_length=100)

class ListAdd(forms.Form):
    list_name = forms.CharField(label='List name', max_length=100)

class PlaceAdd(forms.Form):
    place_name = forms.CharField(label='Place name', max_length=100)

class PlaceSave(forms.Form):
    place_id = forms.CharField(label='Place ID', max_length=100)

class FindFriends(forms.Form):
    username = forms.CharField(label='username', max_length=100)


#1. Search from CityForm
#2. Present the Name
#3. Confirmation page
#4. Add it to the model

# Places Search -- list
#1. for loop in html template + confirmation link
