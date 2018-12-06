from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.core import serializers
import json,uuid,os,hashlib,docx
#from app.scripts.docxtohtml import processDocs
from app.scripts.docxread import read_docx
import docx2txt
from  app.models import Edition,Grade,Subject,Papertype,Pharse,Chapter,PaperList

def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))

def get_edition(request):
    list = Edition.objects.all()
    return list

def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))

def form_info(request):
    edition_list = Edition.objects.all()
    subject_list = Subject.objects.all()
    grade_list = Grade.objects.all()
    paper_list = Papertype.objects.all()
    sheng_list = ['辽宁','上海']
    shi_list = [['大连','丹东'],['浦东','崇明']]

    return render(request,'form_upload.html',{'grade_list':grade_list,'paper_list':paper_list,'edition_list':edition_list,'paper_list':paper_list,'subject_list':subject_list,'sheng_list':sheng_list,'shi_list':shi_list})



def form_upload(request):
    if request.method == "POST":
        subject_ver = request.POST.get('subject_ver')
        grade_ver = request.POST.get('grade_ver')
        paper_ver = request.POST.get('paper_type')
        chapter = request.POST.get('chapter')
        file_obj = request.FILES.get('file')
        file_ext = file_obj.name.split('.')[-1]

    # 生成uuid文件名和目录
        filename = '{}.{}'.format(uuid.uuid4().hex,file_ext)
        hash_v = hash(filename)
        dir1 = str(hash_v & 0xf)
        dir2 = str((hash_v >>4 & 0xf))
        filepath = "/var/www/upload/" + dir1 +"/"+ dir2
        print(filepath +"/"+ filename)
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        f = open(os.path.join(filepath+"/"+filename),'wb+')
        #文件内容进行md5处理
        m = hashlib.md5()

        for chunk in file_obj.chunks(chunk_size=1024):
            f.write(chunk)
            m.update(chunk)
        hashex = m.hexdigest()
        f.close
        print(hashex)
        status = 0
        
        try:
            filehash = PaperList.objects.get(md5hex=hashex)
        except:
            paper_list = PaperList(md5hex=hashex,storage_dir=filepath +"/"+filename)
            print(filepath +"/"+filename)
            paper_list.save()
            print("试卷已保存")
            status = 1;
        else:
            print("试卷已经存在")




    # 读取上传的文件    
        text = []
        if status == 0:
            text.append('本试卷在系统中已经存在!')
            text.append('以下为历史试卷中的试题，如与您的试题不一致，请在上传试卷内随便加入几个空格保存后，重新输入！')
        d = docx.Document(os.path.join(filepath + "/" + filename))
        for p in d.paragraphs:
            if  p.text:   #不显示空行
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
        editor_two = request.POST.get('editor-two')
        print(editor_two)
        print(guanjianzhi)
        print(stda)
        print("--------------")
        context = {}
        context = {'stda':stda,'guanjianzhi':guanjianzhi}
        return HttpResponse('success')
        #return render(request,'result.html',{'result':'ok'})

def chapter(request):
    edition_list = Edition.objects.all()
    subject_list = Subject.objects.all()
    grade_list = Grade.objects.all()
    paper_list = Papertype.objects.all()
    pharse_list = Pharse.objects.all()
    #return render(request,'chapter.html')
    return render(request,'chapter.html',{'grade_list':grade_list,'paper_list':paper_list,'edition_list':edition_list,'pharse_list':pharse_list,'paper_list':paper_list,'subject_list':subject_list})

def get_chapter(request):
    edition = request.POST.get('edition')
    subject = request.POST.get('subject')
    grade = request.POST.get('grade')
    paper_type = request.POST.get('paper_type')
    print(edition)
    chapt_list = Chapter.objects.filter(subjectid=subject,gradeid=grade,editionid=edition).values('chapterid','chapterorder','chapter')

    data = json.dumps(list(chapt_list))
    print(type(chapt_list))
    print(type(data))
    return HttpResponse(data,content_type='application/json')
