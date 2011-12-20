`cycletee` is inspired by `tee`. It reads every line from `stdin`, and cycle print line to output file


Example
=============

    seq 10 | ./tee 1.txt 2.txt 3.txt

    cat 1.txt // prints 1, 4, 7, 10

    cat 2.txt // prints 2, 5, 8

    cat 3.txt // prints 3, 6, 9

Compilation
=============

* Download GNU coreutils >= 8.14 and extract

* link `cycletee.c` to `coreutils-x.xx/src` directory

* run `configure` in `coreutils-x.xx` directory

* run `make` in `coreutils-x.xx/src` directory
