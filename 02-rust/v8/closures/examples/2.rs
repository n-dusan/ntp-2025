/* Ispravi grešku u kodu:
- Nemoj menjati `_reborrow` i `_count_reborrowed`
- Nemoj menjati `assert_eq`
*/
fn main() {
    let mut count = 0;

    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    inc();


    let _reborrow = &count; 

    inc();

    // Nakon zadnjeg poziva funkcije `inc`, zatvorenje više ne mora da radi &mut count pozajmicu. 
    // Prema tome, moguće je ponovo pozajmiti bez greške
    let _count_reborrowed = &mut count; 

    assert_eq!(count, 0);
}
