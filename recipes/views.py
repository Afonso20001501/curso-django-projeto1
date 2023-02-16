from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Afonso Miqueias',
    })
    # return http response
