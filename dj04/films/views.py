from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import FilmForm, RegistrationForm
from .models import Film
from django.db.models import Q
from django.core.paginator import Paginator

def film_list(request):
    query = request.GET.get('q')
    if query:
        films = Film.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )
    else:
        films = Film.objects.all()

    paginator = Paginator(films, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'films/film_list.html', {'page_obj': page_obj, 'query': query})

@login_required
def film_create(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm()
    return render(request, 'films/film_form.html', {'form': form})

@login_required
def film_update(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film_list')
    else:
        form = FilmForm(instance=film)
    return render(request, 'films/film_form.html', {'form': form, 'film': film})

@login_required
def film_delete(request, pk):
    film = get_object_or_404(Film, pk=pk)
    if request.method == 'POST':
        film.delete()
        return redirect('film_list')
    return render(request, 'films/film_confirm_delete.html', {'film': film})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('film_list')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
