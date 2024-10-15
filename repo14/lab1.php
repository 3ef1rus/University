<?php
//https://www.online-ide.com/
//Вяль Иван
/*
19ит-1 15.11.2022
вапр
апро
*/

// задание 1

$a=0;
for ($i = 0; $i <= 25; $i++) {
     $a+=$i;
}
echo $a ."\n";
$b=0;
$y=0;
while($y<=25){
    $b+=$y;
    $y++;
}
echo $b;
// задание 2
echo "\nHello";

// задание 3

$x1=3;
$x2=5;
$x3=8;
echo "\n". $x1 ." ". $x2 ." ". $x3;
$sum=$x1+$x2+$x3;
echo "\n".$sum;
$result=2+6+2/5-1;
echo "\n".$result;
// задание 4

define("R1",41);
const R2= 33;
$sum=R1+R2;
echo "\n".$sum;

// задание 5

$arr1=array(1,2,3,4,5);
$arr2=array(6,7,8,9,10);
array_push($arr1,'element',12);
unset($arr2[0]);
echo "\n".$arr1[2]. $arr2[2];
echo "\n".$arr1[2]. $arr2[2];
echo "\n";
print_r($arr1);
echo "\n";
print_r($arr2);
echo "\n".count($arr1)." и " . count($arr2);
$str1="“Доброе утро”,";
$str2="“дамы”,";
$str3="“и господа”.";
echo "\n".$str1 . $str2 . $str3 ;

