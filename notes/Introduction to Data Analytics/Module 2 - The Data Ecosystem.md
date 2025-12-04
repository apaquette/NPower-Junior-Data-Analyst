# The Data Ecosystem and Languages for Data Professionals
## Analyst Ecosystem
- infrastructure, software, tools, frameworks, and process to gather, clean, analyse, mine, and visualise data
- Structured and unstructured data
- Data repositories: databases, data warehouses, data marts, data lakes, and big data stores
- Languages
	- Query languages ([[SQL]])
	- Programming languages ([[Python]])
	- Shell and scripting languages (Bash)

## Types of Data
- Data is unorganised information
- Comprised of facts, observation, perceptions, numbers, characters, symbols, images
- Data can be
	- structured: well-defined schema
	- semi-structured: some organisational properties that aren't rigid (XML, JSON)
	- unstructured: does not have an easily identifiable structure

## Types of File Formats
- Delimited text file (CSV, TSV)
	- used to store data as text
- Open XML Spreadsheet
	- spreadsheet file format
- XML
- PDF
- JSON

## Sources of Data
- Relational databases
	- examples: SQL Server, Oracle, MySQL
	- stores data in a structured way
- Flat files
	- examples: CSV, TSV
	- store data in plain text format (one record per line)
	- values are separated by delimiters (commas, semi-colons, or tabs)
- Spreadsheet
	- contains multiple worksheets, and each worksheet maps to a different table
	- files can be stored in custom formats to include additional information
- XML datasets
	- support more complex data structures
- APIs and web services
	- listen for incoming requests and return data
- Web scraping
	- used to extract specific data from webpages
	- web scraping tools: BeautifulSoup, Scrapy, Pandas, Selenium
- Data streams
	- source for aggregating constant streams of data
	- data is generally timestamped and geo-tagged
- Feeds

## Languages for Data professionals
- Query Languages
	- designed for accessing and manipulating databases
	- [[SQL]]
- programming languages
	- designed for developing applications and controlling application behaviour
	- [[Python]], [[R]], Java
- Shell scripting
	- Ideal for repetitive and time-consuming operational tasks
	- Unix/Linux Shell, PowerShell
### SQL
- Structured Query Language
- designed for accessing and manipulating information from relational databases
- write instructions to perform operations
	- Insert, Update, Delete
- advantages
	- portable
	- can be used independently of platform
	- can be used for querying data in wide variety of databases
	- simple syntax
	- can retrieve large amounts of data quickly

### [[Python]]
- widely-used open-source general-purpose high-level language
- allows programmers to express concepts in fewer lines of code
- perceived as an easy language to learn
- ideal for beginning programmers
- supports multiple programming paradigms (object-oriented, imperative, functional, procedural)
- advantages
	- fewer lines of code to accomplish tasks
	- open source (free with community-based model)
	- runs on windows and linux environments
	- widespread community support
- libraries and functionalities
	- Pandas (data cleaning and analysis)
	- Numpy and Scipy (statistical analysis)
	- Beautifulsoup and Scrapy (web scraping)
	- Matplotlib and Seaborn (visualisation)
	- Opencv (image processing)

### [[R]]
- open-source programming language and environment for data analysis, visualisation, machine learning, and statistics
- used for developing statistical software
- known for creating compelling visualisation
- advantages
	- open-source platform-independent language
	- can be paired with other languages, including Python
	- highly extensible
	- facilitates the handling of structured and unstructured data
### [[Java]]
- object-oriented programming language
- among top-ranked programming languages used
- used in a number of processing including cleaning data, importing and exporting data, statistical analysis, data visualisation
- popular frameworks written with Java: Hadoop, Hive, Spark
- suited for speed-critical projects

### Unix/Linux Shell
- series of UNIX commands written in plain text to accomplish a task
- fast and easy to write
- useful for repetitive tasks
- typical operations
	- file manipulation
	- program execution
	- system administration
	- installation scripts

