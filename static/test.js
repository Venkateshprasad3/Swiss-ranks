


function groupByApproverData() {
            google.charts.load('current', {'packages': ['corechart']});
            google.charts.setOnLoadCallback(drawCharta);

            function drawCharta()
            {


                var data = google.visualization.arrayToDataTable([
                    ['Engineer ', 'Parts'],
                    ['A 1 ', {{groupByApproverData[0]  }}],
                    ['Engineer 2  ', {{ groupByApproverData[1] }}],
                    ['Engineer 3', {{ groupByApproverData[2] }}],
                    ['Engineer 4', {{ groupByApproverData[3] }}],
                    ['Engineer 5', {{ groupByApproverData[4] }}]
                ]);

                var options = {title: 'Motor Parts By Engineers'};
                drawBarCharta(data,options);

                function drawBarCharta(data, options)
                {
                    var chart = new google.visualization.BarChart(document.getElementById('container'));
                    chart.draw(data, options);
                }
            }
        }