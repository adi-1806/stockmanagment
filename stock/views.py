from django.shortcuts import render,redirect, HttpResponseRedirect 
from .models import motor_products, other_products
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginUser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user= authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('stockpage')
        else:
            messages.info(request, 'Username Or Password is incorrect')
    return render(request, "stock/login.html")

def logoutUser(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='loginpage')
def stock_page(request):
    present_stock=motor_products.objects.all()
    other_stock=other_products.objects.all()
    return render(request, "stock/stock.html",{
        "present_stock":present_stock,
        "other_stock":other_stock
    })

@login_required(login_url='loginpage')
def motors_entrypage(request):
    if request.method=='POST':
        form=request.POST['Yes']
        if form=='Submit':
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
            motor_details.save()

            messages.success(request, ' Motor added successfully')
            return HttpResponseRedirect("/stock_page")
    return render(request, "stock/motors_entry.html")

@login_required(login_url='loginpage')
def other_entrypage(request):
    if request.method=='POST':
        form=request.POST['Yes']
        if form=='Submit':
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
            other_details.save()
            messages.success(request, ' Item added successfully')
            return HttpResponseRedirect("/stock_page")
    return render(request, "stock/other_entry.html")

@login_required(login_url='loginpage')
def delete_motor(request, pk):
    queryset= motor_products.objects.get(id=pk)
    if request.method == 'POST':
        form=request.POST['Yes']
        if form=='yes':
            queryset.delete()
            messages.success(request, ' Motor deleted successfully')
            return HttpResponseRedirect("/stock_page")
    return render(request, 'stock/delete.html')

@login_required(login_url='loginpage')
def delete_other(request, pk):
    queryset= other_products.objects.get(id=pk)
    if request.method == 'POST':
        form=request.POST['Yes']
        if form=='yes':
            queryset.delete()
            messages.success(request, ' Item deleted successfully')
            return HttpResponseRedirect("/stock_page")
    return render(request, 'stock/delete.html')

@login_required(login_url='loginpage')
def edit_motors(request,pk):
    details=motor_products.objects.get(id=pk)
    if request.method== 'POST':
        entered_company=request.POST['company']
        entered_model=request.POST['model']
        entered_hp=request.POST['hp']
        entered_specs=request.POST['specs']
        entered_quantity=request.POST['quantity']
        entered_hsncode=request.POST['hsncode']

        form=request.POST['Yes']
        if form=='Submit':
            if entered_company!="":
                motor_products.objects.filter(company=details.company).update(company=entered_company)
            else:
                motor_products.objects.filter(company=details.company).update(company=details.company)

            if entered_model!="":
                motor_products.objects.filter(company=details.company).update(model_name=entered_model)
            else:
                motor_products.objects.filter(company=details.company).update(model_name=details.model_name)

            if entered_hp!="":
                motor_products.objects.filter(company=details.company).update(hp=entered_hp)
            else:
                motor_products.objects.filter(company=details.company).update(hp=details.hp)

            if entered_specs!="":
                motor_products.objects.filter(company=details.company).update(others=entered_specs)
            else:
                motor_products.objects.filter(company=details.company).update(others=details.others)

            if entered_quantity!="":
                motor_products.objects.filter(company=details.company).update(quantity=entered_quantity)
            else:
                motor_products.objects.filter(company=details.company).update(quantity=details.quantity)

            if entered_hsncode!="":
                motor_products.objects.filter(company=details.company).update(hsncode=entered_hsncode)
            else:
                motor_products.objects.filter(company=details.company).update(hsncode=details.hsncode)
            
            messages.success(request, ' Details updated successfully')
            return HttpResponseRedirect("/stock_page")

    return render(request, 'stock/edit_motor.html',{
        "details":details
    })

@login_required(login_url='loginpage')
def edit_others(request,pk):
    details=other_products.objects.get(id=pk)
    if request.method== 'POST':
        entered_item=request.POST['product']
        entered_specs=request.POST['specs']
        entered_quantity=request.POST['quantity']
        entered_hsncode=request.POST['hsncode']

        form=request.POST['Yes']
        if form=='Submit':

            if entered_item!="":
                other_products.objects.filter(item_name=details.item_name).update(item_name=entered_item)
            else:
                other_products.objects.filter(item_name=details.item_name).update(item_name=details.item_name)

            if entered_specs!="":
                other_products.objects.filter(item_name=details.item_name).update(specifications=entered_specs)
            else:
                other_products.objects.filter(item_name=details.item_name).update(specifications=details.specifications)

            if entered_quantity!="":
                other_products.objects.filter(item_name=details.item_name).update(quantity=entered_quantity)
            else:
                other_products.objects.filter(item_name=details.item_name).update(quantity=details.quantity)

            if entered_hsncode!="":
                other_products.objects.filter(item_name=details.item_name).update(hsncode=entered_hsncode)
            else:
                other_products.objects.filter(item_name=details.item_name).update(hsncode=details.hsncode)
            
            messages.success(request, ' Details updated successfully')
            return HttpResponseRedirect("/stock_page")

    return render(request, 'stock/edit_others.html',{
        "details":details
    })

@login_required(login_url='loginpage')
def shopinfo(request):
    return render(request, 'stock/shopinfo.html')

@login_required(login_url='loginpage')
def history(request):
    return render(request, 'stock/history.html')