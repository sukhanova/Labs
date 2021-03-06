"use strict";

// PART 1: SHOW A FORTUNE

function showFortune(evt) {

    // TODO: get the fortune and show it in the #fortune-text div

    $.get('/fortune', (response) => {
        $('#fortune-text').html(response);
    });
}

$('#get-fortune-button').on('click', showFortune);


// PART 2: SHOW WEATHER

function showWeather(evt) {
    evt.preventDefault();

    let url = "/weather.json";
    let formData = {"zipcode": $("#zipcode-field").val()};
    
    // TODO: request weather with that URL and show the forecast in #weather-info
    $.get(url, formData, (response) => {
        // console.log(response.forecast);
        // console.dir(response);
        $('#weather-info').html(response.forecast);
    });
}

$("#weather-form").on('submit', showWeather);


// PART 3: ORDER MELONS

function orderMelons(evt) {
    evt.preventDefault();

    // TODO: show the result message after your form
    let url = '/order-melons.json';
    let formData = {
        'melon': $('#melon-type-field').val(),
        'qty': $('#qty-field').val()
    }

    $.post(url, formData, (response) =>{
        // $('#order-status').html(`${response.code}, ${response.msg}`);
        if (response.code === 'OK'){
            $('#order-status').html(response.msg);
            clearInput();
         
            // if the result code is ERROR, it will show up in red (see CSS!)    
        } else {
            clearInput();
            $('#order-status').addClass('order-error');
            $('#order-status').html(response.msg);
            // location.reload();
            setInterval('location.reload()', 3000);
        }
    })

   
}

function clearInput(){
    $('#melon-type-field').val("");
    $('#qty-field').val("");
}


$("#order-form").on('submit', orderMelons);


