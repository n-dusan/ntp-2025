// Kreiraj instancu User iz druge instance upotrebom sintakse za ažuriranje (Eng. update syntax)
struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}
fn main() {
    let u1 = User {
        email: String::from("test@email.com"),
        username: String::from("test"),
        active: true,
        sign_in_count: 1,
    };

    let u2 = set_email(u1);

    println!("Success!");
} 

fn set_email(u: User) -> User {
    User {
        email: String::from("test@email.com"),
        __
    }
}
