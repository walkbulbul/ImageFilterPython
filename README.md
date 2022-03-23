# ImageFilterPython

Filter Effects

Image processing are predefined algorithms that allow us to add image effects and effects to
our images in editing programs. Although we do not notice, we encounter image processing
everywhere in our lives. We come across everywhere on social media, movies, magazines,
books. Apparently, if we think of images like functions that position in images to pixel
values, filters are merely systems that generate a new and preferably improved image from
a combination of pixel values of the original image.

![159665625-4fd2fa8f-1af8-48f2-bd5a-7c0b5e4ffe80](https://user-images.githubusercontent.com/58142688/159665763-25a88bcb-90dd-463b-a5bb-ea2ab99b7f1a.png)

![image](https://user-images.githubusercontent.com/58142688/159665866-06a9997d-24c0-43b6-b504-ae1da13c3b45.png)

![image](https://user-images.githubusercontent.com/58142688/159665911-7f6c1f46-1a30-403e-b01c-b0ed82620ae8.png)

![image](https://user-images.githubusercontent.com/58142688/159665960-c6eb26b9-fbf6-45cf-b92d-83924e6cd1c2.png)

![image](https://user-images.githubusercontent.com/58142688/159665973-67edcea8-c1f1-4186-b524-fd4022c9a3ab.png)

![image](https://user-images.githubusercontent.com/58142688/159665989-a002d419-c5fc-4aa8-af08-1b32b7d73a39.png)

Imported Libraries

![image](https://user-images.githubusercontent.com/58142688/159666079-0191b6d2-2f9f-4b15-8fea-e0bb19483902.png)

Blur Effect

There are lots of ways to do the blur effect to the image. We want to use a box filter to achieve this
process. We found a basic equation for the box filter which is;
F(x,y) * H(u,v) = G(x,y)
F(x,y) means our original image and G(x,y) is our output image and of course H means our filter.
This is basically multiplying by 1/9 of all pixels in 3*3 matrix. Also, if we increase our filter size,
the output image will be more blurred.


![image](https://user-images.githubusercontent.com/58142688/159666184-c505e92e-f7da-428c-a002-f5b9d2b92ba9.png)

After using that filter, we can clearly see that the output image is quite blurred but it adds some
noise to our image. Of course, we can use other alternatives for better results like Gaussian Filter.
Eventually, it also reached our goal.


Sharpen Effect

After some research, we found a lot of ways to add sharpen effect to the image. Generally we come
up with an matrix which is;
-1 -1 -1
-1 9 -1
-1 -1 -1
So we created our matrix with np.array in Collab and thanks to the filter2D function, easily
processed this filter with sharpen effect.

![image](https://user-images.githubusercontent.com/58142688/159666344-2c7e1c90-bd24-4d0e-a4b2-1684cafb0017.png)

Vintage Filter

We are basically doing a transformation of the colors. So images consist of 3 channel values which
are R,G,B. Firstly, we split these channels also, we multiplied by our values and have created our
new channels. Of course, these process is not enough to add this filter, we merge these channels
back to their new values.

![image](https://user-images.githubusercontent.com/58142688/159666519-43b74aa7-94b3-4844-975e-096b896e703e.png)
When we use this effect, we created warm, brown color pictures. The color like historical and we use that for
an antique images.

Painting Filter

For this effect, we use predefined OpenCV function which is pencilSketch. It takes 3 different parameter for
size, control and intensity.

![image](https://user-images.githubusercontent.com/58142688/159666670-383b5c73-af38-4bf2-8a1d-5dcfa5a5a92c.png)

Painting effect is a cool, helps us find new ideas and solutions to a graphical problem. This effect is used by
developers in many fields, as well as in the film and animation industry.

Brightness Filter

As we know, the easiest way to adding brightness to an image is using HSB values. But we don't want to use
that idea, we used addWeighted function to add brightness and contrast values.

![image](https://user-images.githubusercontent.com/58142688/159666786-8a3ac679-b041-4eb4-b479-f519864e923d.png)
When we play with the settings in the image, we actually change the value of all the pixel coefficients.
Image becomes brighter when we add positive constant. Similarly, when we reduce constant it gets darker.

Blue Grain Effect

We add that grain effect randomly thanks to randn function. After creating random value, with add function
we applied grain effect to our image.

![image](https://user-images.githubusercontent.com/58142688/159666896-55f286e1-6f40-4524-b644-68657a07488e.png)














