// Ispravi grešku u kodu i popuni praznine.
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
    let msg = Message::Move{x: 1, y: 2};

    if let Message::Move{__} = msg {
        assert_eq!(a, b);
    } else {
        panic!("Ne dozvoli da se ova sekcija izvrši！");
    }

    println!("Success!");
} 
