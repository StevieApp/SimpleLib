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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name="home"),
    path('about/', views.hello, name="about"),
    path('user_register/', views.user_register, name="user_register"),
    path('random_activity/', views.random_activity, name="random_activity"),
    path('simple_gallery/', views.simple_gallery, name="simple_gallery"),
    path('search_gallery/', views.search_gallery, name="search_gallery"),
    path('library/', views.library, name="library"),
    path('login/', views.user_login, name="login"),
]