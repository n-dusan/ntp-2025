# V6 - Programski jezik Rust

## Paketi, moduli, obrada grešaka, testiranje

1. Iz kojih elemenata se sastoji Rust-ov sistem za module?
2. Šta je sanduk (Engl. Crate)?
3. Šta je binarni sanduk (Engl. Binary Crate)?
4. Šta je bibliotečki sanduk (Engl. Library Crate)?
5. Šta je koren (Engl. Root) sanduka?
6. Šta je paket (Engl. Package)?
7. Koliko binarnih ili bibliotečkih sanduka može da se nalazi u jednom paketu?
8. Šta je uobičajen koren za binarni sanduk? A za bibliotečki sanduk?
9. Gde se još binarni sanduci mogu nalaziti?
10. Koje konvencije bismo trebali da pratimo dok definišemo module (Engl. Modules) u sanducima?
11. Da li su moduli uobičajeno privatni?
12. Kako formiramo putanju do stavke (metoda ili funkcija) u stablu modula (Engl. Module Tree)?
13. Da li uobičajeno roditeljski modul (Engl. Parent Module) ima pristup sadržaju unutrašnjeg modula?
14. Pozovi funkciju `add_to_waitlist` uz pomoć apsolutne i relativne putanje na naznačenim mestima:

    ```rust
    mod front_of_house {
        mod hosting {
            fn add_to_waitlist() {}
        }
    }

    pub fn eat_at_restaurant() {
        // TODO: Apsolutna putanja

        // TODO: Relativna putanja
    }
    ```

15. Uzimajući u obzir prethodno pitanje, zašto može `eat_at_restaurant` da pristupi privatnom modulu `front_of_house`?
16. Za šta se koristi ključna reč `super`?
17. Ispravi grešku u sledećem kodu:

    ```rust
    mod back_of_house {
        pub struct Breakfast {
            pub toast: String,
            seasonal_fruit: String,
        }

        impl Breakfast {
            pub fn summer(toast: &str) -> Breakfast {
                Breakfast {
                    toast: String::from(toast),
                    seasonal_fruit: String::from("peaches"),
                }
            }
        }
    }

    pub fn eat_at_restaurant() {
        // Order a breakfast in the summer with Rye toast
        let mut meal = back_of_house::Breakfast::summer("Rye");
        // Change our mind about what bread we'd like
        meal.toast = String::from("Wheat");
        println!("I'd like {} toast please", meal.toast);

        meal.seasonal_fruit = String::from("blueberries");
    }

    fn main() {
        eat_at_restaurant();
    }
    ```

18. Zašto funkcija `summer` mora biti javna (Engl. Public)?
19. Ukoliko je enum javan, da li su i njegove varijacije javne? A strukture (Engl. Structs)?
20. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    mod front_of_house {
        pub mod hosting {
            pub fn add_to_waitlist() {}
        }
    }

    use crate::front_of_house::hosting;

    mod customer {
        pub fn eat_at_restaurant() {
            hosting::add_to_waitlist();
        }
    }
    ```

21. Navedi dva načina da se ispravi greška u sledećem isečku koda:

    ```rust
    mod front_of_house {
        pub mod hosting {
            pub fn add_to_waitlist() {}
        }
    }

    use crate::front_of_house::hosting;

    mod customer {
        pub fn eat_at_restaurant() {
            hosting::add_to_waitlist();
        }
    }

    fn main() {
        customer::eat_at_restaurant();
    }
    ```

22. Koji je proces ponovnog export-ovanja (Engl. Re-Export) imena?
23. Kako dodajemo i koristimo spoljne pakete (Engl. External Package) kao zavisnosti (Engl. Dependency) u našem Rust projektu?
24. Šta je naziv sanduka standardne biblioteke (Engl. Standard Library)?
25. Prepiši sledeći isečak koda da bude koncizniji:

    ```rust
    use std::cmp::Ordering;
    use std::io;
    ```

26. Prepiši sledeći isečak koda da bude koncizniji:

    ```rust
    use std::io;
    use std::io::Write;
    ```

27. Koji tipovi grešaka su podržani u Rust programskom jeziku i kako se ponašaju?
28. Kako mozemo da izazovemo `panic` u Rust-u?
29. Šta je odmotavanje (Engl. unwinding) i kako se sprečava?
30. Da li se u sledećem isečku koda događa `panic`? Ukoliko da, kako možemo pokazati celokupni povratni trag (Engl. Backtrace)?

    ```rust
    fn main() {
        let v = vec![1, 2, 3];

        v[99];
    }
    ```

31. Ukoliko postoji, pokušaj otvoriti `hello.txt`, u suprotnom iskoristi `panic`. Reši problem koristeći `match`.
32. Reši prethodni problem pomoću leksičkog zatvaranja (Engl. Lexical Closure).
33. Isti problem reši koristeći `unwrap`.
34. Isti problem reši koristeći `expect`.
35. Šta je bolje koristiti: `unwrap` ili `expect`?
36. Sledeći isečak koda prepiši u kraći i ekvivalentan kod koristeći `?`. Nije dozvoljeno korišćenje `fs::read_to_string`.

    ```rust
    #![allow(unused)]
    fn main() {
        use std::fs::File;
        use std::io::{self, Read};

        fn read_username_from_file() -> Result<String, io::Error> {
            let username_file_result = File::open("hello.txt");

            let mut username_file = match username_file_result {
                Ok(file) => file,
                Err(e) => return Err(e),
            };

            let mut username = String::new();

            match username_file.read_to_string(&mut username) {
                Ok(_) => Ok(username),
                Err(e) => Err(e),
            }
        }
    }
    ```

37. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    use std::fs::File;

    fn main() {
        let greeting_file = File::open("hello.txt")?;
    }
    ```

38. Šta može biti povratni tip main funkcije?
39. Podseti se igre pogađanja brojeva [na sledećem linku](https://doc.rust-lang.org/book/ch02-00-guessing-game-tutorial.html). Izmeni kod da takođe proverava da li je korisnikov unos u rasponu [1, 100]. Ovu proveru uradi tako što napišeš svoju `Guess` strukturu sa konstruktorom koji izaziva `panic` ukoliko vrednost nije u očekivanom rasponu.
