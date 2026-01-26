// Ispravi grešku u kodu sa minimalnim izmenama.
fn main() {
    let color = String::from("green");

    let print = move || println!("`color`: {}", color);

    let _reborrow = &color;

    println!("{}", color);
}
