
// Ispravi greške u kodu

use std::rc::Rc;

#[derive(Debug)]
struct Sun {}

#[derive(Debug)]
enum Planet {
    Mercury(Rc<Sun>),
    Venus(Rc<Sun>),
    Earth(Rc<Sun>),
    Mars(Rc<Sun>),
    Jupiter(Rc<Sun>),
    Saturn(Rc<Sun>),
    Uranus(Rc<Sun>),
    Neptune(Rc<Sun>),
}

impl Planet {
    fn details(&self) {
        println!("Hi from {:?}!", self)
    }
}

#[test]
fn main() {
    let sun = Rc::new(Sun {});
    println!("reference count = {}", Rc::strong_count(&sun)); // 1 referenca

    let mercury = Planet::Mercury(Rc::clone(&sun));
    println!("reference count = {}", Rc::strong_count(&sun)); // 2 reference
    mercury.details();

    let venus = Planet::Venus(Rc::clone(&sun));
    println!("reference count = {}", Rc::strong_count(&sun)); // 3 reference
    venus.details();

    let earth = Planet::Earth(Rc::clone(&sun));
    println!("reference count = {}", Rc::strong_count(&sun)); // 4 reference
    earth.details();

    let mars = Planet::Mars(Rc::clone(&sun));
    println!("reference count = {}", Rc::strong_count(&sun)); // 5 referenci
    mars.details();

    let jupiter = Planet::Jupiter(Rc::clone(&sun));
    println!("reference count = {}", Rc::strong_count(&sun)); // 6 referenci
    jupiter.details();

    // TODO
    let saturn = Planet::Saturn(Rc::new(Sun {}));
    println!("reference count = {}", Rc::strong_count(&sun)); // 7 referenci
    saturn.details();

    // TODO
    let uranus = Planet::Uranus(Rc::new(Sun {}));
    println!("reference count = {}", Rc::strong_count(&sun)); // 8 referenci
    uranus.details();

    // TODO
    let neptune = Planet::Neptune(Rc::new(Sun {}));
    println!("reference count = {}", Rc::strong_count(&sun)); // 9 referenci
    neptune.details();

    assert_eq!(Rc::strong_count(&sun), 9);

    drop(neptune);
    println!("reference count = {}", Rc::strong_count(&sun)); // 8 referenci

    drop(uranus);
    println!("reference count = {}", Rc::strong_count(&sun)); // 7 referenci

    drop(saturn);
    println!("reference count = {}", Rc::strong_count(&sun)); // 6 referenci

    drop(jupiter);
    println!("reference count = {}", Rc::strong_count(&sun)); // 5 referenci

    drop(mars);
    println!("reference count = {}", Rc::strong_count(&sun)); // 4 reference

    // TODO
    println!("reference count = {}", Rc::strong_count(&sun)); // 3 reference

    // TODO
    println!("reference count = {}", Rc::strong_count(&sun)); // 2 reference

    // TODO
    println!("reference count = {}", Rc::strong_count(&sun)); // 1 reference

    assert_eq!(Rc::strong_count(&sun), 1);
}