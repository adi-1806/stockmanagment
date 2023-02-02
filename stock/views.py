from django.shortcuts import render
from .models import motor_products, other_products

# Create your views here.

def stock_page(request):
    return render(request, "stock/stock.html")

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