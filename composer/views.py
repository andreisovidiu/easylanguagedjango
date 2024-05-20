from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models

# Composer strategy inputs
@login_required
def index(request):
    if request.method == "POST":
        # Get form information
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        trigger = request.POST.get("trigger")
        entrieslimit = request.POST.get("entrieslimit")
        direction = request.POST.get("direction")
        pattern = request.POST.get("pattern")
        stoploss = request.POST.get("stoploss")
        takeprofit = request.POST.get("takeprofit")
        tradeliquid = request.POST.get("tradeliquid")
        # Write strategy on the right side using the user's inputs
        return render(request, "composer/index.html", {
            "starttime": starttime, 
            "endtime": endtime, 
            "trigger": trigger, 
            "entrieslimit": entrieslimit, 
            "direction": direction, 
            "pattern": pattern, 
            "stoploss": stoploss, 
            "takeprofit": takeprofit, 
            "tradeliquid": tradeliquid
            })
    else:
        return render(request, "composer/index.html")

# Instructions GUI
def about(request):
    return render(request, "composer/about.html")

