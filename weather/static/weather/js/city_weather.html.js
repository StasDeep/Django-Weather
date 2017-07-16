$(function () {
    var city_weather_url = $('#url_variable').val();
    var timeout_sec = 10;

    setInterval(function () {
        $.get(city_weather_url, function (data) {
            $('#content').html(data);
        });
    }, timeout_sec * 1000);

});
