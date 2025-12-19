# Data Analysis Basics, Filtering and Sorting Data

## Analysing Data Using Spreadsheets
- we need to visualise the final output
- before starting, we need to answer
	- How big is the dataset?
	- What type of filtering is required?
	- How should it be sorted?
	- What type of calculations are needed?
- sorting the data lets us organise it based on conditions (alphabetically, numerically, etc.)
- we can filter the data to see only a sub section (i/e filter for November)
- Formulas
	- AVERAGE
	- SUM
## Filtering and Sorting Data in Excel
- filtering enables more control over what data is displayed
- can help with the visibility of data by narrowing to specific criteria
- status bar at the bottom of the worksheet will show how many records are displayed out of the total
- sorting enables you to organize your data alphabetically, numerically, chronologically
- sorting makes it easier to conceptualize your data in meaningful ways
## Useful Functions for Data Analysis
- IF
	- most used logical function in Excel
	- enabled you to logically compare a value against a criteria
	- "if something is true, then return a value or do something"
- IFS
	- enables you to replace nested IF functions into a single formula
- COUNTIF
	- used to count the number of cells that meet a criterion
- SUMIF
	- calculate the sum of cells that meet a certain criterion
## Using the VLOOKUP and HLOOKUP Functions
- VLOOKUP
	- one of the most commonly used reference type functions
	- enables you to find data referenced in a lookup table
	- stands for "vertical lookup"
	- useful when you want to find something in a table or a range by column
	- works by using a common shared key between the source and lookup data
- HLOOKUP
	- looks for data by row instead
	- syntax is identical to VLOOKUP except you specify a row index number
	- indicates the row number in the lookup table you're looking for
## Advanced Excel Formulas
- COUNTIFS
	- COUNTIFS(criteria_range_1, criteria_1, [criteria_range_2, criteria_2], ...)
	- counts the number of cells that meet one or more criteria
	- more complex and versatile than COUNTIF
	- used for filtering data with multiple or complex conditions
- SUMIFS
	- SUMIFS(sum_range, criteria_range_1, criteria_1, [criteria_range_2, criteria_2], ...)
	- adds all numbers in a range that meet multiple criteria
	- provides more granular summation control than SUMIF
	- used for financial analysis and data aggregation
- XLOOKUP
	- XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])
	- searches a range or array and returns an item corresponding to the first match found
	- can search both vertical and horizontal ranges
	- replaces both VLOOKUP and HLOOKUP with enhanced functionality
	- used for data retrieval and error handling
## Summary and Highlights
Before shaping your data, you need to visualize the final output, and ask yourself these questions:
- How big is the dataset?
- What type of filtering is required?
- How should the data be sorted?
- What type of calculations are needed?

There are several advantages to formatting your data as a table
- Automatic calculations when filtering
- Column headings never disappear
- Banded rows to make reading easier
- Tables will automatically expand when adding new rows

The most basic way of shaping your data is to sort and filter
- Sorting data helps you to organize it by a specified criteria, such as numerically, alphabetically, or chronologically
- Filtering out data makes it easier to control what data is displayed and what is hidden, based on filtered fields

Excel Functions
- Functions in Excel are arranged into multiple categories
	- mathematical
	- statistical
	- logical
	- financial
	- date and time-based
- Common functions for data analysis include
	- IF, IFS
	- COUNTIF
	- SUMIF
	- VLOOKUP, HLOOKUP

# Using Pivot Tables
## [[Creating Pivot Tables in Excel]]
- provide a simple and quick way to summarize and analyze data
- it is dynamic, it will update with the data
- can be used to draw useful and relevant conclusions about data
- your data must be formatted as a table first
	- home > Styles > 'Format as Table'
	- ensure you select 'My table has headers' if it does
- tables automatically get filters added
- data must be formatted before a pivot table can be used
	- remove blank rows and columns
	- eliminate blank cells

## Pivot Table Features
- Recommended Pivot Tables
	- list of suggested combinations of data that could be used
	- based on the data selected in the worksheet
	- great way to get started
- Can manually expand field to view their contents
- pivot tables have in-built filtering

## Summary and Highlights

Pivot Tables:
- Used to obtain usable and presentable insights into your data
- Provide a simple and quick way to summarize and analyze data
- As you change and add data to the original dataset, the analysis and summary information changes too
- Can be used to draw useful and relevant conclusions about data

Pivot Table Checklist:
- Format  your data as a table
- Ensure column headings are correct, and there is only one header row
- Remove any blank rows and columns, and try to eliminate blank cells
- Ensure value fields are formatted as numbers and not text

Arranging Pivot Tables with Filters and Tables
- Use pivot table fields to add and arrange data fields
- Recommended Pivot Tables are a list of suggested combinations of data that could be used

Filters and Slicers:
- Slicers are on-screen graphical filter objects to filter data using button
- Timelines are another type of filter tool to filter specifically on date-related data

