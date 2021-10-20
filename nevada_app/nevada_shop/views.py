from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import Group, Team, Genre, Repertoire, Price, CommonRider, Rider
from .forms import QuestionForm
import logging

# logger = logging.getLogger(__name__)


class HomeView(View):

    def get(self, request):
        about = Group.objects.filter(pk=1)[0]
        genre = Genre.objects.all().prefetch_related('repertoire_set')
        price = Price.objects.filter(pk=1)[0]
        rider = CommonRider.objects.filter(pk=1)[0]
        form = QuestionForm()
        context = {
            'title_html': 'Главная',
            'about': about,
            'genre': genre,
            'price': price,
            'rider': rider,
            'form': form,
        }
        return render(request, 'nevada_shop/index.html', context=context)

    def post(self, request):
        return HttpResponse('ok')


class AboutView(View):

    def get(self, request):
        team = Team.objects.all()
        context = {
            'title_html': 'О нас',
            'team': team,
        }
        return render(request, 'nevada_shop/about_team.html', context=context)
