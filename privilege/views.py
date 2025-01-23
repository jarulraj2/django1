from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html")

def dashboard(request):
    name = request.POST['name'].capitalize();
    return render(request, "dashboard.html", {'name':name})
