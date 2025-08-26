from django.db import models

class Cabana(models.Model):
    nombre = models.CharField(max_length=100)
    clave = models.CharField(max_length=50, unique=True)
    costo_por_dia = models.DecimalField(max_digits=8, decimal_places=2)
    num_personas = models.PositiveIntegerField()
    num_camas = models.PositiveIntegerField()
    servicios = models.TextField(help_text="Lista de servicios disponibles")
    imagen = models.ImageField(upload_to='cabanas/')
    
    def __str__(self):
        return self.nombre


class Promocion(models.Model):
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self):
        return f"Promoción para {self.cabana.nombre}"


class Opinion(models.Model):
    cabana = models.ForeignKey(Cabana, on_delete=models.CASCADE, related_name='opiniones')
    usuario = models.CharField(max_length=100)
    comentario = models.TextField()
    imagen = models.ImageField(upload_to='opiniones/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Opinión de {self.usuario} sobre {self.cabana.nombre}"
