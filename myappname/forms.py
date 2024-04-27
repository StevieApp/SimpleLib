# Copyright 2024 Steve Nginyo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django import forms    
from .models import BookClub

class RegisterForm(forms.Form):
    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )
    profile_pic = forms.ImageField(
        label="Profile Pic",
        allow_empty_file=True,
        widget = forms.FileInput(
            attrs = {
                "id": "image_field", # you can access your image field with this id for css styling . 
                # "style": "height: 100px ; width : 100px ; border-radius: 50%" # add style from here .
            }
        ),
    )
    username = forms.CharField(label='Username', max_length=50, required=True, min_length=4)
    name = forms.CharField(label='Full Name', max_length=50, required=True, min_length=2)
    email = forms.EmailField(label='Email Address', max_length=100, required=True, min_length=2)
    gender = forms.ChoiceField(required=True, choices=GENDERS)
    book_club = forms.ChoiceField(choices=BookClub.objects.values)
    password = forms.CharField(label="Password", widget=forms.PasswordInput())
    c_password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())
    