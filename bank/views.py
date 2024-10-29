from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'./homepage.html')

def accounts(request):
    return render(request,'./accounts.html')

def loginpg(request):
    return render(request,'./loginpg.html')

def support(request):
    return render(request,'./support.html')

def transaction(request):
    return render(request,'./transaction.html')