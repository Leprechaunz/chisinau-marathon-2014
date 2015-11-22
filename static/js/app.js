$(document).ready(function() {
    var chart;

    $.get("json/10km", function(data) {
        chart = new Chartist.Bar('.ct-chart', data, {
            axisY: {
                onlyInteger: true,
                scaleMinSpace: 50
            },
            width: '100%',
            height: '500px'
        });
    });

    $("#race-dropdown").change(function () {
        var race = $(this).val();
        $.get("json/" + race, function(data) {
            chart.update(data);
        });
    })
});