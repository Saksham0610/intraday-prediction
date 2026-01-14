from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return redirect('dashboard')

@login_required(login_url='login')
def dashboard(request):
    stocks = [
        {
            "company": "RELIANCE",
            "symbol": "RELIANCE.NS",
            "price": 2450,
            "change": 1.2,
            "trend": "Bullish",
            "signal": "BUY",
            "confidence": 78,
            "risk": "Medium",
            "updated": "10:45",
            "chart": [2400, 2420, 2410, 2435, 2450]
        },
        {
            "company": "TCS",
            "symbol": "TCS.NS",
            "price": 3780,
            "change": -0.6,
            "trend": "Bearish",
            "signal": "SELL",
            "confidence": 65,
            "risk": "Low",
            "updated": "10:45",
            "chart": [3820, 3810, 3800, 3790, 3780]
        },
    ]

    return render(request, 'dashboard.html', {"stocks": stocks})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
