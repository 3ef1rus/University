function count() {
  a = prompt('Введите число')
  return a % 2 != 0 ? a : count();
}

alert(count());