#!/usr/bin/env  python
# -*- coding: utf-8 -*-

from docx import Document

def read_docx(docx_file):
    document = Document(docx_file)
    data = []
    for paragraph in document.paragraphs:
        print(paragraph.text)
        data.append(paragraph.text)
    return data

