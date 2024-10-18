from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "october": "hello october",
    "november": "hello november",
    "december": "hello december",
}

# View to display list of months as clickable links
def index(request):
    list_items = ''
    months = list(monthly_challenges.keys())

    # Create list of hyperlinks for each month
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])  # URL for each month
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # Generate and return response with full list of months
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

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
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:  # Handle invalid months 
        return HttpResponseNotFound("Sorry, this month is not found")
