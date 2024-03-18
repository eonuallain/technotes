# Rust #

From the [installation methods](https://forge.rust-lang.org/infra/other-installation-methods.html) page on [rust-lang.org](https://rust-lang.org) run the following in your shell and follow the steps presented.

    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s --

When the installation is finished run the following which adds `~/.cargo/bin` to your PATH environment variable.

    source ~/.cargo/env

Use cargo to create a new project (binary by default), and run it:

    cargo new helloworld
    cd helloworld

    cargo run

    Compiling helloworld v0.1.0 (/home/pi/helloworld)
    Finished dev [unoptimized + debuginfo] target(s) in 3.51s
        Running `target/debug/helloworld`
    Hello, world!

Running `ls -l` shows the executable `helloworld` is 3792552 bytes in size for the default debug build and 3783888 for a release build (`cargo build --release`).