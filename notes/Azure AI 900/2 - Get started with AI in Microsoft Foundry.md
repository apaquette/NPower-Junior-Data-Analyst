# Introduction
- learn how Microsoft enables you to build AI with the latest technologies
- builds on the basic ideas behind AI
- describes how Microsoft Foundry streamlines AI application development

# What is an AI application
- **Artificial Intelligence**: systems designed to perform tasks typically requiring human intelligence
- AI workloads
	- Generative AI
	- Agents and automation
	- Speech
	- Text analysis
	- Computer vision
	- Information Extraction
![[Pasted image 20251216133030.png]]
- broad goal of AI is to create systems that mimic human intelligence
- **Machine Learning**: enables machines to learn patterns from data
	- Supervised and Unsupervised Learning
		- regression (supervised)
		- classification (supervised)
		- clustering (unsupervised)
	- Deep Learning
		- uses neural networks with multiple layers for tasks
		- image recognition and speech synthesis
		- foundation through neural networks that learn complex patterns
	- Generative AI
		- uses deep learning to create new content (text, images, audio, code)

## AI Applications
- software solution that uses AI techniques to perform tasks
- **Model-powered**: use trained models to process inputs and generate outputs
- **Dynamic**: can improve over time through retraining or fine-tuning
- **Conversational Interfaces**: users interact via chatbots or voice assistants
- **Embedded Features**: provide insights or predictions to help users make informed choices
- **Automation**: handle repetitive tasks

### Industry Examples
- Healthcare
- Finance
- Retail
- Manufacturing
- Education

# Components of an AI application
## Data Layer
- foundation of any AI application
- includes collection, storage, and management of data used for training, inference, and decision-making
- common sources: Azure SQL, PostgreSQL, unstructured data, real-time streams
## Model Layer
- involves the selection, training, and deployment of machine learning models
- can be pre-trained or custom-built
- includes tools for fine-tuning, evaluating, and versioning models
- **Microsoft Foundry**: unified Azure platform-as-a-service for enterprise AI operations
## Compute Layer
- computer resources to train and run models
- Azure app service for hosing web apps and APIs
- Azure Functions for serverless, event-driven execution of AI tasks
- Containers for scalable and portable deployment of AI models and services
## Integration & Orchestration Layer
- connects models and data with business logic and UIs
- Foundry roles:
	- agent service for building agents that can reason and act
	- AI Tools like speech, vision, and language APIs
	- Software Development Kits (SDKs) and APIs for integrating AI capabilities into apps
	- Portal tools for managing models, agents, and workflows

# Microsoft Foundry for AI
- a unified, enterprise-grade platform for building, deploying, and managing AI applications
- consolidates models, agent orchestration, monitoring, and governance tools in one platform
- developers can seamlessly design generative AI applications
![[Pasted image 20251216140258.png]]
![[Pasted image 20251216140302.png]]
- **Foundry Models**: Access to foundation and partner models
- **Agent Service**: Build and orchestrate multi-step AI workflows
- **Foundry Tools**: Prebuilt Azure services
- **Governance & Observability**:  centralized identify, policy, and monitoring for AI workloads

## Foundry Models
- supports thousands of models from first and third-party providers
- Azure OpenAI (gpt-4, gpt-5, Meta Llama, and others)
- Can deploy and manage models directly from Foundry's model catalogue
- Offers the ability to test, customize, deploy, and manage models

## Agent Service
- for building production-ready AI agents that autonomously make decisions
- abstracts orchestration, thread management, tool invocation, and embeds governance including content safety and observability
- can create low-code or code-first multi-agent systems

## Foundry Tools
- speech, vision, language, document intelligence, content safety
- provide AI capabilities that can be built into web or mobile applications

## Governance and Observability
- **Governance**: ensures responsible AI development through compliance, identity management, and risk mitigation
- **Observability**: delivers end-to-end visibility for performance, safety, and operational efficiency

# Get started with Foundry
- once creating a Foundry project, you can access
	- model catalogue
	- playgrounds for testing models
	- tools for deploying models, running evaluations, and creating agents
	- a management centre for user roles, quotas, and resource connections

## Characteristics
- Prebuilt and ready to use or customize
- Accessed through APIs
- Available on Azure

### Prebuilt and ready to use
- Foundry makes AI accessible to businesses of all sizes
- uses pretrained machine learning models to deliver AI as a service
- uses high-performance Azure computing to deploy advanced AI models

### Accessed through APIs
- can be built into applications with APIs
- secure communication with APIs is possible through authentication

# Understand Azure
- cloud computing platform
- provides a wide range of services
- helps build, deploy, and manage applications
- supports various programming languages, frameworks, and operating systems

## Cloud capabilities
- delivers core cloud capabilities across four main areas
	- Compute: virtual machines, containers, serverless functions
	- Storage: options for saving data (Blob Storage, Azure files)
	- Networking: connect resources securely and reliability (Azure Virtual Network, Load Balancer)
	- Application services: help developers build and host web apps, APIs, and mobile backends
## Understand how Azure organizes your resources
- through a hierarchy of entities
- tenant: represents a dedicated instance of Azure Active Directory
	- subscriptions: define billing boundaries
		- resource group: logical containers for managing related resources
			- resource: individual services or components
- this structure helps ensure clarity, security, and scalability
- tenants and subscriptions allow for clear separations of concerns
### Foundry runs on Azure
- Foundry uses Azure resource types
- an AI development layer within Azure
- designed to accelerate building and managing generative AI apps
- Foundry tools and models are managed the same as other Azure services

