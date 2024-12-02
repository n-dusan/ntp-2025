// Popuni praznine i ispravi greške u kodu.
// 1. Nemoj koristiti `to_string()`
// 2. Nemoj dodavati ili uklanjati redove
fn main() {
    let mut s: String = "hello, ";
    s.push_str("world".to_string());
    s.push(__);

    move_ownership(s);

    assert_eq!(s, "hello, world!");

    println!("Success!");
}

fn move_ownership(s: String) {
    println!("ownership of \"{}\" is moved here!", s)
}
