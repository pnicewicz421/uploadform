$(document).ready(function() {
    console.log('ready!');  
    <!-- Your task is to use the text of the label for the search input to create "hint" text for the search input. The steps are as follows: 
    <!--    Set the value of the search input to the text of the label element
    
    <!-- get label text
    var $labelText = $('#search label').html();
    var $myValue1 =  $('#search input:first').val();

    $('#search input:first').val($labelText);
    var $myValue2 =  $('#search input:first').val();
    
    console.log($myValue1);
    console.log($myValue2);
    console.log($labelText);
    
     <!--    Add a class of "hint" to the search input
    $('#search input:first').addClass('hint');
    console.log($('#search input:first').hasClass('hint'));
     
      <!--    Remove the label element
    $('#search label').remove();
    
    <!-- Bind a focus event to the search input that removes the hint text and the "hint" class
    $('#search input:first').focus(function() {
        $(this).val('');
        $(this).removeClass('hint');
        console.log('I went into the focus funciton');
        });
        
    <!-- Bind a blur event to the search input that restores the hint text 
    <!-- and "hint" class if no search text was entered
     $('#search input:first').blur(function() {
        
        if ($(this).val() == ''){
            $(this).val($labelText);
            $(this).addClass('hint');
            }
        });
        
 <!-- What other considerations might there be if you were creating this functionality for a real site?
 <!-- Add Tabbed Navigation

 <!-- Open the file /exercises/index.html in your browser. Use the file /exercises/js/tabs.js. Your task is to create tabbed navigation for the two div.module elements. To accomplish this:

 <!--     Hide all of the modules.
      $('div.module').hide();
 
 <!--     Create an unordered list element before the first module.
      $('<ul id="mylist"></ul>').insertBefore($('div.module:first'));
 
 <!-- Iterate over the modules using $.fn.each. For each module, use the text of the h2 element 
 <!-- as the text for a list item that you add to the unordered list element.
    $('div.module').each(function(idx, el) {
        var $h2text = $(this).find('h2').html();
        $('#mylist').append('<li>' + $h2text +'</li>');
        console.log($('#mylist').html());
        });

 <!--     Bind a click event to the list item that:

 <!--         Shows the related module, and hides any other modules
      
 
        $('#mylist li:first').click(function() {
            $('div.module:first').show();
            $('div.module:last').hide();
            $(this).addClass('current');
            $('#mylist li:last').removeClass('current');
            });
            
        $('#mylist li:last').click(function() {
            $('div.module:first').hide();
            $('div.module:last').show();
            $(this).addClass('current');
            $('#mylist li:first').removeClass('current');
            });

 <!--         Adds a class of "current" to the clicked list item

 <!--         Removes the class "current" from the other list item

 <!--     Finally, show the first tab.
         $('div.module:first').show();
    
});