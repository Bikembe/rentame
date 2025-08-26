from django.shortcuts import render, get_object_or_404, redirect
from .models import Cabana, Promocion, Opinion
from .forms import OpinionForm
from django.utils import timezone

def home(request):
    promociones = Promocion.objects.all().order_by('-fecha_inicio')
    cabanas = Cabana.objects.all()
    return render(request, 'cabanas/home.html', {
        'promociones': promociones,
        'cabanas': cabanas
    })


def detalle_cabana(request, id):
    cabana = get_object_or_404(Cabana, id=id)
    opiniones = cabana.opiniones.all()
    return render(request, 'cabanas/detalle_cabana.html', {'cabana': cabana, 'opiniones': opiniones})

def agregar_opinion(request, id):
    cabana = get_object_or_404(Cabana, id=id)
    if request.method == 'POST':
        form = OpinionForm(request.POST, request.FILES)
        if form.is_valid():
            opinion = form.save(commit=False)
            opinion.cabana = cabana
            opinion.save()
            return redirect('detalle_cabana', id=cabana.id)
    else:
        form = OpinionForm()
    return render(request, 'cabanas/agregar_opinion.html', {'form': form, 'cabana': cabana})

def editar_opinion(request, id):
    opinion = get_object_or_404(Opinion, id=id)
    if request.method == 'POST':
        form = OpinionForm(request.POST, request.FILES, instance=opinion)
        if form.is_valid():
            form.save()
            return redirect('detalle_cabana', id=opinion.cabana.id)
    else:
        form = OpinionForm(instance=opinion)
    return render(request, 'cabanas/editar_opinion.html', {'form': form, 'opinion': opinion})


def eliminar_opinion(request, id):
    opinion = get_object_or_404(Opinion, id=id)
    cabana_id = opinion.cabana.id
    if request.method == 'POST':
        opinion.delete()
        return redirect('detalle_cabana', id=cabana_id)
    return render(request, 'cabanas/eliminar_opinion.html', {'opinion': opinion})
