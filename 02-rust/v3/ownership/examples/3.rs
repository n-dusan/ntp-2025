// Ispravi greške u kodu bez izmene koda u main-u
fn main() {
    let s1 = String::from("hello, world");
    let s2 = take_ownership(s1);

    println!("{}", s2);
}

fn take_ownership(s: String) {
    println!("{}", s);
}