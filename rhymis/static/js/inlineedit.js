$(document).ready(function() {

	function getCookie(name) {
    	var cookieValue = null;
    	if (document.cookie && document.cookie !== '') {
      		var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    	}
    return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
    	beforeSend: function(xhr, settings) {
       		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            	xhr.setRequestHeader("X-CSRFToken", csrftoken);
        	}
    	}
	});

// Process the Edit click event
 
    $(document).on('click', '.edit', function() {

    	console.log("I clicked Edit")

    	//retrieve recordid
        
        // only generate an inline row if one is not there already
        if ($('.editfield').length == 0) {

        	var recordid = $(this).attr('id').substring(4); 

        	console.log("VALID ONE:" + recordid)

        	var parentTr = $(this).parents('.trow');
        	//$('.field', parentTr).attr('class', 'editfield')

        	//add an input box for each field in the row
        	$('.field', parentTr).each(function(i){
               var fieldname = $(this).text();
               $(this).attr({'id' :'editfield' + i, 'class' : 'editfield'}); //assign a unique id to each td class name under edit to enter json response back
               $(this).html($("<input>", {type:"text", name:"field" + i, id:"field" + i, class:"newinput", value:fieldname, form:"recordsform"}));
              });

        	//change the delete to cancel and the edit to submit
        	$('.delete', parentTr).html('<a id="cancel" href="Cancel">Cancel</a>');
        	$('.edit', parentTr).replaceWith('<button type="submit" class="OKbutton" id="submitbutton" form="recordsform">OK</button>');

   			$(document).on('click', '#submitbutton', function(event) {
      			event.preventDefault();
        		console.log("form submitted!")
        	    create_post(recordid, parentTr);
                
    			});

        }

    });

    function create_post(recordid, parentTr) {
    	console.log('BEFORE AJAX')
    	var valPropName = { 0 : 'date/' + $('#field0').val(), 
    		1 : 'location/' + $('#field1').val(), 
    		2 : 'staff/' + $('#field2').val(), 
    		3 : 'youth/' + $('#field3').val()
    	}
    	console.log(recordid, $('#field0').val(), $('#field1').val(), $('#field2').val(),$('#field3').val(), $('#field4').val())
    	$.ajax({
    		url : "/records/edit/process", //url
    		type : "POST",
    		data : { '-1' : recordid, '0' : $('#field0').val(), '1' : $('#field1').val(), '2' : $('#field2').val(), '3' : $('#field3').val(), '4' : $('#field4').val()},
    		success : function(json) {
    			$('.newinput').remove(); //remove the input fields
    			console.log(json[0],json[1],json[2],json[3],json[4],json[5]) 
    			console.log("success")
    			//insert the new values
    			var nextTd = $('td:first', parentTr);
    			console.log('*-*-*-*-*-*-*-*-*')
    			console.log(nextTd.next('td').next('td'))

    			for (var key in json) {

    				if (json.hasOwnProperty(key) && key > -1 && key < 4) {
    					console.log('Link:' + valPropName[key])
    					console.log('key:' + key)
    					console.log('value:' + json[key])

    					//We will not have ids any more. Instead we will traverse across the fields. This is 0 to 3.
    					//4 will come next

    					//$('#editfield' + parseInt(key)).html('<a href="/records/view/' + String(valPropName[key]) + '">' + String(json[key]) +'</a>');
    					
    					$('<a href="/records/view/' + String(valPropName[key]) + '">' + String(json[key]) +'</a>').appendTo(nextTd);
    					var nextTd = nextTd.next('td')	

    				} else if (key == 4) {
    					console.log('I reached 4')
    					console.log(json[key])
    					//nextTd is prepped for the last one so that it can just populate it 

    					$(json[key]).appendTo(nextTd);
    					//$('#editfield' + parseInt(key)).html(json[key]);	
    				}
    			//replace the buttons

    			var deleteHref = '"/records/delete/' + String(json[-1]) + '"';
    			var editID = '"edit' + String(json[-1]) + '"';

    			console.log(deleteHref)

    			$('#cancel').replaceWith('<a href=' + deleteHref + '>Delete</a>');
    			$('#submitbutton').replaceWith('<a class="edit" id=' + editID + '>Edit</a>');

    			//what to do with the class and id 

    			$('td[id^="editfield"]').attr('id', 'field');
    			$('.editfield').removeClass('editfield').addClass('field');
    			

    			//finally, get rid of the editfield class
    			//console.log($('.field'))
    			//$('.editfield').attr({'id' : 'field'});


    			}
    			//$('.editfield').each(function(i){ 
    			//	$(this).appendTo(json['notes_text']);
    			//});
    		},
    		error : function(xhr, errmsg, err) {
    			alert('Oops! We have encountered an error :' + errmsg);
    			console.log(xhr.status + ": " + xhr.responseText)
    		}
    	});
    }

});