# Introduction
- generative AI focuses on creating new content
- use cases:
	- Marketing Content Creation
	- Customer Support
	- Code Generation
	- Image and Video Generation
	- Personalized Learning and Tutoring
# Understanding generative AI applications
- built with language models
- they power the app logic component of the interaction between users and gen AI
![[Pasted image 20251218211501.png]]

## Understand assistants
- often appears as integrated chat-based assistants

## Understand agents
- **Agents**: applications that can respond to user input or assert situation autonomously and take actions
- three main components:
	- A language model that powers reason and language understanding
	- Instructions that define the agent's goal, behaviour, and contraints
	- Tools, or functions, that enable the agent to complete tasks

## Use a framework for understanding generative AI applications
| Category                                   | Description                                                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Ready-to-use                               | They do not require any programming work on the user's end to utilize. Can start simply by asking a question.                                                |
| Extendable                                 | Some ready-to-use applications can be extended using your own data. These customizations enable the assistant to better support specific processes or tasks. |
| Applications you build from the foundation | You can build your own assistants and assistants with agentic capabilities starting from a language model.                                                   |
Often services are built to extend or build generative AI applications. These services provide the infrastructure, tools, and frameworks necessary to develop, train, and deploy generative AI models.

# Understanding generative AI development in Foundry
- a powerful ecosystem of tools and services designed to support developers, data scientists, and enterprise for every stage of the AI lifecycle
- can develop gen AI solutions
- **Microsoft Foundry**: united platform for enterprise AI operations, model builders, and application development
- gives developers control over the customization of language models used for building applications
- models can be deployed in the cloud and consumed from custom-developed apps and services

| Component                       | Description                                                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| Microsoft Foundry model catalog | Centralized hub for discovering, comparing, and deploying models for gen AI development. |
| Playgrounds                     | Ready-to-use environments for quick testing and exploring models.                        |
| Foundry Tools                   | Build, test, see demos, and deploy Foundry Tools.                                        |
| Solutions                       | Can build agents and customize models in MS Foundry                                      |
| Observability                   | Ability to monitor usage and performance of your application's models.                   |

# Understand Foundry's model catalogue
- provides a comprehensive and dynamic marketplace containing models sold by Microsoft and partners
- Azure OpenAI models make up first-party model family
	- considered foundation models
- can deploy the models from MS Foundry model catalogue to an endpoint without extra training
- can choose to customize the foundation model for task specialization or domain-specific knowledge

# Understand Foundry capabilities
- provides a UI based around hubs and projects
- **hub**: provides comprehensive access to Azure AI and Azure Machine Learning
- **projects**: can be created inside hubs; provide more specific access to models and agent development
- several tools are created in tandem with the creation of a hub
- multiple foundry tools can be tested
	- Azure Speech
	- Azure Language
	- Azure Vision
	- MS Foundry Content Safety
- MS Foundry provides a playground to test tools and models

## Customizing models
| Method                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Using grounding data                              | Refers to the process of ensuring a system's outputs are aligned with factual, contextual, or reliable data sources. Can be done in various ways, including linking the model to a database, using search engines to retrieve  real-time information, or incorporating domain-specific knowledge bases. The goal is to anchor responses from these data sources, enhancing trustworthiness of general content. |
| Implementing Retrieval-Augmented Generation (RAG) | Connects the model to an organization's proprietary database. Involves retrieving relevant information from a curated dataset and using it for response generation. It enhances the model's performance by providing up-to-date and domain-specific information. Useful for applications where real-time access to dynamic data is cruicial.                                                                   |
| Fine-turning                                      | Involves taking a pretrained model and further training it on a smaller, task-specific dataset to make it more suitable. Allows the model to specialize and perform better at specific tasks that require domain-specific knowledge. Useful for adapting models to domain-specific requirements.                                                                                                               |
| Managing security and governance controls         | Needed to manage access, authentication, and data usage. Help prevent the publication of incorrect or unauthorized information.                                                                                                                                                                                                                                                                                |

# Understand observability
- three dimensions for evaluating and monitoring gen AI
	- **Performance and quality**: assess accuracy, groundedness, and relevance of generated content
	- **Risk and safety**: assess risks associated with AI content to safeguard, including predisposition towards harmful or inappropriate content.
	- **Custom**: industry-specific metrics to meet specific needs and goals
- MS Foundry supports observability features that improve performance and trustworthiness
- **Evaluators**: specialized tools that measure quality, safety, and reliability of responses
	- Groundedness: measures the consistency of the response in respect to the context
	- Relevance: measures how relevant the response is in respect to the query
	- Fluency: measures the natural language quality and readability
	- Coherence: measures logical consistency and flow of responses
	- Content safety: comprehensive assessment of various safety concerns
