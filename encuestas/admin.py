from django.contrib import admin
from encuestas.models import Encuesta,Respuesta


class RespuestaInline(admin.StackedInline):
    model = Respuesta
    extra = 3

class EncuestaAdmin(admin.ModelAdmin):
    #fields = ['fecha_pub', 'pregunta']
    fieldsets = [
        (None,               {'fields': ['pregunta']}),
        ('Date information', {'fields': ['fecha_pub']}),
    ]
    inlines = [RespuestaInline]

admin.site.register(Encuesta,EncuestaAdmin)
#admin.site.register(Respuesta)