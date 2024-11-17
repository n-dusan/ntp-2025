
//  Ispravi grešku u kodu.
fn main() {
    let mut s = String::from("hello world");

    // &s je tipa `&String`, ali funkcija `first_word` očekuje parametar tipa `&str`.
    // Ovo funkcioniše jer se `&String` implicitno konvertuje u `&str. Ovakav tip konverzije se naziva `Deref coercion`. 
    let word = first_word(&s);

    s.clear(); // greška!

    println!("the first word is: {}", word);
}
fn first_word(s: &str) -> &str {
    &s[..1]
}