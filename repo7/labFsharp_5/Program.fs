type Maybe<'a> =
    | Just of 'a
    | Nothing
//простой фанктор это такая штука которая применяет функцию к контексту другой функции
let fmapMaybe f p =
     match p with
     | Just a -> Just (f a)
     | Nothing -> Nothing
// апликативный фанктор применяет функцию которая содержится в контексте к значению которое содержится в контексте
let applyMaybe lf p =
     match lf,p with
     | Just f,Just a -> Just (f a)
     | _ -> Nothing

// Монада. К поднятому значению применяется функция от обычного аргумента, возвращающая поднятое значение (поднятое - взятое из контекста)











let Just2 =Just 2
let add1 x = x + 1 
let add1IfSomething = fmapMaybe add1 Just2 //обычный фанктор
let am1 = applyMaybe (Just (add1)) (Just2)
 
printfn"Функтор = %A" add1IfSomething
printfn"апликативный Функтор = %A" am1