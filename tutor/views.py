from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import tutor_form
from .models import tutor_model
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib import messages



data = tutor_model.objects.all()
# Create your views here.
def home(request):
    cont_win = {'data':data}
    return render(request,'tutor/homepage.html',cont_win)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'account created')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    context_window = {'form': form}

    return render(request,'tutor/register.html', context_window)

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

def scholar_det(request,id):
    if request.method == "POST":
        current_file = get_object_or_404(tutor_model,id=id)
        current_file.delete()
        return redirect('home')

    data_ob = tutor_model.objects.get(id=id)
    context_win = {'data_ob':data_ob}
    return render(request,'tutor/tutor_det.html',context_win)