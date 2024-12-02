# V5 - Programski jezik Rust

## Pametni pointeri, kolekcije

1. Šta predstavlja pointer?
2. Koja je najčešća vrsta pointera u Rust-u?
3. Šta predstavlja pametni pointer (Engl. smart pointer)?
4. Koja je glavna razlika između pametnog pointera i reference?
5. Da li su `String` i `Vec<T>` pametni pointeri?
6. Preko čega se pametni pointeri obično implementiraju?
7. Šta predstavlja `Box<T>`?
8. U kojim situacijama se koristi `Box<T>`?
9. Da li sledeći kod proizvodi grešku? Zašto? Više detalja o `Cons` listi na sledećem [linku](https://doc.rust-lang.org/book/ch15-01-box.html#more-information-about-the-cons-list).

    ```rust
    enum List {
        Cons(i32, List),
        Nil,
    }

    use crate::List::{Cons, Nil};

    fn main() {
        let list = Cons(1, Cons(2, Cons(3, Nil)));
    }
    ```

10. Ispravi grešku u prethodnom kodu upotrebom `Box<T>`.
11. Koja je uloga `Deref` osobine?
12. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
        let x = 5;
        let y = &x;

        assert_eq!(5, x);
        assert_eq!(5, y);
    }
    ```

13. Koja je razlika između prethodnog koda i sledećeg koda?

    ```rust
    fn main() {
        let x = 5;
        let y = Box::new(x);

        assert_eq!(5, x);
        assert_eq!(5, *y);
    }
    ```

14. Šta predstavlja `struct MyBox<T>(T);`?
15. Ispravi grešku u sledećem kodu implementiranjem `Deref` osobine:

    ```rust
    struct MyBox<T>(T);

    impl<T> MyBox<T> {
        fn new(x: T) -> MyBox<T> {
            MyBox(x)
        }
    }


    fn main() {
        let x = 5;
        let y = MyBox::new(x);

        assert_eq!(5, x);
        assert_eq!(5, *y);
    }
    ```

16. Šta predstavlja `Deref` koercija?
17. Pojednostavi poziv `hello` funkcije u sledećem kodu:

    ```rust
    struct MyBox<T>(T);

    impl<T> MyBox<T> {
        fn new(x: T) -> MyBox<T> {
            MyBox(x)
        }
    }

    use std::ops::Deref;

    impl<T> Deref for MyBox<T> {
        type Target = T;

        fn deref(&self) -> &Self::Target {
            &self.0
        }
    }

    fn hello(name: &str) {
        println!("Hello, {name}!");
    }

    fn main() {
        let m = MyBox::new(String::from("Rust"));
        hello(&(*m)[..]);
    }
    ```

18. Kako se `Deref` koercija odnosi prema promenljivositi (Eng. mutability)? Za više informacija pročitati sledeću [sekciju](https://doc.rust-lang.org/book/ch15-02-deref.html#how-deref-coercion-interacts-with-mutability) knjige.
19. Koja je uloga `Drop` osobine?
20. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    struct CustomSmartPointer {
        data: String,
    }

    impl Drop for CustomSmartPointer {
        fn drop(&mut self) {
            println!("Dropping CustomSmartPointer with data `{}`!", self.data);
        }
    }

    fn main() {
        let c = CustomSmartPointer {
            data: String::from("my stuff"),
        };
        let d = CustomSmartPointer {
            data: String::from("other stuff"),
        };
        println!("CustomSmartPointers created.");
    }
    ```

21. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    struct CustomSmartPointer {
        data: String,
    }

    impl Drop for CustomSmartPointer {
        fn drop(&mut self) {
            println!("Dropping CustomSmartPointer with data `{}`!", self.data);
        }
    }

    fn main() {
        let c = CustomSmartPointer {
            data: String::from("my stuff"),
        };
        let d = CustomSmartPointer {
            data: String::from("other stuff"),
        };
        drop(d);
        println!("CustomSmartPointers created.");
    }
    ```

22. Da li postoji deljeno vlasništvo u Rust-u? Ako postoji, kako se realizuje?
23. Da li je `Rc<T>` siguran u kontekstu niti (Engl. threadsafe)?
24. Da li `Rc::clone` obavlja duboko kopiranje vrednosti?
25. Da li `Rc<T>` dozvoljava deljenim vlasnicima da dele i promenljive (Engl. mutable) reference?
26. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    enum List {
        Cons(i32, Rc<List>),
        Nil,
    }

    use crate::List::{Cons, Nil};
    use std::rc::Rc;

    fn main() {
        let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
        println!("count after creating a = {}", Rc::strong_count(&a));
        let b = Cons(3, Rc::clone(&a));
        println!("count after creating b = {}", Rc::strong_count(&a));
        {
            let c = Cons(4, Rc::clone(&a));
            println!("count after creating c = {}", Rc::strong_count(&a));
        }
        println!("count after c goes out of scope = {}", Rc::strong_count(&a));
    }
    ```

27. U kom delu memorije se čuvaju ugrađeni nizovi i torke?
28. U kom delu memorije se čuvaju elementi kolekcije, poput vektora i heš mape?
29. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
    let v = Vec::new();
    }
    ```

30. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
    let v = Vec::new();

    v.push(5);
    v.push(6);
    v.push(7);
    v.push(8);
    }
    ```

