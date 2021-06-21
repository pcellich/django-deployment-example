from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'index.html', context_dict)

def other(request):
    return render(request, 'other.html')

def relative_url(request):
    return render(request, 'relative.html')

def extra(request):
    return render(request, 'extra.html')

# def index(request):
#     return render(request, 'index.html')
