# Gathering Data
## Identifying Data
- determine the information you want to collect
- make decisions regarding
	- the specific information needed
	- possible sources
- determine the data collection method
- define how the data will be collected
- methods depend on the type of data, timeframe, and volume
- once data collection methods are finalised, implement data collection strategy and start collecting data
- make updates to your plan as you go along
- data needs to be free of errors, accurate, complete, relevant, and accessible
- define the quality traits, metric, and checkpoints in order to ensure the analysis will be based on quality
- watch out for issues pertaining to data governance (security, regulation, compliance)
- penalties for non-compliance ran run into millions of dollars
- data privacy: data collected needs to check the boxes for confidentiality, license use, and compliance to mandated regulations
## Data Sources
- can be internal or external
- primary: information obtained directly from the source
- secondary: information retrieved from existing sources
- third: obtained from aggregators who collect data from various sources
- Data exchange is a source of 3rd party data involving the voluntary sharing of data between providers and consumers
- surveys gather information through questionnaires distributed to groups of people
- Census data is used for gathering household data
- Interviews for gathering qualitative data
## How to Gather and Import Data
- [[SQL]] offers simple commands to specify what data is retrieved from the database
- Non-relational databases can be queried with SQL or SQL-like query tools
- some come with their own querying tools
	- CQL for Cassandra
	- GraphQL for Neo4J
- [[APIs ]]
	- a popular tool for extracting data from sources
	- invoked from applications requiring data access and end-point containing data
	- End-points can include databases, web services, and data marketplaces
- [[Web scraping]]
	- used for downloading specific data from web pages
	- used to extract text, contact info, images, videos, podcasts, and product items from web properties
- [[Data streams]]
	- popular source for aggregating constant streams of data flows
	- used for extracting data from social media sites and interactive platforms
- [[Data Exchange platforms]]
	- allow the exchange of data between providers and consumers
	- have a set of well-defined exchange standards, protocols, and formats
	- ensure the security and governance of data are maintained
- Data repositories are optimised for certain types of data
	- Relational databases store structured data with well defined schema
	- NoSQL can store structured, semi-structured, and unstructured data (email data, XML, zipped files)
- JSON is the preferred data type for web service

## Summary and Highlights
- The process of identifying data begins by determining the information that needs to be collected, which is determined by the goal you seek to achieve
- Your next step is to identify the source from which you will extract the required data and define a plan for collection. Decisions regarding the timeframe over which you need your data set, and how much data would suffice for arriving at a credible analysis also weigh at this stage.
- Data sources can be internal or external to the organisation, and they can be primary, secondary, or third-party, depending on how your obtaining the data relative to its original source.
- Some of the data sources you could be gathering data include databases, web, social media, interactive platforms, sensor devices, data exchanges, surveys and observation studies.
- Data identified and gather is combined using tools and methods to provide a single interface using which data can be queried and manipulated.
- The data identified, its source, and the practices employed for gathering have implications for quality, security, and privacy, which need to be considered.
# Wrangling Data
## Data Wrangling
- known as data munging
- iterative process involving data exploration, transformation, validation, and availability for meaningful analysis
- includes a range of task involving preparing raw data, where data has been collated through various data sources in a repository
- typically a 4-step process
	- Discovery/Exploration: understanding your data better with respect to your use-case
	- Transformation: involves tasks to transform data, like structuring, normalising, denormalising, cleaning, and enriching
		- Structuring: actions that change the form and schema of data
		- Normalising: focuses on cleaning the database of unused data and reduce redundancy and inconsistency
		- Denormalising: used to combine data from multiple tables into a single table
		- Cleaning: actions that fix irregularities to produce a credible and accurate analysis
		- Enriching: look at additional data points that could make the analysis more meaningful
	- Validation: check the quality of the data, verify consistency, quality, and security
	- Publishing: delivering the output of the data for downstream project needs

## Tools for Data Wrangling
- Spreadsheets
	- have a host of features and formulae to help identify issues, clean, and transform data
	- Add-ins allow you to import data from several types of sources and clean and transform the data
- OpenRefine
	- open-source tool to import and export data with wide variety of formats
	- can clean and transform data from one format to another
	- easy to learn and use
- Google DataPrep
	- intelligent cloud data service to visually explore, clean, and prepare data for analysis
	- fully managed service, so you don't need to install or manage the software
	- can automatically detect schemas, data types, and anomalies
- Watson Studio Refinery
	- allows you to discover, cleans, and transform data with built-in operations
	- transforms large amounts of raw data into consumable, quality information ready for analytics
	- offers the flexibility of exploring data residing in a spectrum of data sources
	- detects data types and classifications automatically
- Trifacta Wrangler
	- interactive cloud-based service for cleaning and transforming data
	- takes real-world data and cleans it into data tables to be exported to Excel, Tableau, and R
	- known for collaboration features
- [[Python]]
	- has a huge library and set of packages that offer powerful data manipulation
	- [[Jupyter Notebook]]
		- open-source web app widely used for data cleaning and transformation
		- widely used for data cleaning and transformation, statistical modelling, and data visualisation
	- Numpy
		- most basic package offered by [[Python]]
		- fast, versatile, interoperable, and easy to use
		- provides support for large, multi-dimensional arrays and matrices, and high-level mathematical functions
	- Pandas
		- designed for fast and easy data analysis operations
		- allows complex operations such as merging, joining, and transforming chunks of data
- [[R]]
	- offers a series of libraries and packages explicitly created for wrangling messy data
	- you can investigate, manipulate, and analyse data
	- Dplyr
		- powerful library for data wragling
		- has a precise and straightforward syntax
	- Data.table
		- helps aggregate large data sets quickly
	- Jsonlite
		- robust JSON parsing tool
## Data Cleaning
- poor quality data weakens and undermines business objectives
- poor data can lead to false conclusions and ineffective decisions
- data can be corrected manually or automatically with the help of data wrangling tools and scripts
- if it cannot be repaired, it must be removed from the dataset
- data cleaning is a subset of the entire data wrangling process
- typical workflow:
	- Inspection: detect the types of issues and error in the dataset
	- Cleaning
		- techniques applied depend on use case
		- missing values can be filtered out, sourced, or statistically calculated
		- irrelevant data
		- data type conversion
		- syntax errors should be corrected
		- outliers (may or may not be incorrect)
	- Verification:
		- inspect the results to establish effectiveness and accuracy achieved
		- re-inspect the data to make sure the rules and constraints still hold after the corrections

## Summary and Highlights

Once the data identified is gathered and imported, the next step is to make it analysis-ready. This involves the process of Data Wrangling. It is an iterative process involving data exploration, transformation, and validation.

Transformation of raw data includes the tasks you undertake to:
- Structurally manipulate and combine the data using Joins and Unions
- Normalise data, clean the database of unused and redundant data
- Denomalise data, combine data from multiple tables into a single table for fast queries
- Clean data, involving profiling data to uncover quality issues, visualise data to spot outliers, and fixing issues such as missing values, duplicate data, irrelevant data, inconsistent formats, syntax errors, and outliers
- Enrich data, considering additional data points that could add value to the existing data set and lead to a more meaningful analysis.

A variety of tools are available for Data Wrangling. Some include Excel Power Query, Spreadsheets, OpenRefine, Google DataPrep, Watson Studio Refinery, Trifacta Wrangler, Python, and R.