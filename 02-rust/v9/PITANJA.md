# V9 - Programski jezik Rust

## OOP, konkurentno programiranje (fakultativno)

1. Da li je Rust objektno-orijentisan jezik?
2. Da li Rust podržava enkapsulaciju?
3. Da li Rust podržava nasleđivanje?
4. Da li Rust podržava polimorfizam?
5. Šta predstavljaju objekti sa osobinom (Engl. Trait Object)?
6. Da li je moguće implementirati sledeći kod upotrebom generika umesto objekata sa osobinom?

    ```rust
        pub trait Draw {
            fn draw(&self);
        }

        pub struct Screen {
            pub components: Vec<Box<dyn Draw>>,
        }

        impl Screen {
            pub fn run(&self) {
                for component in self.components.iter() {
                    component.draw();
                }
            }
        }

        pub struct Button {
            pub width: u32,
            pub height: u32,
            pub label: String,
        }

        impl Draw for Button {
            fn draw(&self) {
                println!("Drawing a button!")
            }
        }

        struct SelectBox {
            width: u32,
            height: u32,
            options: Vec<String>,
        }

        impl Draw for SelectBox {
            fn draw(&self) {
                println!("Drawing a select box!")
            }
        }


        fn main() {
            let screen = Screen {
                components: vec![
                    Box::new(SelectBox {
                        width: 75,
                        height: 10,
                        options: vec![
                            String::from("Yes"),
                            String::from("Maybe"),
                            String::from("No"),
                        ],
                    }),
                    Box::new(Button {
                        width: 50,
                        height: 10,
                        label: String::from("OK"),
                    }),
                ],
            };

            screen.run();
        }
    ```

7. Da li `self` može biti tipa `Box<Self>`?

    ```rust
        impl State for Draft {
            fn request_review(self: Box<Self>) -> Box<dyn State> {
                Box::new(PendingReview {})
            }
        }
    ```

8. Za šta služi `take` metoda nad `Option` tipom?
9. Za šta služi `as_ref` metoda nad `Option` tipom?
10. Koja je razlika između konkurentnog i paralelnog programiranja?
11. Koji je rezultat izvršavanja sledećeg koda?

    ```rust
    use std::thread;
    use std::time::Duration;

    fn main() {
        thread::spawn(|| {
            for i in 1..10 {
                println!("hi number {} from the spawned thread!", i);
                thread::sleep(Duration::from_millis(1));
            }
        });

        for i in 1..5 {
            println!("hi number {} from the main thread!", i);
            thread::sleep(Duration::from_millis(1));
        }
    }
    ```

12. Da li `main` nit implicitno čeka da se ostale niti završe?
13. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    use std::thread;

    fn main() {
        let v = vec![1, 2, 3];

        let handle = thread::spawn(|| {
            println!("Here's a vector: {:?}", v);
        });

        handle.join().unwrap();
    }
    ```

14. Šta predstavlja kanal (Engl. channel)?
15. U izrazu `let (tx, rx) = mpsc::channel();`, šta predstavlja `mpsc`? Šta predstavljaju `tx` i `rx`?
16. U kom trenutku se kanal zatvara?
17. Koji je rezultat izvršavanja sledećeg koda?

    ```rust
    use std::sync::mpsc;
    use std::thread;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let val = String::from("hi");
            tx.send(val).unwrap();
        });

        let received = rx.recv().unwrap();
        println!("Got: {}", received);
    }
    ```

18. Koja je razlika između metoda `recv` i `try_recv` u kanalu?
19. Da li sledeći kod proizvodi grešku? Zašto?

    ```rust
    use std::sync::mpsc;
    use std::thread;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let val = String::from("hi");
            tx.send(val).unwrap();
            println!("val is {}", val);
        });

        let received = rx.recv().unwrap();
        println!("Got: {}", received);
    }
    ```

20. Da li je sledeći kod validan?

    ```rust
    use std::sync::mpsc;
    use std::thread;
    use std::time::Duration;

    fn main() {
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let vals = vec![
                String::from("hi"),
                String::from("from"),
                String::from("the"),
                String::from("thread"),
            ];

            for val in vals {
                tx.send(val).unwrap();
                thread::sleep(Duration::from_secs(1));
            }
        });

        for received in rx {
            println!("Got: {}", received);
        }
    }
    ```

21. Ispravi grešku u sledećem kodu:

    ```rust
    use std::sync::mpsc;
    use std::thread;
    use std::time::Duration;

    fn main() {
        
        let (tx, rx) = mpsc::channel();

        thread::spawn(move || {
            let vals = vec![
                String::from("hi"),
                String::from("from"),
                String::from("the"),
                String::from("thread"),
            ];

            for val in vals {
                tx.send(val).unwrap();
                thread::sleep(Duration::from_secs(1));
            }
        });

        thread::spawn(move || {
            let vals = vec![
                String::from("more"),
                String::from("messages"),
                String::from("for"),
                String::from("you"),
            ];

            for val in vals {
                tx.send(val).unwrap();
                thread::sleep(Duration::from_secs(1));
            }
        });

        for received in rx {
            println!("Got: {}", received);
        }
    }
    ```

22. Šta predstavlja `Mutex<T>`? Šta predstavlja metoda `lock`?
23. Ispravi grešku u sledećem kodu:

    ```rust
    use std::sync::Mutex;
    use std::thread;

    fn main() {
        let counter = Mutex::new(0);
        let mut handles = vec![];

        for _ in 0..10 {
            let handle = thread::spawn(move || {
                let mut num = counter.lock().unwrap();

                *num += 1;
            });
            handles.push(handle);
        }

        for handle in handles {
            handle.join().unwrap();
        }

        println!("Result: {}", *counter.lock().unwrap());
    }
    ```
