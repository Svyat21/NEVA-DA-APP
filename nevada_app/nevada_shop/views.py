from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Group, Team, Genre, Price, CommonRider, Rider
from .forms import QuestionForm
from .utils import feedback_message
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
        form = QuestionForm(request.POST)
        if form.is_valid():
            feedback_message(form.cleaned_data)
        return redirect('home')


class AboutView(View):

    def get(self, request):
        teams = Team.objects.all()
        context = {
            'title_html': 'О нас',
            'teams': teams,
        }
        return render(request, 'nevada_shop/about_team.html', context=context)


class RiderView(View):

    def get(self, request):
        rider = Rider.objects.all()
        context = {
            'title_html': 'О нас',
            'rider': rider,
        }
        return render(request, 'nevada_shop/full_rider.html', context=context)
