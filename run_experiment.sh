#!/bin/bash

for M in {2..5}
do
    for N in 1 2 3 10 100
    do
        for degree in {5..10}
        do
            for size in `seq 1000 1000 5000`
            do
                time python sim.py $M $N $size $degree $(( $degree + 10 )) >> log.txt 2>&1
            done
        done
    done
done
