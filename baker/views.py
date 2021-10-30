from django.http.response import HttpResponseRedirect
from baker.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, User, Items

def home(request):
    if 'username' in request.session:
        current_user = request.session['username']
        if current_user:
            param = {'current_user': current_user}
            return render(request, 'baker/base.html', param)
    else:
        return redirect('baker:login')



def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email=request.POST.get('email')
        # print(uname, pwd)
        if User.objects.filter(username=username).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = User(username=username, password=password)
            user.save()
            return redirect('baker:login')
    else:
        return render(request, 'baker/signup.html', {})



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        check_user = User.objects.filter(username=username, password=password)
        if check_user:
            request.session['username'] = username
            return redirect('baker:home')
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'baker/login.html')


def logout(request):
    try:
        del request.session['username']
    except:
        return redirect('baker:login')
    return redirect('baker:login')
def add(request):
    if request.method == "POST":
        item=request.POST.get('Name')
        price=request.POST.get('Price')
        it=Items(name=item, price=price)
        it.save()
        return redirect('baker:home')
    return render(request, 'baker/add_items.html', {})
def viewer(request):
    objects=Items.objects.all()
    return render(request, 'baker/view_items.html', {'objects':objects})
def update_item(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        update_name=request.POST.get('Update_name')
        try:
            update_price=request.POST.get('Update_price')
        except:
            update_price=''
        if Name:
            dr=Items.objects.get(name=Name)
            dr.name=update_name
            dr.price=update_price
            dr.save()
            return redirect('baker:home')
        else:
            return HttpResponse("<strong> Please enter a valid Name </strong>")
    return render(request, 'baker/update_items.html', locals())
def delete_item(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        if Name:
            dr=Items.objects.get(name=Name)
            dr.delete()
            return redirect('baker:home')
        else:
            return HttpResponse("<strong> Please enter a valid Name </strong>")
    return render(request, 'baker/delete_items.html', locals())
def orders(request):
    latest_orders=Order.objects.all()
    return render(request, 'baker/orders.html', {'latest_orders':latest_orders})
def profile(request):
    if 'username' in request.session:
        current_user=request.session['username']
        if current_user:
            usr=User.objects.get(username=current_user)
            param={'current_user':usr}
            return render(request, 'baker/profile.html', param)
        else:
            return redirect('baker:home')
