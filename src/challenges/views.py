from django.shortcuts import render
from django.http import Http404 ,HttpResponseNotFound , HttpResponseRedirect 
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.



manthly_challenges = {
    
    "january": "Eat no meat for the entire month!",
    "february": "walk for at least 20 minutes every day!",
    "marth": "learn django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "walk for at least 20 minutes every day!",
    "june": "learn django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "walk for at least 20 minutes every day!",
    "september": "learn django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "walk for at least 20 minutes every day!",
    "december":None,
    
}


def indix(request):
    list_items = ""
    months = list(manthly_challenges.keys())
    return render(request,"challenges/index.html",{"months":months})

def manthly_challenge_by_number(request,month):
    months = list(manthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_month = reverse("month-challenge",args=[redirect_month])
    return HttpResponseRedirect("/challenges/" + redirect_month)

def monthly_challenge(request, month):
    try:
    
        challenge_text = manthly_challenges[month]
        return render(request,"challenges/challenge.html",{"text": challenge_text,"months":month})
       
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
    
    
