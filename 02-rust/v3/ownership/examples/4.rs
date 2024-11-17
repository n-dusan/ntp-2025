// Ispravi greške u kodu bez izmene koda u main-u
fn main() {
    let s = give_ownership();
    println!("{}", s);
}

fn give_ownership() -> String {
    let s = String::from("hello, world");
    // Convert String to Vec
    let _s = s.into_bytes();
    s
}