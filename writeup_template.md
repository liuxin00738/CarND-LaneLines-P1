# **Finding Lane Lines on the Road** 

## Writeup Template

### You can use this file as a template for your writeup if you want to submit it as a markdown file. But feel free to use some other method and submit a pdf if you prefer.

---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report

[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

[image2]: ./test_image_output/input_img.jpg "input_img"

[image3]: ./test_image_output/gray_or_blue_img.jpg "gray_or_blue"

[image4]: ./test_image_output/edge_img.jpg "edge_img"

[image5]: ./test_image_output/maked_edge_img.jpg "marked_edge_img"

[image6]: ./test_image_output/lines_img.jpg "lines_img"

[image7]: ./test_image_output/result.jpg "result"

---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps:
* converte the images to one-channel image. In the beginning, I use grayscale image.However, I found that canny edge detector  fails for some images when using grayscale images. For example, the "challenge3.jpg" in the test_image folder. This image is one frame from the challenge video. I found that using only the blue channel of the original image works the best. So I use the blue channel, instead of the grayscale image. My pipeline has a flag to let the user choose using either gray image or using blue channel.
* apply a gaussian filter to remove noise
* apply canny edge detector to detect edges
* apply a mask to preserve only edges that are infront of the car
* find lines using hough transform
* seperate left lane(assume a slop within [0.5, 2]) and right lanes(assume a slop within [-2,-0.5]), and do an average to get the less noisy left and right lane
* draw the lines on the image

In order to draw a single line on the left and right lanes, I modified the draw_lines() function by the following method:
seperate the left lane(assume a slop within [0.5, 2]) and right lanes(assume a slop within [-2,-0.5]), 
and do an average on the slop and offset of the lines, to get the less noisy left and right lane

Here are the images for each step: 
![alt text][image2]
input image

![alt text][image3]
blue channel of the image

![alt text][image4]
edges

![alt text][image5]
edges after mask

![alt text][image6]
lines

![alt text][image7]
result

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be that this method depends a lot on the threshold of the canny edge detectors. When the light condition changes, it might fail to detect the edges.

Another shortcoming could be that for now, I am assuming the slop within [0.5, 2] to get ride of the lines that are irrelevant. However, this might not be the case since the  car might be turning so the slop would change.


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to make the threshold adaptive. Or, using machine learning.
