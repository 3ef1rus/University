open System
//задание 1
let func1(a,b,c,d,e)=
    let result=(a,b,c,d,e)
    printfn"Кортеж равен = %A" result
    
let func2(a,b)(c,d)(e)=
    let result=(a,b,c,d,e)
    printfn"Кортеж равен = %A" result

let corfun = func2(1,"sdfg")(123.123,"sqqa234")("zxc")


// задание 2
let rec func4(result) =
    printfn"Введите число : "
    let a=Console.ReadLine() |> string

    if a<>"" then 
        func4(result+Convert.ToInt32(a)) 
    else printfn "Конец , результат : %A" result


//задание 3

let rec func3(result) =
    printfn"Введите число : "
    let a=Console.ReadLine() |> string

    if a="" then 
        printfn "Конец , результат : %A" result
    else func3(result+Convert.ToInt32(a)) 

// задание 4

//Определение рекурсивной функции
let rec State1(x:int) =
 printfn "%i - (+1) %i" x (x+1)
 let x_next = x+1
 if x_next>3 then State2(x_next)
 else State1(x_next)
 //ключевое слово and объявляет функцию
 //как взаимно-рекурсивную к предыдущей
 //это необходимо так как функция
 //State1 ссылается на State2 и F#
 //не допускает опережающего описания
and State2(x:int) =
 printfn "%i - (^2) %i" x (x*x)
 let x_next = x+1
 if x_next>6 then State3(x_next)
 else State2(x_next)
and State3(x:int) =
 printfn "%i - (^3) %i" x (x*x*x)
 let x_next = x+1
 if x_next<=10 then State3(x_next)
 //Вызов с начальным условием
 
 //задание 5

let func6(a,b,func: int*int->int)=func(a,b)






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
     let result=0;

     func1(12,'g',123.12,"ghjk","ghjk")
     func3(result)
     State1(1)
     let zd5 = func6(1,2,fun(a,b)->a+b)
     Console.ReadLine() |> ignore
     0 // возвращение целочисленного кода выхода


