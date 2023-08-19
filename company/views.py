from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .operations_c import Company_O, Publication
from django.http import QueryDict
from home.operation_home import Home_O

def Add_Publication(request):
	if request.method == 'POST':
		mutable_post_data = request.POST.copy()
		mutable_post_data['availability_travel'] = int('availability_travel' in request.POST)
		mutable_post_data['change_residence'] = int('change_residence' in request.POST)
		Publication().Create_Publication(mutable_post_data,request.session['pk_user'])

	return render(request,'company/add_publication.html',{
		'area':Company_O().Get_Area(),'city':Company_O().Get_City(),
		'Type_Contract':Company_O().Type_Contract(),'Workday':Company_O().Workday(),
		'Workplace':Company_O().Workplace(),'Minimum_Studiess':Company_O().Minimum_Studiess(),
		'languages':Company_O().languages(),'Languages_Levels':Company_O().Languages_Levels()
	})


def All_List_Application_Company(request):
	data = Publication().All_List_Application_Company(request.session['pk_user'])
	items_per_page = 4
	paginator = Paginator(data, items_per_page)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'company/list_publications.html', {'page_obj': page_obj})

def Edit_Publication(request,pk):
	data = Home_O().Get_Publication(pk)
	print(data)
	return render(request,'company/edit_publication.html',{'data':data,
		'area':Company_O().Get_Area(),'city':Company_O().Get_City(),
		'Type_Contract':Company_O().Type_Contract(),'Workday':Company_O().Workday(),
		'Workplace':Company_O().Workplace(),'Minimum_Studiess':Company_O().Minimum_Studiess(),
		'languages':Company_O().languages(),'Languages_Levels':Company_O().Languages_Levels()
		})






