
use rand::Rng;
use std::time::Instant;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

mod selection_sort;

//funcion que crear arreglos de numeros aleatorios con un tamaño especifico en un rango especifico
fn create_random_array(size: usize, n: i64) -> Vec<i64> {
    let mut rng = rand::thread_rng();
    let mut array: Vec<i64> = Vec::with_capacity(size);
    for _ in 0..size {
        array.push(rng.gen_range(std::ops::Range{start: -1*n, end: 2*n}));
    }
    array
}

fn main() {
    //abrir archivo
    
    let path = Path::new("src/sesort.txt");
    let display = path.display();

    let mut file = File::create("src/bsort.txt")
        .expect("Could not create the file");

    let mut cont:usize = 50000;
    loop {
        if cont > 1000000 {
            break;
        }

        let size = cont;
        let mut n:i64 = cont as i64;
        n *= 2;

        let mut arr = create_random_array(size, n);

        let mut t0 = Instant::now();
        selection_sort::selection_sort(&mut arr);
        let mut t1 = Instant::now();

        //write the size and time to the file
        let mut s = String::new();
        s.push_str(&format!("{}", size));
        s.push_str("\t");
        s.push_str(&format!("{}", t1.duration_since(t0).as_micros()));
        s.push_str("\n");

        file.write_all(&format!("{}", s).as_bytes())
            .expect("Could not write to the file");
        

        println!("{:?} completado", size);
        cont += 25000;
    }
}
