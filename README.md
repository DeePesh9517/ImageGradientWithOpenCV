* Image Gradients are functional building block of many computer vision and image processing routines.
- we use gradient for detecting edges in images, which allows us to find contours and outlines of object in images.
- we use them as inputs for quantifying images through feature extraction - in fact highly successful and well-known image descriptors such as Histogram of Oriented Gradients and SIFT are built upon image gradient representations.
- Gradient images are even used to construct saliency maps, which highlight subjects of an image.

# What are image gradients?
* Image gradients are used as the basic building blocks in many computer vision image processing applications.
* However, the main application of image gradient lies within **edge detection**.
* Edge detection is the process of finding edges in an image which reveals structural information regarding the objects in an image.
* Edges could therefor corresponf to:
- Boundaries of an object in an image.
- Boundaries of shadowing of lighting conditions in an image.
- Boundaries of "parts" within an object.

# Computing image gradient manually
* The first step is to compute the gradient of the image. **Fromally, an image gradient is defined as directional change in image intensity.**
* A gradient measures the change in pixel intensity in a given direction by estimating the direction or orientation along with the magnitude (i.e., how strong the change in direction is), we are able to detect regions of an image that look like edges.