use std::num::ParseIntError;

// Zbog izmenjenog povratnog tipa funkcije, možemo koristiti 'match' izraz bez `unwrap()`.
fn multiply(n1_str: &str, n2_str: &str) -> Result<i32, ParseIntError> {
    match n1_str.parse::<i32>() {
        Ok(n1)  => {
            match n2_str.parse::<i32>() {
                Ok(n2)  => {
                    Ok(n1 * n2)
                },
                Err(e) => Err(e),
            }
        },
        Err(e) => Err(e),
    }
}

// Prepiši `multiply` da bude kraći i jednostavniji
// Trebali bismo da koristimo `and_then` i `map` ovde.
fn multiply1(n1_str: &str, n2_str: &str) -> Result<i32, ParseIntError> {
    // IMPLEMENT...
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {

    let twenty = multiply1("10", "2");
    print(twenty);

    let tt = multiply("t", "2");
    print(tt);

    println!("Success!");
}
