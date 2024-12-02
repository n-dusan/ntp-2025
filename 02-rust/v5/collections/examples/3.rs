// Izmeni sledeći kod tako da se ispiše: 
// 25
// 25
// 25
fn main() {
    let mut s = String::new();

    println!("{}", s.capacity());

    for _ in 0..2 {
        s.push_str("hello");
        println!("{}", s.capacity());
    }

    println!("Success!");
}
