from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
#from app.scripts.docxtohtml import processDocs
from app.scripts.docxread import read_docx
import docx2txt

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
        subject_ver = request.POST.get('subject_ver')
        grade_ver = request.POST.get('grade_ver')
        paper_ver = request.POST.get('paper_type')
        chapter = request.POST.get('chapter')
        file_obj = request.FILES.get('file')
        filename = file_obj.name
        filesize = file_obj.size
        import os,docx
        f = open(os.path.join('/tmp/',filename),'wb+')
        #content = name + ' \n' + str(size)
        for chunk in file_obj.chunks(chunk_size=1024):
            f.write(chunk)
        f.close()
        text = []
        d = docx.Document(os.path.join('/tmp/',filename))
        for p in d.paragraphs:
           # if  len(p.text):
            if  p.text:   #不显示空行
                print(p.text)
                text.append(p.text)
        #return HttpResponse('ok')
        #result = processDocs('/tmp/' + filename)
        #flnm = '/tmp/' + filename
        context = {}
        context = {'subject_ver':subject_ver,'grade_ver':grade_ver,'paper_ver':paper_ver,'chapter':chapter}

        #print(flnm)
        #result = read_docx(flnm)
        #return render(request,'form_test.html',{'aaa': result})
        #return render(request,'form_upload.html',{'aaa': result})
        return render(request,'form_submit.html',{'aaa':text})
        #return render(request,'form_submit.html',{'aaa':context})
    else:
        return HttpResponse('fale')

def form_submit(request):
    if request.method =="POST":
        subject_ver = request.POST.get('subject_ver')
        grade_ver = request.POST.get('grade_ver')
        paper_ver = request.POST.get('paper_type')
        chapter = request.POST.get('chapter')
        context = {}
        context = {'subject_ver':subject_ver,'grade_ver':grade_ver,'paper_ver':paper_ver,'chapter':chapter}

        #return HttpResponse(subject_ver)
        return render(request,'form_submit.html',{'aaa':context})
