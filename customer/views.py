from django.shortcuts import render, redirect
from stock.models import motor_products, other_products
from .models import selled_motor
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='loginpage')
def stock_list(request):
    present_stock=motor_products.objects.all().order_by("company")
    other_stock=other_products.objects.all().order_by("item_name")
    return render(request, "customer/stock_list.html",{
        "present_stock":present_stock,
        "other_stock":other_stock
    })


def billing(request,pk):
    details=motor_products.objects.get(id=pk)
    if request.method=="POST":
        form=request.POST['Yes']

        if form=='Submit':
            details.quantity=details.quantity-1

            entered_name = request.POST['Customer_name']
            entered_phno = request.POST['Customer_phno']
            entered_hno = request.POST['H.no']
            entered_street = request.POST['street']
            entered_village = request.POST['village']
            entered_district = request.POST['District']
            entered_pincode = request.POST['pincode']
            entered_address = entered_hno +", "+ entered_street +", "+ entered_village +", "+ entered_district +", "+ entered_pincode

            selled_details=selled_motor(
                company= details.company,
                model_name=details.model_name,
                hp=details.hp,
                hsncode=details.hsncode,
                price = details.price,
                others = details.others,
                customer_name= entered_name,
                customer_phno= entered_phno,
                customer_address = entered_address
            )
            selled_details.save()
            details.save()

            return redirect('stocklist')
        

    return render(request, "customer/billing.html",{
        "details":details
    })