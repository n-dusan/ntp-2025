# V2 - Programski jezik Rust

## Osnovni programski koncepti

1. Da li su varijable podrazumevano promenljive?
2. Popravi greške pri kompajliranju sledećeg koda:

```rust
fn main() {
    let x = 5;
    println!("The value of x is: {x}");
    x = 6;
    println!("The value of x is: {x}");
}
```

3. Koje su glavne razlike između konstanti i nepromenljivih varijabli?
4. Šta predstavlja životni opseg konstante?
5. Odredi rezultat izvršavanja sledećeg koda:

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

6. Koja je razlika između senčenja promenljivih (Engl. Shadowing) i promenljivosti?
7. Da li je Rust statički ili dinamički tipiziran jezik?
8. Da li sledeći kod proizvodi grešku? Ukoliko da, ispravi je.

```rust
let guess = "42".parse().expect("Not a number!");
```

9. Koja je veličina `isize` i `usize` tipova?
10. Da li je `57u8` validna vrednost?
11. Napredno pitanje: Kako se Rust ponaša u slučaju prelivanja vrednosti broja (Engl. Integer Overflow) [Integer Overflow](https://en.wikipedia.org/wiki/Integer_overflow)?
12. Koja je veličina `bool` tipa? Koja je veličina `char` tipa?
13. Koji su primitivni složeni (Engl. compound) tipovi?
14. Gde se nizovi alociraju u memoriji?
15. Šta su elementi iskaza `let a = [3; 5];`? Šta predstavljaju `3` i `5`?
16. Šta je ulazna tačka za Rust program?
17. Šta znači kada se za Rust tvrdi da je jezik baziran na izrazima (Engl. Expression-based)?
18. Da li opseg predstavlja izraz? Upotpuni odgovor sa primerom.
19. Za šta služi `;`?
20. Da li je sledeća definicija validna?

```rust
fn five() -> i32 {
  5
}
```

21. Šta je rezultat izvršavanja sledećeg koda?

```rust
fn main() {
    let x = plus_one(5);

    println!("The value of x is: {x}");
}

fn plus_one(x: i32) -> i32 {
    x + 1;
}
```

22. Šta su linijski komentari u Rust-u?
23. Šta predstavljaju "ruke" (Engl. arms) u Rust-u?
24. Šta je rezultat izvršavanja sledećeg koda?

```rust
fn main() {
    let number = 3;

    if number {
        println!("number was three");
    }
}
```

25. Da li ključna reč `if` prestavlja izraz u Rust-u?
26. Šta je rezultat izvršavanja sledećeg koda?

```rust
fn main() {
    let condition = true;

    let number = if condition { 5 } else { "six" };

    println!("The value of number is: {number}");
}
```

27. Šta je rezultat izvršavanja sledećeg koda?

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}
```

28. Za svaki `break` iskaz navedi koja je sledeća linija u toku izvršavanja.

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```
