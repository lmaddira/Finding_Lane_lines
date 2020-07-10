# **Finding Lane Lines on the Road** 
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

<img src="examples/laneLines_thirdPass.jpg" width="480" alt="Combined Image" />

Overview
---

When we drive, we use our eyes to decide where to go.  The lines on the road that show us where the lanes are act as our constant reference for where to steer the vehicle.  Naturally, one of the first things we would like to do in developing a self-driving car is to automatically detect lane lines using an algorithm.

In this project we will detect lane lines in images using Python and OpenCV.  OpenCV means "Open-Source Computer Vision", which is a package that has many useful tools for analyzing images.  


**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./test_images_output/gray.png "Grayscale"
[image2]: ./test_images_output/blurr.png "blurred grayscale"
[image3]: ./test_images_output/edges.png "Edges"
[image4]: ./test_images_output/masked_img.png "region of interest"
[image5]: ./test_images_output/solidWhiteCurve.jpg "Final output"
---


### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale.
![Grayscale][image1]
Then I blurred the gray scale image.
![blurred grayscale][image2]
Then I used canny() to generate edges.
![Edges][image3]

Then I have took out the region of interest. 
![region of interest][./test_images_output/masked_img.jpg]

Using hough transform generated 
coloured lines from these edges and then interpolated them with the original image. 
![Final output][image5]

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by adding thickness.



### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when a picture with low gradient change like in challenge.mp4 there is a small area where
yellow line can't be ditected as the gradient change is not so high


### 3. Suggest possible improvements to your pipeline

Dealing with the above shortcoming is something that needs to be improved
