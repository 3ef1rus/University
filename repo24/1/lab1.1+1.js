function checkAge1(age) {
  return (age > 18) ? true : confirm('Родители разрешили?');
}

function checkAge2(age) {
  let result = age > 18 || confirm('Родители разрешили?');
  return result;
}

let age = prompt('Сколько вам лет ?');
//checkAge1(age);
checkAge2(age);