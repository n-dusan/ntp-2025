# V7 - Programski jezik Rust

## Generički tipovi, osobine, životni vek

1. Umesto dve funkcije `largest_i32` i `largest_char`, napiši jednu funkciju koja podržava generičke tipove i pruža istu funkcionalnost u `main` metodi.

    ```rust
        fn largest_i32(list: &[i32]) -> &i32 {
        let mut largest = &list[0];

        for item in list {
            if item > largest {
                largest = item;
            }
        }

        largest
    }

    fn largest_char(list: &[char]) -> &char {
        let mut largest = &list[0];

        for item in list {
            if item > largest {
                largest = item;
            }
        }

        largest
    }

    fn main() {
        let number_list = vec![34, 50, 25, 100, 65];

        let result = largest_i32(&number_list);
        println!("The largest number is {}", result);
        assert_eq!(*result, 100);

        let char_list = vec!['y', 'm', 'a', 'q'];

        let result = largest_char(&char_list);
        println!("The largest char is {}", result);
        assert_eq!(*result, 'y');
    }
    ```

2. Pronađi i ispravi grešku u sledećem isečku koda.

    ```rust
    struct Point<T> {
        x: T,
        y: T,
    }

    fn main() {
        let wont_work = Point { x: 5, y: 4.0 };
    }
    ```

3. Da li je dozvoljeno koristiti generičke tipove unutar enumeracija? Ukoliko da, navedi primer.
4. Šta je rezultat izvršavanja sledećeg isečka koda na `stdout`?

    ```rust
    struct Point<X1, Y1> {
        x: X1,
        y: Y1,
    }

    impl<X1, Y1> Point<X1, Y1> {
        fn mixup<X2, Y2>(self, other: Point<X2, Y2>) -> Point<X1, Y2> {
            Point {
                x: self.x,
                y: other.y,
            }
        }
    }

    fn main() {
        let p1 = Point { x: 5, y: 10.4 };
        let p2 = Point { x: "Hello", y: 'c' };

        let p3 = p1.mixup(p2);

        println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
    }
    ```

5. Da li korištenje generičkih tipova utiče na vreme izvršavanja programa (Engl. Runtime overhead)? Razjasniti.
6. Koji koncept iz Rust-a je sličan intefejsima iz drugih jezika? Koje su razlike između njih?
7. Da li je moguće implementirati `Display` osobinu (Engl. Trait) za `Vec<T>`? Zašto?
8. Da li je moguće pozivati uobičajenu (Engl. Default) implementaciju iz naknadne (Engl. Overriding) implementacije iste metode?
9. Šta je rezultat izvršavanja sledećeg isečka koda na `stdout`?

    ```rust
    pub trait Summary {
        fn summarize_author(&self) -> String;

        fn summarize(&self) -> String {
            format!("(Read more from {}...)", self.summarize_author())
        }
    }


    pub struct Tweet {
        pub username: String,
        pub content: String,
        pub reply: bool,
        pub retweet: bool,
    }

    impl Summary for Tweet {
        fn summarize_author(&self) -> String {
            format!("@{}", self.username)
        }
    }


    pub struct NewsArticle {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    impl Summary for NewsArticle {
        fn summarize_author(&self) -> String {
            format!("@{}", self.author)
        }

        fn summarize(&self) -> String {
            format!("{}, by {} ({})", self.headline, self.author, self.location)
        }
    }


    fn main() {
        let article = NewsArticle {
            headline: String::from("Penguins win the Stanley Cup Championship!"),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                hockey team in the NHL.",
            ),
        };

        println!("New article available! {}", article.summarize());
        
        
        let tweet = Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        };

        println!("1 new tweet: {}", tweet.summarize());
        }
     ```

10. Pojednostavi sledeći kod koristeći sintaksu za ograničenja kroz osobine  (Engl. Trait bounds).

    ```rust
    pub fn notify(item1: &impl Summary, item2: &impl Summary)
    ```

11. Pojednostavi sledeći kod koristeći sintaksu za ograničenja kroz osobine  (Engl. Trait bounds).

    ```rust
    pub fn notify(item: &(impl Summary + Display)) {
    ```

12. Napiši ekvivalentni kod koristeći `where` klauzulu.

    ```rust
    fn some_function<T: Display + Clone, U: Clone + Debug>(t: &T, u: &U) -> i32 {
    ```

