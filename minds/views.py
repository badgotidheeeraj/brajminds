from django.shortcuts import render,redirect
from . models import send_data,dynamic_data
from django.contrib import messages
# Create your views here.
def landing(request):
    data = dynamic_data.objects.all()

    if request.method == 'POST':
        FullName = request.POST.get('FullName')
        Email = request.POST.get('Email')
        PhoneNumber = request.POST.get('PhoneNumber')
        Name = request.POST.get('Name')

        if FullName and Email and PhoneNumber and Name:
            send_data(FullName=FullName, Email=Email, PhoneNumber=PhoneNumber, Name=Name).save()

            # Add a success message
            messages.success(request, 'Thank you for getting in contact with us! ')
            return redirect('landing')
        else:
            # Add an error message if the form is incomplete
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'index.html', {'data': data})
def admin_admin(request):
    return render(request, "admin.html", {'admin': send_data.objects.all(), 'count': send_data.objects.count()})
