#!/usr/bin/node
/* global $ */
$('DIV#toggle_header').click(function () {
    $(this).toggleClass('green red');
});
