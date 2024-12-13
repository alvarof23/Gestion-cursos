from django import forms
from datetime import date
from django.core.exceptions import ValidationError
from .models import Curso, Estudiante, Inscripcion

class curso_form(forms.ModelForm):
    class Meta:
        model = Curso
        fields="__all__"

    def clean(self):
        finicio = self.cleaned_data.get('fecha_inicio')
        ffin = self.cleaned_data.get('fecha_fin')
        if finicio >= ffin:
            raise ValidationError("La fecha de inicio debe ser anterior a la fecha de finalización.")
        
class estudiante_form(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields="__all__"

    def clean(self):
        fnacimiento = self.cleaned_data.get('fecha_nacimiento')
        correo = self.cleaned_data.get('email')

        if Estudiante.objects.filter(correo = correo).exists:
            raise ValidationError("El correo ya está en uso")
        if fnacimiento > date.today():
            raise ValidationError("La fecha de nacimiento no puede ser posterior al día actual.")
        if (date.today() - fnacimiento).days//365 < 18 :
            raise ValidationError("El estudiante debe tener al menos 18 años.")
        

class inscripcion_form(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields="__all__"

    def clean(self):
        finscripcion = self.cleaned_data.get('fecha_inscripcion')
        ffin = self.cleaned_data.get('fecha_fin')
        estudiante = self.cleaned_data.get('estudiante')
        curso = self.cleaned_data.get('curso')

        if finscripcion > date.today():
            raise ValidationError("La fecha de inscripción no puede ser posterior al día actual.")
        if ffin < finscripcion:
            raise ValidationError("No se puede inscribir a un curso que ya ha finalizado.")
        
        if Inscripcion.objects.filter(estudiante=estudiante, curso=curso).exists():
            raise ValidationError("El estudiante ya está inscrito en este curso.")