$('button').click(function(e) {
    e.preventDefault()
    var R = $("#R").val();
    var G = $("#G").val();
    var B = $("#B").val();
    $("#form").css("background-color", "rgb("+R+","+G+","+B+")");
    $.ajax(
      {
        type: "POST",
        url: 'predict.php',
        data: {
          R,
          G,
          B
        },
        success: function(data){
          console.log(data);
          $("#text").css("color", data == 1? "white": "black");
        },
        error: function() {
          alert('There was some error performing the AJAX call!');
        }
      }
    )
    alert("DONE");
    
  });