from django.shortcuts import render,redirect,get_object_or_404
# Create your views here.
from .models import CategoryMovie,Movie,Profile
from django.contrib import messages
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    context={
        'movie_list':movies
    }
    return render(request,"index.html",context)

def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add_movie(request):
    if request.method=='POST':
        title = request.POST.get('title')
        poster = request.POST.get('poster')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        actors = request.POST.get('actors')
        youtube_trailer_link = request.POST.get('youtube_trailer_link')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')
        # category_ids = request.POST.getlist('category')  # Assuming 'category' is a multi-select field

        try:
            # category = CategoryMovie.objects.get(id=category_id)
            movie = Movie.objects.create(
                title=title,
                poster=poster,
                description=description,
                release_date=release_date,
                actors=actors,
                youtube_trailer_link=youtube_trailer_link,
                image=image
            )
            movie = Movie.objects.get(pk=movie.pk)
            movie.category.set(category_id)
            return redirect('/')
        except CategoryMovie.DoesNotExist:
            return render(request, 'base.html')

    else:
            categories=CategoryMovie.objects.all()
            return render(request,'add.html',{'categories': categories})

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")


def category_detail(request):
    category= CategoryMovie.objects.all()
    context = {
        'category_list':category
    }

    return render(request, "category.html", context)

def detail_category(request,category_id):
    category=CategoryMovie.objects.get(id=category_id)
    movies=Movie.objects.filter(category=category)
    return render(request,"category_movies.html",{'category':category,'movies':movies})



