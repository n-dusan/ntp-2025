fn main() {
    let mut s = String::from("hello, ");

    let r1 = &mut s;
    let r2 = &mut s;

    // Dodaj red u kodu da bi se ispisala greška pri kompajliranju: cannot borrow `s` as mutable more than once at a time
    // You can't use r1 and r2 at the same time.
}
