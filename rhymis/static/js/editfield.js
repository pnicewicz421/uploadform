$(document).ready(function() {
    console.log('ready!');  
 
 <!--Process the Edit click event
 
    $('.edit').click(function() {
        
        <!-- only generate an inline row if one isn's there already
        if ($('.trowReplaced').length === 0) {
            <!-- find the parent row
            var parentTr = $(this).parents('.trow');
        
            <!-- find the selector of each td
            var dateTd = $('.date', parentTr);
            var locationTd = $('.location', parentTr);
            var staffTd = $('.staff', parentTr);
            var youthTd = $('.youth', parentTr);
            var notesTd = $('.notes', parentTr);
        
            <!-- find the selector of each text
            var dateText = $('a', dateTd);
            var locationText = $('a', locationTd);
            var staffText = $('a', staffTd);
            var youthText = $('a', youthTd);
            
            
            var formElement = $("<form>", {method:"POST", action:"/records/new/process", class:"trowReplaced"});
            var dateRow = $("<td>", {class:"date"});
            var dateElement = $("<input>", {type:"text", name:"date_text", id:"id_date", value:dateText.html()});
            var locationRow = $("<td>", {class:"location"});
            var locationElement = $("<input>", {type:"text", name:"location_text", id:"id_location", value:locationText.html()});
            var staffRow = $("<td>", {class:"staff"});
            var staffElement = $("<input>", {type:"text", name:"staff_text", id:"staff_location", value:staffText.html()});
            var youthRow = $("<td>", {class:"youth"});
            var youthElement = $("<input>", {type:"text", name:"youth_text", id:"id_youth", value:youthText.html()});
            var notesRow = $("<td>", {class:"notes"});
            var notesElement = $("<input>", {type:"text", name:"notes_text", id:"id_notes", value:notesTd.html()});
            var submitRow = $("<td>", {class:"submit"});
            var submitElement = $("<input>", {type:"submit", name:"submit", id:"id_submit", value:"Save"});
           <!-- var Token = $("{% csrf_token %}");
            
           console.log("Here is the original code:")
           console.log(parentTr.html())
            
           parentTr.html(formElement);
           dateRow.appendTo(formElement);
           dateElement.appendTo(dateRow);
           <!--dateText.html().appendTo(dateElement);
           locationRow.insertAfter(dateRow);
            locationElement.appendTo(locationRow);
            staffRow.insertAfter(locationRow);
           staffElement.appendTo(staffRow);
            youthRow.insertAfter(staffRow);
             youthElement.appendTo(youthRow);
               notesRow.insertAfter(youthRow);
                notesElement.appendTo(notesRow);
                submitRow.insertAfter(notesRow);
                submitElement.appendTo(submitRow);
              <!-- Token.insertAfter(submitRow);
            
            <!-- replace each td with a textbox and populate text
            
            $('td', parentTr).each(function(){
               console.log($(this).className)
               <!--replaceWith('<input type="text" value="' + $(this).html() + '">');
              });
                
          
            console.log(parentTr.html())
            
           <!-- <tr class=\"trowReplaced\">
           
          <!--  parentTr.html('<form method="POST" action="/records/new/process" class="trowReplaced"><td><input name="date_time_text" id="id_date_time" value="' + dateText.html() + '"></td></form>');
            <!--parentTr.html(textHtml);
            
     
                           <!--    <td><input name="location_text" id="id_location" value="' + locationText.html() + '"/></td>\
                           <!--    <td><input name="staff_text" id="id_staff" value="' + staffText.html() + '"/></td>\
                           <!--    <td><input name="youth_name_text" id="id_youth_name" value="' + youthText.html() + '"/></td>\
                           <!--    <td><input name="notes_text" id="id_notes\" value="' + notesTd.text() + '"/></td>\
                              <!-- <td><input type="submit" value="Save" id="id_submit" /></td>{% csrf_token %}</form>');
          <!--  console.log(parentTr.html())
        
            <!-- remove the addnewValue fields on the bottom
            $('#addNewValue').remove()
            }
            
            <!-- Submit function where post data will be processed and saved to the model
            <!-- using AJAX
            
            $('#id_submit').click(function(event){
                event.preventDefault();
                console.log("form submitted!")
                create_post();
                
            });
        
        });
        
    
});