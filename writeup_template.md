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
[image2]: ./test_image_output/input_image.jpg "input image"
---

### Reflection

### 1. Describe your pipeline. As part of the description, explain how you modified the draw_lines() function.

My pipeline consisted of 5 steps:
* converte the images to grayscale
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

![alt text][image1]
[image2]

### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
