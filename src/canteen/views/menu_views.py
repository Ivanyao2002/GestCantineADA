from django.shortcuts import render, redirect
from ..forms.menu_forms import MenuForm
from ..models.menu_model import MenuModel
from django.contrib import messages


# Create your views here.

def menu_list(request):

    context = {}
    search_field = request.GET.get('search_field')
    if search_field:
        menus = MenuModel.objects.filter(flat__name__icontains=search_field, status=True)
        numbers_menus = menus.count()
        context['menus'] = menus
        context['search_field'] = search_field
        context['numbers_menus'] = numbers_menus
    else:
        menus =  MenuModel.objects.filter(status=True)
        numbers_menus = menus.count()
        context['menus'] = menus
        context['numbers_menus'] = numbers_menus

    return render(request, 'pages/menus.html', context)


def menu_add(request):

    context = {
        "title": "Formulaire d'enregistrement d'un menu",
        "submit_btn": "Enregistrer",
    }

    if request.method == "POST":
        menu_form = MenuForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            messages.success(request, " Menu ajouté avec succès ! ")
            return redirect("canteen:menu_index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    else:
        menu_form = MenuForm()
    context['form'] = menu_form    

    return render(request, 'pages/forms.html', context)


def menu_edit(request, id):

    context = {
        "title": "Formulaire de modification d'un menu",
        "submit_btn": "Modifier",
    }

    menu = MenuModel.objects.get(id = id)

    if request.method == "POST":
        menu_form = MenuForm(request.POST, instance=menu)
        if menu_form.is_valid():
            menu_form.save()
            messages.success(request, " Menu modifié avec succès ! ")
            return redirect("canteen:menu_index")
        else:
            messages.error(request, "Erreur dans le formulaire. Veuillez vérifier les champs.")
    else:
        menu_form = MenuForm(instance=menu)
    context['form'] = menu_form    

    return render(request, 'pages/forms.html', context)


def menu_delete(request, id):

    menu = MenuModel.objects.get(id = id)
    menu.status = False
    menu.save()
    messages.success(request, " Menu suprimé avec succès ! ")
    return redirect("canteen:menu_index") 