from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50,blank=False,null=False)
    apellido = models.CharField(max_length=50,blank=False,null=False)
    genero = models.CharField(max_length=50,blank=False,null=False)
    identificacion = models.CharField(max_length=50,blank=True,null=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15,blank=True,null=True)
    mobil = models.CharField(max_length=15,blank=True,null=True)
    direccion = models.CharField(max_length=50,blank=True,null=True)
    ciudad = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.nombre
    
class Mascota(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30,blank=False,null=False)
    apellidos = models.CharField(max_length=30,blank=False,null=False)
    especie = models.CharField(max_length=30,blank=True,null=True)
    color = models.CharField(max_length=30,blank=True,null=True)
    edad = models.CharField(max_length=3 , blank=False, null = False)
    decendencia = models.CharField(max_length = 2, blank=True,null=True,default='No')
    enfermedades = models.CharField(max_length = 2, blank=True,null=True,default='No')
    cirugias = models.CharField(max_length = 2, blank=True,null=True,default='No')
    
    def __str__(self):
        return self.nombre