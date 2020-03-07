from django.http import HttpResponse
from django.template import loader

from .models import Note


def index(request):
    """Controller function for home page"""
    notes = Note.objects.order_by('-created_at')
    template = loader.get_template('index.html')
    context = {'notes': notes}
    return HttpResponse(template.render(context, request))
