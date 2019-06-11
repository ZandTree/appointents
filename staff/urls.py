from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('',views.Dashboard.as_view(),name='index'),
    path('tutors/',views.Tutors.as_view(),name='tutors'),
    path('tutor-detail/<int:pk>/',views.TutorDetail.as_view(),name='tutor-detail'),
]
