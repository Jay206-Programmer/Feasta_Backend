from django.shortcuts import render
from .models import user_info
'''from django.utils.datastructures import MultiValueDictKeyError'''

#from django.contrib.auth.forms import UserCreationForm

'''def login_page(request):
    #form = UserCreationForm()
    #context = {{form}}
    #if request.method =="GET":
    name = request.GET.get('name')
    password = request.GET.get('password')
    context = {'name':name , 'password':password}
    info = user_info.objects.all()
    return render(request, 'login.html', {'info': info})


def add_item(request):
    return render(request, 'Add-Item.html')

def add_item_form_submission(request):
    Product_name = request.GET.get('Product_name',False)
    Price = request.GET.get('Price',False)
    Quantity =request.GET.get('Quantity',False)
    Image = request.GET.get('img',False)
    Description = request.GET.get('Description',False)

    Product_info = user_info(Product_name=Product_name,quantity=Quantity,price=Price,image=Image,description=Description) 
    Product_info.save()
    return render(request , 'Add-Item.html')'''

def index(request):
    dests = user_info.objects.all()
    print(dests)
    return render(request, "Admin-Menu.html", {'dests':dests})