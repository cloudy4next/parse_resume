import zipfile
import unicodedata
from xml.etree.ElementTree import XML
import fitz
import json
from operator import itemgetter
from itertools import groupby
class DocFile:

    def __init__(self, name):
        self.location = './cv_docs/' + name
        self.format = self.location.split(".")[-1]

    def pdf2textlines(self):
        document = list()
        if self.format == 'pdf':
            document = fitz.open(self.location)
        else:
            print('Error! This file is not in PDF format')
        if document:
            header = "CONTACT INFORMATION"  
            footer = "OBJECTIVE"  
            dict = {}
            font_dict = {}
            words = []
            for page in document:
                display_list = page.getDisplayList()
                text_page = display_list.getTextPage()
               
                text = text_page.extractJSON()
                texts = page.get_text_words()
                words.append(texts)
                html = text_page.extractHTML()
                page_dict = json.loads(text)  

                for i in page_dict['blocks']:
                    line = []
                    origin = []
                    for j in i['lines']:
                        for k in j['spans']:
                            if len(k['text'].split()):
                                dict[k['text']] = k['origin']
                                font_dict[k['text']]=k['size']

            return dict , font_dict, words

        else:
            
            print('Reading PDF file aborted.')
            return None


