import enum
from re import search
from Data_Clean import cleaning_data
import os 
import sys
import csv
from functools import partial
import statistics
from statistics import mode
from re import search
import re
from tools.utils import content_heads
import itertools


class Relation():
    def __init__(self, filename):
        self.cleaning_data = cleaning_data
        self.content_heads = content_heads
        self.filename = filename

    def getDuplicatesWithInfo(self,listOfElems):
        dictOfElems = dict()
        index = 0
        for elem in listOfElems:
            if elem in dictOfElems:
                dictOfElems[elem][0] += 1
                dictOfElems[elem][1].append(index)
            else:
                dictOfElems[elem] = [1, [index]]
            index += 1    
    
        dictOfElems = { key:value for key, value in dictOfElems.items() if value[0] > 1}
        return dictOfElems

    def keywords_origin(self, dictionary, font_dict):
        valss,_,_,_,_,_,_,_ = content_heads()
        key_list = list(dictionary.keys())
        val_list = list(dictionary.values())

        for i, words in enumerate(key_list):
            # words=  words.upper()
            # words= re.sub('[^A-Za-z0-9]+', '', words)
            # print(words)
            for exp in valss:
                # print(exp)
                exp = exp.upper()
                # exp= re.sub('[^A-Za-z0-9]+', '', exp)
                if (exp == words):
                    # print(words)
                    for j, val in enumerate(val_list):
                        # print(j,val)
                        if i == j:
                            font_checker= self.get_font_size(i,font_dict)
                            # print (font_checker)
                            return  val , font_checker
        # print(font_checker)

    def all_parent_name(self, origin_first_key, parent):

        all_parents =[]
        for i, val in enumerate(parent):
            if val == origin_first_key:
                all_parents.append(i)

        return all_parents

    def extract_all_parents_name(self, index_dict, font_dict , content_font):
        name_values = list(font_dict.keys())
        font_highest_check = list(font_dict.values())
        max = content_font
        content_head = []
        empty_String = ['',""]

        for k ,v in font_dict.items():
            if max == v:
                k = re.sub(r'[^\x00-\x7F]',' ', k)
                content_head.append(k)

        while ' ' in content_head:
            content_head.remove(' ')
        print("123---------------",max)
        return content_head 

    def get_font_size(self, vals, font_dict):
        
        li = list
        key_list = list(font_dict.values())
        for k , v in enumerate(key_list):
            if vals == k:
                return v

    def lower_or_upper(self, head_value):

        head_value= head_value.upper()

        return head_value

    def parents__(self):

        val_list = []
        grand_parents= []
        parents = []
        child = []
        new_head = {}

        text , origin , dict_val, font_dict, words = self.cleaning_data(self.filename)
        
        val_list.append(origin)
        for sublist in val_list:
            for index , item in enumerate(sublist):
                parents.append(item[0])
                child.append(item[1])
        # print("111111111111111111",child)

        parents_origin_val, size = self.keywords_origin(dict_val, font_dict)
        '''
        #Debug:
                # all_parents_head = self.all_parent_name(parents_origin_val, parents)
                # print(all_parents_head)
                # content_font = self.get_font_size(all_parents_head,font_dict)
        '''
        get_parent_heads = self.extract_all_parents_name(dict_val, font_dict, size)

        content_heads,_,_ ,_ ,_,_,_,_  = self.content_heads()
        
        for i in  content_heads:
            i = i.title()
            i= re.sub('[^A-Za-z0-9]+', '', i)
            for k, j in enumerate(get_parent_heads):
                j = j.title()
                j= re.sub('[^A-Za-z0-9]+', '', j)
                if (i==j) :
                    # print(i)
                    new_head[k]= j

        get_parent_heads_final =[]
        for k,i in enumerate(get_parent_heads):
            for j, l in new_head.items():
                if j==k:
                    # i = re.sub('[^A-Za-z0-9]+', '', i)
                    get_parent_heads_final.append((i))

        print(get_parent_heads_final)


        return get_parent_heads_final, child 


    def parent_2_child_range(self):

        new_pair_dict ={}
        range_list = []
        pair_range = []
        head_range_list = {}
        
        content_list, _child_list =self.parents__()
        _, _ , dict_val, font_dict, _ = self.cleaning_data(self.filename)
        # print(content_list)
        # for m in con


        #"sunday _update"
        range_list_name = []
        for k , v in dict_val.items():
            for i in content_list:
                # k = re.sub('[^A-Za-z0-9]+', '', k)
                # i = re.sub('[^A-Za-z0-9]+', '', i)
                
                if (i==k):
                    range_list.append(v[1])
                    head_range_list[k] = v[0]
                    # check: head_range_list 
                    # if head less 2 standard
                    range_list_name.append(k)
        # print("head_range_list--------------------->",head_range_list)

        check_length =len(range_list)

        if check_length % 2 != 0:
            range_list.append(_child_list[-1])

        for i,k in zip(range_list[:check_length], range_list[1:]):
           pair_range.append( [str(i), str(k)])

        for i,v in enumerate(range_list_name):
            for k,l in enumerate(pair_range):
                if i == k:
                    new_pair_dict[v] = [l]

        return new_pair_dict, _child_list , head_range_list,content_list


    def childs_of_parents(self):
        p2c_or_p2p_dict, _child_list, _,_=  self.parent_2_child_range()
        # item_list = []
        item_list = []
        slice_list1 = []
        # slice_list2 =[]
        slice_list =[]
        shi = []
        for k, v in p2c_or_p2p_dict.items():
            for index , item in enumerate(_child_list):
                if item == float(v[0][0]):
                    # print( index ,'--------------', item)
                    slice_list.append(index)
                    item_list.append(item)
                if item == float(v[0][1]):
                    # print( index ,'------><--------', item)
                    slice_list.append(index)
                    item_list.append(item)
        # lm1=[]
        # lm2=[]
        # print('->>>>>>>>>>>>>>>>',slice_list1)
        # dictOfElems = self.getDuplicatesWithInfo(item_list1)

        # for key, value in dictOfElems.items():
        #     l=0
        #     for k,v in enumerate(value[1]):
        #         if k == 0:
        #             lm1.append(v)
        # dictOfElemss = self.getDuplicatesWithInfo(item_list2)

        # for key, value in dictOfElemss.items():
        #     l=0
        #     for k,v in enumerate(value[1]):
        #         if k == 0:
        #             lm2.append(v)  

        # ist1 = [j for i, j in enumerate(slice_list1) if i not in lm1]
        # print('1->>>>>',ist1)
        # ist2 = [j for i, j in enumerate(slice_list2) if i not in lm2]
        # print('2--->',lm2)
        # slice_list = sorted(ist1 + ist2)
        # print(slice_list)
        
        slice_list = list(dict.fromkeys(slice_list))

        check_length =len(slice_list)
        pair_slice = []

        for i,k in zip(slice_list[:check_length], slice_list[1:]):
            pair_slice.append([int(i), int(k)])
        # print(pair_slice)

        childs =[]
        for pairs in pair_slice:
            first = int(pairs[0])
            second = int(pairs[1])
            childs.append(_child_list[first:second])       

        for i, k in p2c_or_p2p_dict.items():
            shi.append(i)



        final_value = {}
        for i, k in zip(shi, childs):
            final_value[i] = [k]
        # print(slice_list)
        return final_value


    def segmentation(self):
        _ , _ , dict_val, _ , _= self.cleaning_data(self.filename)

        final = self.childs_of_parents()
        final_list = {}
        for i, k in final.items():
            i = i.upper()
            for items in k[0]:
                it = 0
                for j , l in dict_val.items():
                    for vals in l:
                        if items == vals:
                            final_list[j] = i
        # print(final)
        
        return final_list

    def standard(self,final_list):

        # final_list = self.segmentation()

        li = ['EDUCATION']
        dict = {}
        try:

            for i, v in final_list.items():
                for l in li:
                    if search(l, v):
                            print(l,'------>',i)
        except Exception as e:
            print(e)




    def standrad_alike(self, P_origin, content_head):
        _ , _ , _, _, words = self.cleaning_data(self.filename)

        # print('Origins =================>' ,P_origin)
        head_values = []
        new_word_list =[]
        word_dict= {}
        pair_slice = []
        slice_list =[]
        has_first_val ={}
        eduaction = []

        if words:
            if len(words)==1:
                words[0] = [(1,) + elem for elem in words[0] ]
                new_word_list = words[0]
            elif len(words)==2:

                words[0] = [(1,) + elem for elem in words[0] ]
                words[1] = [(2,) + elem for elem in words[1] ]
                new_word_list = words[0] + words[1]

            elif len(words)==3:

                words[0] = [(1,) + elem for elem in words[0] ]
                words[1] = [(2,) + elem for elem in words[1] ]
                words[2] = [(3,) + elem for elem in words[2] ]
                new_word_list = words[0] + words[1] + words[2]

            elif len(words) == 4:
                words[0] = [(1,) + elem for elem in words[0] ]
                words[1] = [(2,) + elem for elem in words[1] ]
                words[2] = [(3,) + elem for elem in words[2] ]
                words[3] = [(4,) + elem for elem in words[2] ]
                new_word_list = words[0] + words[1] + words[2]+ words[3]

            elif len(words) >4:
                print("Cant Process More that 4 Page. Sorry! ")
                pass
        # print("\n")

        new_origin_dict= {}


        valss,_,_,_,experience,_,_ = content_heads()

        new_content_head = []    
        for i in valss:
            i=i.split(" ",1)
            i =i[0].upper()
            # print(i)
            new_content_head.append(i)
        # print(new_content_head)

        for word in new_word_list:
            for index in new_content_head:
                if (index == word[5]):
                    # print("word[5]----------->",word[5])
                    new_origin_dict[word[5]] = word[1]

        for  word in new_word_list:
            for index, value in new_origin_dict.items():
                if search(index , word[5]):
                    if value == word[1]:
                        head_values.append(word[5])
                        word_dict[word[6]] = word[5]
                        has_first_val[word[5]] = word[0]
                        slice_list.append(word[6])


        print(head_values)
        slice_list.append(words[0][-1][6])


        check_length = len(slice_list)

        for i,k in zip(slice_list[:check_length], slice_list[1:]):
            pair_slice.append([int(i), int(k)])

        dict_vals= {}
        for index,  i in enumerate(head_values):
            for index1,  j in enumerate(pair_slice):
                if index == index1:
                    dict_vals[i] = j


        dicts ={}

        for i, j in dict_vals.items():
            for  v in new_word_list:
                if i == v[5]:
                    for index , values in has_first_val.items():
                        if  v[5] == index:
                            if v[0]== values:
                                range_index = dict_vals.get(i)
                                new =[]
                                for ranges in range(range_index[0],range_index[1]):
                                    for li in new_word_list:
                                        if li[0] == values:
                                            if ranges == li[6]:
                                                # print(i,"VAlUE--->",li[5])
                                                new.append(li[5])
                                                dicts[i] = new

        new_dic = {}                                            #eduaction.append(li[5])
        # final_list = ['0','0',]
        for index , value in dicts.items():
            value = list(dict.fromkeys(value))
            value = " ".join(str(x) for x in value)
            # final_list.append(value)
            new_dic[index] = value

        print(new_dic)
        return new_dic

    def check_fail(self):

        _ , _ , P_origin , content_head= self.parent_2_child_range()

        # print(P_origin)
        if True  :
            return self.standrad_alike(P_origin,content_head)
            # final_list = self.segmentation()

            # return self.standard(final_list)
    def find_head_in_list(self, li, string):
        for item in li:
            if string.lower() == item.lower():
                return True
        return False
    
    def generate_list_for_db(self, raw_list):
        null = 0
        list_to_db = [self.filename, '', '', '', '', '', '', '']
        _, _, about_li, education_li, skill_li, experience_li, project_li, reference_li = self.content_heads()
        if raw_list:
            for key in raw_list:
                if self.find_head_in_list(about_li, key):
                    # print('in about')
                    list_to_db[1] = raw_list[key]
                elif self.find_head_in_list(education_li, key):
                    # print('in education_li')
                    list_to_db[2] = raw_list[key]
                elif self.find_head_in_list(skill_li, key):
                    # print('in skill_li')
                    list_to_db[3] = raw_list[key]
                elif self.find_head_in_list(experience_li, key):
                    # print('in experience_li')
                    list_to_db[4] = raw_list[key]
                elif self.find_head_in_list(project_li, key):
                    # print('in project_li')
                    list_to_db[5] = raw_list[key]
                elif self.find_head_in_list(reference_li, key):
                    # print('in project_li')
                    list_to_db[6] = raw_list[key]
                
                else:
                    (print(f"head '{key}' doesnot match"))
                    list_to_db[7] = list_to_db[7] + raw_list[key]
            
        else:
            null = 1
        
        return list_to_db, null




