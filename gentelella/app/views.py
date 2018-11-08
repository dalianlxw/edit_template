from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
#from app.scripts.docxtohtml import processDocs
from app.scripts.docxread import read_docx


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
        #return HttpResponse('ok')
        #result = processDocs('/tmp/' + filename)
        flnm = '/tmp/' + filename
        print(flnm)
        result = read_docx(flnm)
        #return render(request,'form_test.html',{'aaa': result})
        return render(request,'form_upload.html',{'aaa': result})
        #return render(request,'form_upload.html',{'aaa': 'file_type'})
        #return render(request,'form_upload.html',{'aaa':file_obj.chunks()})
    else:
        return HttpResponse('fale')
