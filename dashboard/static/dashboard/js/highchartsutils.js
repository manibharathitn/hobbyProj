function drawBar(divId, xData, yData, titleChart) {
    $(divId).highcharts({
        chart: {
            type: 'column'
        },
        title: {
            text: titleChart
        },
        subtitle: {
            text: null
        },
        xAxis: {
            categories: xData,
            labels: {
                enabled: false
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: '# of booking'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">City code : {point.x}: </td>' +
                '<td style="padding:0"><b>{point.y}</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        plotOptions: {
            column: {
                pointPadding: 0.2,
                borderWidth: 0
            }
        },
		credits : {
			href: 'http://in.linkedin.com/in/manitn',
			text: 'Designed by Mani'
		},
        series: [{
            data: yData
        }]
    });
}


function drawLine(divId, xData, yData, titleChart) {
    $(divId).highcharts({
        title: {
            text: titleChart,
            x: -20 //center
        },
        subtitle: {
            text: null,
            x: -20
        },
        xAxis: {
            categories: xData
        },
        yAxis: {
            title: {
                text: '# of booking'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: null
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle',
            borderWidth: 0
        },
		credits : {
			href: 'http://in.linkedin.com/in/manitn',
			text: 'Designed by Mani'
		},
        series: [{
            name: '# of booking',
            data: yData
        }]
    });
}


function drawPie(divId, xData, yData, titleChart, xLegend) {

    dataValues = [], i = -1;
    while ( xData[++i] ) {
      dataValues.push( [ xData[i], yData[i] ] );
    }


    $(divId).highcharts({
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false
        },
        title: {
            text: titleChart
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: xLegend + ' <b>{point.name}</b>: {point.y}',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
		credits : {
			href: 'http://in.linkedin.com/in/manitn',
			text: 'Designed by Mani'
		},
        series: [{
            type: 'pie',
            name: 'Contribution',
            data: dataValues
        }]
    });
}