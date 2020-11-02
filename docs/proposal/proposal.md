# School of Computing &mdash; Year 4 Project Proposal Form


## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title:       | xxxxxx            |
|Student 1 Name:      | xxxxxx            |
|Student 1 ID:        | xxxxxx            |
|Student 2 Name:      | xxxxxx            |
|Student 2 ID:        | xxxxxx            |
|Project Supervisor:  | xxxxxx            |


## SECTION B


### Introduction

The project will cover the areas of image recognition, machine learning, mobile development, server-client communication, and cloud computing.
The result of the project will be an Android application that uses the mobile device’s camera for gesture recognition. 

### Outline

Our project is to create a mobile app that can use gesture recognition to allow the user to interact with the device without actually touching the device. The user can make various hand gestures in view of the phone’s camera which the app will be able to identify as gestures and distinguish from other gestures. 

Our initial plan is for the app to respond to particular gestures for starting and stopping video recording and to take a photo, but this would easily be extendable to more functionality and more gestures once the basic concept is working. 


### Background

We were interested in doing a mobile app based project because we have experience working together on an Android App for our 3rd project. This experience would allow us to take on a more complex project than if we were working in an area that we had no experience with. 
The idea for the gesture recognition app came to us because we both noticed the problem of taking a picture of yourself with a group using a camera’s timer. Setting up the phone in the right position and having the timer set to a reasonable time is clumsy and overly complicated. It would be much easier to trigger the camera off by making a gesture. 
Having identified this problem we realised how gesture recognition could be applied to other features, such as starting and stopping video. 

### Achievements

The project will result in an Android application that can take photos, and start and stop video recordings by recognising the gestures of the user. 
The app isn’t aimed at any particular demographic but would be useful for anyone wanting more control of their phone’s camera at a distance.

### Justification

The Android app will be useful for taking pictures and videos with a phone without needing to actually physically interact with the phone.
This can be used by families for taking group photos at the beach, athletes for recording their technique, or for amateur video makers who don’t have a dedicated cameraperson. 
But we think that the real value in the project isn’t the Android app itself, but the technology behind the app’s main functionality. Once a phone’s camera can recognise a user’s gestures the possibilities are endless. This technology could be used to control music playback, sending messages, or any other number of functions that a user might want to do without having to actually pick up their phones. The technology could even be used outside a mobile app to assist elderly persons using a home security camera to call for help.

### Programming language(s)

1. Python
2. Java 

### Programming tools / Tech stack

####Open Pose
Software that can analyse and track key points on a person. Key points can include elbow, shoulders, finger joints etc. A machine learning program can use key points locations to identify and distinguish between various gestures.

####Python
The machine learning program that will take keypoint analyses from OpenPose as an input will be written in Python. It will use a neural network to classify images and then output whether or not the image is an identified gesture or what gesture it is. 

####Python Flask
The API that will allow the mobile device and the server to communicate will be based on the Python Flask framework. Images will be sent from the mobile device to the server to be processed over the API, and the result will be sent back over the API.

####Amazon Web Services (AWS)
The instance of OpenPose, our python gesture analysis program, and the network API will be running on an AWS server. A server with an external GPU is needed as the GPU is a serious performance bottleneck when running OpenPose on a standard server. 

####Android Studio/Java/XML
The android app component of the project will be built with Android Studio using Java and XML. 


### Hardware

A server with a powerful graphics processing unit (GPU) will be needed for the image processing. This should be accessible through Amazon Web Services, which provides students with $100 of credits for any service they provide. 
There will be no other specialised hardware required. 

### Learning Challenges

1. Machine learning algorithms
2. Using OpenPose
3. AWS hosting 
4. Python Flask (network API)
5. Android development 
6. PyUnit, JUnit
7. Integration testing, System testing

### Breakdown of work

#### Paul

- OpenPose/Machine learning 
- AWS Hosting 
- Server side testing 
        - Integration testing
        - Unit testing


#### Colin

- User feedback 
- App front end development 
- Network API 
- Android testing
        - Unit testing
        - User testing
        - Accessibility testing

#### Joint effort
- Wireframes/prototypes of app
- UML diagrams 
- System testing

