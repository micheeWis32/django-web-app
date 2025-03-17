from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Title

# Create your views here.
def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""<h1>hello Django!</h1>
                        <p> Mes groupes préférés sont : </p>
                        <ul>
                            <li> {bands[0].name}</li>
                            <li> {bands[1].name}</li>
                            <li> {bands[2].name}</li>
                        </ul>
""")

def listing(request):
    titles = Title.objects.all()
    return HttpResponse(f"""<h1>Ma liste</h1> 
                        <p>Mes Titres préférés sont :</p>
                       <ul>
                            <li> {titles[0].name}</li>
                            <li> {titles[1].name}</li>
                            <li> {titles[2].name}</li>
                        </ul>                          
""")
def about(request):
    return HttpResponse('<h1>A propos de nous</h1> <p>nous aimons merch</p>')
def contacts(request):
    return HttpResponse('<h1>Nos contact</h1> <p>nous aimons merch</p>')