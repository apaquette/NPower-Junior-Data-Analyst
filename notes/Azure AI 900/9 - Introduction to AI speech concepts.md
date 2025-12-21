# Introduction
- speech is the most natural way humans communicate
- bringing speech capabilities to AI creates intuitive, accessible, and engaging user experiences
# Speech-enabled solutions
- speech capabilities transform how users interact with AI agents
- speech recognition converts spoken words into text
- speech synthesis generates natural-sounding audio from text
- integrating speech into AI:
	- Expand accessibility: Serve users with visual impairments
	- Increase productivity: Enable multitasking by removing the need for keyboards and screens 
	- Enhance user experience: Create natural conversations that feel more human
	- Reach global audiences: Support multiple languages and dialects
## Common speech recognition scenarios
- speech recognition (speech-to-text): listens to audio input and transcribes into text
### Customer service and support
- Transcribe customer calls in real time for agent reference
- Route callers to the right department
- Analyze call sentiment and identify common customer issues
- Generate searchable call records for compliance and training
**Business value**: reduces manual note-taking, improves response accuracy, captures insights that improve service quality
### Voice-activated assistants and agents
- Accept voice commands for hands-free control of devices and applications
- Answer questions using natural language
- Complete tasks like setting reminders, sending messages, or searching information
- Control smart home devices, automotive systems, and wearable technology
**Business value**: Increases user engagement, simplifies complex workflows, enables operation in situations where screens aren't practical
### Meeting and interview transcription
- Create searchable meeting notes and action item lists
- Provide real-time captions for participants who are deaf or hard of hearing
- Generate summaries of interviews, focus groups, and research sessions
- Extract key discussion points for documentation and follow-up
**Business value**: Saves hours of manual transcription work, ensures accurate records, makes spoken content accessible to everyone
### Healthcare documentation
- Dictate patient notes directly into health records
- Update treatment plans without interrupting patient care
- Reduce administrative burden and prevent physical burnout
- Improve documentation accuracy by capturing details in the moment
**Business value**: Increases time available for patient care, improves record completeness, reduces documentation errors
## Common speech synthesis scenarios
- speech synthesis (text-to-speech): converts written text into audio
### Conversational AI chatbots
- Respond to users with natural-sounding voices
- Create personalized interactions by adjusting tone, pace, and speaking style
- Handle customer inquiries through voice channels like phone systems
- Provide consistent brand experiences across voice and text interfaces
**Business value**: Makes AI agents more approachable, reduces customer effort, extends service availability to voice-only channels
### Accessibility and content consumption
- Announce important alerts, reminders, and status updates
- Provide navigation instructions in mapping and GPS applications
- Deliver time-sensitive information without needing users to look at screens
- Communicate system status in industrial and operation environments
**Business value**: Ensures critical information reaches users even when visual attention isn't available, improving safety and responsiveness
### E-learning and training
- Create narrated lessons and course content
- Provide pronunciation examples for language learning
- Generate audio version of written materials for different learning preferences
- Scale content production across multiple languages
**Business value**: Lowers production costs, enables rapid prototyping, creates customized experiences
### Entertainment and media
- Generate character voices for games and interactive experiences
- Produce podcast drafts and audiobook prototypes
- Create voice-overs for videos and presentations
- Personalize audio content based on user preference
**Business value**: Lowers production costs, enables rapid prototyping, create customized experiences at scale
## Combining speech recognition and synthesis
- Voice-driven customer service: Agents listen to customer questions, process requests, and respond with helpful answers
- Interactive voice response (IVR): Callers speak their needs, and the system guides them through options with natural dialogue
- Language learning applications: Students speak practice phrases and the system provides feedback and corrections
- Voice-controlled vehicles: Drivers give commands hands-free and the system confirms actions and provides updates
## Key considerations before implementing speech
- Audio quality requirements
- Language and dialect support
- Privacy and compliance
- Latency expectations
- Accessibility standards
# Speech recognition
- also called speech-to-text, enables applications to convert spoken language into written text
- involves six coordinates stages
	- capturing audio
	- preparing features
	- modelling acoustic patterns
	- applying language rules
	- decoding the most likely words
	- refining the final output
## Audio capture
- begins when a mic converts sound waves into a digital signal
- system samples the analog audio thousands of times per seconds
- the system often applies basic filtering to remove background noise
## Pre-processing
- raw audio contains too much information for pattern recognition
- transforms the waveform into a compact representation that highlights speech characteristics discarding irrelevant details
### Mel-Frequency Cepstral Coefficients (MFCCs)
- the most common feature extraction technique in speech recognition
- mimics how human ears perceive sound by emphasizing frequencies
#### How it works
1. Divide audio into frames
2. Apply Fourier transform
3. Map to Mel scale
4. Extract coefficients
The result is a sequence of feature vectors that captures what the audio sounds like without storing every sample

