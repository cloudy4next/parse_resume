import pandas as pd
from all_content_head_extract import read_csv

def save_txt_head_titile(csv_filename:str = 'Resume_Content_heads.csv', save_file_name:str = "title_list.txt"):
    '''
    it doesn't split or remove anything.
    just save the head titile from the csv file.
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
            # heads = [x for x in data[col].tolist() if pd.isnull(x) == False]
            textfile.write("'"+col+"',\n")
            # ret_heads.append(head)
        textfile.close() 
    except:
        raise IOError(f"Couldn't open the CSV ({csv_filename}) file.")


if __name__ == '__main__':
    save_txt_head_titile()
    print('Done..')