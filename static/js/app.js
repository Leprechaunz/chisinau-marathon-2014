$(document).ready(function() {
    var chart;

    $.get("graph/10km/", function(data) {
        chart = new Chartist.Bar('.ct-chart', data, {
            axisY: {
                onlyInteger: true
            },
            width: '100%',
            height: '500px'
        });
    });

    $("#race-dropdown, #gender-dropdown").change(function () {
        var race = $("#race-dropdown").val();
        var gender = $("#gender-dropdown").val();

        $.get("graph/" + race + "/" + gender, function(data) {
            chart.update(data);
        });
    });
});