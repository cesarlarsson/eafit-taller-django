# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from encuestas.models import Encuesta, Respuesta
#from django.template import Context, loader
#from django.shortcuts import render

from django.http import Http404
from django.shortcuts import get_object_or_404, render # acceso rapido a la porpieda loader

def index(request):
    #latest_poll_list = Encuesta.objects.order_by('-fecha_pub')[:5]
    #output = ', '.join([p.pregunta for p in latest_poll_list])
    #return HttpResponse(output)
    #return HttpResponse("Esta es nuestra pagina de encuestas por defecto")

    #ultimas_encuestas = Encuesta.objects.order_by('-fecha_pub')[:5]
    #template = loader.get_template('encuestas/index.html')
    #context = Context({
    #    'ultimas_encuestas': ultimas_encuestas,
    #})
    #return HttpResponse(template.render(context))    

    ultimas_encuestas = Encuesta.objects.order_by('-fecha_pub')[:5]
    context = {'ultimas_encuestas': ultimas_encuestas}
    return render(request, 'encuestas/index.html', context)

def detalles(request, encuesta_id):
    #return HttpResponse("La encuesta que estas buscando es la %s." % encuesta_id)

    try:
        encuesta = Encuesta.objects.get(pk=encuesta_id)
    except Encuesta.DoesNotExist:
        raise Http404
    return render(request, 'encuestas/detalles.html', {'encuesta': encuesta})    

def voto(request, encuesta_id):
    p = get_object_or_404(Encuesta, pk=encuesta_id)
    try:
        selected_choice = p.respuesta_set.get(pk=request.POST['resp'])
    except (KeyError, Respuesta.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'encuestas/detalles.html', {
            'encuesta': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votos += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('encuestas:resultados', args=(p.id,)))

def resultados(request, encuesta_id):
    poll = get_object_or_404(Encuesta, pk=encuesta_id)
    return render(request, 'encuestas/resultados.html', {'encuesta': poll})

