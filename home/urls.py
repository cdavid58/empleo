from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^$',Index,name="Index"),
	url(r'^View_Publication/(\d+)/$',View_Publication,name="View_Publication"),
	url(r'^List_Application/$',List_Application,name="List_Application"),
	url(r'^Delete_Aplication/$',Delete_Aplication,name="Delete_Aplication"),
]