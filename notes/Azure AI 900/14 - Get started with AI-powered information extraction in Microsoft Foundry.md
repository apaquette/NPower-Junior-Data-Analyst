# Introduction
AI-powered information extraction and analysis enables organizations to gain actionable insights from data that might otherwise be inaccessible. Azure AI includes multiple services that can be used to support information extraction.
# Azure AI services for information extraction
- Provides a wide range of cloud-based services for various AI tasks

| Service                     | Description                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Azure Vision Image Analysis | Enables you to extract insights from images. Includes object identification, generation of captions and tags, and extraction of text. |
| Azure Content Understanding | A generative AI-based multimodal analysis service that can extract insights from structured documents, images, audio, and video       |
| Azure Document Intelligence | Designed to extract fields and values from digital forms.                                                                             |
| Azure AI Search             | Performs AI-assisted indexing in which a pipeline of AI skills are used to systematically extract and index information from content  |
You can use each of these services separately, or combine them to build comprehensive solutions:
- Data capture
- Business process automation
- Meeting summarization and analysis
- Digital asset management (DAM)
- Knowledge mining
# Extract information with Azure Vision
Azure Vision Image Analysis service can be used to extract insights from photographs or small scanned documents.
## Automated caption and tag generation
Can use Azure Vision Image Analysis to generate descriptive text associated with an image. The service can analyze an image and generate:
- A caption that describes the image
- A set of suggested dense captions for key objects in the image
- A collection of tags that help categorize the image
## Object detection
Azure Vision Image Analysis can detect common objects and people in an image.
## Optical character recognition (OCR)
Azure Vision Image Analysis can use OCR to determine the location and content of each line of text, and each individual word. These capabilities are useful when you need to read text in an image for further processing.
# Extract multimodal information with Azure Content Understanding
Azure Content understanding uses AI models to analyze content in multiple formats:
- Text-based forms and documents
- Audio
- Images
- Video
## Analyzing forms and documents
- includes schema-based extraction of fields and their values
## Analyzing audio
- capable of analyzing audio files to provide transcriptions, summaries, and other insights
## Analyzing images and video
- supports analysis of images and video to extract information
# Extract information from forms with Azure Document Intelligence
- supports complex document and form processing scenarios
- offers a large library of prebuilt models
- can also create custom models
# Create a knowledge mining solution with Azure AI Search
- a cloud service for indexing and searching data
- uses of AI skills to extract insights from multiple formats to integrate with other AI services
## Indexers, indexes, and skills
- Defines a repeatable process
1. Ingest data from a source
2. Crack documents to extract content
3. Apply a sequence of tasks to retrieve information and generate a hierarchy of fields
4. Persisting the extracted fields as an index
![[Pasted image 20251222153001.png]]
## Persisting extracted data to a knowledge store
- can persist the extracted data assets to a knowledge store in Azure Storage
- Indexer can save the following kinds of assets
	- tables of field values
	- images extracted from documents
	- JSON documents representing data structures
