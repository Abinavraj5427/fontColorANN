<?php
    function predict(){
        $RGB = $_REQUEST["q"];
        $R = explode('-', $RGB,0);
        $G = explode('-', $RGB,1);
        $B = explode('-', $RGB,2)
        
        echo "<script>console.log("$R")</script>";
        echo shell_exec("python -c from fontANN.py import *; print predict("+R+","+G+","+B+")");
    }
?>