from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .operation_home import Home_O

def Index(request):
    data = Home_O().All_List_Application()
    items_per_page = 4
    paginator = Paginator(data, items_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ecommerce/product-list.html', {'page_obj': page_obj})

def View_Publication(request,pk):
    data = Home_O().Get_Publication(pk)
    result = False
    if 'pk_user' in request.session:
        for i in data['list_user']:
            if int(i['pk_user']) == int(request.session['pk_user']):
                result = True
    if request.is_ajax():
        result = Home_O().Applicat_Publication(request.session['pk_user'],data['pk_publication'])
        return HttpResponse(True)
    return render(request,'ecommerce/product_details.html',{'data':data,'applicat': result})

def List_Application(request):
    if 'pk_user' in request.session:
        data = Home_O().Get_All_List_Applications(request.session['pk_user'])
        items_per_page = 4
        paginator = Paginator(data['data'], items_per_page)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'applications.html', {'page_obj': page_obj, 'total_application':data['number_applications']})
    return redirect('Login')


def Delete_Aplication(request):
    if request.is_ajax():
        data = request.GET
        print(data)
        result = Home_O().Delete_Application_Publication(data['pk_publication'], request.session['pk_user'])['result']
        return HttpResponse(result)