## Summary and Highlights

Data analyst ecosystem includes the infrastructure, software, tools, frameworks, and processes used to gather, clean, analyse, mine, and visualise data.

Data can be categorised as:
- Structured: well organised in formats that can be stored in databases
- Semi-structured: partially organised and partially free form
- Unstructured: cannot be organised conventionally into rows and columns

There are a variety of file formats, including delimited text files, spreadsheets, XML, PDF, and JSON.

Data is extracted from multiple data sources, ranging from relational and non-relational databases to APIs, web services, data streams, social platforms, and sensor devices.

Once the data is identified and gathered, it needs to be staged in a data repository so that it can be prepared for analysis. The type, format, and source of data influence the type of data repository that can be used.

Data professionals need a host of languages that can help them extract, prepare, and analyse data.
- Querying languages: SQL
- Programming languages: Python, R, Java
- Shell and scripting languages: Unix/Linux Shell, PowerShell

# Understanding Data Repositories and Big Data Platforms
## Data Repositories
- Types of repositories: database, data warehouse, big data stores
- Database: collection of data designed for input, storage, search and retrieval of data
- Database management system: set of programs that creates and maintains the database
- Relational databases: data organised into tabular format with rows and columns, optimised for data operations
- SQL: standard querying languages for relational databases
- Non-relational database: built for speed, flexibility, and scale, making it possible to store data in schema-less fashion
- ETL process: extract, transform, and load process helps you extract data from different sources and load it into the data repository
- Big data stores: distributed computational storage infrastructure to store, scale, and process very large datasets

## Relational Databases
- Collection of data organised into a table structure
- Tables can be linked or related based on common data
- Build on the organisational principles of flat files (spreadsheets) with data organised in rows and columns
	- rows = "records"
	- columns = "attributed"
- Use SQL for querying data
- Ideal for optimised storage, retrieval, and processing of data
- Fields can be restricted to specific data types and values
- They can be
	- open-source and internally supported
	- open-source with commercial support
	- commercial closed-source systems
- RDMS is a mature and well-documented technology
- Reduced redundancy: minimise data redundancy
- Ease of backup and disaster recovery: easy export and import options
- ACID-compliance: Atomicity, Consistency, ISolation, and Durability
- Use-cases
	- Online Transaction Processing (OLTP): focused on transaction-oriented tasks at high rates
	- Data warehouses: RDBs can be optimized for online analytical processing
	- IoT Solutions: require speed and the ability to collect and process data
- Limitations
	- does not work well with unstructured data
	- migrations between two RDBMS can be dificult
	- have limit on the length of the data field

## NoSQL
- non-relational database design that provides flexible schemas for storage and retrieval of data
- recently become more popular (cloud, big data, high-volume web)
- chose for their attributes around scale, performance, and ease of use
- built for specific data models with flexible schemas that allow programmers to create and manage modern applications
- don't use traditional row/column/table design
- typically don't use [[SQL]] to query data (may support [[SQL]] interfaces)
- stores data in a free-form fashion
- any data can be stored
- four types of common types of databases
	- key-value store: stored in key-value pairs (key is attribute, value is data)
	- document-based: each record and associated data in a document
	- column-based: stores data in cells grouped as columns instead of rows
	- graph-based: use a graphical model to represent and store data
- advantages
	- ability to handle large volumes of structures and unstructured data
	- ability to run as distributed systems
	- an efficient and cost-effective scale-out architecture with additional capacity and performance with each new node
	- simpler design, better control over availability, and improved scalability
- different between relational and non-relational
	- Relational: rigidly defined data and storage
	- NoSQL: schema-agnostic, allowing for storage and manipulation of unstructured data

## Data Marts, Data Lakes, ETL, and Data Pipelines
- Data warehouse
	- works like multi-purpose storage
	- data entering the warehouse is already modelled and structured
	- stores current and historical data that is cleansed, conformed, and categorised
	- multi-purpose enabler of operational and performance analytics
