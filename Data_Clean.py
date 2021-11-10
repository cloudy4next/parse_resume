from DocFile import DocFile
import os
import re

def cleaning_data(filename):

  squeeze =[]
  text_box  =[]
  files= DocFile(filename)
  text_dict , font_dict, words= files.pdf2textlines()
  # print(json_data)
  new_dict = {}
  for i, j in text_dict.items():
    # print(i)
    i = re.sub('[^A-Za-z0-9]+', '', i)
    new_dict[i] =  j

  for text, v in text_dict.items():
      round_origin= [round(number) for number in v]
      # format(math.pi, '.2f')
      __int2str__ = ['{}'.format(num) for num in round_origin]
      squeeze.append(v)
      text_box.append(text)

          
  return text_box , squeeze , new_dict , font_dict, words

    # squeeze =[]
    # text_box  =[]
    # dictionary = {
    #     'filename':[],
    #     'text_box':[],
    #     'squeeze':[],
    #     'text_dict':[], 
    #     'font_dict':[], 
    #     'words':[]
    # }
    # for filename in os.listdir('./cv_docs/'):
    #     files= DocFile(filename)
    #     text_dict , font_dict, words= files.pdf2textlines()
    #     # print(json_data)
    #     for text, v in text_dict.items():
    #         round_origin= [round(number) for number in v]
    #         # format(math.pi, '.2f')
    #         __int2str__ = ['{}'.format(num) for num in round_origin]
    #         squeeze.append(v)
    #         text_box.append(text)
    #     dictionary["filename"].append(filename)
    #     dictionary["text_box"].append(text_box)
    #     dictionary["squeeze"].append(squeeze)
    #     dictionary["text_dict"].append(text_dict)
    #     dictionary["font_dict"].append(font_dict)
    #     dictionary["words"].append(words)
        
    # return dictionary
            

          
    #   return text_box , squeeze , text_dict , font_dict, words

# if __name__ == "__main__":
#     dic = cleaning_data()

#     for i, d in dic.items():
#         print(i, d)