open System
//задание 1
let func1(a,b,c)=
    let result=(a+1,b+1.0,c+" ")
    printfn"Кортеж равен = %A" result
 



// задание 2
let funcSum(a,b,c)= 
    let result =a+b+c
    printfn"Кортеж равен = %A" result

let funcGen(a,b,c,funcSum)= funcSum(a,b,c)
let funcint(a,b,c)= funcGen(a,b,c,fun(a,b,c)->a+b+c)
let funcfloat(a,b,c)= funcGen(a,b,c,fun(a,b,c)->a+b+c+0.0)
let funcStr(a,b,c)= funcGen(a,b,c,fun(a,b,c)->a+b+c+" ")  


//задание 3

let func3() =
    let list = [for x in [1..10] do if x%2=0 then yield (x,x*x,x*x*x) ]
    printfn"Кортежи из списка %A" list
     


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


     let sumstr = funcStr("a","b","c")
     let sumfloat= funcfloat(1.1,2.2,3.3)
     let sumint = funcint(1,2,3)
     func3()             
     Console.ReadLine() |> ignore
     0 // возвращение целочисленного кода выхода

