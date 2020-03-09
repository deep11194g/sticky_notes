from django.http import HttpResponse
from django.template import loader

from .models import Note


def index(request):
    """Controller function for home page"""
    if request.method == "POST":
        new_note = request.POST.get('new_text')
        if not new_note:
            print(request.POST)
            return HttpResponse('New Note is empty', status=400)
        note = Note(text=new_note)
        note.save()
    notes = Note.objects.all().order_by('-created_at')
    template = loader.get_template('index.html')
    context = {'notes': notes}
    return HttpResponse(template.render(context, request))
