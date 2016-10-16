from django.db import models



class Departamento(models.Model):
    cod_depto = models.IntegerField(primary_key=True)
    nom_depto = models.CharField(max_length=50)


    def __str__(self):
        return '{}'.format(self.nom_depto)

class Localidad(models.Model):
    cod_localidad = models.IntegerField(primary_key=True)
    nom_localidad =models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nom_localidad)

    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Domicilio(models.Model):
    cod_domicilio = models.AutoField(primary_key= True)
    calle = models.CharField(max_length=50)
    nro_calle = models.IntegerField()
    coordenadas = models.CharField(max_length=30)

    localidad = models.OneToOneField(Localidad)

    def __str__(self):
        return 'calle {} nro {}'.format(self.cod_domicilio, self.nro_calle)


class Comercio(models.Model):
    cod_comercio = models.AutoField(primary_key= True)
    nombre_cadena = models.CharField(max_length=40)
    nombre_comercio = models.CharField(max_length=40)
    rubro = models.CharField(max_length=20)
    horarios = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=150)
    disponibilidad = models.BooleanField()

    domicilio = models.OneToOneField(Domicilio, on_delete= models.CASCADE)
    img_comercio = models.ImageField(upload_to='img_comercios')

    def __str__(self):
        return 'comercio: {}'.format(self.nombre_comercio)

class Telefono(models.Model):
    nro_tel = models.CharField(primary_key= True, max_length=25)
    descripcion = models.TextField(max_length=30)
    disponibilidad_tel = models.BooleanField()

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nro_tel)

class Pago(models.Model):
    cod_pago = models.AutoField(primary_key=True)
    nombre_pago = models.CharField(max_length=20)
    descripcion = models.TextField(max_length=50)
    disponibilidad_pago = models.BooleanField()

    comercio = models.ForeignKey(Comercio, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nombre_pago)

