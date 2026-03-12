from django.shortcuts import render
from .services import save_contact

def home(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "message": request.POST.get("message")
        }
        save_contact(data)

    return render(request, "landing/index.html")
    