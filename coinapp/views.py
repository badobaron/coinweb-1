from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'coinapp/index.html', {})

def get_log_from_disk():
    ## Your code comes here
    return "Test 1 OK; Test 2 OK"

def get_log(request):
    results = get_log_from_disk()
    return HttpResponse(results)