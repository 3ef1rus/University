function stroka() {
  a = prompt('Введите число')
  return Number(a) == a ? a : stroka();
}
alert(stroka());