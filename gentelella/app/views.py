from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json,uuid,os,hashlib,docx
#from app.scripts.docxtohtml import processDocs
from app.scripts.docxread import read_docx
import docx2txt
from  app.models import Edition,Grade,Subject,Papertype,Pharse,Chapter,Paper

import logging


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
        
        edition_ver = request.POST.get('edition')
        subject_ver = request.POST.get('subject')
        grade_ver = request.POST.get('grade')
        paper_ver = request.POST.get('paper_type')
        chapter_ver = request.POST.get('chapter')
        file_obj = request.FILES.get('file')

#        logging.debug("-------")
        logging.debug(file_obj)

        file_ext = file_obj.name.split('.')[-1]

        logging.debug("edition_ver:%s,subject_ver:%s,grade_ver:%s,paper_ver:%s,chapter:%s" % (edition_ver,subject_ver,grade_ver,paper_ver,chapter_ver))

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
        logging.debug(hashex)
        editionid = Edition.objects.get(id=edition_ver)
        subjectid = Subject.objects.get(id=subject_ver)
        gradeid = Grade.objects.get(id=grade_ver)
        chapterid = Chapter.objects.get(id=chapter_ver)

        #f = Paper.objects.filter(md5hex=hashex).exists()
        if Paper.objects.filter(md5hex=hashex).exists():
            #Author.objects.filter(id=2).exists()    可以这样判断记录是否存在
            logging.debug("文件已经存在")
            #PaperList.objects.filter(md5hex=hashex).delete()
            return HttpResponse("{\"status\":1}")
        else:
            logging.debug("md5hex:%s,editionid:%s,subjectid:%s,gradeid:%s,chapterid:%s" % (hashex,editionid.id,subjectid.id,gradeid.id,chapterid.id))
            paper_list = Paper(md5hex=hashex,storage=filepath +"/"+filename,editionid=editionid,subjectid=subjectid,gradeid=gradeid,chapterid=chapterid) 
            print(filepath +"/"+filename)
            paper_list.save()
            c = Paper.objects.latest('id')
            logging.debug(c.id)
            return JsonResponse({"status":0,"id":c.id},safe=False);

    else:
        logging.debug("非post请求")
        return HttpResponse('非post请求')

def read_file(request,id):
#    logging.debug("------"+id+"-------")
    try:
        filehash = Paper.objects.get(id=id)
        mid5hex = filehash.md5hex
        storage = filehash.storage
        editionid = filehash.id
        subjectid = filehash.id
        gradeid = filehash.id
        chapter = filehash.id
        logging.debug(storage)
    except:
        logging.debug("查询数据库失败")
           
#            return JsonResponse({"status":0,"md5hex":hashex},safe=False);
#    return  render(request,'form_submit2.html',{"aaa":md5hex})

    text = []    
    d = docx.Document(storage)
    for p in d.paragraphs:
        if  p.text:   #不显示空行
            text.append(p.text)
            logging.debug(p.text)
    #context = {}
       #context = {'subject_ver':subject_ver,'grade_ver':grade_ver,'paper_ver':paper_ver,'chapter':chapter}
    #context = {"status":"0"}
#    logging.debug("this way")
    #return HttpResponse(context)
        #return HttpResponse("{\"status\":0,\"aaa\":\"context\"}")
    return render(request,'form_submit.html',{"aaa":text})


def singe_submit(request):
    if request.method =="POST":
        paperedit = request.POST.get('editor')
        paperquestion = request.POST.get('stda')
        keyquestion = request.POST.get('tags_1')
        context = {}
        context = {'editor':paperedit,'stda':paperquestion,'tags_1':keyquestion}
        logging.debug(paperquestion)
        logging.debug(paperedit)
        logging.debug(keyquestion)
       #return HttpResponse('success')
        return HttpResponse("{\"status\":1}")
    else:
        return HttpResponse("{\"status\":0}")
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
    #chapt_list = Chapter.objects.filter(subjectid=subject,gradeid=grade,editionid=edition).values('id','chapterorder','chapter')
    chapt_list = Chapter.objects.filter(subjectid=subject,gradeid=grade,editionid=edition).values('id','chapterorder','chapter');
    data = json.dumps(list(chapt_list))
 #   print(type(chapt_list))
 #   print(type(data))
    return HttpResponse(data,content_type='application/json')
def form_test(request):
    upfile=request.FILES.get('file')
    upfile1=request.FILES.get('file1')
    logging.debug(upfile)
    logging.debug(upfile1)
    return HttpResponse("{\"status\":200,\"mesg\":\"success\"}",content_type='application/json')
