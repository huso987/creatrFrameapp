
import sys
import argparse
import os

import cv2

klasör= "video3yyy" #fotoların klasörünü oluşturma
parent_dir = "/home/huseyin/Pictures/"
os.mkdir(os.path.join(parent_dir, klasör))
print(cv2.__version__)
#videonun yolu girilir ve sonra hangi klasöre fotolar atılacak ise onun yolu yazılır
def extractImages(pathIn, pathOut):
    pathIn = "/home/huseyin/Videos/video3.mp4" #videonun yolu 
    pathOut = "/home/huseyin/Pictures/video3yyy/"  #fotoların yolu 
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*2000))    
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        cv2.imwrite( pathOut + "frame%d.jpg" %count, image) 
        count = count + 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="path to video")
    a.add_argument("--pathOut", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)