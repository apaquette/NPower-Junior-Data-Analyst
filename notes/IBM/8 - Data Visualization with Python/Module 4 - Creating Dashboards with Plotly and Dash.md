# Creating Dashboard with Plotly
## Dashboarding Overview
- Real-time visuals simplify business moving parts
- Display Key Performance Indicators (KPI)
- Help businesses by providing the big pictures
### Web-based dashboarding
- plotly Dash
- Panel
- voila
- Streamlit
## Introduction to Plotly
- Interactive open source plotting library
- Supports over 40 unique chart types
- Includes various types of charts
- **Plotly Graph Objects**: Low-level interface to figures, traces, and layout
- **Plotly Express**: High-level wrapper
# Working with Dash
## Introduction to Dash
- Open-source UI Python library from Plotly
- Easy to build GUI
- Declarative and Reactive
- Rendered in a web browser and can be deployed to servers
- Inherently cross-platform and mobile ready
### Dash Components
- Core components
	- Higher-level interactive components generated with React.js 
- HTML Components
	- Component for every HTML tag
	- Keyword arguments describe the HTML attributes (style, className, and id)
## Make Dashboards Interactive
- **Callback function**: python function automatically called by Dash
	- `@app.callback(Output,Input)` decorator used on function
	- Output: sets results returned from callback
	- Input: provided to the callback function
- 