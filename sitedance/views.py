from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render


# Create your views here.
from sitedance.forms import AppointmentForm
from sitedance.models import Post


def index_view(request):
    object_list = Post.published.get_queryset()
    paginator = Paginator(object_list, 10)  # 3 поста на каждой странице
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, поставим первую страницу
        posts = paginator.page(1)
    except EmptyPage:
        # Если страница больше максимальной, доставить последнюю страницу результатов
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page': page, 'posts': posts})


def sport_view(request):
    return render(request, 'template.html')


def covid_view(request):
    return render(request, 'template.html')


def contacts_view(request):
    return render(request, 'template.html')


def about_view(request):
    return render(request, 'template.html')


def achievements_view(request):
    return render(request, 'template.html')


def info_view(request):
    return render(request, 'template.html')


def appointment_view(request):
    form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})
