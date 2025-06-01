// Ispravi grešku u kodu.

// Program bi trebalo da generiše više niti koje svaka traje najmanje 250ms, i
// svaka nit treba da vrati koliko je trajala. Program treba da sačeka da sve
// niti završe i da njihove rezultate sakupi u vektor.

use std::thread;
use std::time::{Duration, Instant};

fn main() {
    let mut handles = vec![];
    for i in 0..10 {
        handles.push(thread::spawn(move || {
            let start = Instant::now();
            thread::sleep(Duration::from_millis(250));
            println!("thread {} is complete", i);
            start.elapsed().as_millis()
        }));
    }

    let mut results: Vec<u128> = vec![];
    for handle in handles {
        // TODO: sačekaj da se sve niti završe
    }

    if results.len() != 10 {
        panic!("Oh no! All the spawned threads did not finish!");
    }

    println!();
    for (i, result) in results.into_iter().enumerate() {
        println!("thread {} took {}ms", i, result);
    }
}