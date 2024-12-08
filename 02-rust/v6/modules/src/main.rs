mod front_of_house;

fn main() {
    assert_eq!(front_of_house::hosting::seat_at_table(), "sit down please");
    assert_eq!(modules::eat_at_restaurant(),"yummy yummy!");
}