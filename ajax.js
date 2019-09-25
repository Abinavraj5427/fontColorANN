$('button').click(function(e) {
    e.preventDefault()
    var R = $("#R").val();
    var G = $("#G").val();
    var B = $("#B").val();
    $("#form").css("background-color", "rgb("+R+","+G+","+B+")");
    str = R+ "-"+G+"-"+B;
    $.ajax(
      {
        type: "POST",
        url: 'request_ajax_data.php',
        data: str,
      },
      {
        success: function(data){
          $("#text").css("color", data === 0? "white": "black");
        },
        error: function() {
          alert('There was some error performing the AJAX call!');
        }
      }
    )
    
  });