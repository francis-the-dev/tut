from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import tutor_form
from .models import tutor_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib import messages
from .forms import CustomLoginForm,customuserform,search
from django.contrib.auth import authenticate, login





data = tutor_model.objects.all()
# Create your views here.
def home(request):
    dt = tutor_model.objects.all()
    
    query = request.GET.get("a","").lower()

    if query:
        dt = dt.filter(expertise=query) | dt.filter(unit=query)
    else:
        dt = tutor_model.objects.all()
    
    cont_win = {'data':dt}
    return render(request,'tutor/homepage.html',cont_win)

# register
def register(request):
    if request.method == 'POST':
        form = customuserform(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created')
            return redirect('login')
    else:
        form = customuserform()
    
    context_window = {'form': form}

    return render(request,'tutor/register.html', context_window)
# become a tutor
def bc_tutor(request):
    if request.method == 'POST':
        form = tutor_form(request.POST,request.FILES)
        if form.is_valid() :
            form.save(request.user)

            return redirect('home')
    else:
        form = tutor_form()

    cont_win = {'form':form}

    return render(request, 'tutor/bc_tutor.html',cont_win)
 
#  indivdual tutors details
def scholar_det(request,id):
    if request.method == "POST":
        current_file = get_object_or_404(tutor_model,id=id)
        current_file.delete()
        return redirect('home')

    data_ob = tutor_model.objects.get(id=id)
    context_win = {'data_ob':data_ob}
    return render(request,'tutor/tutor_det.html',context_win)

# login form
def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = CustomLoginForm()
    return render(request, 'tutor/login.html', {'form': form})



    

