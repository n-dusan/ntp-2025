
fn main() {
    let o = Some(7);

    // Iskoristi `if let` sintaksu umesto `match` bloka. 
    match o {
        Some(i) => {
            println!("This is a really long string and `{:?}`", i);

            println!("Success!");
        }
        _ => {}
    };
}