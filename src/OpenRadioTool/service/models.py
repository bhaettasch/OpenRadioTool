from django.db import models
import datetime


class Traffic(models.Model):
    def __unicode__(self):
        """
        Get string representation

        :return: A string allowing to peek at the information
        :rtype: String
        """
        return self.where + " " + self.direction + ": " + self.get_what_display()

    def save(self):
        """
        Store current entry in database and update timestamps accordingly
        """
        if not self.id:
            self.created = datetime.date.today()
        self.updated = datetime.datetime.today()
        super(Traffic, self).save()
    
    def getHeader(self):
        """
        Get the headline for this traffic information

        :return: A string containing the position and the category of the information (if applicable)
        :rtype: String
        """
        begin = self.where + " " + self.direction() if (self.direction != '') else self.where
        end = ": " + self.get_what_display() if self.what != 'OTHER' else ""
        
        return begin + end

    def getBody(self):
        """
        Get the body of the traffic information

        :return body of the traffic information
        :rtype String
        """
        return self.text

    def isPrio(self):
        """
        Check priority of the information

        :return: True if information has high priority, false if not
        """
        return self.prio

    
    WHAT_CHOICES = (
                      ('JAM', 'Stau'),
                      ('SLOW', 'Stockender Verkehr'),
                      ('DANGER', 'Gefahr'),
                      ('PFULL', 'Parkplatz voll'),
                      ('CLOSED', 'Sperrung'),
                      ('DETOUR', 'Umleitung'),
                      ('ROADWORKS', 'Baustelle'),
                      ('OTHER', 'Sonstiges')
                      )
    
    where = models.CharField("Wo", max_length=50, help_text="Grober Ort, z.B. A5, B46, P3")
    direction = models.CharField("Richtung", max_length=200, blank=True)
    what = models.CharField("Was?", max_length=10, choices=WHAT_CHOICES, default="JAM")
    text = models.TextField("Beschreibung")
    created = models.DateTimeField("Angelegt am", editable=False)
    updated = models.DateTimeField("Aktualisiert am", editable=False)
    prio = models.BooleanField("Eilmeldung", default=False, help_text="Besonders wichtige und dringende Meldung")

    class Meta:
        verbose_name = "Verkehrsmeldung"
        verbose_name_plural = "Verkehrsmeldungen"
        ordering = ['-prio', 'where']


class WeatherForecast(models.Model):
    weather = models.CharField("Wetter", max_length=200)
    minTemperature = models.FloatField("Minimale Temperatur")
    maxTemperature = models.FloatField("Maximale Temperatur")
    humidity = models.FloatField("Feuchtigkeit", help_text='%')
    symbol = models.CharField(max_length=3)
    begin = models.DateTimeField()

    class Meta:
        verbose_name = "Wettervorhersage"
        verbose_name_plural = "Wettervorhersagen"
        ordering = ['begin']


class WeatherCurrent(models.Model):
    def save(self):
        """
        Store current entry in database and update timestamps accordingly
        """
        self.updated = datetime.datetime.today()
        super(WeatherCurrent, self).save()

    weather = models.CharField("Wetter", max_length=200)
    temperature = models.FloatField("Aktuelle Temperatur")
    humidity = models.FloatField("Feuchtigkeit", help_text='%')
    symbol = models.CharField(max_length=3)
    updated = models.DateTimeField('Letzte Aktualisierung', editable=False)

    class Meta:
        verbose_name = "Aktuelles Wetter"
        verbose_name_plural = "Aktuelles Wetter"