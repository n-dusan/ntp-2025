# V6 - Programski jezik Rust

## Paketi, moduli, kolekcije, obrada grešaka, testiranje

1. Upotrebom `cargo` alata kreirati novi `test-binary` paket sa sledećim rasporedom:

        ```
        .
        ├── Cargo.toml
        └── src
            └── main.rs

        1 directory, 2 files
        ```

2. Upotrebom `cargo` alata kreirati novi `test-library` paket sa sledećim rasporedom:

        ```
        .
        ├── Cargo.toml
        └── src
            └── lib.rs

        1 directory, 2 files
        ```

3. Dodati `library` sanduk unutar `test-binary` paketa. Dopuniti prazne linije ispod sa imenom datoteka.

        ```
        ├── Cargo.lock
        ├── Cargo.toml
        ├── src
        │   ├── __
        │   └── __
        ```

4. Razmestiti module iz primera `modules` van `lib.rs` i smestiti u odgovarajuće `.rs` datoteke prema rasporedu ispod.

        ```
        .
        ├── Cargo.toml
        ├── src
        │   ├── back_of_house.rs
        │   ├── front_of_house
        │   │   ├── hosting.rs
        │   │   ├── mod.rs
        │   │   └── serving.rs
        │   ├── lib.rs
        │   └── main.rs
        ```

5. Pokrenuti primere i ispraviti greške iz projekta `errors`.
