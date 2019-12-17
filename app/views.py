from datetime import datetime
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, Http404, QueryDict
from django.db import IntegrityError
from django.contrib.auth import (authenticate, get_user_model, login, logout,)
from .forms import UserLogin, ExtendedRegisterForm, ItemForm
from .models import UserModel, Items, User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
currentUser = ''

"""View all the items that is avaliable to bid"""
@csrf_exempt
def home_view(request):
    title="Latest Items"
    subtitle="Search"
    Item_header = ['Image','Item', 'Added By ', 'Auction Ends ', 'Current Price', 'Highest Bidder']
    buy = "Buy Item"
    contents = {"title":title, "subtitle":subtitle, "buy": buy, "Item_header": Item_header}
    return render(request, "app/form.html", contents)


"""View one specific item with all the details and input the bidding value"""
@csrf_exempt
def bidding_view(request, id):
    title="Bid Item"
    item_object = Items.objects.get(pk=id)
    if request.method == 'POST':
        price = request.POST['updatePrice']
        if str(price) == "":
            pass
        else:
            highestbiddername = request.POST['updateUsername']
            item_object.itemPrice = float(price)
            item_object.highestBidder = highestbiddername
            item_object.bidderList += highestbiddername+": £"+str(price)+","
            item_object.save()
            return redirect('home')
    return render(request, "app/bid.html", {"title":title, "bid_id":id, "item":item_object})

"""View current user's profile with DoB, emaail etc... and an item that the current user have won. """
@csrf_exempt
def profile_view(request, id):
    title="Profile"
    title2="Items Won"
    user_object = UserModel.objects.get(pk=id)
    global currentUser
    currentUser = user_object.username
    header = ['First Name', 'Last Name', 'Email', 'Date Of Birth']
    header2 = ['Image','Item', 'Description', 'Winning Price']
    return render(request, "app/profile.html", {"title": title, "title2": title2, "objects": user_object, "header": header, "header2": header2})
    

"""View all the items that has passed the end date auction """
@csrf_exempt
def auction_view(request):
    title="Closed Auctions"
    auc="Search"
    Item_header = ['Image','Item', 'Added By ', 'Auction Ends ', 'Price', 'Bidder', 'Winner']
    return render(request, "app/form.html", {"title":title, "auc":auc, "Item_header": Item_header})

    ##login view to get the user name and password and doing validation checks


"""Allow user to login the auction site """
@csrf_exempt
def login_view(request):
    title = "Login"
    form_class = UserLogin()
    return render(request, "app/login.html", {"form":form_class, "title":title})

@csrf_exempt
def register_complete_view(request):
    return render(request, "app/register_complete.html")


"""Using built-in form, allow user to sign up for auction site """
@csrf_exempt
def register_view(request):
    title= "Register"
    subtitle = "Please Sign Up"
    member_class = ExtendedRegisterForm
    member = member_class(request.POST)
    if request.method == 'POST':
        member = ExtendedRegisterForm(request.POST)
        if member.is_valid():
            user = member.save()
            new_password = member.cleaned_data["password"]
            user.set_password(new_password)
            user.save()
            return redirect("register_complete")
        else:
            print("errorrs")
    else:
        member = ExtendedRegisterForm()
    return render(request, "app/register.html", { "subtitle":subtitle, "title":title, "member": member_class})


"""Once the user logged out, will redirect to home page"""
@csrf_exempt
def logout_view(request):
    logout(request)
    title = "Logout"
    return redirect("/")


"""
retrieve all the data from Database and pass the data to ajax frontend 
data includes items with before end date and after end date
include items after end date with the current user logged in  
"""
@csrf_exempt
def getItems_view(request):
    return JsonResponse({
        'items' : list(Items.objects.filter(itemAuctonEnd__gt=datetime.now()).values()),
        'itemClosed' : list(Items.objects.exclude(itemAuctonEnd__gt=datetime.now()).values()),
        'itemToBidder' : list(Items.objects.exclude(itemAuctonEnd__gt=datetime.now()).filter(highestBidder=currentUser).values())
    })


"""Allow user to add item to bid, but it requires login to add an item"""
@login_required
def addItem(request):
    title="Add Item"
    if request.method == "POST":
        form  = ItemForm(request.POST, request.FILES)
        New_User = User.objects.get(username = request.user)
        user_id = New_User.id
        temp = UserModel.objects.get(pk = user_id)
        if form.is_valid():
            name = form.cleaned_data['itemName']
            description = form.cleaned_data['itemDescription']
            price = form.cleaned_data['itemPrice']
            end_time  = form.cleaned_data['itemAuctonEnd']
            pic = form.cleaned_data['itemImage']
            NewItem = Items(
                itemName = name,
                itemDescription = description,
                itemPrice = price,
                itemAdded = datetime.now(),
                itemAuctonEnd = end_time,
                seller = temp,
                itemImage = pic,
            ) 
            NewItem.save()
            return redirect('home')
        else:
            return HttpResponse("The form is invalid")
    item_form  = ItemForm()
    return render(request, "app/addItem.html", {"title":title, "form": item_form})
