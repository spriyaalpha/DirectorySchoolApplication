from django.urls import path

from . import views

urlpatterns = [
    path('registration', views.teacher_registration, name='teacher-registration'),
    path('list', views.teacher_list, name='teacher-list'),
    path('profile/<FinalUploadedDetails_id>/', views.teacher_profile, name='teacher-profile'),
    path('list/sort/', views.teacher_list_sort, name='teacher-list-sort'),
    path('load-upazilla', views.load_upazilla, name='load-upazilla'),
]
