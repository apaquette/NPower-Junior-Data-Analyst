# Introduction
- Speech capabilities enable us to mange systems with voice instructions
- **Speech recognition**: ability to detect and interpret spoken input
- **Speech synthesis**: ability to generate spoken output
- **Azure Speech**: provides speech to text, text to speech, and speech translation capabilities
# Understand speech recognition and synthesis
- **Speech Recognition**: Takes spoken words and converts it into data that can be processed
- spoken words can be in the form of a recorded voice or audio file
- speech patterns are analyzed to determine patterns that are mapped to words
- **acoustic**: model that converts audio signal into phonemes
- **language**: model that maps phonemes to words
- recognized words are typically converted to text
	- providing closed captions for recorded of live videos
	- creating transcripts
	- automated note dictation
	- determining intended user input
- **Speech synthesis**: vocalizing data, usually by converting text to speech requiring
	- text to be spoken
	- voice to be used to vocalize speech
- the system typically tokenizes the text to break it into individual words, assigning phonetic sounds to each word
- phonetic transcription is broken into prosodic units (phrases, clauses, sentences)
- can use output of speech synthesis for many purposes
	- Generating spoken responses
	- Creating voice menus for phone systems
	- Reading email or text messages aloud
	- Broadcasting announcements in public locations
# Get started with speech on Azure
- MS Azure offers speech recognition and synthesis capabilities through Azure Speech providing
	- Speech to text
	- Text to speech
	- Speech translation
## Speech to text
- Azure speech to text API performs real-time or batch transcription of audio into text
- audio source can be real-time stream or audio file
- based on Microsoft's Universal Language Model
- data is Microsoft-owned and deployed to azure
- optimized for two scenarios: conversational and dictation
- can create and train your own custom models: acoustics, language, pronunciation
- **Real-time transcription**: allows to transcribe audio streams into text
- **Batch transcription**: audio recordings stored on a file runs asynchronous transcription
## Text to Speech
- enables the conversion of text input into audible speech
- **Speech synthesis voices**: can specify the voice to vocalize the text
- offers the flexibility to personalize speech synthesis solutions and give it specific character
- service includes multiple predefined voices with support for multiple languages and regional pronunciations
- can develop custom voices and use them with the text to speech API
## Speech translation
- enables real-time translation of spoken language by taking inputs of audio streams and returning text in a specified language
- works by converting speech to text using automatic speech recognition
- then translating the recognized text into one or more target languages
- service supports a wide range of source and target languages
- can deliver translations a text or synthesized speech
- developers can integrate this functionality into applications with REST APIs or SDKs
# Use Azure Speech
- available through several tools and programming languages
	- Studio interfaces
	- Command Line Interface (CLI)
	- REST APIs and Software Development Kits (SDKs)
## Using Studio Interfaces
- can create Azure speech projects using MS Foundry portal's Speech Playground
## Azure resources for Azure Speech
- to use Azure Speech, you must create an appropriate resource in your Azure subscription
- can choose either of the following types:
	- **Speech resource**: use if you plan to use Azure Speech only, or want to manage access and billing separately from other services
	- **Foundry Tools resource**: use if you plan to use Azure Speech in combination with other tools
