$(document).ready(function () {
    $('#textarea').change(function () {
        if ($('#event_name').val() && $('#event_location').val() && $('#event_description').val() && $('#email').val() && $('#username').val() != ''){

            $('#output').html('Someway your box is being reported as empty... sadness.');

        } else {

            $('#output').html('Your users managed to put something in the box!');
            //No guarantee it isn't mindless gibberish, sorry.

        }
    });
});