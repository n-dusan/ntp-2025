//Ispravi grešku u kodu implementiranjem `Deref` osobine za `MyBox` strukturu.

struct MyBox<T>(T);

impl<T> MyBox<T> {
  fn new(x: T) -> MyBox<T> {
      MyBox(x)
  }
}


fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}