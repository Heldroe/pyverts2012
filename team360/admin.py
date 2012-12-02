from team360.models import Criterion, WeekCriterion, WeekRater, Rating
from django.contrib import admin


class CriterionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    
class WeekCriterionAdmin(admin.ModelAdmin):
    list_display = ('criterion', 'date')
    date_hierarchy = 'date'
    
class WeekRaterAdmin(admin.ModelAdmin):
    list_display = ('rater', 'rated', 'date')
    date_hierarchy = 'date'
    
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rater', 'rated', 'criterion', 'value', 'date')
    date_hierarchy = 'date'
    
admin.site.register(Criterion, CriterionAdmin)
admin.site.register(WeekCriterion, WeekCriterionAdmin)
admin.site.register(WeekRater, WeekRaterAdmin)
admin.site.register(Rating, RatingAdmin)
