# Introduction
- NLP is a field of AI focused on enabling machines to understand, interpret, and respond to human language
- goal is to analyze and extract meaning or structure from text

# Understand natural language processing on Azure
- core tasks
	- language detection
	- sentiment analysis
	- named entity recognition
	- text classification
	- translation
	- summarization

| Service                                                          | Description                                                                                                                                                                                               |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![[Pasted image 20251220184439.png]]<br>Azure Language service   | Cloud-based service with features for understanding and analyzing text. Includes support for sentiment analysis, key phrase identification, text summarization, and conversational language understanding |
| ![[Pasted image 20251220184545.png]]<br>Azure Translator service | Cloud-based service that uses Neural Machine Translation (NMT) for translation. It analyzes the semantic context of the text and renders a more accurate and complete translation.                        |
# Understanding Azure Language's text analysis capabilities
- **Azure Language**: a part of Foundry tools that can perform advanced natural language processing
- features
	- **Named entity recognition**: identifies people, places, events, and more. Can be customized to extract custom categories
	- **Entity linking**: identifies known entities together with a link to Wikipedia
	- **Personal identifying information (PII)**: identifies personally sensitive information, including personal health information (PHI)
	- **Language detection**: identifies the language of the text and returns a language code
	- **Sentiment analysis and opinion mining**: identifies whether the text is positive or negative
	- **Summarization**: summarizes text by identifying the most important information
	- **Key phrase extraction**: lists the main concepts from the text
## Entity recognition and linking
- can provide Azure Languages with unstructured text and it returns a list of entities that it recognizes
- **entity**: an item of a particular type of category
- Azure Language supports entity linking to help disambiguate entities by linking to a specific reference
## Language Detection
- identifies the language in which the text is written
- For each document, it detects:
	- The language name
	- The ISO 6391 language code
	- A score indicating the level of confidence in the language detection
## Sentiment analysis and opinion mining
- can evaluate text and return a sentiment score and labels for each sentence
- useful for detecting positive and negative sentiment
- uses a pre-built machine learning classification model to evaluate
- returns sentiment score in three categories: positive, neutral, negative
## Key phrase extraction
- identifies the main points from text
# Azure Language's conversational AI capabilities
## Question answering
- provides the ability to create conversational AI solutions
- Question answering supports workloads that require automated conversation elements
- can response immediately, answer concerns, and interact with users in a natural way
## Conversational language understanding
- can use CLU to build language models that interpret the meaning of phrases in a conversational setting
- CLU describes a set of features that can be used to build end-to-end conversational applications
# Azure Translator capabilities
- literal translations: translation where each word is translated to the corresponding target language
- issues with this approach include not having equivalent words in the target language and change of meaning in phrase without contextual consideration
- AI systems can understand the semantic context in which words are used
- this results in more accurate translations of input phrases
- **Azure Translator**: supports text-to-text translation between more than 130 languages
## Using Azure Translator
- Text translation: used for quick and accurate text translation
- Document translation: used to translate multiple documents across all supported languages
- Custom translation: used to enable enterprise, app developers, and language service providers to build customized neural machine translation (NMT) systems
- can be used in Microsoft Foundry
# Get start in Microsoft Foundry
- Azure language and translator provide building blocks for incorporating language capabilities into applications
- appropriate resources must be provided to use Azure Language or Azure Translator
	- Language resource
	- Translator resource
	- Foundry Tools resource
## Get started in Microsoft Foundry portal
- MS Foundry provides a unified platform for enterprise AI operations, model builders, and app development
- provides a UI based around hubs and projects
- you can create a project in MS Foundry, which will create a Foundry Tools resource for you
- Projects act as containers for datasets, models, and other resources