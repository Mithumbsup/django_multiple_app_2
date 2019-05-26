from django.shortcuts import render, HttpResponse, redirect
from .models import Portfolio
from .forms import PortfolioForm


# Create your views here.

def portfolio(request):
    Portfolios = Portfolio.objects
    return render(request,'portfolio.html', {'portfolios':Portfolios})
    
def portfolio_create(request):    
    if request.method == 'POST':
        Portfolio_form = PortfolioForm(request.POST,request.FILES)
        if Portfolio_form.is_valid():
            Portfolio = Portfolio_form.save(commit=False)
            Portfolio.save()
            return redirect('portfolio')
        
    else:
        Portfolio_form = PortfolioForm()


    return render(request, 'upload.html', {
        'Portfolio_form':Portfolio_form,
    }) 