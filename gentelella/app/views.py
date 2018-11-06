from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from docx import Document


def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

def form_upload(request):
    if request.method == "POST":
        file_obj = request.FILES.get('file')
        filename = file_obj.name
        filesize = file_obj.size
        import os
        f = open(os.path.join('/tmp/',filename),'wb+')
        #content = name + ' \n' + str(size)
        for chunk in file_obj.chunks(chunk_size=1024):
            f.write(chunk)
        f.close()
        print('111111')
        return HttpResponse('ok')
    else:
        return HttpResponse('fale')
