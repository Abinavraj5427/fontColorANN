<?php
        $R = $_POST["R"];
        $G = $_POST["G"];
        $B = $_POST["B"];
        echo shell_exec("python -c from fontANN.py import *; print predict("+$R+","+$G+","+$B+")");
?>