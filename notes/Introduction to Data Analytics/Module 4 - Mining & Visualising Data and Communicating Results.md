# Analysing and Mining Data

## Overview of Statistical Analysis
- **Statistics**: branch of math dealing with collection, analysis, interpretation, and presentation of numerical data
- Statistics is applied for decision-making based on data
- **Statistical Analysis**: The application of statistical methods to data in order to develop and understanding of what it represents
- **Sample**: a representative selection drawn from a total population
- **Population**: a discrete group of people or things that can be identified by at least one common characteristic
- Mainly useful to ensure data is interpreted correctly
- **Descriptive statistics**: summarise information about a sample
	- *Central Tendency*: where most values lie (mean, median, mode)
	- *Dispersion*: measure of variability (variance, standard deviation, range)
	- *Skewness*: measure of whether the distribution is symmetrical around a central value
- **Inferential statistics**: make inferences or generalisations about the broader population
	- *Hypothesis testing*: tells you whether the efficacy observed in a sample is likely to exist in the population
	- *Confidence intervals*: incorporates the uncertainty and sample error to create a range of values the population is likely to fall within
	- *Regression analysis*: incorporates hypothesis tests that help determine if relationships observed in the sample actually exist in the population

## Data Mining
- the process of extracting knowledge from data
- involves the use of pattern recognition technologies, statistical analysis, and mathematical  techniques
- **Pattern recognition**: the discovery of regularities or commonalities in data
- **Trend**: the general tendency of a set of data to change overtime
- Data mining applications
	- profiling customer behaviours
	- predict patient likelihood for health conditions
	- prediction student academic achievement levels
	- help deploy police where the likelihood of crime is higher
- **Classification**: classifies attributes into target categories
- **Clustering**: grouping data into clusters to treat them as groups

## Tools for Data Mining
- [[Spreadsheets]]
	- common for basic data mining tasks
	- used to host data from other systems
	- can pivot tables to show aspects of data
	- easier to make comparisons between sets of data
	- Add-ins for Excel: Data Mining Client, XLMiner, KnowledgeMiner
		- allows for classification, regression, association rules, clustering, model building
- [[R]]-Language
	- most widely used languages for statistical modelling
	- packaged with hundreds of libraries built for data mining operations
		- regression, classification, data clustering, association rule mining, text mining, outlier detection, social network analysis
	- packages: tm, twitterR, 
	- IDE: R Studio
- [[Python]]
	- libraries: Pandas, Numpy
	- Pandas
		- open-source module for working with data structures and analysis
		- one of the most popular libraries for data analysis in Python
		- allows for uploading data in any format
		- provides simple organisation, sorting, and data manipulation
		- can perform basic numerical computations (mode, median, mean, range)
- IBM SPSS Statistics
	- closed source, requires a license
	- easy to user interface requiring minimal coding
	- comprises of efficient data management tools
- IBM Watson Studio
	- leverages a collection of open source tools (Jupyter)
	- enables team members to collaborate on projects
- SAS Enterprise Miner
	- comprehensive graphical workbench for data mining
	- provides capabilities for interactive data exploration
	- can manage data from various sources
	- can identify patterns, explore relationships and anomalies, analyse big data, validate reliability

## Summary and Highlights

Statistics is a branch of mathematics dealing with the collection, analysis, interpretation, and presentation of numerical or quantitative data.

Statistical Analysis involves the use of statistical models in order to develop an understanding of what the data represents

It can be:
- Descriptive: provides a summary of what the data represents, including Central Tendency, Dispersion, and Skewness
- Inferential: makes generalisations about data, including Hypothesis Testing, Confidence Intervals, and Regression Analysis

Data Mining is the process of extracting knowledge from data. It involves pattern recognition technologies, statistical analysis, and mathematical techniques, in order to identify correlations, patterns, variations, and trends in data.

There are several techniques that can help mine data, such as classifying attributes of data, clustering data into groups, establishing relationships between events, variables, and input and output.

A variety of software and tools are available for analysing and mining data. Some of the popular ones include [[Spreadsheets]], [[R]]-Language, [[Python]], IBM SPSS Statistics, IBM Watson Studio, and SAS, each with their own set of characteristics.