31. Koji je rezultat izvršavanja sledećeg koda? Zašto? Ukoliko program proizvodi grešku, izmeni kod tako da se uspešno izvrši.

    ```rust
    fn main() {
        let v = vec![1, 2, 3, 4, 5];
        
        let does_not_exist = &v[100];
    }
    ```

32. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
    let mut v = vec![1, 2, 3, 4, 5];

    let first = &v[0];

    v.push(6);

    println!("The first element is: {first}");
    }
    ```

33. Da li pravila vlasništva važe i u kontekstu vektora?
34. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
    let mut v = vec![100, 32, 57];
    for i in &v {
        i += 50;
    }
    }
    ```

35. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    n main() {
    let mut v = vec![100, 32, 57];
    for i in &mut v {
        *i += 50;
        v.push(55)
    }
    }
    ```

36. Da li je naredni isečak koda ispravan?

    ```rust
    fn main() {
    enum SpreadsheetCell {
        Int(i32),
        Float(f64),
        Text(String),
    }

    let row = vec![
        SpreadsheetCell::Int(3),
        SpreadsheetCell::Text(String::from("blue")),
        SpreadsheetCell::Float(10.12),
    ];
    }
    ```

37. U kom trenutku se elementi vektora oslobađaju iz memorije?
38. Koja je razlika između stringa tipa `String` i stringa tipa `str` (ili `&str`)?
39. Izmeni sledeći isečak koda koristeći `to_string` metodu nad string literalom:

    ```rust
    fn main() {
        let s = String::from("initial contents");
    }
    ```

40. Da li `push_str` uzima vlasništvo nad parametrom? Proveriti na sledećem primeru koda:

    ```rust
    fn main() {
        let mut s1 = String::from("foo");
        let s2 = "bar";
        s1.push_str(s2);
        println!("s2 is {s2}");
    }
    ```

41. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
        let s1 = String::from("Hello, ");
        let s2 = String::from("world!");
        let s3 = s1 + s2;
    }
    ```

42. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
        let s1 = String::from("Hello, ");
        let s2 = String::from("world!");
        let s3 = s1 + &s2;
        println!("{s1}, {s2}")
    }
    ```

43. Koji je rezultat izvršavanja sledećeg koda?

    ```rust
    fn main() {
        let s1 = String::from("tic");
        let s2 = String::from("tac");
        let s3 = String::from("toe");

        let s = format!("{s1}-{s2}-{s3}");
        println!("{s1}, {s2}, {s3}: {s}")
    }
    ```

44. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
        let s1 = String::from("hello");
        let h = s1[0];
    }
    ```

45. Koji je rezultat izvršavanja sledećeg koda?

    ```rust
    #![allow(unused)]
    fn main() {
        let hello = "Здравo";
        let s = &hello[0..4];
        println!("{s}")
    }
    ```

46. Da li sledeći kod proizvodi grešku?

    ```rust
    #![allow(unused)]
    fn main() {
        let hello = "Здравo";
        let s = &hello[0..1];
        println!("{s}")
    }
    ```

47. Koji su ispisi sledeća dva isečka koda?

    ```rust
    // Snippet 1
    #![allow(unused)]
    fn main() {
        for c in "Зд".chars() {
            println!("{c}");
        }
    }
    // Snippet 2
    #![allow(unused)]
    fn main() {
        for b in "Зд".bytes() {
            println!("{b}");
        }
    }
    ```

48. Koja je uloga `copied` i `unwrap_or` u sledećem kodu?

    ```rust
    fn main() {
        use std::collections::HashMap;

        let mut scores = HashMap::new();

        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Yellow"), 50);

        let team_name = String::from("Blue");
        let score = scores.get(&team_name).copied().unwrap_or(0);
    }  
    ```

49. Iteriraj kroz ključeve i vrednosti sledeće heš mape:

    ```rust
    fn main() {
        use std::collections::HashMap;

        let mut scores = HashMap::new();

        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Yellow"), 50);

        // TODO: Add code here
    }
    ```

50. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
        use std::collections::HashMap;

        let mut scores = HashMap::new();

        let blue = String::from("Blue");
        let ten = 10;
        let yellow = String::from("Yellow");
        let fifty = 50;

        scores.insert(blue, ten);
        scores.insert(yellow, fifty);

        println!("{blue}, {ten}; {yellow}, {fifty}")
    }
    ```

51. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn main() {
        use std::collections::HashMap;

        let mut scores = HashMap::new();

        scores.insert(String::from("Blue"), 10);
        scores.insert(String::from("Blue"), 25);

        println!("{:?}", scores);
    }
    ```

52. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn main() {
        use std::collections::HashMap;

        let mut scores = HashMap::new();
        scores.insert(String::from("Blue"), 10);

        scores.entry(String::from("Yellow")).or_insert(50);
        scores.entry(String::from("Blue")).or_insert(50);

        println!("{:?}", scores);
    }
    ```

53. U kojoj situaciji se poziva `or_insert` metoda nad `Entry` enumeracijom?
54. Odredi rezultat izvršavanja sledećeg koda:

    ```rust
    fn main() {
        use std::collections::HashMap;

        let text = "hello world wonderful world";

        let mut map = HashMap::new();

        for word in text.split_whitespace() {
            let count = map.entry(word).or_insert(0);
            *count += 1;
        }

        println!("{:?}", map);
    }
    ```
