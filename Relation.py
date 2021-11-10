from re import search
import re
from Data_Clean import cleaning_data
from re import search
import re
from tools.utils import content_heads
import copy
import operator
from tools.head_title_list import give_head_title
import os

class test():

    def __init__(self, filename):
        self.cleaning_data = cleaning_data
        self.content_heads = content_heads
        self.filename = filename

    def generate_one_word_list(self):
        '''
        one word list
        '''
        one_word_list = list()
        origin_list = list()
        for word in self.new_word_list:
            origin = (word[0], word[6], word[7], word[8])
            origin_list.append(origin)
            one_word_list.append(re.sub('\W+','',word[5]))
        one_word_list = list(zip(one_word_list, origin_list, origin_list))
        return one_word_list

    def generate_two_word_list(self):
        '''
        two word list
        '''
        two_word_list = list()
        origin_list = list()
        last_origin_list = list()
        for i, word in enumerate(self.new_word_list):
            if i != len(self.new_word_list)-1:
                this_word = word
                next_word = self.new_word_list[i+1]
                st = re.sub('\W+','', this_word[5]) + " " + re.sub('\W+','', next_word[5])
                # st = this_word[5] + " " + \
                #     next_word[5]
                origin = (this_word[0], this_word[6], this_word[7], this_word[8] )
                last_origin = (next_word[0], next_word[6], next_word[7], next_word[8])
                two_word_list.append(st)
                origin_list.append(origin)
                last_origin_list.append(last_origin)
        two_word_list = list(zip(two_word_list, origin_list,last_origin_list))
        return two_word_list

    def generate_three_word_list(self):
        '''
        three word list
        '''
        three_word_list = list()
        origin_list = list()
        last_origin_list = list()
        for i, word in enumerate(self.new_word_list):
            if i < len(self.new_word_list)-2:
                this_word = word
                next_word = self.new_word_list[i+1]
                next_next_word = self.new_word_list[i+2]
                st = re.sub('\W+','', this_word[5]) + " " + \
                    re.sub('\W+','', next_word[5]) + " " + \
                    re.sub('\W+','', next_next_word[5])
                # st = this_word[5] + " " + \
                #     next_word[5] + " " + \
                #     next_next_word[5]
                origin = (this_word[0], this_word[6], this_word[7], this_word[8])
                three_word_list.append(st)
                origin_list.append(origin)
                last_origin = (next_next_word[0], next_next_word[6], next_next_word[7], next_next_word[8])
                last_origin_list.append(last_origin)
        three_word_list = list(zip(three_word_list, origin_list, last_origin_list))
        return three_word_list

    def extract_heads(self, one_word_list, two_word_list, three_word_list):
        # print(one_word_list)
        '''
        Extract the head
        '''
        origin = list()
        head_li = list()
        head_title = list()
        last_origin = list()
        for tot_head in self.reference_head_list:
            head = re.sub('\W+',' ', tot_head[0]).lower()
            if len(head.split()) == 1:
                for word in one_word_list:
                    
                    if word[1][3] != 0:
                        continue
                    # print(re.sub('\W+','', head.lower()), re.sub('\W+','', word[0].lower()),\
                    #     re.sub('\W+','', head.lower()) == re.sub('\W+','', word[0].lower())\
                    #     )
                    if re.sub('\W+','', head.lower()) == re.sub('\W+','', word[0].lower()):
                        # print(word[0])
                        head_li.append(word[0])
                        head_title.append(tot_head[1]) # add this to others
                        origin.append(word[1])
                        last_origin.append(word[2])
            elif len(head.split()) == 2:
                for word in two_word_list:
                    # print(word[0], head)
                    if word[1][3] != 0:
                        continue
                    # print(re.sub('\W+','', head.lower()) , re.sub('\W+','', word[0].lower()))
                    # print(re.sub('\W+','', head.lower()) == re.sub('\W+','', word[0].lower()))
                    if re.sub('\W+','', head.lower()) == re.sub('\W+','', word[0].lower()):
                        head_li.append(word[0])
                        head_title.append(tot_head[1])
                        origin.append(word[1])
                        last_origin.append(word[2])
            elif len(head.split()) == 3:
                for word in three_word_list:
                    if word[1][3] != 0:
                        # print(word)
                        continue
                    if re.sub('\W+','', head.lower()) == re.sub('\W+','', word[0].lower()):
                        # print(re.sub('\W+','', head.lower()), re.sub('\W+','', word[0].lower()))
                        head_li.append(word[0])
                        head_title.append(tot_head[1])
                        origin.append(word[1])
                        last_origin.append(word[2])
        head_li = list(zip(head_li, origin, last_origin, head_title))
        # print(head_li)
        return head_li
      
    def remove_duplicate_heads(self, head_li):
        '''
        Remove copies
        '''
        # print(head_li)

        # new_head_li = copy.copy(head_li)
        for i, val in enumerate(head_li):
            # print("head->", val)
            if not re.sub('\W+','', val[0])[0].isupper():
                # print("From is title->", val[0])
                head_li[i] = ("", "", "", "")
                # del new_head_li[i]
                # new_head_li.remove(val)
            for j, head in enumerate(head_li):
                if j>=i:
                    continue
                # print(re.sub('\W+','', head[0]).lower(), re.sub('\W+','', val[0]).lower(), \
                #     re.sub('\W+','', val[0]).lower().find(re.sub('\W+','',head[0] ).lower()))
                if re.sub('\W+','', head[0]).lower().find(re.sub('\W+','',val[0] ).lower()) > -1:
                    # print(head[0].find(val[0]))
                    # if val in new_head_li:
                        # new_head_li.remove(val)
                        # print("From copy head->", val[0])
                        # del new_head_li[i]
                    head_li[i] = ("", "", "", "")
        new_head_li = [val for val in head_li if val!=("", "", "", "")]
        new_head_li = sorted(new_head_li, key=operator.itemgetter(1))
        head_li = list()
        for i, val in enumerate(new_head_li):
            if i == len(new_head_li)-1:
                head_li.append(val)
            else:
                if new_head_li[i][1]!= new_head_li[i+1][1]:
                    head_li.append(val)

        return head_li

    def extract_child(self, head_list):
        '''
        Child searchings
        '''
        # print(self.new_word_list)
        # print("From child",head_list)
        child_list = ['']*len(head_list)
        head_ind = - 1
        others = ""
        
        first_word = self.new_word_list[0]
        first_word_origin = (first_word[0], first_word[6], first_word[7], first_word[8])
        first_head_origin = head_list[0][1]
        if first_word_origin == first_head_origin:
            head_ind = 0
            

        for word_ind, word in enumerate(self.new_word_list):
            word_origin = (word[0],word[6],word[7],word[8])
            if head_ind == -1:
                next_word = self.new_word_list[word_ind + 1]
                next_word_origin = (next_word[0], next_word[6], next_word[7], next_word[8])
                if next_word_origin == head_list[head_ind+1][1]:
                    head_ind += 1
                others += word[5] + " "
            
            elif head_ind < len(head_list) - 1:
                try:
                    # print(head_list[head_ind])
                    # print(word[5], word_origin >= head_list[head_ind][1], word_origin <= head_list[head_ind][2])
                    if word_origin >= head_list[head_ind][1] and word_origin <= head_list[head_ind][2]:
                        # print("f ", word_origin, head_list[head_ind][1])
                        continue
                    next_word = self.new_word_list[word_ind + 1]
                    next_word_origin = (next_word[0], next_word[6], next_word[7], next_word[8])
                    # print(head_ind, word_origin, head_list[head_ind][1])
                    # print("---->", next_word_origin, head_list[head_ind+1][1])
                    child_list[head_ind] += word[5] + " "
                    if next_word_origin == head_list[head_ind+1][1]:
                        head_ind += 1
                except:
                    from termcolor import colored
                    print('\x1b[6;30;41m'+"Problem in CV", '\x1b[0m')
                    return 0
            else:
                if  word_origin <= head_list[head_ind][2]:
                    continue
                child_list[len(head_list) - 1] +=  word[5] + " "
        child_list.insert(0, others)

        return child_list

    def extract_lines(self):
        '''
        extract lines
        '''
        line_list = []
        start_origin_li = []
        end_origin_li = []
        prev_line = -1
        line_list_ind = -1
        end_origin = []
        for word in self.new_word_list:
            '''
            iterate through word and change the line
            number if the word[7] changes
            '''
            
            line_number = (word[6], word[7])
            if prev_line != line_number:
                start_origin = (word[0], word[6], word[7], word[8])
                prev_line = line_number
                start_origin_li.append(start_origin)
                line_list.append("")
                end_origin_li.append("")
                line_list_ind += 1
            line_list[line_list_ind] +=  word[5]
            end_origin = (word[0], word[6], word[7], word[8])
            end_origin_li[line_list_ind] = end_origin
        z = zip(line_list, start_origin_li, end_origin_li)
        line_li = list(z)
        return line_li

    def extract_heads_from_lines(self, line_li):
        origin_li = []
        last_origin_li = []
        head_li = []
        head_title = []
        for head in self.reference_head_list:
            head_ = re.sub('\W+','', head[0])
            # print(head)
            for word in line_li:
                if re.sub('\W+','', head_.lower()) == re.sub('\W+','', word[0].lower()):
                    head_li.append(head[0].title())
                    head_title.append(head[1])
                    origin_li.append(word[1])
                    last_origin_li.append(word[2])
        z = zip(head_li, origin_li, last_origin_li, head_title)
        head_list = list(z)
        return head_list

    def standrad_alike(self):
        _ , _ , _, _, words = self.cleaning_data(self.filename)

        head_values = []
        new_word_list =[]
        word_dict= {}
        pair_slice = []
        slice_list =[]
        has_first_val ={}

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
                words[3] = [(4,) + elem for elem in words[3] ]
                new_word_list = words[0] + words[1] + words[2]+ words[3]

            elif len(words) > 4:
                print('\x1b[6;30;41m'+"Cant Process More that 4 Page. Sorry! "+'\x1b[0m')
                
                return -1


        new_origin_dict= {}

        # print(new_word_list)

        temp = []
        for word in new_word_list:
            li = list(word)
            li[5] = re.sub('\\t',' ',li[5])
            temp.append(tuple(li))
        
        new_word_list = copy.copy(temp)

        # print(new_word_list)
        # exit()
            # word[5] = word[5] == re.sub('\W+','', this_word[5])
        # x = "Education:\tYMCA\tInternational\tCollege"
        # y = re.sub('\\t',' ',x)
        # print(y)
        # exit()

        valss,one_list,_,_,experience,_,_,_ = content_heads()
        self.new_word_list = new_word_list
        self.reference_head_list = one_list
        # [h[0] for h in one_list]

        new_one_list = []
        for word in one_list:
            st = ''.join(e for e in word[0] if e.isalnum())
            new_one_list.append(st)
        # print(new_one_list)

        new_content_head = []    
        for i in one_list:
            i=i[0].split(" ",1)
            i =i[0].title()
            new_content_head.append(i)

        new_word_list_ = list()
        
        for i in new_word_list:
            if re.sub('\W+','', i[5]) != "":                
                li = list(i)
                li[5] = re.sub('\W+','', li[5])                
                new_word_list_.append(tuple(li))
        

        one_word_list = self.generate_one_word_list()
        two_word_list = self.generate_two_word_list()
        three_word_list = self.generate_three_word_list()

        new_head_li = self.remove_duplicate_heads(self.extract_heads(one_word_list, two_word_list, three_word_list))
        # print(new_head_li)
        # print(self.new_word_list)
        # child_list = self.extract_child(new_head_li)



        # for word in new_word_list:
        #     print(word)
        
        # print(new_head_li)

        
        print(new_head_li)

        '''
        Squeezing.......................
        '''
        if len(new_head_li) < 2:
            print('Not enough heads')
            '''
            extract lines
            '''
            
            line_li = self.extract_lines()
            head_list = self.remove_duplicate_heads(self.extract_heads_from_lines(line_li))
            print("From sqz: ", head_list)
            if len(head_list) == 0:
                print('\x1b[6;30;41m'+'Problem in CV'+'\x1b[0m')
                return 0
            '''
            - extract the childs according to head
            '''
            child_list = self.extract_child(head_list)
            if child_list == 0:
                return 0
            head_val = [head[0] for head in head_list]
            head_titl = [head[3] for head in new_head_li]
            tot_list = list(zip(head_val, head_titl, child_list))
        
        else:
            head_val = [head[0] for head in new_head_li]
            head_titl = [head[3] for head in new_head_li]
            child_list = self.extract_child(new_head_li)
            if child_list == 0:
                return 0
            
        head_val.insert(0, 'others')
        head_titl.insert(0, 'others')
        tot_list = list(zip(head_val, head_titl, child_list))    

            

        for input in tot_list:
            print(input[0])
            print("--------------------------------")
            print(input[2])
            print("-----------------------------------------------------------------------------")
        # print("tot list---->",tot_list)

        return tot_list

        '''
        squeeze end................
        '''




        # for word in new_word_list:
        #     for index in new_content_head:
        #         if ( index == word[5]):
        #             new_origin_dict[word[5]] = word[1]


        # for  word in new_word_list:
        #     for index, value in new_origin_dict.items():
        #         if (index==word[5]):
        #             if value == word[1]:
        #                 head_values.append(word[5])
        #                 word_dict[word[6]] = word[5]
        #                 has_first_val[word[5]] = word[0]
        #                 slice_list.append(word[6])

        # slice_list.append(words[0][-1][6])


        # check_length = len(slice_list)

        # for i,k in zip(slice_list[:check_length], slice_list[1:]):
        #     pair_slice.append([int(i), int(k)])

        # dict_vals= {}
        # for index,  i in enumerate(head_values):
        #     for index1,  j in enumerate(pair_slice):
        #         if index == index1:
        #             dict_vals[i] = j


        # dicts ={}

        # for i, j in dict_vals.items():
        #     for  v in new_word_list:
        #         if i == v[5]:
        #             for index , values in has_first_val.items():
        #                 if  v[5] == index:
        #                     if v[0]== values:
        #                         range_index = dict_vals.get(i)
        #                         new =[]
        #                         for ranges in range(range_index[0],range_index[1]):
        #                             for li in new_word_list:
        #                                 if li[0] == values:
        #                                     if ranges == li[6]:
        #                                         # print(i,"VAlUE--->",li[5])
        #                                         new.append(li[5])
        #                                         dicts[i] = new

        # new_dic = {}                                            
        # for index , value in dicts.items():
        #     value = list(dict.fromkeys(value))
        #     value = " ".join(str(x) for x in value)
        #     new_dic[index] = value

        # print(new_dic)
        # return new_dic

    def check_fail(self):
        if True  :
            return self.standrad_alike()

    def extrct_phone_number(self, content):
        lines = self.extract_lines()
        for line in lines:
            # print(line)
            # cont = re.sub('\W+','', line[0])
            cont = line[0]
            # print("Cont----->",cont)
            regex = r"[+,' '][\d]{7}[-,$,' ',][\d]{0,6}|[+,' '][\d]{3}[,-,$,' ',][\d]{4}[-,$,' ',][\d]{0,6}|[(][(+,' '][\d]{3}[)][-,$,' '][\d]{4}\b[-,$,' ',][\d]{0,6}|[[+,' '][\d]{3}[-,$,' ',][\d]{4}[-,$,' ',][\d]{0,6}|[(][(+,' '][\d]{3}[)][-,$,' '][\d]{4}\b[-,$,' ',][\d]{0,6}|[+,' '][\d]{0,7}[-,$,' ',][\d]{0,6}|(880)[\d]{9}|(880)[\d]{4}[-,$,' ',][\d]{0,6}"
            phone = re.search(regex, cont)
            # print(phone)
            if phone:
                # print(cont, phone)
                return phone.group(0)
        return ''

            
    def extrct_email(self, content): 
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email = re.search(regex, content)
        if email:
            return email.group(0)
        else:
            return ''
    
    def find_personal_info(self):
        # os.system('clear')
        st = ""
        for word in self.new_word_list:
            st += word[5] + ' '
        # print(st)
        phone = self.extrct_phone_number(st)
        email = self.extrct_email(st)
        # exit()
        return phone, email
        
    def find_head_in_list(self, li, string):
        for item in li:
            if string.lower() == item.lower():
                return True
        return False
    
    def generate_list_for_db(self, raw_list):
        # self.find_personal_info()
        flag = 0
        _,one_list,_,_,_,_,_,_ = content_heads()
        titles = give_head_title()
        phone, email = self.find_personal_info()

        keys_of_dict = ['resume_id', 'phone', 'email']
        for title in titles:
            keys_of_dict.append(title)

        new_dict = dict(zip(keys_of_dict, ('' for _ in keys_of_dict)))
        # print(new_dict)
        new_dict['resume_id'] = self.filename
        new_dict['phone'] = re.sub('\W+','', phone)
        # print(new_dict['phone'])
        # exit()
        new_dict['email'] = email
        # print(raw_list)
        for item in raw_list:
            # print(item[2])
            new_dict[item[1]] = new_dict[item[1]] + item[2] + " "

        flag = 0
        
        return new_dict, flag