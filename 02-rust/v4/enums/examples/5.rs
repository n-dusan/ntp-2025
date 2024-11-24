// Izbriši strukturu `IpAddr`` i ispravi sledeći kod tako da koristi samo enumeraciju.
fn main() {
    enum IpAddrKind {
        V4,
        V6,
    }
  
    struct IpAddr { // izbriši
        kind: IpAddrKind, // ..
        address: String, // ..
    }
  
    let home = IpAddr {
        kind: IpAddrKind::V4,
        address: String::from("127.0.0.1"),
    };
  
    let loopback = IpAddr {
        kind: IpAddrKind::V6,
        address: String::from("::1"),
    };
  }