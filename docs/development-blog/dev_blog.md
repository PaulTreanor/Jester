# Jester Development Blog 

This blog is to document the research and design done during the development of Jester. 

_____



## Data-preprocessing - Paul - 02/02/2021

In order to use our dataset to create a classifier, the images needed to be processed by OpenPose and then preprocessed to make the data more consistent, complete, and interpretable.  

### Getting OpenPose output
Our dataset of images was stored in 3 folders (1 for each class). We labelled each image file with a class name using simple python program that renames images with the format *fileName+ imageNumber*.  This will make supervised machine learning possible later. 

We used the pose detection library [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) to extract keypoint data from the images in our dataset. By default OpenPose takes a folder as input and processes all images within that folder. We found that  if more than 2 or 3 images were in a folder OpenPose would throw an "out of memory" error and crash. This error occured on both our machines with several version of OpenPose. 

To fix this we wrote *batch_image_processor.py* which iterates through our dataset and places each image in its own folder, then writes a line to a batch file to run OpenPose on that folder. The batchfile runs OpenPose automatically for all the folders, and doesn't crash because the input folders only contain one image each.

When the batch file OpenPose returned a json file of keypoint data for each image.   

### Data cleaning 
Data cleaning is an important part of data preprocessing where inconsistent data is removed [1]. In our case this meant removing items from the dataset with no keypoint data. These were blurry images which OpenPose couldn't process. 

The program *data_cleaning.py* iterates through all the OpenPose output JSON files and adds the right hand keypoint data to a *gesture_dataset.csv* file. Files that contain no values for right hand keypoint coordinates were removed. 

### Data transformations
Data transformations were carried to change the data into a homogeneous form that would allow for more accurate machine learning [1]. We carried out transformations on the dataset to normalise the size of the keypoint distribution and place the keypoints in the same position and orientation.

The program *data_tranformer.py* applies a translation, an enlargement, and a rotation to each tuple in the dataset. These transformations move the keypoint 0 to the origin, normalise the distance between *point 0* and *point 9* to 10 units, and rotate the coordinates around the origin so that *point 0* and *point 9* both lie on the y axis. 

OpenPose hand keypoint labels |
:-------------------------:
![](images/keypoints_hand.png) |

Coordinates before transformations	             |  Coordinates after transformations	
:-------------------------:|:-------------------------:
![](images/before.png)  |  ![](images/after.png)

In addition to the transformation program we also wrote unit tests for the functions in the program. It is vital that the transformations work the way they are supposed to in order for the classifier to be accurate. 

### References  
 1. Han, J. Kamber, M. Pei, J. (2012). Data Mining Concepts and Techniques. Waltham, USA: Morgan Kaufmann, pages 85 & 111


## App Development - Colin - 28/01/2021
The main application is build on Android Studio using Java and XML.

### Starting off
The beginning process for the app was to plan out the layout of what the UI will look like. This was relatively straightforward as there are only two interfaces that the user will interact with: the main screen with the camera preview and  a secondary setting menu screen.

### Development
When it came to developing, I put together a simple splash screen first. This displayed our logo on a simple gradient background. The splash is purely for aesthetic purposes but I believe it is a nice feature to include in the app.

Afterwards, I began with implementing a basic camera feature. Android's originally **Camera** package is outdated and is deprecated. So, I looked into Google's **Jetpack CameraX** package. However, this package is implemented in Kotlin, the new Android devleopment language. After much discussion with Paul, we decided to stick to programming in Java and use the imporved **camera2** package supplied by Android Studio.

Firstly, I had to go into the app's <code>AndroidManifest.xml</code> and ask permission to use the device's camera. After that, I set up a <code>TextureView</code> in the MainActivity. This allows a preview screen to appear on the device's screen, and a simple button to capture a image <code>onClick</code>.

Using Ansdroid Studio's online libraries and documents on **camera2**, I implemented a basic image capturing camera.

Splash Screen             |  MainActivity 		| 
:-------------------------:|:--------------------
![](images/splash.png)  |  ![](images/basic_camera.png)

Next stage is to implement a way to safely store these images into an easily accessably folder.

## Dataset Collection - Paul - 22/01/2021

In order to train a classifier to recognise hand gestures, we need a large training set of hand gesture images. We decided to gather our own training set.

