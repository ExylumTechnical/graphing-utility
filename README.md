# graphing-utility for Chart.js
I developed some code in python so that I could easily generate graphs and charts to be displayed in HTML, hope you enjoy and find this code usefull in your own projects.

## How it works
Ill go over the use of the class functions briefly all of these functions can be found in the produceGraphClass.py file

## graphs.makeTable(self,data)
This returns an html table the data variuble should be a python list. There is basically no constraint on how many columns or rows you can have, the function will put more columns in a row even if there is not a title for that row. Likewise it will put fewer columns into a row than there are columns. That being said you will need to check the data before it is entered into this function. Still pretty useful for displaying raw data.

data variuble example:
dat=[
["len","width","contents"],
[50,50,"mystery"],
[50,50,"another mystery"]
]
dat[0] is the title of each column
dat[1:] is the data to be put into each row


## graphs.makeChart(self, varNames, varValue, chartLabel, barColors=["blue"])
This will output a bar graph chart for data fed into the function. I will explain each variuble below as well as the default values

varNames - these are the names to be displayed for each bar
varValue - this is what the value intiger will be for the corrosponding bar
chartLable - VERY IMPORTANT, this will be what the chart ID that will be called by the HTML element to display the variuble
TbarColors - set to blue by default to make things easier, but can be a list of colors such as ["blue","green","red"]

## graphs.makeLineGraph(self,lables,values,tname,tLabel="frequency over time")
This function will output a line graph with the supplied data below is an explination of input to be supplied
labels - This will be the lables put onto the y axis
values - This will need to be an intiger value for the graph to display
tname - VERY IMPORTANT, this will be what the chart ID that will be called by the HTML element to display the variuble
tLabel - This will be the title displayed on the graph



## Notes about implementation
At the bottom of the file I have included an exapmple of how the code should be used to send the code to standard out.

There are two ways to display the graphs, first is to dump the input into a .js file and call the file in your html code (see below). The second is to use these functions in conjunction with other functions or tooling in the generation of .html files.

Where exampleChart is either the chartLable for a chart or the tname for a graph. The dataOutput.js is the output from the function in a file.
<canvas id="exampleChart" style="width:100%;max-width:600px"></canvas>
<script src="dataOutput.js"></script>
