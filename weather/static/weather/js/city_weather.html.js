$(function () {
    var city_weather_url = $('#url_variable').val();
    var timeout_sec = 60;
    var progress_bar_value;
    var $bar = $('#progress-bar');

    function refreshProgressBar(reset) {
        if (reset) {
            progress_bar_value = timeout_sec;
        } else if (progress_bar_value > 0) {
            progress_bar_value -= 1;
        }

        $bar.css('width', progress_bar_value * 100 / timeout_sec + '%');
        $bar.text(progress_bar_value + ' sec');
    }

    refreshProgressBar(true);

    setInterval(function () {
        $.get(city_weather_url, function (data) {
            $('#weather').html(data);
            refreshProgressBar(true);
        });
    }, timeout_sec * 1000);

    setInterval(function () {
        refreshProgressBar();
    }, 1000);

});
