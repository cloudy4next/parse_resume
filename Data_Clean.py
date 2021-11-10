from DocFile import DocFile
import os
import re

def cleaning_data(filename):

  squeeze =[]
  text_box  =[]
  files= DocFile(filename)
  text_dict , font_dict, words= files.pdf2textlines()
  new_dict = {}
  for i, j in text_dict.items():
    i = re.sub('[^A-Za-z0-9]+', '', i)
    new_dict[i] =  j

  for text, v in text_dict.items():
      round_origin= [round(number) for number in v]
      __int2str__ = ['{}'.format(num) for num in round_origin]
      squeeze.append(v)
      text_box.append(text)

          
  return text_box , squeeze , new_dict , font_dict, words

