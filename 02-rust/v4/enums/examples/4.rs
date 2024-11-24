
// Ispravi grešku u kodu i popuni praznine.
fn main() {
    let five = Some(5);
    let six = plus_one(five);
    let none = plus_one(None);

    if let ___ = six {
        println!("{}", n);

        println!("Success!");
    }
        
    panic!("Add some code above to prevent this line from running!");
} 

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        __ => None,
        __ => Some(i + 1),
    }
}