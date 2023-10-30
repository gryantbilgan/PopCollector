from django.shortcuts import render

# Create your views here.
pops = [
    {'name': 'Infinite Deku', 'brand': 'My Hero Academia', 'model_no': 1008, 'description': 'Infinite Deku with Eri on his back.'},

    {'name': 'Batman', 'brand': 'DC Super Heroes', 'model_no': 409, 'description': 'Batman con Dia de los Muertos'},

    {'name': 'El Animal Indestructible', 'brand': 'Marvel Lucha Libre', 'model_no': 711, 'description': 'Wolverine as a Luchador'},

    {'name': 'Phantasm', 'brand': 'Batman the AS', 'model_no': 198, 'description': 'Mask of the Phantasm'},

    {'name': 'White Lantern Batman', 'brand': 'DC Super Heroes', 'model_no': 139, 'description': 'Batman in a White Lantern Outfit'},

    {'name': 'Trunks', 'brand': 'Dragon Ball Z', 'model_no': 107, 'description': 'Future Trunks'}
]

def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def pops_index(request):
    return render(request, 'pops/index.html', {
        'pops': pops
    })