## Acoustic modelling
- learns the relationship between audio features and phonemes
### From features to phonemes
- modern models use transformer architectures, a type of deep learning network that excels at sequence tasks
- transformer processes the MFCC feature vectors and predicts which phoneme is most likely at each moment in time
- achieves effective phoneme prediction through:
	- Attention mechanism: model examines surrounding frames to resolve ambiguity
	- Parallel processing: analyze multiple frames simultaneously improving speed and accuracy
	- Contextualized predictions: learns that certain phoneme sequences occur frequently in natural speech
- The output is a probability distribution over phonemes for each audio frame

## Language modelling
- phoneme predictions alone don't guarantee accurate transcriptions
- some words share identical phonemes
- models resole ambiguity by applying knowledge of vocabulary, grammar, and common word patterns
- word sequence prediction:
	- **Statistical patterns**: The model knows 'the weather is nice' appears more often than 'The whether is nice'
	- **Context awareness**: After hearing "I need to" to model expects verbs like "go" or "finish", and not nouns
	- **Domain adaptation**: Custom language models trained on medical or legal terminology improve accuracy for specialized scenarios
## Decoding
- search through millions of possible word sequences to find transcription that best matches both acoustic and language model predictions
- balances two competing goals:
	- staying faithful to the audio signal
	- producing readable, grammatically correct text
### Beam search decoding
- most common technique maintains a shortlist of top-scoring partial transcriptions
- at every step, it extends each hypothesis with the next most likely word, prunes low-scoring paths, and keeps only the best candidates

## Post-processing
- decoder produces raw text that often requires cleanup before presentation
- applied formatting rules and corrections to improve readability and accuracy
### Common post-processing tasks
- Capitalization
- Punctuation restoration
- Number formatting
- Profanity filtering
- Inverse text normalization
- Confidence scoring
## How the pipeline works together
1. Audio capture
2. Pre-processing
3. Language modelling
4. Decoding
5. Post-processing
# Speech synthesis
- text-to-speech converts written text into spoken audio
- encountered when
	- virtual assistants read notifications
	- navigation apps announce directions
	- accessibility tools help users consume written content
- process text through four distinct stages
## Text normalization
- prepare raw text for pronunciation by expanding abbreviations, number, and symbols into spoken forms
- common normalization tasks
	- Expanding abbreviations
	- Converting numbers to words
	- Handling dates and times
	- Processing symbols and special characters
	- Resolving homographs based on context
## Linguistic analysis
1. Segments text into words and syllables
2. Looks up word pronunciations in lexicons
3. Applies G2P rules or neural models to handle unknown words
4. Marks syllable boundaries and identifies stressed syllables
5. determines phonetic context for adjacent sounds
## Grapheme-to-phoneme conversion
- G2P conversion maps written letters to pronunciation sounds
- Modern G2P systems user neural netowrks trained on pronunciation dictionaies
- the models learn patterns between spelling and sound
- handle
	- uncommon words
	- proper names
	- regional variations
- linguistic analysis often uses transformer model to help consider context
## Prosody generations
- refers to the rhythm, stress, and intonation patterns that make speech sound natural
- determines how to say words, not just which sounds to produce
### Elements of prosody
- Pitch contours: raising or falling pitch signalling questions vs statements
- Duration: how long to hold each sound, creating emphasis or rhythm
- Intensity: volume variations that highlight important words
- Pauses: breaks between phrases or sentences that aid comprehension
- Stress patterns: which syllables receive emphasis within words or sentences
### Transformer-based prosody prediction
- modern speech synthesis use transformer neural networks to predict prosody
- excel at understanding context across entire sentences, not just adjacent words
#### The prosody generation process
1. Input encoding
2. Contextual analysis
3. Prosody prediction
4. Style factors
Transformers predict prosody by learning from thousands of hours of recorded speech paired with transcripts. The model discovers patterns: questions rise in pitch at the end, commas signal brief pauses emphasized words lengthen slightly, and sentence-final words often drop in pitch.
#### Factors influencing prosody choices
- syntax
- semantic
- discourse context
- speaker identity
- emotional tone
## Speech synthesis
- generates the final audio waveform based on the phoneme sequence and prosody specifications
### Waveform generation approach
- neural vocoders: deep learning models that generate audio samples directly
	- WaveNet, WaveGlow, HiFi-GAN
#### The synthesis process
1. Acoustic feature generation
2. Vocoding
3. Post-processing
The vocoder essentially performs the inverse of what automatic speech recognition does. While speech recognition converts audio into text, the vocoder converts linguistic representations into audio.
## The complete pipeline in action
1. Text normalization
2. Linguistic analysis
3. Prosody generation
4. Speech synthesis
# Summary
- Speech scenarios and applications
- Speech recognition fundamentals
- Speech synthesis fundamentals