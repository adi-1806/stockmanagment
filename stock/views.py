from django.shortcuts import render,redirect
from .models import motor_products, other_products
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        entered_username=request.POST['username']
        entered_password=request.POST['password']
        if entered_username=='krishna' and entered_password=='kittu':
            return redirect(request,"/stock/stock.html")
        else:
            messages.info(request, 'invalid details')
    return render(request, "stock/login.html")

def stock_page(request):
    present_stock=motor_products.objects.all()
    other_stock=other_products.objects.all()
    return render(request, "stock/stock.html",{
        "present_stock":present_stock,
        "other_stock":other_stock
    })

def motors_entrypage(request):
    if request.method=='POST':
        entered_company=request.POST['company']
        entered_model=request.POST['model']
        entered_hp=request.POST['hp']
        entered_specs=request.POST['specs']
        entered_quantity=request.POST['quantity']
        entered_hsncode=request.POST['hsncode']
        motor_details=motor_products(
            company=entered_company,
            model_name= entered_model,
            hp= entered_hp,
            others=entered_specs,
            quantity= entered_quantity,
            hsncode= entered_hsncode
        )
        # print(entered_company)
        # print(entered_hp)
        motor_details.save()
    return render(request, "stock/motors_entry.html")

def other_entrypage(request):
    if request.method=='POST':
        entered_product=request.POST['product']
        entered_hsncode=request.POST['hsncode']
        entered_specs=request.POST['specs']
        entered_quantity=request.POST['quantity']
        other_details=other_products(
            item_name=entered_product,
            specifications=entered_specs,
            quantity= entered_quantity,
            hsncode= entered_hsncode
        )
        # print(entered_company)
        # print(entered_hp)
        other_details.save()
    return render(request, "stock/other_entry.html")

