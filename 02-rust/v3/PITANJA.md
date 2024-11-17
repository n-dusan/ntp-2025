# V3 - Programski jezik Rust

## Vlasništvo i pozajmljivanje

1. Šta predstavlja vlasništvo u programskom jeziku Rust?
2. Koja su tri pravila vlasništva?
3. Koji je opseg važenja varijable?
4. Da li je string literal (`str`) podrazumevano promenljiv ili nepromenjiv?
5. Da li su varijable tipa `String` promenljive ili nepromenjive?
6. U kom trenutku se navedeni String briše iz memorije?

    ```rust
    {
        let s = String::from("hello"); // s is valid from this point forward

        // do stuff with s
    }      
    ```

7. Za šta služi ugrađena funkcija `drop` u Rust-u?
8. Koja je interna organizacija `String` objekta? Šta se čuva na steku, a šta se čuva na hipu?
9. Koja je razlika između plitkog kopiranja (Eng. shallow-copy) i dubokog kopiranja (Eng. deep-copy)?
10. Pri dodeli `let s2 = s1`, da li programski jezik Rust obavlja plitko kopiranje, duboko kopiranje ili nešto treće?
11. U kontekstu vlasništva, šta predstavlja pojam premeštanja varijabli?
12. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn main() {
        let s1 = String::from("hello");
        let s2 = s1;

        println!("{}, world!", s1);
      }
    ```

13. Koja je uloga `Copy` osobine (Eng. trait)?
14. Koji tipovi mogu da implementiraju `Copy` osobinu? Upotpuni odgovor sa primerom.
15. Da li referenca ima vlasništvo nad objektom koji pokazuje?
16. Šta predstavlja pojam pozajmljivanja?
17. Da li su reference podrazumevano nepromenjive?
18. Da li referenca može da bude promenljiva?
19. Koliko promenljivih referenci na isti objekat može da postoji u istom opsegu? Zašto?
20. Pod kojim uslovima se dešava trka do podataka?
21. Da li mogu da postoje promenljiva i nepromenjiva referenca u istom opsegu u isto vreme?
22. Da li je naredni isečak koda ispravan?

    ```rust
    fn main() {
      let mut s = String::from("hello");

      let r1 = &s;
      let r2 = &s;
      println!("{} and {}", r1, r2);

      let r3 = &mut s;
      println!("{}", r3);
    }
    ```

23. Koji je opseg (vreme života) reference?
24. Šta predstavlja viseći pokazivač (referenca) (Eng. dangling pointer)?
25. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
      let reference_to_nothing = dangle();
    }

    fn dangle() -> &String {
        let s = String::from("hello");

        &s
    }
    ```

26. Da li je sledeća tvrdnja tačna? *U svakom trenutku možemo imati ili jednu promenjivu ili proizvoljan broj nepromenjivih referenci*
27. Šta predstavlja isečak (Eng. slice)?
28. Na koji način kreiramo string isečak?
29. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn first_word(s: &String) -> &str {
      let bytes = s.as_bytes();

      for (i, &item) in bytes.iter().enumerate() {
          if item == b' ' {
              return &s[0..i];
          }
      }

      &s[..]
    }

    fn main() {
        let mut s = String::from("hello world");

        let word = first_word(&s);

        s.clear();

        println!("the first word is: {}", word);
    }
    ```

30. Da li string literali predstavljaju string isečke? Ukoliko jesu, da li su promenljivi ili nepromenjivi?
31. Odredi tip isečka u sledećem kodu:

    ```rust
    let a = [1, 2, 3, 4, 5];

    let slice = &a[1..3];
    ```

32. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn first_word(s: &str) -> &str {
      let bytes = s.as_bytes();

      for (i, &item) in bytes.iter().enumerate() {
          if item == b' ' {
              return &s[0..i];
          }
      }

      &s[..]
    }

    fn main() {
        let my_string = String::from("hello world");

        let word = first_word(&my_string[0..6]);
        let word = first_word(&my_string[..]);

        let word = first_word(&my_string);

        let my_string_literal = "hello world";

        let word = first_word(&my_string_literal[0..6]);
        let word = first_word(&my_string_literal[..]);

        let word = first_word(my_string_literal);
    }
    ```

33. Ispravi greške u sledećem kodu:

    ```rust
    fn main() {
      let s = String::from("hello");  // s comes into scope

      takes_ownership(s);             
      println!("{}", s);

      let x = 5;                      

      makes_copy(x);   
      
      println!("{}", x)
    } 

    fn takes_ownership(some_string: String) {
        println!("{}", some_string);
    } 
    fn makes_copy(some_integer: i32) {
        println!("{}", some_integer);
    }
    ```

34. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn main() {
      let s1 = gives_ownership(); 

      let s2 = String::from("hello");

      let s3 = takes_and_gives_back(s2);
    }

    fn gives_ownership() -> String {
        let some_string = String::from("yours");

        some_string 
    }

    fn takes_and_gives_back(a_string: String) -> String {
        a_string
    }
    ```