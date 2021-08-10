from django.db import models

# Create your models here.

class Furniture(models.Model):
    SOFA, CHAIR, BEDFRAME, OTHER = 'SF', 'CH', 'BF', 'O'
    TYPES = [(SOFA, 'sofa'),
             (CHAIR, 'chair'),
             (BEDFRAME, 'bed frames'),
             (OTHER,  'other')]

    RED, BLUE, GREEN = 'R', 'B', 'G'
    COLOR = [(RED, 'red'),
             (BLUE, 'blue'),
             (GREEN, 'green')]

    MODERN, VICTORIAN, FANCY, SIMPLE = 'MOD', 'VCT', 'FAN', 'SIM'
    STYLE = [(MODERN, 'modern'),
             (VICTORIAN, 'victorian'),
             (FANCY, 'fancy'),
             (SIMPLE, 'simple')]

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250,
                                   default='')
    type = models.CharField(max_length=2,
                            choices=TYPES,
                            default=OTHER)
    color = models.CharField(max_length=2,
                             choices=COLOR,
                             default=RED)
    style = models.CharField(max_length=3,
                             choices=STYLE,
                             default=SIMPLE)
    size = models.FloatField()
    cost = models.FloatField()
    thumbnail = models.ImageField(upload_to='gallery_ims/',
                              default='gallery_ims/question_mark.png')

    def __str__(self):
        return self.name
