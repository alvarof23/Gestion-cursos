from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código")
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio del curso")
    fecha_fin = models.DateField(verbose_name="Fecha de finalización del curso")

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def clean(self):
        if self.fecha_inicio >= self.fecha_fin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")

    def __str__(self):
        return f"{self.pk} - {self.nombre}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    email = models.EmailField(unique=True, verbose_name="Email")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def clean(self):
        if self.fecha_nacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser posterior al día actual.")
        if (date.today() - self.fecha_nacimiento).days//365 < 18 :
            raise ValidationError("El estudiante debe tener al menos 18 años.")

    def __str__(self):
        return f"{self.pk} - {self.nombre}"


class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name="inscripciones")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="inscripciones")
    fecha_inscripcion = models.DateField(verbose_name="Fecha de inscripción")

    def clean(self):
        if self.fecha_inscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser posterior al día actual.")
        if self.curso.fecha_fin < self.fecha_inscripcion:
            raise ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
        
    def __str__(self):
        return f"Inscripción {self.pk}: Estudiante {self.estudiante.nombre} en Curso {self.curso.nombre}"
