from django.shortcuts import render,redirect
from .forms import *

def index(request):
    context = {}
    return render(request,'index.html',context)

def verPersonas(request):
    personas = Persona.objects.all()
    context = {'personas' : personas}
    return render(request,'detailPersonas.html',context)

def verMascotas(request):
    mascotas = Mascota.objects.all()
    context = {'mascotas':mascotas}
    return render(request,'detailMascotas.html',context)

def borrar(request,id):
    persona = Persona.objects.get(id = id)
    persona.delete()
    return redirect('verPersonas')

def borrarMascota(request,id):
    mascota = Mascota.objects.get(id = id)
    mascota.delete()
    return redirect('verMascotas')

def editar(request,id):
    persona = Persona.objects.get(id = id)
    if request.method == 'POST':
        form = PersonaForm(request.POST, instance = persona)
        if form.is_valid:
            form.save()
            return redirect('verPersonas')
    else:
        form = PersonaForm(instance = persona)
    context = {
        'form':form,
        'id':id
    }
    return render(request,'personasCreate.html',context)

def editarMascota(request,id):
    mascota = Mascota.objects.get(id = id)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance = mascota)
        if form.is_valid:
            form.save()
            return redirect('verMascotas')
    else:
        form = MascotaForm(instance = mascota)
    context = {
        'form':form,
        'id':id
    }
    return render(request,'mascotasCreate.html',context)

def registroPersonas(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('verPersonas')
    else:
        form = PersonaForm
    context = { 'form': form}
    return render(request,'personasCreate.html',context)

def registroMascotas(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('verMascotas')
    else:
        form = MascotaForm
    context = { 'form': form}
    return render(request,'mascotasCreate.html',context)
