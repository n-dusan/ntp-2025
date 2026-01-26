fn main() {
    let mut s = String::new();

    let update_string = |str| s.push_str(str);

    exec(update_string);

    println!("{:?}",s);
}

// Popuni prazninu
fn exec<'a, F: ___>(mut f: F)  {
    f("hello")
}
