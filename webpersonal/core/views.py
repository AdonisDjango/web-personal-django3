from django.shortcuts import render, HttpResponse

html_base = """
    <H1>Mi web Personal</H1>
    <ul>
    <li><a href="/"> Inicio</a></li>
    <li><a href="/About/"> Acerca de....</a></li>
    <li><a href="/Portfolio/"> Breve explicacion de un Portfolio</a></li>
    <li><a href="/contact/"> Nuestros contactos</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def About(request):
    return render(request, "core/About.html")


def contact(request):
    return render(request, "core/contact.html")