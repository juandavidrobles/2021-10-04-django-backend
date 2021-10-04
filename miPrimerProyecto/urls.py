"""miPrimerProyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from miPrimerProyecto.views import get_age, get_image, get_image_by_id, get_time, hello, introduction, get_users_list
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('time/', get_time),
    path('image/', get_image),
    path('image/<str:image_id>', get_image_by_id),
    path('age/<int:birth_year>', get_age),
    path('introduction/<str:name>/<str:age>/<str:city>/<str:gender>', introduction),
    path('users-list/', get_users_list)
]
