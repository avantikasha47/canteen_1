from django.shortcuts import render,redirect
from django.http import HttpResponse 
from . models import menus,burger,hotbeverages,maggi,shake,snacks,chinese,pudding,sandwich,garlicbread,coolref,pastries,parantha,mocktail,egg
from math import ceil
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
from django.shortcuts import render

def menu(request):
    item= menus.objects.all()
    n= len(item)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item':item}
    return render(request,'menu1.html',params)
def hotbev(request):
    item1=hotbeverages.objects.all()
    n=len(item1)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item1':item1}
    return render(request,'hotbeverages.html',params)

def burgers(request):
    item3=burger.objects.all()
    n=len(item3)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item3':item3}
    return render(request,'burgers.html',params)
def shakes(request):
    item4=shake.objects.all()
    n=len(item4)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item4':item4}
    return render(request,'shake.html',params)
def snack(request):
    item5=snacks.objects.all()
    n=len(item5)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item5':item5}
    return render(request,'snacks.html',params)
def coolrefs(request):
    item6=coolref.objects.all()
    n=len(item6)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item6':item6}
    return render(request,'coolrefreshers.html',params)
def maggis(request):
    item7=maggi.objects.all()
    n=len(item7)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item7':item7}
    return render(request,'maggi.html',params)
def pasteriess(request):
    item8=pastries.objects.all()
    n=len(item8)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item8':item8}
    return render(request,'pastries.html',params)
def puddings(request):
    item9=pudding.objects.all()
    n=len(item9)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item9':item9}
    return render(request,'pudding.html',params)
def mocktails(request):
    item10=mocktail.objects.all()
    n=len(item10)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item10':item10}
    return render(request,'mocktails.html',params)
def garlicbreads(request):
    item11=garlicbread.objects.all()
    n=len(item11)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item11':item11}
    return render(request,'garlicbread.html',params)
def sandwichs(request):
    item12=sandwich.objects.all()
    n=len(item12)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item12':item12}
    return render(request,'sandwich.html',params)
def eggs(request):
    item13=egg.objects.all()
    n=len(item13)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item13':item13}
    return render(request,'egg.html',params)
def chineses(request):
    item14=chinese.objects.all()
    n=len(item14)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item14':item14}
    return render(request,'chineseS.html',params)
def paranthas(request):
    item15=parantha.objects.all()
    n=len(item15)
    nSlides= n//4 + ceil((n/4)+(n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'item15':item15}
    return render(request,'parantha.html',params)


    
def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')    
            messages.success(request,f'your account has been created.You can now Login')
            return redirect('menus')
    else:
        form = UserRegistrationForm()
    return render(request,'register.html',{'form':form})


@login_required
def profile(request):
    return render(request,'profile.html')   

def login(request):
    return render(request,'login.html',{'login':login})
def cart(request):
    return render(request,'cart.html',{'cart':cart})

