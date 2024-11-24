//Popuni prazninu kako bi se struktura mogla ispisati na ekran.
#[__]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
        width: dbg!(30 * scale), // Ispiši debug info i dodeli vrednost `30 * scale` na atribut `width`
        height: 50,
    };

    dbg!(&rect1); // Ispiši debug info

    println!(__, rect1); // Ispiši debug info na stdout
}
