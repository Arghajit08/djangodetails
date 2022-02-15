from django.http import HttpResponse
from django.shortcuts import render,redirect
def home(request):
    from django.shortcuts import render,redirect
    return render(request,"index.html")
def result(request):
    from django.shortcuts import render,redirect
    name=request.GET['name']
    address=request.GET['P']
    document=request.GET['category']
    from twilio.rest import Client
    
    sid='ACad20495dd3bf324541f3c9a60657ddf9'
    authToken='06fbf11c35fb80bb47a24105f33cd18d'

    client=Client(sid,authToken)

    from_whatsapp_number='whatsapp:+14155238886'
    to_whatsapp_number='whatsapp:+919863103113'
    
    message=client.messages.create(body=name,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    
    message=client.messages.create(body=address,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)

    
    message=client.messages.create(body=document,
                                   from_=from_whatsapp_number,
                                   to=to_whatsapp_number)
    return redirect("https://xeroxfin.herokuapp.com/")

    
    
