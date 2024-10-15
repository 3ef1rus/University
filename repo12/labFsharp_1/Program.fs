open System

let sum1(a:double, b:double,c:double):unit =
 //создание временной переменной
 let D = b*b-4.0*a*c
 if D = 0.0 then 

  let result = -b / (2.0 * a)

  printf "Один корень %A \n" result
 else if D<0.0 then
  printf "Нету корней \n"
 else if D>0.0 then
  let x1= (-b + Math.Sqrt(D))/(2.0 * a)
  let x2= (-b - Math.Sqrt(D))/(2.0 * a)

  printf"Два кореня %A и %A \n" x1 x2

[<EntryPoint>]
 let main argv =

     let a1 = 1.0;
     let b1 = 0.0;
     let c1 = -4.0;
     //1 корень
     let a2 = 1.0;
     let b2 = 0.0;
     let c2 = 0.0;
     //нет корней
     let a3 = 1.0;
     let b3 = 0.0;
     let c3 = 4.0;

     sum1(a1,b1,c1)
     sum1(a2,b2,c2)
     sum1(a3,b3,c3)

     Console.ReadLine() |> ignore
     0 // возвращение целочисленного кода выхода



