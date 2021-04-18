from itertools import groupby

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from sitedance.forms import AppointmentForm
from sitedance.models import Post, SportPost


def index_view(request):
    object_list = Post.published.get_queryset()
    paginator = Paginator(object_list, 3)  # 3 поста на каждой странице
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


# def sport_view(request):
#     return render(request, 'sport.html')


class SportListView(ListView):
    model = SportPost
    template_name = 'sport.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SportListView, self).get_context_data(*args, **kwargs)
        years = []
        for models in SportPost.objects.get_queryset():
            # years.append(int(models.year_publish))
            years.append(models.year_publish)

        new_years = [el for el, _ in groupby(years)]
        for i in range(len(new_years)):
            new_years[i] = int(new_years[i])

        context['vars'] = new_years
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['vars'] = SportPost.objects.get(year_publish=self.kwargs['year_published'])
    #     return context

    def get_queryset(self):
        var = self.kwargs.get('var', None)
        if var is None:
            print(var)
            return SportPost.objects.all()
        else:
            return SportPost.objects.all()


# def sport_filter(request, var):
#     print(var)
#     return render(request, 'sport.html')


def covid_view(request):
    return render(request, 'covid19.html')


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
