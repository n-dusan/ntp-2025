# V2 - Programski jezik Rust

U drugom terminu vežbi studenti bi trebalo da kroz par primera provežbaju najčešće programske koncepte, poput kreiranja varijabli, osnovni tipovi podataka, funkcije i kontrola toka programa. Osnovni programski koncepti opisani su u trećem poglavlju knjige [na sledećoj adresi](https://doc.rust-lang.org/book/ch03-00-common-programming-concepts.html).

## Osnovni programski koncepti

1. Implementirati _[fizz-buzz](https://en.wikipedia.org/wiki/Fizz_buzz)_ igru reči za prvih 100 brojeva.

2. Napisati `n-fibonacci` program koji računa _n-ti_ Fibonačijev broj. Parametar _n_ se zadaje putem tastature.

3. Napisati funkciju `pretty_print` koja ispisuje elemente matrice i funkciju `transpose` koja transponuje matricu (prebaci redove u kolone). Smernice možete naći [ovde](https://google.github.io/comprehensive-rust/exercises/day-1/for-loops.html).

    ```rust
    fn transpose(matrix: [[i32; 3]; 3]) -> [[i32; 3]; 3] {
        unimplemented!()
    }

    fn pretty_print(matrix: &[[i32; 3]; 3]) {
        unimplemented!()
    }

    fn main() {
        let matrix = [
            [101, 102, 103],
            [201, 202, 203],
            [301, 302, 303],
        ];

        println!("matrix:");
        pretty_print(&matrix);

        let transposed = transpose(matrix);
        println!("transposed:");
        pretty_print(&transposed);
    }
    ```
