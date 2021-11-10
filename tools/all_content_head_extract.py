import pandas as pd

# Resume_Content_heads.csv


def read_csv(file_name):
    try:
        raw_data = pd.read_csv(file_name)
        # dictionary = {'category': [], 'content': []}
        # for col in raw_data.columns:
        #     heads = [x for x in raw_data[col].tolist() if pd.isnull(x) == False] # removes Nan
        #     for head in heads:
        #         dictionary['category'].append(col)
        #         dictionary['content'].append(head)
        # df = pd.DataFrame.from_dict(dictionary)
        return raw_data
    except:
        raise RuntimeError("Could not open the CSV.")   

def split_only_word(string:str):
    
    '''
    takes a word and
    returns splitted word.
    Example:
    Input: 'language'
    Output: ['l anguage', 'la nguage', 'lan guage']
    '''
    
    ret_list = list()
    word = string.split()
    if len(word) > 1:  # must be one word string
        raise RuntimeError('string can only contain one word.')
    else:
        for n in range(1,4):
            split_word = string[0:n]+" "+string[n:]
            ret_list.append(split_word)
        return ret_list
    


def split_first_word(string:str):
    '''
    takes a string and
    returns splitted (only on first word) string.
    Example:
    Input: 'language (&) ability'
    Output: ['l anguage (&) ability', 'la nguage (&) ability', 'lan guage (&) ability']
    '''
    
    ret_list = list()
    word = string.split()
    if len(word) <= 1:
        raise RuntimeError('string must contain at least two words.')    
    else:
        for n in range(1,4):
            split_string = string[0:n]+" "+string[n:]
            ret_list.append(split_string)
    return ret_list

def split_all_word(string:str):
    '''
    takes a string and
    returns splitted string.
    Example:
    Input: 'language (&) ability'
    Output: ['l anguage (&) a bility', 'la nguage (&) ab ility', 'lan guage (&) abi lity']
    '''
    
    ret_list = list()
    words = string.split()
    if len(words) <= 1:
        raise RuntimeError('string must contain at least two words.')
    else:
        for n in range(1,4):
            formtd_string = ""
            counter = 0
            for word in words:
                counter+=1
                if word == '(&)':
                    splitd_word = word
                else:
                    splitd_word = word[0:n]+" "+word[n:]

                if counter < len(words):
                    formtd_string += splitd_word + " "
                else:
                    formtd_string += splitd_word
                
            ret_list.append(formtd_string)
        return ret_list
    
def remove_character_from_front(string:str):
    '''
    takes a string and
    returns string with removed character from front.
    Example:
    Input: 'language (&) ability'
    Output: ['anguage (&) ability', 'nguage (&) ability', 'guage (&) ability']
    '''
    ret_list = list()
    for n in range(1,4):
        removed_string = string[n:]
        ret_list.append(removed_string)
    return ret_list

def remove_character_from_every_word(string:str):
    '''
    takes a string and
    returns string with removed character from every word.
    Example:
    Input: 'language (&) ability'
    Output: ['anguage (&) bility', 'nguage (&) ility', 'guage (&) lity']
    '''
    ret_list = list()
    words = string.split()
    if len(words) <= 1:
        raise RuntimeError('string must contain at least two words.')
    else:
        for n in range(1,4):
            formtd_string = ""
            counter = 0
            for word in words:
                counter+=1
                if word == '(&)':
                    formtd_word = word
                else:
                    formtd_word = word[n:]

                if counter < len(words):
                    formtd_string += formtd_word + " "
                else:
                    formtd_string += formtd_word
                
            ret_list.append(formtd_string)

    return ret_list


def generate_head_list(col_li: list, filename:str = 'Resume_Content_heads.csv'):
    try:
        data = read_csv(filename)
    except:
        raise IOError(f"Couldn't open the CSV ({filename}) file.")
    generated_heads = list()
    if not col_li:
        # if col_li list is empty (means we need all heads) 
        # then push all head to col_li.
        col_li = data.columns
    for col in data.columns:
        if col in col_li:
            # remove NaN values
            heads = [x for x in data[col].tolist() if pd.isnull(x) == False]
            for head in heads:
                word = head.split()
                if len(word) > 1:
                    generated_heads.extend(split_all_word(head))
                    generated_heads.extend(split_first_word(head))
                    generated_heads.extend(remove_character_from_every_word(head))
                else:
                    generated_heads.extend(split_only_word(head))
                generated_heads.extend(remove_character_from_front(head))
                generated_heads.append(head)
    return generated_heads

def save_txt(col_li = [], save_file_name:str = "list.txt"):
    '''
    if col_li is [] then it will extract all heads,
    if you want to extract the specific columns then pass through the
    col_li list.
    '''
    try:
        heads = generate_head_list(col_li)
        textfile = open(save_file_name, "w")
        for head in heads:
            textfile.write("'"+head+"'" + ",\n")
        textfile.close()
    except:
        raise IOError(f"Could not save the txt ({save_file_name}) file.")
    
def save_txt_one(csv_filename:str = 'Resume_Content_heads.csv', save_file_name:str = "list_one.txt"):
    '''
    it doesn't split or remove anything.
    just save the head from the csv file.
    '''
    try:
        try:
            textfile = open(save_file_name, "w")
        except:
            raise IOError(f"Could not save the txt ({save_file_name}) file.")
        data = read_csv(csv_filename)
        ret_heads = list()
        for col in data.columns:
            # remove NaN values
            print(col)
            heads = [x for x in data[col].tolist() if pd.isnull(x) == False]
            for head in heads:
                textfile.write("['"+head+"', '"+col+"'],\n")
                # ret_heads.append(head)
        textfile.close() 
    except:
        raise IOError(f"Couldn't open the CSV ({csv_filename}) file.")


# Testing all functions
assert split_only_word('language') == ['l anguage', 'la nguage', 'lan guage']
assert split_first_word('language (&) ability') == \
    ['l anguage (&) ability', 'la nguage (&) ability', 'lan guage (&) ability']

assert split_all_word('language (&) ability') == \
    ['l anguage (&) a bility', 'la nguage (&) ab ility', 'lan guage (&) abi lity']
# split_all_word('language')
assert remove_character_from_front('language (&) ability') == \
    ['anguage (&) ability', 'nguage (&) ability', 'guage (&) ability']
assert remove_character_from_every_word('language (&) ability') == \
    ['anguage (&) bility', 'nguage (&) ility', 'guage (&) lity']


if __name__ == '__main__':
    col = []  # [] means all
    save_txt(col)
    save_txt_one()