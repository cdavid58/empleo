from django.conf.urls import url
from .views import *

urlpatterns=[
	url(r'^Add_Publication/$',Add_Publication,name="Add_Publication"),
	url(r'^All_List_Application_Company/$',All_List_Application_Company,name="All_List_Application_Company"),
	url(r'^Edit_Publication/(\d+)/$',Edit_Publication,name="Edit_Publication"),
]