### Choosing gestures 
The first thing to consider was which hand gestures to use. The hand gestures would need to be well known, low in variablity, easy to make, and if possible intuitive to use alongside the functions of the app. The thumbs up and peace sign hand gestures are universally well known and very distinguishable from eachother so were good choices. The "stop" hand gestures (palm facing away from the person) was a natural choice to trigger the stop video recording function of the mobile app. After deciding on these hand gestures I verified that OpenPose could reliably detect all hand keypoints in photos of these gestures. 

### Guidelines for dataset images
The images in the dataset need to be able to be processed by OpenPose, so I tested a variety of images on the software to see what should be avoided when collecting the dataset. I found that OpenPose struggles to identify hand keypoints if a person's face and elbow is not in image, if the hands appear small in the image, and if the image is dark. 

Image too dark             |  Elbows not detected 		| Hands too small
:-------------------------:|:-------------------------:|:-------------------------:
![](images/dark.png)  |  ![](images/elbow.png)|  ![](images/small.png)

### Determining how big the dataset needs to be

When the dataset is not big enough, varience impacts the resulting model more [1]. This leads to overfitting, which reduces the accuracy of the classifier.  A larger training set will create a more robust classifier, allowing it to work with users who have different hand sizes and who make hand gestures in slightly different ways. 

A potential reason in needing a large dataset is the large number of attributes that the 3 classes have. When the number of attributes in a class grows, the amount of items needed in the dataset can grow exponentially, this is known as the "curse of dimensionality" [2]. A rule of thumb is that there should be approximately 5 items for every attribute in the class [3], since our classes have 21 attributes each we would need at least 105 items in our dataset based of this heuristic. 

Two existing hand gesture datasets, the HGM-4 dataset and the Creativ Senz3D dataset have approximately 150 images per class. The Tiny Hand Gesture Recognition dataset uses augmented images to get 70,000 items per class. Due to the low number and distinct shape of our hand gesture classes it is unlikely that we will need this many images per class to make an accurate classifier, although more is always better. 

Practical factors that limit the size of the dataset are the amount of images participants send us and the amount of processing time needed to run the dataset through OpenPose on a standard desktop computer (every 100 images takes roughly 10 minutes of processing providing that there is no issues). We also need to be conscious about how long we spend gathering the dataset since this project has a relatively short deadline. 


### Other dataset considerations
Sample bias can happen when a class appears more often than other classes in a dataset, causing a classifier to learn to select it more often. To avoid sample bias we need an  equal distribution of the 3 classes in our dataset. 

Our dataset will only contain hand gestures made with people's right hands. In the final system we will detect which hand the user is making a gesture with (OpenPose makes this simple) and if the left hand is detected, the hand co-ordinates can be mirrored so the input works with our right hand classifier. 

### The final dataset 
Over the course of 5 days we were able to gather 1800 images across the 3 classes and 13 different people. This should allow us to produce a large enough training set to train our classifier. 

### References 
1. Brain, D. Webb, G. (2000), On the Effect of Data Set Size on Bias and Variance in Classification Learning. Proceedings of the Fourth Australian Knowledge Acquisition Workshop. Available at: https://www.researchgate.net/publication/2456576_On_the_Effect_of_Data_Set_Size_on_Bias_and_Variance_in_Classification_Learning [Accessed 22 Jan. 2021]

2. Raudys, S. Jain, A. (1991). Small Sample Size Effects in Statistical Pattern Recognition: Recommendations for Practitioners. Transactions on pattern analysis and machine intelligence, volume 13, page 262. Available at: https://sci2s.ugr.es/keel/pdf/specific/articulo/raudys91.pdf [Accessed 22 Jan. 2021]

3. Vishwesh, K. (2020). Curse of Dimensionality: An intuitive and practical explanation with examples. Medium. Available at https://medium.com/flutter-community/curse-of-dimensionality-an-intuitive-and-practical-explanation-with-examples-399af3e38e70 [Accessed 22 Jan. 2021]
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE5MDgyMjEwNCwxMDgxNDk3MTk0LC0xNz
ExMDgzODg0LC04MzkxODUyMDAsMTkzOTM1OTgsLTE0NjAzMDAx
MjYsMTQxMTY4Mzc5MV19
-->