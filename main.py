#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from helper import*
import math
import os
from moviepy.editor import VideoFileClip
from IPython.display import HTML


##########################################
# for pics output from the dir above uncomment the below 2 lines
##########################################
dir = os.listdir("test_images/")
for file in dir:
    process_image(file)

######################################################
# VideoFileClip
######################################################



## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
# clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)

dir2 = os.listdir("test_videos/")
for file in dir2:
    white_output = os.path.join('test_videos_output/', file) #'test_videos_output/challenge.mp4' #
    clip1 = VideoFileClip(os.path.join('test_videos/', file))#'test_videos/challenge.mp4')#

    white_clip = clip1.fl_image(process_image1) #NOTE: this function expects color images!!
    # %time 
    white_clip.write_videofile(white_output, audio=False)
    HTML("""
    <video width="960" height="540" controls>
    <source src="{0}">
    </video>
    """.format(white_output))


