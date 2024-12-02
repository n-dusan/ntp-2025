// Popuni praznine i ispravi greške u kodu.
use std::collections::HashMap;
fn main() {
    // Inferencija tipova nam dozvoljava da ne navodimo eksplicitno tip heš mape, koji bi
    // u ovom slučaju bio HashMap<&str, u8>
    let mut player_stats = HashMap::new();

    // `entry` unosi ključ jedino ukoliko već ne postoji
    player_stats.entry("health").or_insert(100);

    assert_eq!(player_stats["health"], __);

    // `or_insert_with`, za razliku od `or_insert` može biti i funkcija sa novom vrednošću
    player_stats.entry("health").or_insert_with(random_stat_buff);
    assert_eq!(player_stats["health"], __);

    let health = player_stats.entry("health").or_insert(50);
    assert_eq!(health, __);
    *health -= 50;
    assert_eq!(*health, __);

    println!("Success!");
}

fn random_stat_buff() -> u8 {
    42
}
