$('button').click(function(e) {
    e.preventDefault()
    var R = $("#R").val();
    var G = $("#G").val();
    var B = $("#B").val();
    $("#form").css("background-color", "rgb("+R+","+G+","+B+")");
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function(){
      if(this.readyState == 4 && this.status == 200){
        $("#text").css("color", this.responseText === 0? "white": "black");
      }
    }
    str = R+ "-"+G+"-"+B;
    xmlhttp.open("GET", "fontANN.php?q="+str, true);
    xmlhttp.send();
  });