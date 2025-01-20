<?php
#the php
$food = array("sushi", "pizza", "burger", "chips", "chocolate");
$ans = readline("your food ");
if (in_array($ans, $food)) {
    echo "i know $ans!";
} else {
    echo "WHAT THE HECK IS THAT ($ans)";
}
?>
