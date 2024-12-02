// Ispravi greške u kodu
// Nemoj dodavati ili uklanjati redove
use std::collections::HashMap;
fn main() {
  let v1 = 10;
  let mut m1 = HashMap::new();
  m1.insert(v1, v1);
  println!("v1 is still usable after inserting to hashmap : {}", v1);

  let v2 = "hello".to_string();
  let mut m2 = HashMap::new();
  // Vlasništvo premešteno ovde
  m2.insert(v2, v1);
    
  assert_eq!(v2, "hello");

  println!("Success!");
}
