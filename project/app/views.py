from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    try:
        data=request.session['fname']
    # return render(request,'app/base.html')
        request.session.modified=True
        return render(request,'app/home.html',{'data':data})
    except:
        return render(request,'app/home.html')

def about(request):
    try:
        data=request.session['fname']
        request.session.modified=True
        return render(request,'app/about.html',{'data':data})
    except:
        return render(request,'app/about.html')

def category(request):
    try:
        data=request.session['fname']
        request.session.modified=True
        return render(request,'app/category.html',{'data':data})
    except:
        return render(request,'app/category.html')

def services(request):
    try:
        data=request.session['fname']
        request.session.modified=True
        return render(request,'app/services.html',{'data':data})
    except:
        return render(request,'app/services.html')


def contact(request):
    try:
        data=request.session['fname']
        request.session.modified=True
        return render(request,'app/contact.html',{'data':data})
    except:
        return render(request,'app/contact.html')


def register(request):
    return render(request,'app/register.html')


def login(request):
    return render(request,'app/login.html')  

def savedata(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    email=request.POST['email']
    contact=request.POST['contact']
    password=request.POST['password']
    cpassword=request.POST['cpassword']
    # print(fname)
    # print(lname)
    # print(email)
    # print(contact)
    # print(password)
    # print(cpassword)
    
    request.session['fname']=fname
    request.session['lname']=lname
    request.session['email']=email
    request.session['contact']=contact
    request.session['password']=password
    request.session['cpassword']=cpassword
    return render(request,'app/login.html')

def dashlogin(request):
    email=request.POST['email']
    password=request.POST['password']
    # print(email)
    # print(password)

    if 'email' in request.session:
        email_id=request.session['email']
        pwd=request.session['password']

        if email_id==email and password==pwd:
            name=request.session['fname']
            request.session.modified=True
            return render(request,'app/dashboard.html',{'data':name})
    else:
        msg="SESSION EXPIRED !!!"
        return render(request,'app/register.html',{'msg':msg})

    
def logout(request):
    if 'fname' in request.session:
        del request.session['fname']
        request.session.flush()

    return render(request,'app/home.html')

# def get(request):
#     if 'name' in request.session:
#         request.session.modified = True
#         name=request.session['name']
#         # name = request.session.get('name','Guest')
#         return render(request,'app/get.html',{'name':name})
#     else:
#         return HttpResponse("<h1> SESSION OUT !!! </h1>")