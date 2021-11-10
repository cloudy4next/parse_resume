import os
from Relation_test import test

from db.data_to_db import TODatabase
from tools.utils import content_heads
from Image_Extractor import ImageExtractor
import shutil



if __name__=="__main__":
    NaN_count = 0
    overf_count = 0
    tot =len(os.listdir('./cv_docs/')) - 1
    for filename in os.listdir('./cv_docs/'):
        if filename == ".init":
            continue
        # resume_id, about, education, skills, experience, projects, references,
        print(filename)
        relation = test(filename)
        new = relation.check_fail()

        # image extraction using ImageExtractor
        image_extractor  = ImageExtractor(filename)
        image_extractor.save_image()  # save image to '/image' directory
        img_name = image_extractor.image_name

        img_dict = {'img_file': img_name}

        # print(new)
        if new == -1:
            source = './cv_docs/' + filename
            destination = './overf_3/' + filename
            dest = shutil.copy(source, destination)
            overf_count += 1
            continue
        # print("----------------------------------------------------------------")
        # os.system('clear')
        
        # print('list: ', new)
        # print("----------------------------------------------------------------")
        
        # # os.system('clear')
        
        # print('list: ', new)
        # print("----------------------------------------------------------------")
        
        # # for i in range()
        # print(len(new))

        elif new == 0:
            NaN_count += 1
            source = './cv_docs/' + filename
            destination = './problem_c/' + filename
            dest = shutil.copy(source, destination)
            print("-------------------------------------------------------------------------------")
            continue
        
        dict_to_db, flag = relation.generate_list_for_db(new)
        dict_to_db.update(img_dict)
        # print("Dict to db ---->", dict_to_db)
        # exit()
        NaN_count += flag
        # print(len(dict_to_db))
        data = TODatabase(dict_to_db)
        data.insert_data()
        print("-------------------------------------------------------------------------------")
        if flag == 1:
            source = './cv_docs/' + filename
            destination = './problem_c/' + filename
            dest = shutil.copy(source, destination)
        elif flag == 0:
            source = './cv_docs/' + filename
            destination = './good_c/' + filename
            dest = shutil.copy(source, destination)
    if tot > 0:
        print('None in ', NaN_count)
        print('Overflow in ', overf_count)
        print('Total number: ', tot-overf_count)
        print('Successfully Extracted: ', tot-overf_count-NaN_count)
        print('Accuracy: ', (tot-overf_count-NaN_count)/(tot-overf_count))
    else:
        print('No files..........')
# input to database in col
# resume_id, about, education, skills, experience, projects, reference