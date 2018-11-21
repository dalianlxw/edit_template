from django.views.decorators.csrf import csrf_exempt 
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
def form_upload2(request):
    if request.method == "POST":
        subject_ver = request.POST.get('subject_ver')
        print(subject_ver)
    return HttpResponse('fale')

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
        return render(request,'form_submit2.html',{'aaa':text})
        #return render(request,'form_submit.html',{'aaa':context})
    else:
        return HttpResponse('fale')

def singe_submit(request):
    if request.method =="POST":
        stda = request.POST.get('stda')
        guanjianzhi = request.POST.get('tags_1')
        editor_one = request.POST.get('editor-one')
        print(editor_one)
        print(guanjianzhi)
        print(stda)
        print("--------------")
        context = {}
        context = {'stda':stda,'guanjianzhi':guanjianzhi}

        return HttpResponse('ok')
        #return render(request,'result.html',{'result':'ok'})
