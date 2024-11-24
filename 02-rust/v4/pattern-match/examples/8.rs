// Ispravi grešku u kodu.
fn main() {
    let s = String::from("hello, world!");

    match s {
        val => println!("The value of the string is {:?}", val),
    }
    print!("The value of the after match is {}", s);
}