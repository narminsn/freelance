from django.shortcuts import render, redirect
from freelancer_app.models import MenuModel, HeaderModel, PortfolioItem, PortfolioModel, About_session, Contact_sessionModel, CopyrightModel,FooterModel, FooterIcon
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import  messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
@csrf_exempt
def home_page(request):
    
    context={
        'menu':MenuModel.objects.all(),
        'form': ContactForm,
        'header': HeaderModel.objects.first(),
        'portfolio_item': PortfolioItem.objects.all(),
        'portfolio': PortfolioModel.objects.first(),
        'about': About_session.objects.first(),
        'copyright': CopyrightModel.objects.first(),
        'contact': Contact_sessionModel.objects.first(),
        'footer': FooterModel.objects.all(),
        'icons': FooterIcon.objects.all()
    }

    if request.method=="POST":
        data_form=request.POST
        form= ContactForm(data_form)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "We will contact you"
            )
            return redirect("/#contact")
            # return redirect("home")

        else:
            messages.error(
                request,
                "Form is not valid"
            )
            context["form"] = form
            # return redirect("/#contact",context)
        
    return  render(request, "index.html",context)

