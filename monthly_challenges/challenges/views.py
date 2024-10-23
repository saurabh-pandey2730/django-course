from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render

# Dictionary with months and their challenges
monthly_challenges = {
    "january": "hello january",
    "february": "hello february",
    "march": "hello march",
    "april": "hello april",
    "may": "hello may",
    "june": "hello june",
    "july": "hello july",
    "august": "hello august",
    "september": "hello september",
    "october":None,
    "november": "hello november",
    "december": "hello december",
}

# View to display list of months as clickable links
def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{
        "months": months,
    })

# View to handle requests by month number and redirect to the respective month
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):  # Check if month number is valid
        return HttpResponseNotFound("Invalid month number")
    
    redirect_month = months[month - 1]  # Get month name for the number
    redirect_path = reverse("month-challenge", args=[redirect_month])  # Redirect URL
    return HttpResponseRedirect(redirect_path)

# View to handle specific month challenges
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]  # Fetch challenge for month
        # response_data = f'<h1>{challenge_text}</h1>'
        # response_data = render_to_string("challenges/challenge.html")
        response_data = render(request ,"challenges/challenge.html",{
            "text": challenge_text ,
            "month_name": month
        })
        return HttpResponse(response_data)
    except:  # Handle invalid months 
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
