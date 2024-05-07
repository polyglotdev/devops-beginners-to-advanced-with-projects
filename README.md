# DevOps Beginners to Advanced with Projects

[DevOps Beginners to Advanced with Projects](https://www.udemy.com/course/decodingdevops/)

## Table of Contents

- [DevOps Beginners to Advanced with Projects](#devops-beginners-to-advanced-with-projects)
  - [Table of Contents](#table-of-contents)
  - [What is DevOps?](#what-is-devops)
  - [What is Continuous Integration?](#what-is-continuous-integration)
  - [What is Continuous Deployment?](#what-is-continuous-deployment)
  - [Virtualization](#virtualization)
  - [Linux](#linux)
    - [Commands and File System](#commands-and-file-system)
    - [Where things live on the filesystem](#where-things-live-on-the-filesystem)
    - [VIM Editor](#vim-editor)
    - [Installing from a URL](#installing-from-a-url)

## What is DevOps?

DevOps is a set of practices that combines software development (Dev) and IT operations (Ops). It aims to shorten the systems development life cycle and provide continuous delivery with high software quality. DevOps is complementary with Agile software development; several DevOps aspects came from Agile methodology.

## What is Continuous Integration?

Continuous Integration (CI) is a development practice that requires developers to integrate code into a shared repository several times a day. Each check-in is then verified by an automated build, allowing teams to detect problems early.

## What is Continuous Deployment?

Continuous Deployment is a software release process that uses automated testing to validate if changes are correct and if they meet quality criteria. It is the natural extension of Continuous Integration: an approach in which teams ensure that every change to the system is releasable.

## Virtualization

Virtualization is the process of creating a software-based, or virtual, representation of something, such as virtual applications, servers, storage, and networks. It is the single most effective way to reduce IT expenses while boosting efficiency and agility for all size businesses.

## Linux

Linux is a family of open-source Unix-like operating systems based on the Linux kernel, an operating system kernel first released on September 17, 1991, by Linus Torvalds. Linux is typically packaged in a Linux distribution.

Linus Torvalds released the Linux kernel in 1991. He developed the Linux kernel on MINIX using the GNU C Compiler. He was inspired by MINIX, a Unix-like operating system based on a microkernel architecture.

### Commands and File System

- `ls`: List files and directories
- `pwd`: Print working directory
- `cd`: Change directory
- `touch`: Create a file
- `mkdir`: Create a directory
- `rm`: Remove a file
- `rmdir`: Remove a directory
- `cp`: Copy files and directories
- `mv`: Move and rename files and directories
- `cat`: Concatenate files and print on the standard output
- `more`: File perusal filter for crt viewing
- `less`: Opposite of more
- `head`: Output the first part of files
- `tail`: Output the last part of files
- `grep`: Print lines matching a pattern
- `find`: Search for files in a directory hierarchy
- `chmod`: Change file mode bits
- `chown`: Change file owner and group
- `ps`: Report a snapshot of the current processes
- `kill`: Send a signal to a process
- `killall`: Kill processes by name
- `ifconfig`: Configure a network interface
- `ping`: Send ICMP ECHO_REQUEST to network hosts

### Where things live on the filesystem

- `/`: The root directory
- `/bin`: Essential command binaries
- `/boot`: Static files of the boot loader
- `/dev`: Device files
- `/etc`: Host-specific system configuration
- `/home`: Home directories
- `/lib`: Essential shared libraries and kernel modules
- `/media`: Mount point for removable media
- `/mnt`: Mount point for mounting a filesystem temporarily
- `/opt`: Add-on application software packages
- `/proc`: Virtual filesystem providing process and kernel information

> `cat /etc/os-release` # Display the operating system name and version

### VIM Editor

- `i`: Insert mode
- `Esc`: Normal mode
- `:w`: Save
- `:q`: Quit
- `:wq`: Save and quit
- `:q!`: Quit without saving
- `dd`: Delete a line
- `yy`: Copy a line
- `p`: Paste a line
- `u`: Undo
- `Ctrl + r`: Redo
- `:set number`: Show line numbers
- `:set nonumber`: Hide line numbers
- `:set autoindent`: Enable auto-indent
- `:set noautoindent`: Disable auto-indent
- `:set hlsearch`: Highlight search results
- `:set nohlsearch`: Disable highlight search results
- `:set ignorecase`: Ignore case when searching
- `:set noignorecase`: Do not ignore case when searching
- `:set incsearch`: Show search results incrementally

### Installing from a URL

Here is the command I ran `wget -r -np -nH --cut-dirs=3 -R "index.html*" https://release.archboot.com/aarch64/latest/`

- `-r`: Turn on recursive retrieving
- `-np`: Do not ever ascend to the parent directory
- `-nH`: Disable generation of host-prefixed directories
- `--cut-dirs=3`: Ignore 3 directory components
- `-R "index.html*"`: Reject files matching the pattern
- `https://release.archboot.com/aarch64/latest/`: URL to download
- `wget`: The non-interactive network downloader

In all honesty, I don't think I needed to download everything from the url, I needed the ISO. but its a start!
