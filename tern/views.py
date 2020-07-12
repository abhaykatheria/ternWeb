from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render  
#importing loading from django template  
from django.template import loader  
# Create your views here.  
from django.http import HttpResponse

from .forms import NameForm
@csrf_exempt
@csrf_exempt
def image(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            print(str(request.body).split('&')[1])
            #return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()

    return render(request, 'image.html', {'form': form})

def dockerfile(request):
    return  HttpResponse("bitmch")

def index(request):  
    template = loader.get_template('index.html') # getting our template  
    return HttpResponse(template.render())       # rendering the template in HttpResponse  