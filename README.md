# xenblocks lightnode
Voter fetches records from XENBLOCKs ledger and runs verification in CPU 

Installation instructions:

Clone the repo:

$ git clone https://github.com/xenkonieczny/voter

$ cd voter

Install Rust:

$ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

. "$HOME/.cargo/env"

check if cargo is installed:

$ cargo -v 

sudo apt install pkg-config libssl-dev
sudo apt install build-essential

Build project:

$ cargo build --release

Run lightnode:

$ ./target/release/voter

During initialization, the node will create id.json file with your private key so you are be identified among other nodes,
this is also where you will receive your future rewards.
As your lightnode runs, it will submit computed data to xenblocks consensus ledger, which can be accessed here:
http://xenminer.mooo.com:5000/show_data (update: http://xenblocks.io:5000/store_data)



The node will also write into a log file (voter.log) in the same directory.

Update xenkonieczny:

+address update http://xenblocks.io:5000/store_data


tips&tricks:

if linker cc not found use:

sudo apt update

sudo apt install build-essential
