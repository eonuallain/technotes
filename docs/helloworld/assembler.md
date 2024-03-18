# Assembler #

Install `nasm` if not available on your system. On my Ubuntu box I ran
```
sudo apt install -y nasm
```

Save the following to `helloworld.asm`

    section .data
        hello db 'Hello, World!', 0

    section .text
        global _start

    _start:
        ; write the string to stdout
        mov eax, 4
        mov ebx, 1
        mov ecx, hello
        mov edx, 13
        int 0x80

        ; exit the program
        mov eax, 1
        xor ebx, ebx
        int 0x80

Compile `helloworld.asm` with

    nasm -f elf32 -o helloworld.o helloworld.asm

Use the GNU linker to create an output file (executable) `helloworld` from the `helloworld.o` object file

    ld -m elf_i386 -o helloworld helloworld.o

`ld -V` will list the available emulations which can be used with the above `-m` parameter

    GNU ld (GNU Binutils for Ubuntu) 2.38
      Supported emulations:
       elf_x86_64
       elf32_x86_64
       elf_i386
       elf_iamcu
       elf_l1om
       elf_k1om
       i386pep
       i386pe

Running `ls -l` shows the executable `helloworld` is 8648 bytes in size.
