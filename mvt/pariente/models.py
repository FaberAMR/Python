from django.db import models

class Parientes(models.Model):
    name = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    fecha = models.Datefiel()
    
    
    #field usables:
    ##Charfield letra
    #Integerfield numero
    #Datefield fecha
    #Textfield texto no pide length de caracteres tiene 400 de max