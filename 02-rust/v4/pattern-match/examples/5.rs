
fn main() {}
// Simbol | se koristi za podudaranje više vrednosti, dok se ..= koristi za podudaranje inkluzivnog opsega.
fn match_number(n: i32) {
    match n {
        // Podudaranje jedne vrednosti
        1 => println!("One!"),
        // Popuni prazninu sa `|`
        __ => println!("match 2 -> 5"),
        // Podudaranje inkluzivnog opsega
        6..=10 => {
            println!("match 6 -> 10")
        },
        _ => {
            println!("match -infinite -> 0 or 11 -> +infinite")
        }
    }
}
