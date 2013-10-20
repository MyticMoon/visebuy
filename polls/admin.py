from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# admin.site.register(Poll)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)