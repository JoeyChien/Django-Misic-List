from django.shortcuts import render, redirect
from .models import Artist
from .forms import ArtistForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('新增成功'))
        else:
            messages.success(request, ('新增失敗'))

    all_artists = Artist.objects.order_by('-created_at')
    return render(request, 'artist/home.html', {'all_artists': all_artists})
