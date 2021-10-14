from django.contrib import admin
from .models import Group, Team, Genre, Repertoire, Price, CommonRider, Rider


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)


class RepertoireAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'genre',)
    list_display_links = ('id', 'name',)


class RiderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'main_rider',)
    list_display_links = ('id', 'name',)


admin.site.register(Group)
admin.site.register(Team, TeamAdmin)
admin.site.register(Genre)
admin.site.register(Repertoire, RepertoireAdmin)
admin.site.register(CommonRider)
admin.site.register(Rider, RiderAdmin)
admin.site.register(Price)
