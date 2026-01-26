# V8 - Programski jezik Rust

## Pametni pointeri (drugi deo), FP, iteratori i zatvorenja

1. Šta predstavlja obrazac interne promenjivosti?
2. Koja je razlika između `Box<T>` i `RefCell<T>`?
3. U kojoj situaciji je potrebno da se pravila pozajmljivanja proveravaju u vreme izvršavanja programa umesto u vreme kompajliranja?
4. Izmeni sledeći kod upotrebom `RefCell<T>` tako da se testovi uspešno izvrše:

    ```rust
    pub trait Messenger {
    fn send(&self, msg: &str);
    }

    pub struct LimitTracker<'a, T: Messenger> {
        messenger: &'a T,
        value: usize,
        max: usize,
    }

    impl<'a, T> LimitTracker<'a, T>
    where
        T: Messenger,
    {
        pub fn new(messenger: &'a T, max: usize) -> LimitTracker<'a, T> {
            LimitTracker {
                messenger,
                value: 0,
                max,
            }
        }

        pub fn set_value(&mut self, value: usize) {
            self.value = value;

            let percentage_of_max = self.value as f64 / self.max as f64;

            if percentage_of_max >= 1.0 {
                self.messenger.send("Error: You are over your quota!");
            } else if percentage_of_max >= 0.9 {
                self.messenger
                    .send("Urgent warning: You've used up over 90% of your quota!");
            } else if percentage_of_max >= 0.75 {
                self.messenger
                    .send("Warning: You've used up over 75% of your quota!");
            }
        }
    }


    #[cfg(test)]
    mod tests {
        use super::*;

        struct MockMessenger {
            sent_messages: Vec<String>,
        }

        impl MockMessenger {
            fn new() -> MockMessenger {
                MockMessenger {
                    sent_messages: vec![],
                }
            }
        }

        impl Messenger for MockMessenger {
            fn send(&self, message: &str) {
                self.sent_messages.push(String::from(message));
            }
        }

        #[test]
        fn it_sends_an_over_75_percent_warning_message() {
            let mock_messenger = MockMessenger::new();
            let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

            limit_tracker.set_value(80);

            assert_eq!(mock_messenger.sent_messages.len(), 1);
        }
    }
    ```

5. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    pub trait Messenger {
    fn send(&self, msg: &str);
    }

    pub struct LimitTracker<'a, T: Messenger> {
        messenger: &'a T,
        value: usize,
        max: usize,
    }

    impl<'a, T> LimitTracker<'a, T>
    where
        T: Messenger,
    {
        pub fn new(messenger: &'a T, max: usize) -> LimitTracker<'a, T> {
            LimitTracker {
                messenger,
                value: 0,
                max,
            }
        }

        pub fn set_value(&mut self, value: usize) {
            self.value = value;

            let percentage_of_max = self.value as f64 / self.max as f64;

            if percentage_of_max >= 1.0 {
                self.messenger.send("Error: You are over your quota!");
            } else if percentage_of_max >= 0.9 {
                self.messenger
                    .send("Urgent warning: You've used up over 90% of your quota!");
            } else if percentage_of_max >= 0.75 {
                self.messenger
                    .send("Warning: You've used up over 75% of your quota!");
            }
        }
    }


    #[cfg(test)]
    mod tests {
        use super::*;
        use std::cell::RefCell;

        struct MockMessenger {
            sent_messages: RefCell<Vec<String>>,
        }

        impl MockMessenger {
            fn new() -> MockMessenger {
                MockMessenger {
                    sent_messages: RefCell::new(vec![]),
                }
            }
        }

        impl Messenger for MockMessenger {
            fn send(&self, message: &str) {
                let mut one_borrow = self.sent_messages.borrow_mut();
                let mut two_borrow = self.sent_messages.borrow_mut();

                one_borrow.push(String::from(message));
                two_borrow.push(String::from(message));
            }
        }

        #[test]
        fn it_sends_an_over_75_percent_warning_message() {
            let mock_messenger = MockMessenger::new();
            let mut limit_tracker = LimitTracker::new(&mock_messenger, 100);

            limit_tracker.set_value(80);

            assert_eq!(mock_messenger.sent_messages.borrow().len(), 1);
        }
    }
    ```

6. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
        let add_one_v4 = |x|  x + 1;
    }
    ```

7. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
        let example_closure = |x| x;

        let s = example_closure(String::from("hello"));
        let n = example_closure(5);
    }
    ```

8. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
        fn main() {
        let list = vec![1, 2, 3];
        println!("Before defining closure: {:?}", list);

        let only_borrows = || println!("From closure: {:?}", list);

        println!("Before calling closure: {:?}", list);
        only_borrows();
        println!("After calling closure: {:?}", list);
    }
    ```

9. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
        let mut list = vec![1, 2, 3];
        println!("Before defining closure: {:?}", list);

        let mut borrows_mutably = || list.push(7);
        println!("Before calling closure: {:?}", list);
        borrows_mutably();
        println!("After calling closure: {:?}", list);
    }
    ```

10. Ispravi grešku u sledećem kodu:

    ```rust
    use std::thread;

    fn main() {
        let list = vec![1, 2, 3];
        println!("Before defining closure: {:?}", list);

        thread::spawn(|| println!("From thread: {:?}", list))
            .join()
            .unwrap();
    }
    ```

11. U zavisnosti od zapamćene vrednosti u zatvorenju, koje tri `Fn` osobine zatvorenje može da implementira?
12. Koju `Fn` osobinu implementiraju svi tipovi zatvorenja?
13. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    #[derive(Debug)]
    struct Rectangle {
        width: u32,
        height: u32,
    }

    fn main() {
        let mut list = [
            Rectangle { width: 10, height: 1 },
            Rectangle { width: 3, height: 5 },
            Rectangle { width: 7, height: 12 },
        ];

        let mut sort_operations = vec![];
        let value = String::from("by key called");

        list.sort_by_key(|r| {
            sort_operations.push(value);
            r.width
        });
        println!("{:#?}", list);
    }
    ```

14. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    #[derive(Debug)]
    struct Rectangle {
        width: u32,
        height: u32,
    }

    fn main() {
        let mut list = [
            Rectangle { width: 10, height: 1 },
            Rectangle { width: 3, height: 5 },
            Rectangle { width: 7, height: 12 },
        ];

        let mut num_sort_operations = 0;
        list.sort_by_key(|r| {
            num_sort_operations += 1;
            r.width
        });
        println!("{:#?}, sorted in {num_sort_operations} operations", list);
    }
    ```

15. Da li su iteratori "lenji" u Rust-u?
16. Šta predstavlja `Iterator` osobina?
17. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let v1_iter = v1.iter();

        assert_eq!(v1_iter.next(), Some(&1));
        assert_eq!(v1_iter.next(), Some(&2));
        assert_eq!(v1_iter.next(), Some(&3));
        assert_eq!(v1_iter.next(), None);
    }
    ```

18. Ispravi grešku u sledećem kodu:

    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let mut v1_iter = v1.iter();

        let mut first = v1_iter.next().unwrap();
        first += 1;
    }
    ```

19. Šta su konzumirajući adapteri (Engl. consuming adapters)?
20. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn main() {
        let v1 = vec![1, 2, 3];

        let v1_iter = v1.iter();

        let total: i32 = v1_iter.sum();

        assert_eq!(total, 6);
        
        let give_me_next_pls = v1_iter.next();
    }
    ```

21. Šta su iterator adapteri (Engl. iterator adapters)?
22. Ispravi grešku u sledećem kodu:

```rust
    fn main() {
        let v1: Vec<i32> = vec![1, 2, 3];
        let v2 = v1.iter().map(|x| x + 1).collect();
        assert_eq!(v2, vec![2, 3, 4]);
    }
```

23. Ispravi grešku u sledećem kodu:

    ```rust
    #[derive(PartialEq, Debug)]
    struct Shoe {
        size: u32,
        style: String,
    }

    fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
        shoes.iter().filter(|s| s.size == shoe_size).collect()
    }

    #[cfg(test)]
    mod tests {
        use super::*;

        #[test]
        fn filters_by_size() {
            let shoes = vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker"),
                },
                Shoe {
                    size: 13,
                    style: String::from("sandal"),
                },
                Shoe {
                    size: 10,
                    style: String::from("boot"),
                },
            ];

            let in_my_size = shoes_in_size(shoes, 10);

            assert_eq!(
                in_my_size,
                vec![
                    Shoe {
                        size: 10,
                        style: String::from("sneaker")
                    },
                    Shoe {
                        size: 10,
                        style: String::from("boot")
                    },
                ]
            );
        }
    }
    ```

24. Pri dodeli drugoj varijabli, da li Rust podrazumevano obavlja kopiranje (`Copy`) varijable?
25. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    fn inc(x: i32) -> i32 {
        x + 1
    }

    fn main() {
        let x = 5;
        let y = inc(x);
        println!("{x}, {y}");
    }
    ```

26. Napiši koncizniji kod umesto sledećeg koda upotrebom iterator adaptera i `filter` metode.

    ```rust
    pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
        let mut results = Vec::new();

        for line in contents.lines() {
            if line.contains(query) {
                results.push(line);
            }
        }

        results
    }
    ```
