from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.



def monthly_challenge(request,month):
    challenge_text =None
    
    if month == 'january':
        challenge_text = "january month !"
    elif month == 'february':
        challenge_text = "february month !"
    else :
        return HttpResponseNotFound("unknown month")
    return HttpResponse(challenge_text)
