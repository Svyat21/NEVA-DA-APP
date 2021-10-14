from django.shortcuts import render
from django.views.generic import View
from .models import Group, Team, Genre, Repertoire, Price, CommonRider, Rider
import logging

logger = logging.getLogger(__name__)


class HomeView(View):

    def get(self, request):
        about = Group.objects.filter(pk=1)[0]
        genre = Genre.objects.all().prefetch_related('repertoire_set')
        price = Price.objects.filter(pk=1)[0]
        rider = CommonRider.objects.filter(pk=1)[0]
        context = {
            'title_html': 'Главная',
            'about': about,
            'genre': genre,
            'price': price,
            'rider': rider,
        }
        return render(request, 'nevada_shop/index.html', context=context)
