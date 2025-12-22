# Introduction
AI information extraction are used to extract structured data fields from unstructured media (documents, images, videos, and audio).

Common examples of extraction scenarios:
- Financial document processing
	- Invoice processing
	- Receipt processing
	- Financial statements
- Legal and compliance documents
	- Contract processing
	- Regulatory forms
- Healthcare documentation
	- Medical records
- Supply chain and logistics
	- Shipping documents
	- Purchase Orders
# Overview of information extraction
- a workload that combines multiple AI techniques to extract data
![[Pasted image 20251222142440.png]]
1. Text detection and extraction from images using OCR
2. Value identification and mapping from the OCR results to data fields
## Choosing the right approach
It's important to consider the requirements and constraints the system must address.

Some key considerations:
- Document characteristics
	- Layout consistency
	- Volume requirements
	- Accuracy requirements
- Technical infrastructure requirements
	- Security and privacy
	- Processing power
	- Latency requirements
	- Scalability needs
	- Integration complexity
# Optical character recognition (OCR)
- automatically converts visual text in images into text data
- OCR enabled automated data extraction from
	- scanned invoices and receipts
	- digital photographs of documents
	- PDF files containing images of text
	- Screenshots and captured content
	- Forms and handwritten notes
## The OCR pipeline
![[Pasted image 20251222142741.png]]
1. Image acquisition and input
2. Preprocessing and image enhancement
3. Text region detection
4. Character recognition and classification
5. Output generation
### Stage 1: Image acquisition and input
The pipeline begins when an image containing text enters the system
- a photograph
- a scanned document
- a frame extracted from a video
- a PDF page rendered as an image
### Stage 2: Preprocessing and image enhancement
Before detection begins, the following techniques are used to optimize the image:
- Noise reduction
- Contrast adjustment
- Skew correction
- Resolution optimization
### Stage 3: Text region detection
The system analyzes the preprocessed image to identify areas containing text
- Layout analysis
- Text block identification
- Reading order determination
- Region classification
### Stage 4: Character recognition and classification
The core of the OCR process where individual characters are identified:
- Feature extraction
- Pattern matching
- Context analysis
- Confidence scoring
### Stage 5: Output generation and post-processing
Final stage converts recognition results into usable text
- Text compilation
- Format preservation
- Coordinate mapping
- Quality validation
# Field extraction and mapping
- the process of taking text output from OCR and mapping individual text to specific labelled data fields
- OCR tells you what exists in a document, field extract tells you what the text means

## The field extraction pipeline
![[Pasted image 20251222143517.png]]
1. OCR output ingestion
2. Field detection and candidate identification
3. Field mapping and association
4. Data normalization and standardization
5. Integration with business processes and systems

### Stage 1: OCR output ingestion
- Raw text content: actual characters and words
- Positional metadata: bounding box coordinates, page location, reading order
- Confidence scores: engine confidence levels for elements
- Layout information: document structure, line breaks, paragraph boundaries
### Stage 2: Field detection candidate identification
This stage identifies potential field value in the OCR output.
#### Template-based detection
Can be accomplished using the following techniques
- predefined document layouts with known field positions and anchor keywords
- search for label-value pairs
- regular expressions and string matching
**Advantages**: high accuracy for known document types, fast processing, and explainable results
**Limitations**: requirement for manual template creation, complexity caused by layout validation or field naming inconsistencies
#### Machine learning-based detection
Can use a corpus of example documents to train a model that extracts fields based on learned relationships. Training approaches include
- Supervised learning
- Self-supervised learning
- Multi-modal learning
- Advanced model architecture
	- Graph Neural Network (GNN)
	- Attention mechanisms
	- Sequence-to-sequence models
#### Generative AI for schema-based extraction
- Prompt-based extraction: provide the LLM with document text and schema definition
- Few-shot learning: train models with minimal examples
- Chain-of-thought reasoning: guides models through step-by-step field identification logic
### Stage 3: Field mapping and association
#### Key-value paring techniques
Common techniques used:
- Proximity analysis
	- spatial clustering
	- reading order analysis
	- geometric relationships
- Linguistic pattern recognition
	- Named entity recognition (NER)
	- Part-of-speech tagging
	- Dependency parsing
#### Table and structured content processing
Some documents include more complex structures of text, such as tables. The presence of a table can be determining the following techniques:
- Specialized convoluted neural network (CNN) architectures
- Object detection approaches adapted for table cell id
- Graph-based parsing approaches that model table structure as graph relationships
Field extraction solution might employ one or more of the following
- Row-column association
- Header detection
- Hierarchical processing
#### Confidence scoring and validation
Field extraction accuracy depends on many factors. Various techniques are employed to evaluate the accuracy of the predicted field values:
- OCR confidence
- Pattern matching confidence
- Context validation
- Cross-field validation
### Step 4: Data normalization and standardization
Raw extracted values are transformed into consistent formats
#### Format standardization
- Date normalization
	- Format detection
	- Parsing algorithms
	- Ambiguity resolution
- Currency and numeric processing
	- Symbol recognition
	- Decimal normalization
	- Unit conversion
- Text standardization
	- Case normalization
	- Encoding standardization
	- Abbreviation expansion
#### Data Validation and Quality Assurance
The standardization process enables further validation of the values that have been extracted:
- Rule-based validation
	- Format checking
	- Range validation
	- Requiring field checking
- Statistical validation
	- Outlier detection
	- Distribution analysis
	- Cross-document validation
### Stage 5: Integration with business processes and systems
The final stage involves integrating the extracted field values into a business process system
#### Schema mapping
The extracted fields need to be further transformed or reformatted to align with application schemas used for data ingestion.
- Database schema
- API payloads
- Message queues
The schema-mapping processing might involve transformations
- Field renaming
- Data type conversion
- Conditional logic
#### Query metrics and reporting
The evaluation and report of the quality of the extracted data.
- Field-level confidence scores
- Document-level quality assessment
- Error categorization
