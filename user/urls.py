from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Login/$',Login,name="Login"),
	url(r'^LogOut/$',LogOut,name="LogOut"),
	url(r'^Settings_Profile/$',Settings_Profile,name="Settings_Profile"),
	url(r'^Profile/$',Profile,name="Profile"),
	url(r'^Update_Information_Person/$',Update_Information_Person,name="Update_Information_Person"),
	url(r'^Register_Company/$',Register_Company,name="Register_Company"),
	url(r'^Register_User/$',Register_User,name="Register_User"),
	url(r'^Create_Studies/$',Create_Studies,name="Create_Studies"),
	url(r'^Validation_Email/$',Validation_Email,name="Validation_Email"),
	url(r'^verified_company/(\d+)/(\w+)/$',verified_company,name="verified_company"),
]