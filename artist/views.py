from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Artist
from .forms import ArtistForm
from django.contrib import messages

@login_required
def home(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            messages.success(request, ('新增成功'))
        else:
            messages.success(request, ('新增失敗'))

    all_artists = Artist.objects.filter(user = request.user).order_by('-created_at')
    return render(request, 'artist/home.html', {'all_artists': all_artists})
