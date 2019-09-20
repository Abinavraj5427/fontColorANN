<?php
    function predict($name){
        echo shell_exec("python fontANN.py");
    }
?>