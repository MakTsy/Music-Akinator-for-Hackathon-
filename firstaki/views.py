from django.shortcuts import render
from .forms import UserForm
from .getsong import Find_by_lyrics
from django.views.decorators.csrf import csrf_exempt


 
@csrf_exempt 
def index(request):
    try:
        userform = UserForm()
        if request.method == "POST":
            name = request.POST.get("name")
            info = Find_by_lyrics(name)[0]
            link = Find_by_lyrics(name)[1]
            vlink = Find_by_lyrics(name)[2]
            return render(request, "index.html", {"form": userform, "text": info, "videoid": link, "cation": vlink})
        else:
            return render(request, "carpet.html", {"form": userform})

    except AttributeError:
        return render(request, "index.html", {"form": userform})
