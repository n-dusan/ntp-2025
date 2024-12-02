
// Rekurzivni tip koji implementiramo je `cons` lista. 
// Predstavlja popularnu strukturu podataka u funkcionalnom programiranju koja sadrži uređen par od dva elementa. 
// Prvi element je trenutna vrednost, dok drugi element predstavlja vrednost sledećeg elementa, odnosno ostatak liste.
// Poslednja vrednost `Nil` označava kraj liste.

// Ispravi greške u kodu i implementiraj todo!().

// 1. Koristi `Box` u definiciji enumeracije kako bi se kod kompajlirao.
// 2. Implementiraj todo!() za praznu i popunjenu `cons` listu

// Više detalja o cons listi na: https://en.wikipedia.org/wiki/Cons
// Box: https://doc.rust-lang.org/rust-by-example/std/box.html

#[derive(PartialEq, Debug)]
pub enum List {
    Cons(i32, List),
    Nil,
}

fn main() {
    println!("This is an empty cons list: {:?}", create_empty_list());
    println!(
        "This is a non-empty cons list: {:?}",
        create_non_empty_list()
    );
}

pub fn create_empty_list() -> List {
    todo!()
}

pub fn create_non_empty_list() -> List {
    todo!()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_create_empty_list() {
        assert_eq!(List::Nil, create_empty_list())
    }

    #[test]
    fn test_create_non_empty_list() {
        assert_ne!(create_empty_list(), create_non_empty_list())
    }
}