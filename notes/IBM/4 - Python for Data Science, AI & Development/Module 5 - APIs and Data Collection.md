# Simple APIs
APIs (Application Programming Interfaces) allow developers to create new applications by leveraging existing functionality from other systems. They define how software components should interact and facilitate communication between services without direct implementation
## Applications of APIs
1. Social media platforms
2. E-commerce websites
3. Weather applications
4. Maps and navigation applications
5. Payment gateways
6. Messaging applications
# REST APIs, Web Scraping, and Working with Files
## Web Scraping and HTML Basics
- the process of extracting information from web pages
- involves automated retrieval of data from sources
- used for various applications including data analysis, mining, price comparison, content aggregation
### How it works
- HTTP request
	- The process begins with an HTTP request. A web scraper sends a request to a specific URL. The request is usually a GET request, which retrieves the web page's content
- Web page retrieval
	- The web server hosting the website responds to the request by returning the HTML content. This content includes visible text and media elements underlying HTML structure
- HTML parsing
	- Parsing involves breaking down the HTML structure into components, such as tags, attributes, and text content. You can use BeautifulSoup in Python, which creates a structured representation of the HTML content that can be easily navigated and manipulated.
- Data extraction
	- With the content parsed, web scrapers can identify and extract the specific data they needs. This can include text, links, images, tables, product prices, news articles, and more. Scrapers locate the data by searching relevant HTML tags, attributes, and patterns
- Data transformation
	- Extracted data may need further processing and transformation. For instance, you can remove tags from text, convert data formats, or clean up messy data. This step ensures the data is ready for analysis.
- Storage
	- After extraction and transformation, you can store the scraped data in various formats, such as databases, spreadsheets, JSON, or CSV files.
- Automation
	- Scripts or programs can automate web scraping. These tools allow recurring data extraction from multiple web pages. This is especially useful for collecting data from dynamic websites that regularly update their content.
## Web Scraping: A Key Tool in Data Science
- Web scraping: a technique to extract large amounts of data from websites
- converts unstructured website data into structured form
### Importance of Web Scraping in Data Science
1. Data Collection: A primary method of collecting data from the internet.
2. Real-time Application: Used for real-time apps like weather updates, price comparison, etc.
3. Machine Learning: Provides the data needed to train machine learning models
### Web Scraping with Python
1. BeautifulSoup
	- library used for web scraping
	- pulls the data out of HTML and XML files
	- creates a parse tree from page source code used to extract data in a hierarchical and readable manner
2. Scrapy
	- open-source and collaborative web crawling framework
	- used to extract data from websites
3. Selenium
	- used for controlling web browsers through programs and automating tasks
### Applications of Web Scraping
1. Price Comparison: Services use web scraping to collect data from online shopping sites and use it to compare the prices of products
2. Email address gathering: Companies use web scraping to collect email ID and send bulk emails for marketing
3. Social Media Scraping: Used to collect data from Social Media websites to find out what's trending
# Web Scraping Tables using Pandas
- pandas library contains function `read_html()`
- can be used to extract tabular information from any web page
# Summary
- Simple APIs in Python are application programming interfaces that provide methods for interacting with services, libraries, or data
- Rest APIs allow you to communicate through the internet, taking advantage of resources like storage, access more data, AI algorithms, and so on
- The HTTP (HyperText Transfer Protocol) transfers data, including web pages and resources, between a client and a server
- Requests is a Python library that allows you to send HTTP/1.1 requests
- Web scraping involves extracting and parsing data from websites to gather information for various applications
- Tabular data can be extracted from web pages using the `read_html` method in Pandas
- Beautiful Soup in Python is a library for parsing and navigating HTML and XML documents
- To parse a document, pass it through the Beautiful Soup constructor to get a beautiful soup object representing the document as a nested data structure
- Beautiful soup represents HTML as a set of tree-like objects with methods to parse
- Navigable string is like Python string that supports beautiful soup functionality
- `find_all` is a method used to extract content based on the tag's name, its attributes, the text of a string, or a combination
- The `find_all` method looks through a tag's descendants and retrieves all descendants that match your filters