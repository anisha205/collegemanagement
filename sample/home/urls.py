from django.urls import path
from . import views

urlpatterns = [
path('profile/',views.Profile.as_view(),name='profile'),
path('loginhome/',views.Loginhome.as_view(),name='loginhome'),
path('editprofile/',views.Editprofile.as_view(),name='editprofile'),
path('staff/',views.Staffs.as_view(),name='staff'),
path('eniqury/',views.Enquiry.as_view(),name='eniqury'),
# path('profile/',views.Profile.as_view(),name='profile'),
path('students/',views.students.as_view(),name='students'),
path('conformation/',views.Conformation.as_view(),name='conformation'),
path('edit/',views.Edit.as_view(),name='edit'),
path('delete/',views.Delete.as_view(),name='delete'),
]