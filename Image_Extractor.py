import cv2
import fitz
import os

if not os.path.exists('haarcascade_frontalface_default.xml'):
    raise ImportError ("haarcascade_frontalface_default.xml file not found.")
else:
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cv_home_dir = "./All_cv/"
temp_dir = "./temp/"
save_dir = "./images/"
icon_dir = "./icon/"

class ImageExtractor(object):

    def __init__(self, cv_filename):
        self.filename = cv_filename
        self.image_name = ""
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
 
    def is_face(self):

        image = temp_dir+self.filename[:-4]+".png"
        try:
            img = cv2.imread(image)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            return len(faces)
        except AssertionError:
            print("Face Not Found.")
    
    def save_image(self):
        '''
            Save the extracted image from CV.
        '''
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        doc = fitz.open(cv_home_dir+self.filename)
        flag = 0
        icon_count = 0
        for i in range(len(doc)):
            for img in doc.getPageImageList(i):
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)
                if pix.n < 5:       # this is GRAY or RGB
                    try:
                        pix.writePNG(temp_dir+self.filename[:-4]+".png")
                        if self.is_face():
                            if flag != 1:
                                pix.writePNG(save_dir+self.filename[:-4]+".png")
                                self.image_name = self.filename[:-4]+".png"
                                flag = 1
                        os.remove(temp_dir+self.filename[:-4]+".png")
                        
                    except AssertionError:
                        print("Image could be not saved.")
                        
                    
                else:               # CMYK: convert to RGB first
                    pix1 = fitz.Pixmap(fitz.csRGB, pix)
                    try:
                        pix1.writePNG(temp_dir+self.filename[:-4]+".png")
                        if self.is_face():
                            if flag != 1:
                                pix.writePNG(save_dir+self.filename[:-4]+".png")
                                flag = 1
                            
                        os.remove(temp_dir+self.filename[:-4]+".png")
                        pix1 = None
                    except AssertionError:
                        print("Image could be not saved.")
                pix = None
        os.rmdir(temp_dir)


if __name__ == "__main__":
    for filename in os.listdir('./All_cv/'):
        if filename == ".init":
            continue
        image_extractor  = ImageExtractor(filename)
        image_extractor.save_image()