13. Da li sledeći kod proizvodi grešku?

    ```rust
    pub trait Summary {
        fn summarize_author(&self) -> String;

        fn summarize(&self) -> String {
            format!("(Read more from {}...)", self.summarize_author())
        }
    }


    pub struct Tweet {
        pub username: String,
        pub content: String,
        pub reply: bool,
        pub retweet: bool,
    }

    impl Summary for Tweet {
        fn summarize_author(&self) -> String {
            format!("@{}", self.username)
        }
    }


    pub struct NewsArticle {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    impl Summary for NewsArticle {
        fn summarize_author(&self) -> String {
            format!("@{}", self.author)
        }

        fn summarize(&self) -> String {
            format!("{}, by {} ({})", self.headline, self.author, self.location)
        }
    }


    fn main() {
        let article = NewsArticle {
            headline: String::from("Penguins win the Stanley Cup Championship!"),
            location: String::from("Pittsburgh, PA, USA"),
            author: String::from("Iceburgh"),
            content: String::from(
                "The Pittsburgh Penguins once again are the best \
                hockey team in the NHL.",
            ),
        };

        println!("New article available! {}", article.summarize());
        
        
        let tweet = Tweet {
            username: String::from("horse_ebooks"),
            content: String::from(
                "of course, as you probably already know, people",
            ),
            reply: false,
            retweet: false,
        };

        println!("1 new tweet: {}", tweet.summarize());
    }
    
    
    fn returns_summarizable(switch: bool) -> impl Summary {
        if switch {
            NewsArticle {
                headline: String::from(
                    "Penguins win the Stanley Cup Championship!",
                ),
                location: String::from("Pittsburgh, PA, USA"),
                author: String::from("Iceburgh"),
                content: String::from(
                    "The Pittsburgh Penguins once again are the best \
                    hockey team in the NHL.",
                ),
            }
        } else {
            Tweet {
                username: String::from("horse_ebooks"),
                content: String::from(
                    "of course, as you probably already know, people",
                ),
                reply: false,
                retweet: false,
            }
        }
    }
    ```

14. Šta predstavlja `blanket` implementacija?
15. Šta je životni vek reference (Engl. Reference Lifetime)?
16. Da li sledeći kod proizvodi grešku? Ukoliko da, ispravi je.

    ```rust
    fn main() {
        let r: i32;
        println!("r: {}", r);
    }
    ```

17. Da li sledeći kod prozvodi grešku? Zašto? Pomoć: *viseća referenca* (Engl. dangling pointer).

    ```rust
    fn main() {
        let r;

        {
            let x = 5;
            r = &x;
        }

        println!("r: {}", r);
    }
    ```

18. Kako funkcioniše `borrow checker` u Rust-u?
19. Pronađi i ispravi greške u sledećem isečku koda.

    ```rust
    fn main() {
        let string1 = String::from("abcd");
        let string2 = "xyz";

        let result = longest(string1.as_str(), string2);
        println!("The longest string is {}", result);
    }

    fn longest(x: &str, y: &str) -> &str {
        if x.len() > y.len() {
            x
        } else {
            y
        }
    }
    ```

20. Da li je sledeći kod validan? Zašto?

    ```rust
    fn main() {
        let string1 = String::from("long string is long");

        {
            let string2 = String::from("xyz");
            let result = longest(string1.as_str(), string2.as_str());
            println!("The longest string is {}", result);
        }
    }

    fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
        if x.len() > y.len() {
            x
        } else {
            y
        }
    }
    ```

21. Da li se sledeći kod uspešno kompajlira? Zašto?

    ```rust
    fn main() {
        let string1 = String::from("long string is long");
        let result;
        {
            let string2 = String::from("xyz");
            result = longest(string1.as_str(), string2.as_str());
        }
        println!("The longest string is {}", result);
    }

    fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
        if x.len() > y.len() {
            x
        } else {
            y
        }
    }
    ```

22. Popravi greške u sledećem isečku koda.

    ```rust
    fn main() {
        let string1 = String::from("abcd");
        let string2 = "xyz";

        let result = longest(string1.as_str(), string2);
        println!("The longest string is {}", result);
    }

    fn longest<'a>(x: &str, y: &str) -> &'a str {
        let result = String::from("really long string");
        result.as_str()
    }
    ```

23. Popravi greške u sledećem isečku koda.

    ```rust
    struct ImportantExcerpt {
        part: &str,
    }

    fn main() {
        let novel = String::from("Call me Ishmael. Some years ago...");
        let first_sentence = novel.split('.').next().expect("Could not find a '.'");
        let i = ImportantExcerpt {
            part: first_sentence,
        };
    }
    ```

24. Šta su ulazni i izlazni životni vekovi (Engl. Input and Output Lifetimes)?
25. Šta su pravila za *eliziju životnog veka* (Engl. Lifetime Elision)?
26. Da li su nam potrebne eksplicitne anotacije životnog veka u sledećem primeru? Zašto?

    ```rust
    fn first_word(s: &str) -> &str {
    ```

