# C #

Install `gcc` and other dev tools, e.g. make on Ubuntu with
```
sudo apt install build-essential
```

Save the following to `helloworld.c`

    #include <stdio.h>
    int main() {
       printf("Hello, World!");
       return 0;
    }

Compile and link `helloworld.c` with

    gcc helloworld.c -o helloworld

Running `ls -l` shows the executable `helloworld` is 15968 bytes in size.
