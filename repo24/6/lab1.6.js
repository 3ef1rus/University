function mas() {
  let a = Array.from({
    length: 10
  }, () => Math.floor(Math.random() * 20));
  alert(a);
  for (let key of a) {
    if (key % 2 == 0 && key != 0) {
      alert(key);
    }
  }
}

mas();