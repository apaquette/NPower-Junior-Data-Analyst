# Introduction
- text analysis is a subset of natural language processing (NLP)
- it enables machines to extract meaning, structure, and insights from unstructured text
- common use cases
	- Key term extraction: identifying important words and phrases
	- Entity detection: identifying named entities
	- Text classification: categorizing text documents based on content
	- Sentiment analysis: predicts the sentiment of the text
	- Text summarization: reducing the volume of text while retaining salient points

# Tokenization
- first step in analyzing text is to break it down into tokens
- each distinct word in the text can be a token
- tokens can be generated for partial words or combinations of words and punctuation
- each token is assigned a discrete value

| Technique                     | Description                                                                                                                                                                                             |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Text normalization            | Might choose to normalize text by remove punctuation and changing all words to lower case. This approach improves overall performance for word frequency analysis. Some semantic meaning could be lost. |
| Stop word removal             | Stop words are words that should be excluded from analysis. They make the text easier to read but add little semantic meaning. Excluding these words might allow to better identify important words.    |
| N-gram extraction             | Considering frequently appearing sequences of words as a group can improve text analysis and make better sense of the text.                                                                             |
| Stemming                      | Technique used to consolidate words by stripping endings before counting them. Words with the same etymological root are interpreted as being the same token                                            |
| Lemmentization                | Similar to stepping, uses linguistic rules and vocabulary to ensure the resulting form is a valid word ("running" -> "run")                                                                             |
| Parts of speech (POS) tagging | Labelling each token with its grammatical category. Uses linguistic rules to determine the correct tag based on both the token and its context in the sentence.                                         |
# Statistical text analysis
## Frequency Analysis
- count the number of times each normalized token appears
- terms that are used more frequently can help identify subjects or themes

## Term Frequency - Inverse Document Frequency (TF-IDF)
- a technique that calculates scores based on how often a word or term appears in one document compared to its general frequency across a collection of documents
- high degree of relevance is assumed for words that appear frequently in a particular document, but less in others
- To calculate TF-IDF:
	1. **Calculate Term Frequency**: how many times a word appears in a document
	2. **Calculate Inverse Document Frequency**: `idf(t) = log(N / df(t))` where `N` is the total number of documents and `df(t)` is the number of documents that contain the word `t`
	3. **Combine them to calculate TF-IDF**: Multiply TF and IDF to get the score: `tfidf(t, d) = tf(t, d) * log(N/ df(t))`
- a high score indicates a word appears often in one document but rarely in others
- a low score indicates that word is common in many documents

## "Bag-of-words" machine learning techniques
- name given to a feature extraction technique that represents text tokens as vector of word frequencies or occurrences
- representation becomes the input for machine learning algorithms like Naive Bayes
- can implement sentiment analysis by using the same method to classify text by emotional tone

## TextRank
- unsupervised graph-based algorithm that models text as a network of connected nodes
- each sentence in a document could be considered a node, and the connections between them are scored based on their similarity
- commonly used to summarize text based on identifying a subset of sentences within a document
- algorithm applies the same principles as Google's PageRank algorithm
- key idea is a sentence is important if it's similar to many other importance sentences
- algorithm steps:
	1. **Build a graph**: Each sentence becomes a node, and edges that connect them are weighted by similarity
	2. **Calculate ranks iteratively**: each node's score is calculated based on the scores of the nodes connected to it.
	3. **Expand top-ranked sentences**: after convergence, the sentences with the highest scores are selected
# Semantic language models
- as NLP has advanced, the ability to train models encapsulating the semantic relation between tokens has led to powerful deep learning language models
- the vector-based approach to modelling text became a common technique
- during training, dimension values are assigned to reflect semantic characteristics
- mathematical relationships between vectors can be exploited to perform common text analysis more efficiently
- a recent advancement is to use a technique called attention
- it considered each token in context, and calculates the influence of the tokens around it
## Representing text as vectors
- vectors represent a point in multidimensional space, defined by coordinates along axes
- each vector describes a direction and distance from origin
- semantically similar tokens should have vectors with similar orientations
## Finding related terms
- words with similar semantic meanings have similar orientations
- can use calculations between vectors to make meaningful comparison (cosine similarity)
## Vector translation through addition and subtraction
- can add or subtract vectors to produce new vector-based results
- these results can be used to find tokens with matching vectors
- enables intuitive arithmetic-based logic to determine appropriate terms
## Using semantic models for text analysis
### Text summarization
- semantic embeddings enable extractive stigmatization
- identifies sentences with vectors most representative of the overall document
- encodes each sentence as a vector, and calculates which sentences are most central to the documents meaning
- central sentences can b e extract to form a summary capturing key themes
### Keyword extraction
- vector similarity can identify the most important terms in a document by comparing each word's embedding
- words whose vectors are most similar, or most central when considering all word vectors are likely to be key terms representing the main  topics
### Named entity recognition
- semantic models can be fine-tuned to recognize named entities
- learn vector representations that cluster similar entity types together
- during inference the model examines each token's embedding and context to determine if it represents a named entity and its type
### Text classification
- tasks like sentiment analysis or topic categorization, documents can be represented as aggregate vectors
- document vectors can be used as features for ML classifiers, or compared directly to class prototype vectors to assign categories