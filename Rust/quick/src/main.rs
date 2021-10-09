
use rand::Rng;
use std::time::Instant;
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

mod quick_sort;

//funcion que crear arreglos de numeros aleatorios con un tamaño especifico en un rango especifico
fn create_random_array(size: usize, n: i32) -> Vec<i32> {
    let mut rng = rand::thread_rng();
    let mut array: Vec<i32> = Vec::with_capacity(size);
    for _ in 0..size {
        array.push(rng.gen_range(std::ops::Range{start: -1*n, end: 2*n}));
    }
    array
}

fn main() {
    //abrir archivo
    let mut file = File::create("src/qsort.txt")
        .expect("Could not create the file");

    let mut cont:usize = 50000;
    loop {
        if cont > 1000000 {
            break;
        }

        let size = cont;
        let mut n:i32 = cont as i32;
        n *= 2;

        let mut acum = 0;
        for t in 0..10 {
            let mut array = create_random_array(size, n);
            
            let start = Instant::now();
            quick_sort::quick_sort(&mut array);
            let end = start.elapsed();
            
            acum += end.as_micros();
        }

        let mut s = String::new();
        s.push_str(&format!("{}", size));
        s.push_str("\t");
        s.push_str(&format!("{}", acum/10));
        s.push_str("\n");

        file.write_all(&format!("{}", s).as_bytes())
            .expect("Could not write to the file");
        

        println!("{:?} completado", size);
        cont += 25000;
    }
}
