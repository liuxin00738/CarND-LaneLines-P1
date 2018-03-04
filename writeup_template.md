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

[image2]: ./test_image_output/input_img.jpg "input"

[image3]: ./test_image_output/gray_or_blue.jpg "blue_channel"

[image4]: ./test_image_output/edge_img.jpg "edge"

[image5]: ./test_image_output/marked_edge_img.jpg "masked_edge"

[image6]: ./test_image_output/lines_img.jpg "lines"

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

![alt text][image1]

![alt text][image2]

![alt text][image3]

![alt text][image4]

![alt text][image5]

![alt text][image6]

![alt text][image7]
### 2. Identify potential shortcomings with your current pipeline


One potential shortcoming would be what would happen when ... 

Another shortcoming could be ...


### 3. Suggest possible improvements to your pipeline

A possible improvement would be to ...

Another potential improvement could be to ...
