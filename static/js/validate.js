/**
 * Created by naveen sai kiran on 01-08-2016.
 */
// function to submit score
$(document).ready(function(){
    function show_result(count,total)
    {
        $("#count").text(count);
        $("#total").text(total);
        $("#score").slideDown();
    }

    function test(data,count)
    {
        j = 1;
        $(".select-option").click(function(){
			$(".glyphicon-ok").attr("class","glyphicon glyphicon-unchecked");
			$(this).find(".glyphicon").attr("class","glyphicon glyphicon-ok");
            $("#option-answer").val($(this).find(".option").text());
		});
        $("#verify").click(function(){
            $(".list-group").toggleClass("disabled"); // disabled click on choices
            $("#verify").toggleClass("disabled"); // disabled click on verify
            $(".before").hide();
            $(".after").show();
            if($("#option-answer").val() == data[j-1].answer)
            {
                $(".after-ok").show();
            }
            else{
                $(".after-not-ok").show();
            }
        });
        $("#after").click(function(){
            if($(".list-group").hasClass("disabled")){
                $(".list-group").toggleClass("disabled"); // enable click on choices
                $("#verify").toggleClass("disabled"); // enable click on verify
            }
            if($("#option-answer").val() == data[j-1].answer)
                count++;
            if(j >= data.length)
            {
                $(".after").hide();
                $(".after-ok").hide();
                $(".after-not-ok").hide();
                $(".glyphicon-ok").attr("class","glyphicon glyphicon-unchecked");
                $(".before").show();
                $("#question-display").hide();
                show_result(count,data.length);
                return;
            }
            $(".question-place").html(data[j].question);
            $(".option1-place").html(data[j].option1);
            $(".option2-place").html(data[j].option2);
            $(".option3-place").html(data[j].option3);
            $(".option4-place").html(data[j].option4);
            $(".after").hide();
            $(".after-ok").hide();
            $(".after-not-ok").hide();
            $(".glyphicon-ok").attr("class","glyphicon glyphicon-unchecked");
            $(".before").show();
            j++;
        });
    }
    $("#exam_list").on('click','.exam-panel',function(){
            $("#exam_list").hide();
            exam_id = $(this).find(".exam_template").attr('id');
            
            $.get("/quiz/api/question/",function(data,status){
                var i;
               // alert("hello");
                data2 = [];
               for(i=0;i<data.length;i++)
               {
                   if(data[i].exam == exam_id)
                   {
                       //console.log(data[i].exam+' '+exam_id);
                       data2.push(data[i]);
                   }
               }
                i=0;
                //alert(data);
                data = data2;
                //console.log(data.length);
                if (data.length == 0 ) {
                    $("#no-questions").show();
                    return;
                }
                $("#question-display").show();
                //alert(questions);
                $(".question-place").html(data[i].question);
                $(".option1-place").html(data[i].option1);
                $(".option2-place").html(data[i].option2);
                $(".option3-place").html(data[i].option3);
                $(".option4-place").html(data[i].option4);
                test(data,0);
            });
    });
    
    $(".exit-btn").click(function(){
        count = $('#count').text();
        total = $('#total').text();
        nilaimu = parseInt(count)/parseInt(total) * 100;

        $("#test-score").attr("value", nilaimu);
        $("#test-name").attr("value", exam_id);
        $("#lulus").attr("value", "teguh");
        window.location.reload();
    });
});
