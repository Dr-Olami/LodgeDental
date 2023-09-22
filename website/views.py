from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_subject = request.POST['message-subject']
        message = request.POST['message']

        # send an email
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['muhammedabdulrasheed1992@gmail.com'], # To email
        )

        return render(request, 'contact.html', {'message_name': message_name})
    
    else:
        return render(request, 'contact.html', {})
    
def about(request):
    return render(request, 'about.html', {})

def price(request):
    return render(request, 'price.html', {})

def service(request):
    return render(request, 'service.html', {})

def appointment(request):
    if request.method == "POST":
        selected_service = request.POST['selected-service']
        doctor = request.POST['doctor']
        your_name = request.POST['your-name']
        your_mobile = request.POST['your-mobile']
        your_email = request.POST['your-email']
        patient_class = request.POST['patient-class']
        appointment_date = request.POST['appointment-date']
        appointment_time = request.POST['appointment-time']

        

        # # send an email
        # send_mail(
        #     message_name, # subject
        #     message, # message
        #     message_email, # from email
        #     ['muhammedabdulrasheed1992@gmail.com'], # To email
        # )
        
        return render(request, 'appointment.html', {
            'selected_service': selected_service,
            'doctor': doctor,
            'your_name': your_name,
            'your_mobile': your_mobile,
            'your_email': your_email,
            'patient_class': patient_class,
            'appointment_date': appointment_date,
            'appointment_time': appointment_time,
            })
    
    else:
        return render(request, 'home.html', {})