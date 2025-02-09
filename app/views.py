from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import ErrorLog
from django.conf import settings

GOOGLE_API_KEY = getattr(settings, "GOOGLE_API_KEY", "")
SEARCH_ENGINE_ID = getattr(settings, "SEARCH_ENGINE_ID", "")
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hola Mundo</h1>")

def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)


def error(request, exception):
    return 7/0
    
def onepage(request):
    return render(request, 'onepage.html')

def error_logs(request):
    return render(request, 'error_logs.html')

def get_error_logs(request):
    errors = ErrorLog.objects.values('codigo', 'mensaje', 'fecha')
    return JsonResponse({'data': list(errors)})

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": GOOGLE_API_KEY,
        "cx": SEARCH_ENGINE_ID
    }
    response = requests.get(url, params=params)
    return response.json()


def search_view(request):
    query = request.GET.get('q', "")
    results = []
    if query:
        data = google_search(query)
        results = data.get('items', [])

    return render(request, 'search.html', {'results': results, 'query': query})


