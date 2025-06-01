// Dopuni potpis `call_me` funkcije tako da se program uspešno izvršava.
fn call_me {
    f();
}

fn function() {
    println!("I'm a function!");
}

fn main() {
    let closure = || println!("I'm a closure!");

    call_me(closure);
    call_me(function);
}