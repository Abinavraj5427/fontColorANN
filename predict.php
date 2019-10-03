<?php
        $R = $_POST["R"];
        $G = $_POST["G"];
        $B = $_POST["B"];
        $command = "py -c 'from fontANN import predict; print(predict($R,$G,$B))'";
        $res = shell_exec($command);
        echo $command

?>