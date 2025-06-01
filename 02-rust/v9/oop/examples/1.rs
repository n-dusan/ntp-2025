// Implementiraj GUI biblioteku za iscrtavanje widget-a na komandnom prozoru.

// GUI biblioteka podržava tri tipa widget-a: Label, Button i Window.
// Implementiraj Widget osobinu za svaki tip widget-a i `draw_into` metodu.

// Rezultat ispisa na komandnom prozoru je:
//-----------------------------------------
// ========
// Rust GUI Demo 1.23
// ========

// This is a small text GUI demo.

// | Click me! |
//-----------------------------------------

// Dodatni zadatak:
// - Implementiraj `Widget` za `Window` tako da iscrtava sve widget-e u okviru prozora.

// +--------------------------------+
// |       Rust GUI Demo 1.23       |
// +================================+
// | This is a small text GUI demo. |
// | +-----------+                  |
// | | Click me! |                  |
// | +-----------+                  |
// +--------------------------------+

// Smernice i rešenje možeš naći na sledećem linku - https://google.github.io/comprehensive-rust/methods-and-traits/exercise.html

pub trait Widget {
    /// Natural width of `self`.
    fn width(&self) -> usize;

    /// Draw the widget into a buffer.
    fn draw_into(&self, buffer: &mut dyn std::fmt::Write);

    /// Draw the widget on standard output.
    fn draw(&self) {
        let mut buffer = String::new();
        self.draw_into(&mut buffer);
        println!("{buffer}");
    }
}

pub struct Label {
    label: String,
}

impl Label {
    fn new(label: &str) -> Label {
        Label {
            label: label.to_owned(),
        }
    }
}

pub struct Button {
    label: Label,
}

impl Button {
    fn new(label: &str) -> Button {
        Button {
            label: Label::new(label),
        }
    }
}

pub struct Window {
    title: String,
    widgets: Vec<Box<dyn Widget>>,
}

impl Window {
    fn new(title: &str) -> Window {
        Window {
            title: title.to_owned(),
            widgets: Vec::new(),
        }
    }

    fn add_widget(&mut self, widget: Box<dyn Widget>) {
        self.widgets.push(widget);
    }

    fn inner_width(&self) -> usize {
        std::cmp::max(
            self.title.chars().count(),
            self.widgets.iter().map(|w| w.width()).max().unwrap_or(0),
        )
    }
}

// TODO: Implementiraj `Widget` for `Label`.

// TODO: Implementiraj `Widget` for `Button`.

// TODO: Implementiraj `Widget` for `Window`.

fn main() {
    let mut window = Window::new("Rust GUI Demo 1.23");
    window.add_widget(Box::new(Label::new("This is a small text GUI demo.")));
    window.add_widget(Box::new(Button::new("Click me!")));
    window.draw();
}
