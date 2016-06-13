/*
I am playing around with JavaScript and am determined to incorporate it into my webpage
*/

$(document).ready(function() {
    console.log('ready!');   
});

var myfn = function(i) {
  return function() { alert(i); };  
};

/*for (var a=1; a<=5; a++) {
    $('<p>' + a + '</p>').appendTo('h1').click(myfn(a));
} */

var $h1 = $('h1').width();
$('h1').html($h1);
