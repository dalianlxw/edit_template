#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb;

def InsertDb(gradeId,chapter,chapterOrder):
    db = MySQLdb.connect("172.18.250.39","eduser","0D3ced@9BEC10","diliedu",charset='utf8')
    cursor = db.cursor()
    print(chapter)
    #import edition for xinrenjiaoban,code 2;
    #sql = "insert chapter_002(subjectId,pharseId,gradeId,editionId,chapter,unit,section,knowledgeId,chapterOrder,unitOrder,sectionOrder) values(2,1,%s,2,'%s','','',20003,%s,0,0);" % (gradeId,chapter,chapterOrder)
    #import edition for hujiaoban,code 21;
    sql = "insert chapter_002(subjectId,pharseId,gradeId,editionId,chapter,unit,section,knowledgeId,chapterOrder,unitOrder,sectionOrder) values(2,1,%s,21,'%s','','',20003,%s,0,0);" % (gradeId,chapter,chapterOrder)
    #sql + gradeId +",21,"+chapter + ",'','',20003,chapterOrder,int(0),int(0))"
    print(sql)
    cursor.execute(sql);
    db.commit();
    db.close
    
with open('/tmp/scripts/hu_grade.txt','r') as f:
#with open('/tmp/scripts/renjiaoban_grade.txt','r') as f:
    for line in f.readlines():
        #print(line);
        chapterOrder = 0
        for l in line.split(','):
            l = l.strip('\n')
            if chapterOrder == 0:
                gradeId = l;
                chapterOrder += 1
            else:
                if len(l)>0:
                    print(l)
                    print(chapterOrder)
                    InsertDb(gradeId,l,chapterOrder)
                    chapterOrder += 1
                else:
                    print("is null")
