from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import UserRegisterForm,AddRecordsForm
from .models import record

# Create your views here.
def home(request):
	records = record.objects.all()

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "You've been logged in succesfully!")
			return redirect('home')
		else:
			messages.success(request, 'Invalid user')
			return redirect('home')
	else:
		return render(request, 'website/home.html', {'records':records})

def logout_user(request):
	logout(request)
	messages.success(request, "You've been logged out!")
	return render(request, 'website/logout.html', {})

def register_user(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username} succesfully.You can now login!')
			return redirect('home')
		else:
			form = UserRegisterForm(request.POST)
	else:
		form = UserRegisterForm()
	return render(request, 'website/register.html', {'form':form})

def record_detail(request, pk):
	if request.user.is_authenticated:
		records_detail = record.objects.get(id=pk)
		return render(request, 'website/record_detail.html', {'records_detail':records_detail})
	else:
		messages.success(request, 'You are not logged in!')
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		record_delete = record.objects.get(id=pk)
		record_delete.delete()
		messages.success(request, 'Record deleted successfully!')
		return redirect('home')
	else:
		messages.success(request, 'You are not logged in!')
		return redirect('home')

def add_records(request):
	
	if request.user.is_authenticated:
		if request.method == 'POST':
			a_form = AddRecordsForm(request.POST)	
			if a_form.is_valid():
				a_form.save()
				messages.success(request, 'Record added successfully')
				return redirect('home')
		else:
			a_form = AddRecordsForm()
		return render(request, 'website/add_record.html', {'form':a_form})
	else:
		messages.success(request, 'Login to add record')
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = record.objects.get(id=pk)

		form = AddRecordsForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, 'Record updated successfully!')
			return redirect('home')
				
		return render(request,'website/update_record.html', {'form':form})
	else:
		messages.success(request, 'Login to updates')
		return redirect('home')