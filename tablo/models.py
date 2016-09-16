from django.db import models
from django import forms
import itertools

# Registered users can organize games with schedules, join games, and rate players they've played with.

DAYS_TIMES = itertools.product(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],['Morning','Afternoon','Evening','Night'])

#Game
class Ludo(models.Model):
  name = models.CharField(max_length=200)
  # stuff we want to model
  #bgg_api: http://lcosmin.github.io/boardgamegeek/

  class Meta:
    verbose_name_plural = 'ludoj'

#Player
class Ludanto(models.Model):
  #user_id
  # which games interested in playing
  # where (postal code?)
  # frequency, days of the week, and times available
  games = models.ManyToManyField(Ludo)
  where = models.CharField(max_length=200)
  when = models.CharField(max_length=200, choices=DAYS_TIMES)

  class Meta:
    verbose_name_plural = 'ludantoj'

#Organizer/Game Master
class Mastro(models.Model):
  #user_id
  # which games
  # where (postal code?); should be roughly where the games will be hosted, not necessarily where the organizer is
  # how many seats
  # day(s) of the week (or one-off?)
  # rsvp cutoff
  games = models.ManyToManyField(Ludo)
  where = models.CharField(max_length=200)
  when = models.CharField(max_length=200, choices=DAYS_TIMES)

  class Meta:
    verbose_name_plural = 'mastroj'

#Game Session
class Kunsido(models.Model):
  # which game
  # who organized it
  # who is playing it
  # how many seats there are
  # accepting new players?
  game = models.ManyToManyField(Ludo)
  seats = models.IntegerField()
  date = models.DateField()
  start_time = models.TimeField()
  end_time = models.TimeField()
  players = models.ManyToManyField(Ludanto)
  organizer = models.ForeignKey(Mastro)
  rsvp_cutoff = models.IntegerField()
  new_players = models.BooleanField()
  # location is assumed to be whatever the organizer chose

  class Meta:
    verbose_name_plural = 'kunsidoj'
