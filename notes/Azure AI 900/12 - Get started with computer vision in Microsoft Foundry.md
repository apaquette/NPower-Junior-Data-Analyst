# Introduction
Computer vision is a field of AI that enables machines to interpret and understand visual information from the world. Computer vision capabilities support automation of time-intensive tasks.

Some applications:
- Manufacturing - Defect Detection
- Healthcare - Medical Imaging Analysis
- Retail - Shelf Monitoring
- Transportation - Autonomous Vehicles

AI vision systems can be created using a range of Foundry tools.
# Understand Foundry Tools for computer vision
- **Azure Vision**: provides prebuilt and customizable computer vision models based on deep learning models
- Azure vision contains several products
	- **Azure Vision Image Analysis**: Detects common objects in images, tags visual features, generates captions, and support OCR
	- **Azure AI Face service**: Detects, recognizes, and analyzes human faces in images

Applications of Azure Vision's image analysis and face detection:
- Search engine optimization
- Content moderation
- Security
- Social media
- Missing persons
- Identity validation
- Museum archive management
# Understand Azure Vision Image Analysis
- Can be used with or without customization
- some capabilities not requiring customization:
	- Describing an image with captions
	- Detecting common objects
	- Tagging visual features
	- Optical character recognition
## Describing an image with captions
- Azure vision has the ability to analyze an image, evaluate objects, and generate human-readable description of the image
## Detecting common objects
- Azure Vision can identify thousands of common objects. 
- It returns predictions including confidence score indicating how confident the model is in the objects identified
- Azure returns a bounding box coordinate that indicate the top, left, width, and height of the object
## Tagging visual features
- Azure Vision can suggest tags for an image based on its contents
- Tags are associated with images as metadata
- tags summarize attributes of the image
## Optical character recognition
- Azure Vision can use OCR to detect text in images
## Training custom models
- can use the service to train a custom model for image classification or object detection
### Image classification
- used to predict the category or class of an image
### Object detection
- detect and classify objects in an image
- it returns a bounding box coordinate for each object
- can train a custom object detection model with your own images
# Understand Azure Vision's Face services capabilities
- Azure AI Face supports specific use cases
	- verifying user identity
	- liveliness detection
	- touchless access control
	- face redaction
## Facial detection
- involves identifying regions of an image that contain a human face
- typically returns a bounding box coordinates around the face
- facial features can be used to train ML models to return other information such as facial features
## Facial recognition
- train a model to identify known individuals from their facial features
- uses multiple images of an individual to train the model
- can improve efficiency, security, and customer experiences
## Azure AI face service capabilities
- Accessories: indicates if the face has accessories
- Blur: how blurred is the face
- Exposure: underexposed or overexposed detection
- Glasses: whether the person is wearing glasses
- Head pose: face's orientation in 3D space
- Mask: whether the face is wearing a mask
- Noise: visual noise of the image
- Occlusion: if there might be objects blocking the face
- Quality for Recognition: rating of high, medium, or low reflecting the images quality
## Responsible AI use
Anyone can use Face service to:
- Detect the location of faces
- Determine if a person is wearing glasses
- Determine if there's occlusion, blur, noise
- Return the head pose coordinates
The Limited Access policy requires customers to submit an intake form to access additional features
- Face verification
- Face identification
- Liveness detection
# Get started in Microsoft Foundry portal
Azure Vision provides building blocks for incorporating vision capabilities in applications.
## Azure resources for Azure Vision service
- **Azure Vision**: specific resource of the azure vision service
- **Foundry Tools**: General resource including Azure Vision along many other Foundry tools
## Get started
- provides a unified platform for enterprise AI operations, model builders, and application develpoment
- provides a UI based around hubs and projects
- create a project to use Foundry Tools including Azure Vision
- Projects 
	- help organize work and resources effectively
	- acts as containers for datasets, models, and other resources
# Summary
Azure Vision is a cloud-based service offering prebuilt and customizable computer vision models powered by deep learning. It supports a variety of tasks including
- object detection
- image tagging
- caption generation
- OCR
The service is divided into specialized components:
- Image Analysis: Detect objects, tags features, generates captions, and performs OCR
- Face Service: Detects and analyzes human faces with advanced facial recognition capabilities