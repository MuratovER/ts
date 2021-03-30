google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawChart);

function drawChart() {
var data = google.visualization.arrayToDataTable([
    ['Date', 'Работа', 'Учеба', 'Саморазвитие'],
    ['19 Пн',  3,      4,       1      ],
    ['20 Вт',  2,      4,       1       ],
    ['21 Ср',  1,       4,      2       ],
    ['22 Чт',  2,      2,       3       ],
    ['23 Пт',  1,       2,      4       ],
    ['24 Сб',  1,       3,      5       ],
    ['22 Вс',  4,       4,      5       ]
]);

var options = {
    vAxis: {minValue: 0}
};

var chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
chart.draw(data, options);
}
