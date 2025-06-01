// Ispravi grešku u kodu i popuni prazninu.

// Želimo da svaka nit koju smo pokrenuli ažurira vrednost deljene promenljive Jobstatus.jobs_completed

use std::sync::Arc;
use std::thread;
use std::time::Duration;

struct JobStatus {
    jobs_completed: u32,
}

fn main() {
    let status = Arc::new(JobStatus { jobs_completed: 0 });
    let mut handles = vec![];
    for _ in 0..10 {
        let status_shared = Arc::clone(&status);
        let handle = thread::spawn(move || {
            thread::sleep(Duration::from_millis(250));
            // TODO: potrebno je prvo dobiti ekskluzivan pristup deljenoj promenljivoj
            status_shared.jobs_completed += 1;
        });
        handles.push(handle);
    }
    for handle in handles {
        handle.join().unwrap();
        // TODO: ispiši vrednost deljene promenljive
        println!("jobs completed {}", _____);
    }
}
