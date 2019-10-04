<?php
        $R = $_POST["R"];
        $G = $_POST["G"];
        $B = $_POST["B"];
        $command = "py -c 'from fontANN import nada; print(nada())'";
        $res = shell_exec($command);
        echo $res

?>