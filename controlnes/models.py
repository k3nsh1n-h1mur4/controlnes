from django.db import models


class nesModel(models.Model):
    class Meta:
        db_table = "propuestastbl"

    id = models.IntegerField(primary_key=True, blank=True)
    f_reg = models.CharField('FECHA DE REGISTRO', max_length=255, blank=True)
    aspirante = models.CharField('NOMBRE ASPIRANTE', max_length=255, blank=True)
    categoria = models.CharField('CATEGORIA ASPIRANTE', max_length=255, blank=True)
    cel1 = models.CharField('# CELULAR', max_length=255, blank=True)
    cel2 = models.CharField('# CELULAR2', max_length=255, blank=True)
    apoyo = models.CharField('APOYO', max_length=255, blank=True)
    observaciones = models.CharField('OBSERVACIONES', max_length=255, blank=True)
    zona = models.CharField('ZONA', max_length=255, blank=True)
    status = models.CharField('STATUS', max_length=255, blank=True)
    f_exam = models.CharField('FECHA EXAMEN', max_length=255, blank=True)
    f_env_admi = models.CharField('', max_length=255, blank=True)
    r_exam = models.CharField('RESULTADO EXAMEN', max_length=255, blank=True)
    solicitud = models.CharField('SOLICITUD', max_length=255, blank=True)
    f_audiencia = models.CharField('AUDIENCIA', max_length=255, blank=True)
    paq = models.CharField('# DE PAQUETE', max_length=255, blank=True)


    def __repr__(self):
        return self.id
