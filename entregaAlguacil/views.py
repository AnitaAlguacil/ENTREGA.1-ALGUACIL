from contextvars import Context
from django.http import HttpResponse
from django.template import Context, Template



def hola (request):
    return HttpResponse('<h1> Esto es nuevo</h1>')

def miNombreEs (request, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    
    return HttpResponse(documentoDeTexto)

def mi_template(request):
    cargar_archivo = open (r'C:\Users\analu\OneDrive\Documentos\ENTREGA.1-ALGUACIL\entregaAlguacil\template\template1.html', 'r')
    template = Template (cargar_archivo.read())
    cargar_archivo.close()
    
    contexto = Context()
    template_renderizado = template.render(contexto)
    
    
    return HttpResponse(template_renderizado)



     
    