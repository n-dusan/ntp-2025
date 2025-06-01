// Ispravi greške
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}


pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl __ for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}

impl Tweet {
    fn new(username: String, content: String) -> Self {
        Tweet {
            username,
            content,
            reply: false,
            retweet: false,
        }
    }
}


pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
    pub published_date: String,
}

impl __ for NewsArticle {
    fn summarize_author(&self) -> String {
        format!("@{}", self.author)
    }

    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

impl NewsArticle {
    fn new(headline: String, location: String, author: String, content: String, published_date: String) -> Self {
        NewsArticle {
            headline,
            location,
            author,
            content,
            published_date,
        }
    }
}


fn main() {
    let article = NewsArticle::new(
        String::from("Penguins win the Stanley Cup Championship!"),
        String::from("Pittsburgh, PA, USA"),
        String::from("Iceburgh"),
        String::from("The Pittsburgh Penguins once again are the best hockey team in the NHL."),
        String::from("May 21, 2023"),
    );

    println!("New article available! {}", article.summarize());

    let tweet = Tweet::new(
        String::from("horse_ebooks"),
        String::from("of course, as you probably already know, people"),
    );

    println!("1 new tweet: {}", tweet.summarize());
}