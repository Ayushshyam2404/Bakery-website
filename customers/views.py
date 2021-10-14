from django.http.response import HttpResponseRedirect
from baker.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from baker.models import Items, Order

# Create your views here.
def home(request):
    if 'username' in request.session:
        current_user=request.session['username']
        if current_user:
            return render(request, 'customers/base.html', {'current_user':current_user})
    else:
        return redirect("customers:login")
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        if Customer.objects.filter(username=username).count() > 0:
            return HttpResponse('Username already exists')
        else:
            user=Customer(username=username, password=password)
            user.save()
            return redirect('customers:login')
    return render(request, 'customers/signup.html', {})
def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        check_user=Customer.objects.filter(username=username, password=password)
        if check_user:
           request.session['username']=username
           return redirect("customers:home")
        else:
            return HttpResponse('Please enter a valid username or password')
    return render(request, 'customers/index.html', {})
def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('customers:login')
    return redirect('customers:login')
def orders(request):
    latest_items=Items.objects.all()
    order_item={
        'items':[]
    }
    if request.method=="POST":
        name=request.POST.get('items')
        if name:
            return redirect('/cart/{0}'.format(name))
        else:
            return HttpResponse('not valid')
    return render(request, 'customers/items.html', {'item':latest_items})
def cart(request, id):
    item=Items.objects.get(pk=id)
    price=item.price
    if request.method=="POST":
        if item:
            name=request.POST.get('name')
            quantity=request.POST.get('quantity')
            address=request.POST.get('address')
            number=request.POST.get('phone')
            quan=int(quantity)
            ls=int(quan*price)
            if (quantity, address, number):
                od=Order(name=name, item_name=item, quantity=quantity, address=address, num=number)
                od.save()
                return HttpResponse(f'<strong>Thank you for placing your order <br> Please pay {ls} to the delivery boy</strong>')
            else:
                return HttpResponse('Please enter valid details')
    return render(request, 'customers/cart.html', {'item':item, 'price':price,})


