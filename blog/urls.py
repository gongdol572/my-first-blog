from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('Bongpyeong.html', views.Bongpyeong, name = 'Bongpyeong'),
    path('jinhae.html', views.jinhae, name = 'jinhae'),
    path('inje.html', views.inje, name = 'inje'),
    path('index.html', views.index, name = 'index'),
    path('gangreung.html', views.gangreung, name = 'gangreung'),
]
