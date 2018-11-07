#!/usr/bin/env  python
# -*- coding: utf-8 -*-

import  mammoth
#import zipfile
import os

def write_file(content,file_name):
    file = open(file_name,"w")
    file.write(content)
    file.close()

def convert_image(image):
    return {
    	"src":""
    }

def extractImage(docx_file):
	ziped = zipfile.ZipFile(docx_file)
	allFiles = ziped.namelist()
	imgs = filter(lambda x: x.startswith('word/media'),allFiles)
	imgNameArr = []
	for img in imgs:
		data = ziped.read(img)
		idxStr = os.path.basename(img).split(".")[0][-1:]
		#idxStr = os.path.basename(img).split("")
		img_name = os.path.basename(img)
		imgDict = {}
		imgDict["index"] = int(idxStr)-1
		imgDict["fileName"] = img_name
		imgNameArr.append(imgDict)
		targetPath = 'word/media/'
		#print(targetPath)
		target = open(targetPath + img_name,"wb")
		target.write(data)
		target.close()
	ziped.close()
	return imgNameArr

def parseFile(docx_file):
	with open(docx_file,"rb") as docx_file:
		result = mammoth.convert_to_html(docx_file,convert_image=mammoth.images.img_element(convert_image))
		html = result.value
		message = result.messages
		write_file(html,"doc_convert_to_html.html")
		return html

def processDocs(docx_file):
	article = parseFile(docx_file)
	imgNameArr = extractImage(docx_file)
	contentArr = article.split("<img")
	result = []
	#print(contentArr)
	for idx,section in enumerate(contentArr):
		for info in  imgNameArr:
			print(info)
			contentArr[idx] = section + "<img alt= '" + info["fileName"]+"'"
	article = '' .join(contentArr)
	result.append(article)
	#print(result)
	#	for info in imgNameArr:

processDocs('4grade.docx')






















































