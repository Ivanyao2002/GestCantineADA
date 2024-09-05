from django.shortcuts import render, redirect
from ..forms.flat_forms import FlatForm
from ..models.flat_model import FlatModel
from django.contrib import messages


# Create your views here.

def flat_list(request):

    context = {}
    search_field = request.GET.get('search_field')
    if search_field:
        flats = FlatModel.objects.filter(name__icontains=search_field, status=True)
        numbers_flats = flats.count()
        context['flats'] = flats
        context['search_field'] = search_field
        context['numbers_flats'] = numbers_flats
    else:
        flats =  FlatModel.objects.filter(status=True)
        numbers_flats = flats.count()
        context['flats'] = flats
        context['numbers_flats'] = numbers_flats

    return render(request, 'pages/plats.html', context)


def flat_add(request):

    context = {
        "title": "Formulaire d'enregistrement d'un plat",
        "submit_btn": "Enregistrer",
    }

    if request.method == "POST":
        flat_form = FlatForm(request.POST)
        if flat_form.is_valid():
            flat_form.save()
            messages.error(request, " Plat ajouté avec succès ! ")
            return redirect("canteen:flat_index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    else:
        flat_form = FlatForm()
    context['form'] = flat_form    

    return render(request, 'pages/forms.html', context)


def flat_edit(request, id):

    context = {
        "title": "Formulaire de modification d'un plat",
        "submit_btn": "Modifier",
    }

    flat = FlatModel.objects.get(id = id)

    if request.method == "POST":
        flat_form = FlatForm(request.POST, instance=flat)
        if flat_form.is_valid():
            flat_form.save()
            messages.success(request, " Plat modifié avec succès ! ")
            return redirect("canteen:flat_index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    else:
        flat_form = FlatForm(instance=flat)
    context['form'] = flat_form    

    return render(request, 'pages/forms.html', context)


def flat_delete(request, id):

    flat = FlatModel.objects.get(id = id)
    flat.status = False
    flat.save()
    messages.success(request, " Plat suprimé avec succès ! ")
    return redirect("canteen:flat_index") 