# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./test_images_output/gray.jpg 
[image2]: ./test_images_output/blurr.jpg 
[image3]: ./test_images_output/edges.jpg 
[image4]: ./test_images_output/masked_img.jpg 
[image5]: ./test_images_output/solidWhiteCurve.jpg 

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps. First, I converted the images to grayscale.
![alt text][image1]
Then I blurred the gray scale image.
![alt text][image2]
Then I used canny() to generate edges.
![alt text][image3]
Then I have took out the region of interest. 
![alt text][image4]
Using hough transform generated 
coloured lines from these edges and then interpolated them with the original image. 
![alt text][image5]

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by adding thickness.





### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when a picture with low gradient change like in challenge.mp4 there is a small area where
yellow line can't be ditected as the gradient change is not so high


### 3. Suggest possible improvements to your pipeline

Dealing with the above shortcoming is something that needs to be improved
