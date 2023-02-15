"""wavare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, register_converter

from home.views import welcome, nazare, forecast, location
from home import converters

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="home"),
    path('nazare', nazare, name="nazare"),
    path('forecast/<int:location>/<date:date>/<str:interval>', forecast, name="forecast"),
    path('location', location, name="location"),
    # path('location/<int:id>', location, name="location")
]
