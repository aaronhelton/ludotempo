from django.contrib import admin
from .models import Ludo, Ludanto, Mastro, Kunsido

class LudoAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['name']})
  ]

class LudantoAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['games','where','when']})
  ]

class MastroAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['games','where','when']})
  ]

class KunsidoAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['game','seats','date','start_time','end_time','players','organizer','rsvp_cutoff','new_players']})
  ]

admin.site.register(Ludo, LudoAdmin)
admin.site.register(Ludanto, LudantoAdmin)
admin.site.register(Mastro, MastroAdmin)
admin.site.register(Kunsido, KunsidoAdmin)
