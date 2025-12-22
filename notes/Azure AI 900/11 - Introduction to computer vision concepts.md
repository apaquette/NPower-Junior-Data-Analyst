# Introduction
- **Computer vision**: core areas of AI focusing on solutions enabling visual information processing
	- autonomous vehicle needs to detect and response to traffic and pedestrians
	- store uses smart checkouts with cameras to determine the product in a customer's basket
	- doorbell camera detects people at your front door
# Computer vision tasks and techniques
- refers to a range of tasks and techniques
## Image classification
- one of the oldest computer vision solutions
- a model is trained with a large number of images to predict a text label based on contents
## Object detection
- examines multiple regions in an image to find individual objects and their locations
- resulting prediction includes which objects were detected, and the specific regions of the image
## Semantic segmentation
- a model is trained to find objects, and classify individual pixels in the image based on the objects they belong to
- result is a more precise prediction of the location of objects in the image
## Contextual image analysis
- multimodal computer vision models are trained to find contextual relationships between objects in images that describes them
- provides the ability to semantically interpret an image to determine what objects and activities it depicts
# Images and image processing
- an image is an array of numeric pixel values
- array consists of rows and columns representing pixel values of an image (image resolution)
- each pixel has a value between 0 ad 255
- the array defines a single rectangle of pixel values
- a single layer of pixel values is a grayscale image
- most images consist three layers representing red, green, and blue (RGB)
## Filters
- common way to perform image processing is to apply filters that modify the pixel value to create a visual effect

| Original Image                       | Filtered Image                       |
| ------------------------------------ | ------------------------------------ |
| ![[Pasted image 20251222130954.png]] | ![[Pasted image 20251222131002.png]] |
# Convolutional neural networks
- ability to apply filters is useful in image processing
- the goal of computer vision is to extract meaning, or actionable insights, from images
- **convolutional neural network (CNN)**: type of deep learning architecture to extract numeric feature maps from images and feed the feature values into a model to generate label predictions
- during training, filter kernels are defined using random weight values
- as the training process progresses, the model predictions are evaluated against known labels, and the filter weight is adjusted to improve accuracy
![[Pasted image 20251222132826.png]]
1. Images with known labels are fed into the network to train the model
2. One or more layers of filters is used to extract features from each image. The filter kernels start with randomly assigned weights and generate arrays of feature maps. Additional layers may downsize the feature maps to create smaller arrays that emphasize key visual features.
3. The feature maps are flattened into a single dimensional array of feature values
4. The feature values are fed into a fully connected neural network.
5. The output layer uses a softmax or similar function to produce a result that contains a probability value for each possible class
- the output probabilities are compared to the actual class label
- the difference between the predicted and actual class is used to calculate the loss in the model
- training process repeats over multiple epochs until an optimal set of weights has been learned
- the weights are then saved and the model can be used to predict labels
# Vision transformers and multimodal models
- CNNs have been the core of computer vision for many years
- they're commonly used to solve image classification problems
- many advances in computer vision have been driven by improvements in CNN-based models
## Semantic modelling for language - Transformers
- **Transformers**: work by processing huge volumes of data and encoding language as tokens and vector-based embeddings
- attention: used to assign embedding values that reflect aspects of how each token is used in the context of other tokens
- can think of embeddings as vectors in multidimensional space, where each dimension embeds a linguistic attribute of a token based on its context
- tokens semantically similar are encoded in similar directions
![[Pasted image 20251222133434.png]]
## Semantic model for images - Vision transformers
- vision transformers (ViT): a model is trained using a large volume of images, extracting patches of pixel values from the image to generate linear vectors from the pixel values
![[Pasted image 20251222133533.png]]
- same attention technique used in language models embeds contextual relationships between tokens is used to determine contextual relationships between patches
- instead of encoding linguistic characteristics, the embedded values are based on visual features (color, shape, contract, texture)
- result is a multidimensional "map" of features based on how they are commonly seen in training images
![[Pasted image 20251222133650.png]]
- embeddings result in visual features that are similar in context having similar vector directions
## Bringing it all together - Multimodal models
- **language transformer:** creates embeddings that define linguistic vocabulary that encode semantic relationship between words
- **vision transformer**: creates a visual vocabulary that does the same for visual features
- **multimodal model**: combination of these encoders from both transformers to define a unified spatial representation of the embeddings
![[Pasted image 20251222133908.png]]
- combination of language and vision enables the model to discern semantic relationship between language and visual features
- enables the model to predict complex description for images it hasn't seen
# Image generation
- same multimodal architecture that enables AI to create natural language responses to visual input can be used to create images in response to natural language prompts
- an image synthesis model can take a description of a desired image or video and generate it
- most modern image-generation models use diffusion
- a prompt is used to identify a set of related visual features that can be combined to create an image
- the image is created iteratively starting with a random set of pixel values and removing "noise"
- after each iteration, the model evaluates the image so far to compare it to the prompt, until a final image that depicts the desired scene is produced
- example: A dog carrying a stick in its mouth
![[Pasted image 20251222134252.png]]
- some models can apply a similar process  to generating videos
- video generation process uses the same technique to identify visual features associated with language tokens
# Summary
Computer vision is built on the analysis and manipulation of numeric pixel values in images. ML models are training with a large volume of images to enable common computer vision scenarios, including image classification, object detection, semantic segmentation, caption generation, and others.

The models have evolved from statistics-based image classifiers through convolutional neural networks to transformer-based multimodal models. Cutting-edge models can interpret visual input and generate visual output.