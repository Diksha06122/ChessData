from django.shortcuts import render
from .ChessData import ChessData

def home(request):
    try:
        theChessData = {}
        if request.method == "POST":
            username = request.POST.get("username")
            getData = ChessData(username)
            theChessData = getData.getChessData()
    except:
        pass
    return render(request, "index.html", theChessData)