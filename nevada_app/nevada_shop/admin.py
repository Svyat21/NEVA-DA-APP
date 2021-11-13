from django.contrib import admin
from .models import Group, Team, Genre, Repertoire, Price, CommonRider, Rider


class RepertoireInline(admin.TabularInline):
    model = Repertoire


class TeamInline(admin.TabularInline):
    model = Team


class RiderInline(admin.StackedInline):
    model = Rider


@admin.register(Genre)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    inlines = [RepertoireInline]


@admin.register(Group)
class RepertoireAdmin(admin.ModelAdmin):
    inlines = [TeamInline]


@admin.register(CommonRider)
class RiderAdmin(admin.ModelAdmin):
    inlines = [RiderInline]


@admin.register(Price)
class RiderAdmin(admin.ModelAdmin):
    pass