27. Popravi greške u sledećem isečku koda.

    ```rust
    struct ImportantExcerpt<'a> {
        part: &'a str,
    }

    impl ImportantExcerpt {
        fn level(&self) -> i32 {
            3
        }
    }

    impl ImportantExcerpt {
        fn announce_and_return_part(&self, announcement: &str) -> &str {
            println!("Attention please: {}", announcement);
            self.part
        }
    }

    fn main() {
        let novel = String::from("Call me Ishmael. Some years ago...");
        let first_sentence = novel.split('.').next().expect("Could not find a '.'");
        let i = ImportantExcerpt {
            part: first_sentence,
        };
    }
    ```

28. Napiči ekvivalentan kod koji koristi eksplicitan životni vek.

    ```rust
    let s: &str = "I have a static lifetime.";
    ```

29. Koliko je dugačak životni vek string literal-a?
30. Koja ja razlika između korišćenja asociranih tipova i generičkih tipova pri implementaciji osobina?
31. Da li sledeći kod izaziva `panic`?

    ```rust
    use std::ops::Add;

    #[derive(Debug, Copy, Clone, PartialEq)]
    struct Point {
        x: i32,
        y: i32,
    }

    impl Add for Point {
        type Output = Point;

        fn add(self, other: Point) -> Point {
            Point {
                x: self.x + other.x,
                y: self.y + other.y,
            }
        }
    }

    fn main() {
        assert_eq!(
            Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
            Point { x: 3, y: 3 }
        );
    }
    ```

32. Zašto sledeći primer koristi `Add<Meters>` a ne samo `Add` kao prethodni?

    ```rust
    use std::ops::Add;

    struct Millimeters(u32);
    struct Meters(u32);

    impl Add<Meters> for Millimeters {
        type Output = Millimeters;

        fn add(self, other: Meters) -> Millimeters {
            Millimeters(self.0 + (other.0 * 1000))
        }
    }
    ```

33. Šta je rezultat izvršavanja sledećeg isečka koda?

    ```rust
    trait Pilot {
        fn fly(&self);
    }

    trait Wizard {
        fn fly(&self);
    }

    struct Human;

    impl Pilot for Human {
        fn fly(&self) {
            println!("This is your captain speaking.");
        }
    }

    impl Wizard for Human {
        fn fly(&self) {
            println!("Up!");
        }
    }

    impl Human {
        fn fly(&self) {
            println!("*waving arms furiously*");
        }
    }

    fn main() {
        let person = Human;
        person.fly();
    }
    ```

34. Ponovo napiši `main` funckiju iz prethodnog primera tako da se pozovu sve 3 implementacije `fly` metode.
35. Šta je rezultat izvršavanja sledećeg isečka koda?

    ```rust
    trait Animal {
        fn baby_name() -> String;
    }

    struct Dog;

    impl Dog {
        fn baby_name() -> String {
            String::from("Spot")
        }
    }

    impl Animal for Dog {
        fn baby_name() -> String {
            String::from("puppy")
        }
    }

    fn main() {
        println!("A baby dog is called a {}", Dog::baby_name());
    }
    ```

36. Ponovo napiši `main` funkciju iz prethodnog primera tako da poziva obe `baby_name` metode.
37. Sledeći kod se ne kompajlira. Implementiraj odgovarajuću osobinu na `Point` tipu.

    ```rust
    use std::fmt;

    trait OutlinePrint: fmt::Display {
        fn outline_print(&self) {
            let output = self.to_string();
            let len = output.len();
            println!("{}", "*".repeat(len + 4));
            println!("*{}*", " ".repeat(len + 2));
            println!("* {} *", output);
            println!("*{}*", " ".repeat(len + 2));
            println!("{}", "*".repeat(len + 4));
        }
    }

    struct Point {
        x: i32,
        y: i32,
    }

    impl OutlinePrint for Point {}
    ```

38. Implementiraj `Display` osobinu na `Vector<T>` tipu.
39. Šta sledeći kod prikazuje na `stdout`?

    ```rust
    fn main() {
        type Kilometers = i32;
        let x: i32 = 5;
        let y: Kilometers = 5;
        println!("x + y = {}", x + y);
    }
    ```

40. Šta je *never type*?
41. Šta su divergirajuće funkcije (Engl. Divering functions)?
42. Koji je tip `guess` varijable u sledećem isečku koda?

    ```rust
            let guess: u32 = match guess.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };
    ```

43. Šta je tip `loop` izraza u sledećem isečku koda?

    ```rust
        print!("forever ");

        loop {
            print!("and ever ");
        }
    ```

44. Da li se sledeći isečak koda uspešno kompajlira? Zašto?

    ```rust
    fn main() {
        let s1: str = "Hello there!";
        let s2: str = "How's it going?";
    }
    ```

45. Da li su osobine tipovi dinamičke veličine (Engl. Dynamically Sized)?
46. Koja osobina je korisna u toku rada sa tipovima dinamičke veličine (DST - Dynamically Sized Type)?
47. Da li generičke funkcije uobičajeno podržavaju rad sa tipovima dinamičke veličine?
