#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
import os
from moviepy.editor import VideoFileClip
from IPython.display import HTML

def grayscale(img):
    """Applies the Grayscale transform
    This will return an image with only one color channel
    but NOTE: to see the returned image as grayscale
    (assuming your grayscaled image is called 'gray')
    you should call plt.imshow(gray, cmap='gray')"""
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # Or use BGR2GRAY if you read an image with cv2.imread()
    # return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
def canny(img, low_threshold, high_threshold):
    """Applies the Canny transform"""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size):
    """Applies a Gaussian Noise kernel"""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """
    Applies an image mask.
    
    Only keeps the region of the image defined by the polygon
    formed from `vertices`. The rest of the image is set to black.
    `vertices` should be a numpy array of integer points.
    """
    #defining a blank mask to start with
    mask = np.zeros_like(img)   
    
    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255
        
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    
    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    """
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.
        
    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
    draw_lines(line_img, lines,thickness=20)
    return line_img

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, α=0.8, β=1., γ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.
    
    `initial_img` should be the image before any processing.
    
    The result image is computed as follows:
    
    initial_img * α + img * β + γ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, γ)

def process_image(filename):
    # reading in an image
    image = mpimg.imread(os.path.join('test_images/', filename))

    #printing out some stats and plotting
    print('This image is:', type(image), 'with dimensions:', image.shape)
    gray_img = grayscale(image)
    # plt.imshow(gray_img, cmap='gray')  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')
    kernel_size = 5
    blur_img = gaussian_blur(gray_img,kernel_size)
    # plt.imshow(blur_img,cmap="gray")
    low_threshold = 50
    high_threshold = 150
    edges = canny(blur_img,low_threshold,high_threshold)
    # plt.imshow(edges,cmap = 'Greys_r')
    # Next we'll create a masked edges image using cv2.fillPoly()
    imshape = image.shape

    vertices = np.array([[(50,imshape[0]),(450, 320), (500,320), (imshape[1]-50,imshape[0])]], dtype=np.int32)
    masked_img = region_of_interest(edges,vertices)
    # plt.imshow(masked_img,cmap = 'Greys_r')

    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = 1*np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15    # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 10 #minimum number of pixels making up a line
    max_line_gap = 20    # maximum gap in pixels between connectable line segments

    line_img = hough_lines(masked_img, rho, theta, threshold, min_line_length, max_line_gap)
    # plt.imshow(line_img)
    # Create a "color" binary image to combine with line image
    # color_edges = np.dstack((edges, edges, edges)) 
    line_edges = weighted_img(line_img,image,0.8,1,0)
    plt.imshow(line_edges)
    plt.show()
    print('This line_edges is:', type(line_edges), 'with dimensions:', line_edges.shape)
    return line_edges
    # mpimg.imsave(os.path.join('test_images_output/', filename),line_edges)


def process_image1(image):
    # reading in an image
    # image = mpimg.imread(os.path.join('test_images/', filename))

    #printing out some stats and plotting
    # print('This image is:', type(image), 'with dimensions:', image.shape)
    gray_img = grayscale(image)
    # plt.imshow(gray_img, cmap='gray')  # if you wanted to show a single color channel image called 'gray', for example, call as plt.imshow(gray, cmap='gray')
    kernel_size = 5
    blur_img = gaussian_blur(gray_img,kernel_size)
    # plt.imshow(blur_img,cmap="gray")
    low_threshold = 100
    high_threshold = 200
    edges = canny(blur_img,low_threshold,high_threshold)
    # plt.imshow(edges,cmap = 'Greys_r')
    # Next we'll create a masked edges image using cv2.fillPoly()
    imshape = image.shape

    # vertices = np.array([[(50,imshape[0]),(450, 320), (500,320), (imshape[1]-50,imshape[0])]], dtype=np.int32)
    vertices = np.array([[(imshape[1]*0.1,imshape[0]*0.9),(imshape[1]/2 -10, imshape[0]*0.6), (imshape[1]/2 +10,imshape[0]*0.6), (imshape[1]*0.9,imshape[0]*0.9)]], dtype=np.int32)
    masked_img = region_of_interest(edges,vertices)
    # plt.imshow(masked_img,cmap = 'Greys_r')

    # Define the Hough transform parameters
    # Make a blank the same size as our image to draw on
    rho = 2 # distance resolution in pixels of the Hough grid
    theta = 1*np.pi/180 # angular resolution in radians of the Hough grid
    threshold = 15    # minimum number of votes (intersections in Hough grid cell)
    min_line_length = 10 #minimum number of pixels making up a line
    max_line_gap = 20    # maximum gap in pixels between connectable line segments

    line_img = hough_lines(masked_img, rho, theta, threshold, min_line_length, max_line_gap)
    # plt.imshow(line_img)
    # Create a "color" binary image to combine with line image
    # color_edges = np.dstack((edges, edges, edges)) 
    line_edges = weighted_img(line_img,image,0.8,1,0)
    # plt.imshow(line_edges)
    # plt.show()
    # mpimg.imsave(os.path.join('test_images_output/', filename),line_edges)
    # print('This line_edges is:', type(line_edges), 'with dimensions:', line_edges.shape)
    return line_edges
    
