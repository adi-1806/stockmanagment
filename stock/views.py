from django.shortcuts import render,redirect, HttpResponseRedirect 
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

def delete_motor(request, pk):
    queryset= motor_products.objects.get(id=pk)
    if request.method == 'POST':
        form=request.POST['Yes']
        if form=='Submit':
            queryset.delete()
            return HttpResponseRedirect("/stock_page")
    return render(request, 'stock/delete.html')

def delete_other(request, pk):
    queryset= other_products.objects.get(id=pk)
    if request.method == 'POST':
        form=request.POST['Yes']
        if form=='Submit':
            queryset.delete()
            return HttpResponseRedirect("/stock_page")
    return render(request, 'stock/delete.html')

def edit_motors(request,pk):
    details=motor_products.objects.get(id=pk)
    if request.method== 'POST':
        entered_company=request.POST['company']
        entered_model=request.POST['model']
        entered_hp=request.POST['hp']
        entered_specs=request.POST['specs']
        entered_quantity=request.POST['quantity']
        entered_hsncode=request.POST['hsncode']

        if entered_company is not None:
            motor_details=motor_products(
            company=entered_company)
            motor_details.save()
        else:
            motor_details=details.company
            motor_details.save()
        
        if entered_quantity is not None:
            motor_details=motor_products(
            company=entered_quantity)
            motor_details.save()
        else:
            motor_details=details.quantity
            motor_details.save()
        
        if entered_model is not None:
            motor_details=motor_products(
            company=entered_model)
            motor_details.save()
        else:
            motor_details=details.model_name
            motor_details.save()
        
        if entered_hp is not None:
            motor_details=motor_products(
            company=entered_hp)
            motor_details.save()
        else:
            motor_details=details.hp
            motor_details.save()
        
        if entered_hsncode is not None:
            motor_details=motor_products(
            company=entered_hsncode)
            motor_details.save()
        else:
            motor_details=details.hsncode
            motor_details.save()

        if entered_specs is not None:
            motor_details=motor_products(
            company=entered_specs)
            motor_details.save()
        else:
            motor_details=details.others
            motor_details.save()

    return render(request, 'stock/edit_motor.html',{
        "details":details
    })