from django.shortcuts import render
from user.models import userform
from user.models import contact
from user.models import buy_form

def home(request):
    try:
        name = request.GET.get('name')
        email = request.GET.get('email')
        description = request.GET.get('description')
        ob = contact(name=name,email=email,description=description)
        ob.save()

    except:
        pass
    return render(request,"home.html")

def flat(request):
    ob = userform.objects.filter(category__icontains='flat').values()
    return render(request, "flat.html",{'key':ob})

def plot(request):
    ob = userform.objects.filter(category__icontains='plot').values()
    return render(request, "plot.html",{'key':ob})

def fh(request):
    ob = userform.objects.filter(category__icontains='farm').values()
    return render(request, "fh.html",{'key':ob})

def bs(request):
    try:
        name = request.GET.get('name')
        email = request.GET.get('email')
        contact = request.GET.get('contact')
        price = request.GET.get('price')
        description = request.GET.get('description')
        category = request.GET.get('category')
        location = request.GET.get('location')
        ob = userform(name=name,contact=contact,email=email,price=price,description=description,category=category,location=location,status="Available")
        ob.save()
    except:
        pass   
    return render(request, "bs.html",{'choices':userform.CHOICES})

def buy(request):
    obj = userform.objects.all()
    return render(request, "buy.html",{'key':obj})
    
def prop(request):
    try:
        p_id = request.GET.get('p_id')
        name = request.GET.get('name')
        email = request.GET.get('email')
        contact = request.GET.get('contact')
        ob = buy_form(p_id=p_id,name=name,email=email,contact=contact)
        ob.save()
    except:
        pass
    return render(request, "prop.html")

def service(request):
    return render(request, "service.html")