- Data mart
	- sub-section of a data warehouse
	- built for particular business function
	- provides stakeholders data most relevant to them
	- offer analytical capabilities for restricted area of the warehouse
	- offers business-specific reporting and analytics
- Data lake
	- storage repo that can store large amounts of structured, semi-structured, and unstructured data in their native format classified with metadata
	- a pool of raw data where each data element is given a unique identifier
	- use this if you  generate or have access to large volumes of data on an going basis without being restricted to pre-defined use cases
	- retains all source data, without exclusion
	- sometimes used as a staging area for a data warehouse
- Extract, Transform, Load (ETL)
	- how raw data is converted into analysis-ready data
	- automated process where you gather raw data from identified sources, extract information, clean, standardise, and transform the data into suitable formats, and load into the repository
	- Extract: data from source location is collected
	- Transform: execution of rules functions to convert raw data into usable data
	- Load: processed data is transported to a destination system or repository
	- has historically been used for batch workloads
- Data pipelines
	- architected for batch processing, streaming, or both
	- particularly useful for data that needs constant updating
	- high performing system that supports long-running batch queries and smaller interactive queries
	- destination is typically a data lake

## Foundation of Big Data
- Ernst and Young: big data refers to dynamic, large, and disparate volumes of data being created by people, tools, and machines
- requires new innovative scalable technologies to collect, host, and process
- no one definition of big data, but there are common elements
- Big Vs of big data
	- Velocity: speed of data accumulation
	- Volume: scale of the data or the increase in amount of data
	- Variety: diversity of the data
	- Veracity: the quality and origin of data and its conformity to facts and accuracy
	- Value: refers to benefits of the data (financial, social, personal, etc.)

## Big Data Processing Tools
- provide ways to work with large sets of data
- Apache Hadoop: tools providing distributed storage and processing of big data
	- can scale from a single node to any number of nodes
	- provides reliable, scalable, and cost-effective solution for storing data with no format requirement
	- can incorporate emerging data formats with data not traditionally used in a data warehouse
	- can provide real-time self-service access all stakeholders
	- can optimise and streamline costs by consolidating data
- Apache Hive: data warehouse for data query and analysis
	- data warehouse software for reading, writing, and managing large data set files
	- not suitable for transaction processing that involves high percentage of write operations
	- better suited for data warehousing tasks such as ETL, reporting, and data analysis
	- includes tools to enable easy access to data via SQL
- Apache Spark: distributed data analytics framework designed to perform complex data analytics
	- general-purpose data  processing engine designed to extract and process large volumes of data
	- takes advantage of in-memory processing to significantly increase the speed of computations and spilling to disk
	- can run using standalone clustering technology
	- can access data in large variety of sources

## Summary and Highlights

A Data Repository is a general term to refer to data that is collected, organised, and isolated to be used for reporting, analytics, and archival.

Types of Data repositories
- Databases
	- can be relational or non-relational
	- following a set of organisational principles
- Data Warehouses
	- consolidate incoming data into one comprehensive storehouse
- Data Marts
	- sub-sections of a data warehouse
	- built to isolate data for a particular use-case
- Data Lakes
	- serve as storage repositories for large amounts of data in their native format
- Big Data Stores
	- provide distributed computational and storage infrastructure
	- store, scale, and processes large data sets

ETL (Extract, Transform, and Load) process is an automated process that converts raw data into analysis-ready data
- extracts data from source
- transforms data by cleaning, enriching, standardising, and validating
- loads the processed data into a destination system or data repository

Data Pipelines encompasses the entire journey of moving data from source to destination using ETL.

Big data refers to the vast amounts of data being produced each moment of every day. It is described by the five big Vs: velocity, volume, variety, veracity, and value. These challenges led to the emergence of processing tools and platforms, including Hadoop, Hive, and Spark.