# Communicating Data Analysis Findings

## Overview
- Data analysis process starts with understanding a problem and ends with communicating findings
- Data projects are the result of collaborative efforts involving multi-disciplinary skills where the findings are incorporated into larger initiatives
- Success of communication depends on how well others understand and trust your insights
- You need to tell the story by visualising the insights clearly and creating a structured narrative
- Your presentation needs to be framed around the level of information your audience already has
- You decide what, and how much information is essential to understand the findings
- Begin the presentation by demonstrating your understanding of the problem
- Organise your presentation for maximum impact
	- reference data you collected
	- share your data sources, hypotheses, and validations
	- be deliberate in taking either top-down or bottom-up approach
	- be consistent
- tell a story through graphical depiction of facts
	- graphs, charts, diagrams

## Data Visualisation
- The discipline of communication information through visual elements
- Goal is to make information easy to comprehend, interpret, and retain
- Can provide a summary of relationships, trends, and patterns in the data
- You have to choose the visualisation that most effectively delivers your findings
- Visualisations can be static or interactive
- Types of visualisations
	- Bar charts: great for comparing related data sets
	- Column charts: compare values side-by-side to show change over time
	- Pie Charts: show the breakdown of an entity into it's sub-parts and its proportions
	- Line Charts: display trends, how a data value is changing in relation to a continuous variable
- Dashboards
	- organise and display reports and visualisations coming from multiple sources
	- can be used to monitor daily progress or overall health
	- can present both operational and analytical data


## Visualisation and Dashboarding Software
- [[Spreadsheets]]
	- most commonly used software for graphical representation
	- easy to learn and have lots of documentation
	- provides several chart types
- [[Jupyter]] Notebook
	- [[Python]] provides a host of libraries for data visualisation
	- Matplotlib
		- provides different kinds of 2D and 3D plots
		- allows you to create high-quality interactive graphs and plots
	- Bokeh
		- provides interactive charts and plots known for high-performance interactivity
		- offers flexibility in applying interaction, layouts, and styles
		- can also transform visualisations written in other Python libraries
	- Dash
		- build interactive web applications in Python
		- easily maintainable, cross-platform, and mobile ready
	- R-Studio
		- create basic visualisations including histograms, bar charts, line charts, box plots, and scatter plots
		- Shiny
			- package to help build interactive web apps
			- these web apps can seamlessly display R objects including visualisations
			- can also build a dashboard
	- IBM Cognos Analytics
		- end-to-end analytics solutions
		- visualisation features provided include importing custom visualisations, forecasting features, recommendation visualisations based on data
	- Tableau
		- produces interactive data visualisation products
		- create interactive graphs and charts
		- also offers option to publish results
		- can import R and Python scripts in Tableau
		- compatible with Excel files, text files, relational databases, and cloud databases
	- Power BI
		- cloud-based business analytics software from Microsoft
		- powerful and flexible tool known for speed and efficiency
		- compatible with Excel, SQL server, and cloud-based repositories

## Summary and Highlights
 
 Data has value through the stories it tells. In order to communicate findings impactfully:
- Ensure the audience trusts, understands, and relates to your findings and insights
- Establish credibility of findings
- Present data in a structured narrative
- Support communications with strong visualisations for the message to be clear and concise

Data visualisation is the discipline of communicating information through visual elements such as graphs, charts, and maps. The goal is to make information easy to comprehend, interpret, and retain.
- Think about the key takeaway for your audience
- Anticipate their information needs and questions, then plan visualisations that deliver your message clearly and impactfully

There are several types of graphs and charts to be able to plot any kind of data, including bar charts, column charts, pie charts, and line charts.

You can also build dashboards, which organise and display reports and visualisations coming from multiple sources into a single interface. They are easy to comprehend and allow to generate reports on the go.

Some popular tools for data visualisations include Spreadsheets, Jupyter Notebook, Python libraries, R-Studio and R-Shiny, IMB Cognos Analytics, Tableau, and Power BI.