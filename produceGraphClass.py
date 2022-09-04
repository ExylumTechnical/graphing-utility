class graphs:
        def makeTable(self, data):
                title=data[0]
                html="<table border='1'>\n"
                html=html+"     <tr>\n"
                for i in title:
                        html=html+"             <td style='padding:5px;background-color:#E0E0E0;text-align:center;'>"+str(i)+"</td>\n"
                html=html+"     </tr>\n"
                for x in data[1:]:
                        html=html+"     <tr>\n"
                        for y in x:
                                html=html+"             <td style='padding:5px;background-color:#F0F0F0;text-align:center;'>"+str(y)+"</td>\n"
                        html=html+"     </tr>\n"
                html=html+"</table>\n"
                return html



        def makeChart(self, varNames, varValue, chartLabel, barColors=["blue"]):
                chartName=""
                chartValues=""
                chartColors=""
                for i in varNames:
                        chartName=chartName+"\""+str(i)+"\","
                for o in varValue:
                        chartValues=chartValues+str(o)+","
                for k in barColors:
                        chartColors=chartColors+"\""+str(k)+"\","
                chart=("""
var xValues = ["""+chartName[0:-1]+"""];
var barColors = ["""+chartColors[0:-1]+"""];
var yValues = ["""+chartValues[0:-1]+"""];
new Chart(\""""+chartLabel+"""\", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "todays events overview"
    }
  }
});
                """)
                return chart

        def makeLinegraph(self,lables,values,tname,tLabel="frequency over time"):
                if(type(lables) == "<class 'list'>" or type(values)=="<class 'list'>"):
                        lineGraph="Falure during parsing of making line graph"
                else:
                        lableStr=""
                        valueStr=""
                        for i in lables:
                                lableStr=lableStr+str(i)+","
                        for x in values:
                                valueStr=valueStr+str(x)+","
                        valueStr=valueStr[:-1]
                        lableStr=lableStr[:-1]
                        lineGraph="""
var xValues = ["""+lableStr+"""];
new Chart("""+tname+""", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      data: [ """+valueStr+"""],
      borderColor: "blue",
      fill: false
    }]
  },
  options: {
    legend: {display: false},
    title: {
        display: true,
        text:\""""+tLabel+"""\"
    }
  }
});
"""
                return lineGraph;



####################### Examples of how to use the makeLinegraph and makeChart functions of this class ####################
#chart=graphs()
#testLabels=["field1","field2"]
#testValues=[10,20]
#testName="TableID"
#print(chart.makeLinegraph(testLabels,testValues,testName))
#print(chart.makeChart(testLabels,testValues))
