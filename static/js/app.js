$(document).ready(function() {
    $.get( "json/42km", function( data ) {
        new Chartist.Bar('.ct-chart', data, {
            axisY: {
                onlyInteger: true,
                scaleMinSpace: 50
            },
            width: 1824,
            height: 800
        });
    });
});