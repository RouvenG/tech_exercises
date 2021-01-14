# Terminal Seminar

## Contents

1. What is the Terminal
1. `man` and reading manuals / man-pages (synopsis)
1. path variables 
1. absolute vs relative path
1. Important commands
    1. `ls -lah`
    1. `pwd`
    1. `history` and `ctrl-r`
    1. `mkdir`
    1. `rm` and `rmdir`
    1. `cd`
    1. `df`
    1. `ps`
    1. `kill`
    1. `touch`
    1. `cat`
    1. `mv`
    1. `less`
    1. `alias`
    1. `wget`
    1. `find`
    1. `which`
    1. `grep`
    1. `sed`
    1. `echo`
    1. `tar`
    1. `tree`
    1. piping and `>`
    1. `shasum`

## Pratice

The practice session consists of a capture the flag. In capture the flag we are trying to find a set of flags hidden somewhere e.g. as the name of a file or somewhere in a file. The goal is to collect as many flags as possible. The team with the most flags in the end of the games wins.

### The flags
All the flags are 10 symbols strings like `2E4T1R3T2E9H`. They do not have a meaning by themselves. If you find one write enter it here https://forms.gle/ZJF3Qj85zZKtQy8j7. All flags are hidden in the folder `./TERMINAL_CTF`.

#### flag 1 `ls`
The first flag can be found using the ls command with the right arguments.
Hints: Size matters. Sort it

#### flag 2 `find`

Find a file which is exactly 512 bytes large. 

#### flag 3 `ps` and `grep` 

To find this flag run the program flag3. Then you have 100 secs to find the flag. If you don't find it in that time start the program again.
You have to you ps with the correct arguments and grep. The is a keyword. 
