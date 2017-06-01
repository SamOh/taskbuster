# -*- coding: utf-8 -*-
from django.contrib import admin
from . import models


class ProjectsInLine(admin.TabularInline):
    model = models.Project
    extra = 1

class TagsInLine(admin.TabularInline):
    model = models.Tag
    extra = 1

class TasksInLine(admin.TabularInline):
    model = models.Task
    extra = 1

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ("username", "interaction", "_projects", "_tags", "_tasks")

    search_fields = ["user__username"]

    inlines = [
        ProjectsInLine, TagsInLine, TasksInLine
    ]

    def _projects(self, obj):
        return obj.projects.all().count()

    def _tags(self, obj):
        return obj.tags.all().count()

    def _tasks(self, obj):
        return obj.tasks.all().count()
