from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method=='POST':
        uname=request.POST['uname'] 
        umail=request.POST['umail']
        subject=request.POST['subject']
        message=request.POST['message']

        data={
            'name':uname,
            'email':umail,
            'subject':subject,
            'message':message,
        }

        message = '''
        New message: {}
        From: {}
        '''.format(data['message'],data['email'])
        send_mail(data['subject'],message, '' , ['debadritapaul76@gmail.com'])
        context={}
        context['success'] = 'Mail sends successfully.'
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')