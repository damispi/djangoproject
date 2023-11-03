from django.db import models

class clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name='Direccion')
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=7)
    
    class Meta:
        ordering=["nombre"]
        verbose_name_plural ="Clientes"
    
    def __str__(self):
        return "el nombre es %s " % (self.nombre)



class articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()   

    class Meta:
        ordering=["nombre"]
        verbose_name_plural ="Articulos"

    def __str__(self):
        return "el nombre es %s la seccion es %s y el precio es %s" % (self.nombre, self.seccion, self.precio)

class pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


    class Meta:
        ordering=["numero"]
        verbose_name_plural ="Pedidos"
    def __str__(self):
        return  " %s, %s,%s " %(self.numero, self.fecha, self.entregado)