from django.contrib import admin
from .models import Post

# Register your models here.

admin.site.register(Post)


def get_region_data(request):
    region_name = request.GET.get('region')
    region_model = None
    
    # Trouver le modèle de région approprié en fonction du nom de la région
    if region_name == 'Bamako':
        region_model = Bamako
    elif region_name == 'Gao':
        region_model = Gao
    elif region_name == 'Kidal':
        region_model = Kidal
    elif region_name == 'Koulikoro':
        region_model = Koulikoro
    elif region_name == 'Mopti':
        region_model = Mopti
    elif region_name == 'Ségou':
        region_model = Ségou
    elif region_name == 'Sikasso':
        region_model = Sikasso
    elif region_name == 'Timbuktu':
        region_model = Timbuktu
    elif region_name == 'Kayes':
        region_model = Kayes

    if region_model:
        regions = region_model.objects.all()  # Sélectionner toutes les instances
        data = [{'habitats': region.habitats, 'image': region.image} for region in regions]
        return JsonResponse({'data': data})
    else:
        return JsonResponse({'error': 'Région non trouvée'})