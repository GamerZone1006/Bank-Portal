# imports 
import decimal
from django.http import HttpResponse
from django.shortcuts import render , redirect
from .models import User_reg , Transactions , Supports
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User
from django.contrib import messages

# homepage 
def homepage(request):
    return render(request,'./homepage.html')

# User profile page
def User_profile(request):
    user = User_reg.objects.get(user=request.user)

    context = {
        "User" : user ,
    }
    
    return render(request,'./user.html',context)

# Login page
def loginpg(request):
    if request.method == 'POST':
        username_user = str(request.POST['username'])
        password_user = str(request.POST['password'])
        user = authenticate(username=username_user, password=password_user)
        if user :
            login(request,user)
        #     return HttpResponse("You are loged in")
            return redirect("Dashboard")
        else:
            messages.error(request,"invalid Credentials")
            return redirect("login page")
    
    return render(request,"./loginpg.html")

# customer support page
def support(request):
    if request.method == 'POST':
        Name = request.POST['name']
        email = request.POST['email']
        issue = request.POST['issue']

        support = Supports.objects.create(name=Name,email=email,issue=issue)
        support.save()
    return render(request,'./support.html')

# Transaction page
def transaction(request):
    user = User_reg.objects.get(user=request.user)
    transactions = Transactions.objects.filter(user=user)
    context={
        "User" : user,
        "Transactions" : transactions,
    }
    return render(request,'./transaction.html',context)

# Sign-up page
def sign_up(request):

    if request.method == 'POST':
        username = request.POST["username"]
        Email = request.POST["email"]
        password = request.POST['password']
        ac_number = request.POST['account_number']
        phone = request.POST['phone']
        ac_type = request.POST['account-type']
        gender = request.POST['Gender']
        address = request.POST['address']
        Photo = request.FILES['photo']
        pan = request.POST['pan']
        Aadhaar = request.POST['aadhaar']
        dob = request.POST['dob']
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username exists")
            return redirect("Sign-up")
        
        user = User.objects.create(username=username,password=password)
        User_reg.objects.create(user=user,account_number=ac_number,phone=phone,email=Email,account_type=ac_type,gender=gender,address=address,image=Photo,Pan=pan,aadhaar=Aadhaar,DoB=dob)
        login(request,user)
        return redirect("Dashboard")
    
    return render(request,"./signup.html")

# DashBoard page
def dashboard(request):
    user_profile = User_reg.objects.get(user=request.user)
    funds = Transactions.objects.filter(user=user_profile)[4:]
    context = {
        "User" : user_profile,
        "Transactions":funds,
    }
    return render(request,"./dashboard.html",context)

# Deposit page
def deposit(request):
    if request.method=="POST":
        amount = float(request.POST["deposit-amount"])
        account = request.POST["account-number"]
        user = User_reg.objects.get(account_number=account)
        user.balance += decimal.Decimal(amount)
        user.save()

        Transactions.objects.create(user=user,transaction_type="DEPOSIT",amount=amount,receiptent_no="Self",receiptent=amount,about="Deposit")
        return redirect("Dashboard")

    return render(request,"./deposit.html")

# Withdrawal page
def withdrawal(request):
    if request.method=="POST":
        amount = decimal.Decimal(request.POST["withdrawal-amount"])
        account = request.POST["account-number"]
        user = User_reg.objects.get(account_number = account)

        if user.balance < amount :
            messages.error(request,"Tu bikhari")
            return redirect("Dashboard")
        
        else:
            user.balance -= amount
            user.save()


        Transactions.objects.create(user=user,transaction_type="WITHDRAW",amount=amount,receiptent_no="Self",receiptent=amount,about="WithDraw")
        return redirect("Dashboard")
    return render(request,"./Withdrawal.html")

# Transfer page
def Transfer(request):
    if request.method == "POST":
        user_account = request.POST["user-account"]
        receiptent_ac = request.POST["Receiptent-account"]
        amount = decimal.Decimal(request.POST["transfer-amount"])
        discription = request.POST["transaction-description"]
        user = User_reg.objects.get(user=request.user)
        
        try:
            receiptent_transfer = User_reg.objects.get(account_number=receiptent_ac)
        except User_reg.DoesNotExist:
            messages.error(request,"User does not exist")
            return redirect("Transfer")
        
        if amount > user.balance:
            messages.error(request,"Balance insufficient")
            return redirect("Transfer")
        
        else:
            user.balance -= amount
            receiptent_transfer.balance += amount
            user.save()
            receiptent_transfer.save()
            

        Transactions.objects.create(user=user,transaction_type="TRANSFER",amount=amount,receiptent_no=receiptent_ac,receiptent=receiptent_transfer.balance,about=discription)
        return redirect("Dashboard")
    return render(request,"./transfer.html")

# Log-out function 
def user_logout(request):
    logout(request)
    return redirect('login page')


