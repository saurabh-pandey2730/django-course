from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


monthly_challenges = {
       "january":"hello january",
       "february" :"hello february",
       "march" :"hello march",
       "april" :"hello april",
       "may" :"hello may",
       "june" :"hello june",
       "july" :"hello july",
       "august" :"hello august",
       "september" :"hello september",
       "october" :"hello october",
       "november" :"hello november",
       "december" :"hello december",
    
}

def monthly_challenge_by_number(request,month):
     return HttpResponse(month)

def monthly_challenge(request,month):
    try:
        challenge_text =monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("month not found")
        

