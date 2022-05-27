$(document).ready(function () {
    $.get("https://valorant-api.com/v1/agents?language=es-ES", function (data) {
        $.each(data.data, function (i, item) {
            $("#agente").append('<option value=' + i + '>' + item.displayName + '</option>');
        });
    });
    $.get("https://valorant-api.com/v1/maps?language=es-ES", function (data) {
        $.each(data.data, function (i, item) {
            $("#mapa").append('<option value=' + i + '>' + item.displayName + '</option>');
        });
    });
});



