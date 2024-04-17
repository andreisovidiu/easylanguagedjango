from django.shortcuts import render

# Create your views here.
# Composer UI
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
        
        return render(request, "composer/index.html", {"starttime": starttime, "endtime": endtime, "trigger": trigger, 
                                                       "entrieslimit": entrieslimit, "direction": direction, "pattern": pattern, 
                                                       "stoploss": stoploss, "takeprofit": takeprofit, "tradeliquid": tradeliquid})
    else:
        return render(request, "composer/index.html")
    
        # if request.method == "GET":
        #     return render(request, 'composer/index.html')

# Instructions GUI
def about(request):
    return render(request, "composer/about.html")
