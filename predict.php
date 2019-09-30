<?php
        $R = $_POST["R"];
        $G = $_POST["G"];
        $B = $_POST["B"];
        echo shell_exec("py -c 'from fontANN  import predict; print(predict("+$R+","+$G+","+$B+"))'");
?>