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
      - [Modes](#modes)
    - [Installing from a URL](#installing-from-a-url)
    - [Linux File Types](#linux-file-types)
  - [Commands](#commands)
  - [Users and Groups](#users-and-groups)
    - [Types of Users](#types-of-users)
  - [How to read `/etc/passwd` file](#how-to-read-etcpasswd-file)
  - [File Permissions](#file-permissions)
    - [Permissions Breakdown](#permissions-breakdown)
    - [Octal Notation](#octal-notation)
    - [Symbolic Notation](#symbolic-notation)
    - [Permission Categories](#permission-categories)
    - [Practical Use](#practical-use)
    - [Symbolic Notation (`dr-xr-xr-x`)](#symbolic-notation-dr-xr-xr-x)
    - [Octal Notation](#octal-notation-1)
    - [Converting `dr-xr-xr-x` to Octal](#converting-dr-xr-xr-x-to-octal)
  - [`sudo` Command](#sudo-command)

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

#### Modes

- `Normal mode`: The mode in which you can navigate through the file and perform actions like copying, pasting, and deleting text.
- `Insert mode`: The mode in which you can insert text.
- `Visual mode`: The mode in which you can select text.


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

Yeah now that I am looking at it, this could have been done with:
```bash
wget https://release.archboot.com/aarch64/latest/iso/archboot-2024.04.30-17.10-6.8.7-1-aarch64-ARCH-aarch64.iso.sig
```

### Linux File Types

- `-`: Regular file
- `d`: Directory
- `l`: Symbolic link
- `c`: Character device file
- `b`: Block device file
- `s`: Socket file
- `p`: Named pipe
- `D`: Door
- `n`: Network file
- `?`: Other file
- `!`: Doors

> you can use `file` command to determine the file type

```bash
[root@fedora-linux-38 /]# file /etc/passwd
/etc/passwd: ASCII text
```

## Commands

- `grep`: Print lines matching a pattern
  - `grep -i`: Ignore case
  - `grep -v`: Invert match
  - `grep -r`: Recursive search
- `find`: Search for files in a directory hierarchy
  - `find / -name file.txt`: Search for a file
  - `find / -type d`: Search for a directory
  - `find / -type f`: Search for a file
  - `find / -user user1`: Search for files owned by a user
  - `find / -size +1G`: Search for files greater than 1GB
  - `find / -size -1G`: Search for files less than 1GB
  - `find / -empty`: Search for empty files and directories
  - `find / -mtime -1`: Search for files modified in the last 24 hours
  - `find / -mtime +1`: Search for files modified more than 24 hours ago
  - `find / -exec command {} \;`: Execute a command on the search results
- `chmod`: Change file mode bits
  - `chmod 777 file.txt`: Give all permissions to everyone
  - `chmod 755 file.txt`: Give read, write, and execute permissions to the owner, and read and execute permissions to others
  - `chmod 700 file.txt`: Give all permissions to the owner, and no permissions to others
  - `chmod u+x file.txt`: Give execute permission to the owner
  - `chmod g+w file.txt`: Give write permission to the group
  - `chmod o-r file.txt`: Remove read permission from others
- `chown`: Change file owner and group
  - `chown user1 file.txt`: Change the owner of a file
  - `chown user1:group1 file.txt`: Change the owner and group of a file

## Users and Groups

- Users and Groups are used to control access to the system and its resources.
- Users login to the system and have unique usernames.
- Every process has an owner and group affiliation.

### Types of Users

| User Type | Description        | User ID (UID) | Group ID (GID) | Home Directory           | Shell         |
|-----------|--------------------|---------------|----------------|--------------------------|---------------|
| Root      | Superuser          | 0             | 0              | /root                    | /bin/bash     |
| Regular   | Normal user        | 1000+         | 1000+          | /home/user1              | /bin/bash     |
| Service   | ftp, apache, mysql | 1-999         | 1-999          | /var/www, /var/lib/mysql | /sbin/nologin |

## How to read `/etc/passwd` file

Here is a sample `/etc/passwd` file:

```bash
root:x:0:0:Super User:/root:/bin/bash
bin:x:1:1:bin:/bin:/usr/sbin/nologin
daemon:x:2:2:daemon:/sbin:/usr/sbin/nologin
adm:x:3:4:adm:/var/adm:/usr/sbin/nologin
lp:x:4:7:lp:/var/spool/lpd:/usr/sbin/nologin
sync:x:5:0:sync:/sbin:/bin/sync
shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown
halt:x:7:0:halt:/sbin:/sbin/halt
mail:x:8:12:mail:/var/spool/mail:/usr/sbin/nologin
```

- `root`: Username
- `x`: Password placeholder
- `0`: User ID (UID)
- `0`: Group ID (GID)
- `Super User`: User description
- `/root`: Home directory
- `/bin/bash`: Shell

Here is the groups output from `/etc/group` file:

```bash
parallels:x:1000:
domhallan:x:1001:
```

The `id` command can be used to display the user and group information for the current user:

```bash
[root@fedora-linux-38 etc]# id domhallan
uid=1001(domhallan) gid=1001(domhallan) groups=1001(domhallan),10(wheel)
```

The `useradd` command can be used to add a new user:

```bash
[root@fedora-linux-38 etc]# useradd ansible
```

The `groupadd` command can be used to add a new group:

```bash
[root@fedora-linux-38 etc]# groupadd devops
```

We can run `usermod` to add a user to a group and the `id` command to verify the changes:

```bash
[root@fedora-linux-38 etc]# usermod -aG devops ansible
[root@fedora-linux-38 etc]# id ansible
uid=1002(ansible) gid=1002(ansible) groups=1002(ansible),1003(devops)
```

> You can also add users in the `/etc/group` file manually, but it is not recommended.

You can use the `passwd` command to change the password for a user:

```bash
[root@fedora-linux-38 etc]# passwd ansible
Changing password for user ansible.
New password:
Retype new password:
passwd: all authentication tokens updated successfully.
```

`lsof -u user1` command can be used to list all open files for a user:

```bash
[root@fedora-linux-38 etc]# lsof -u domhallan
COMMAND   PID USER   FD   TYPE DEVICE SIZE/OFF    NODE NAME
systemd     1 root  cwd    DIR    8,1     4096       2 /
systemd     1 root  rtd    DIR    8,1     4096       2 /
```

`userdel` and `groupdel` commands can be used to delete a user and group respectively:

```bash
[root@fedora-linux-38 etc]# userdel ansible
[root@fedora-linux-38 etc]# groupdel devops
```

## File Permissions

- `r`: Read
- `w`: Write
- `x`: Execute
- `-`: No permission
- `d`: Directory
- `l`: Symbolic link
- `s`: Setuid or Setgid
- `t`: Sticky bit

Here is an example of file permissions:

```bash
[root@fedora-linux-38 /]# ls -l
total 28
dr-xr-xr-x.   1 root root    0 Jan 23 19:00 afs
lrwxrwxrwx.   1 root root    7 Jan 23 19:00 bin -> usr/bin
dr-xr-xr-x.   9 root root 4096 May  7 14:51 boot
lrwxrwxrwx.   1 root root   37 May  7 15:40 cmds -> /opt/dev/ops/devops/test/commands.txt
```

In the first line of the output, the permissions are `dr-xr-xr-x`. Here is the breakdown:

- `d`: Directory
- `r-x`: Owner has read and execute permissions
- `r-x`: Group has read and execute permissions
- `r-x`: Others have read and execute permissions
- `1`: Number of links
- `root`: Owner
- `root`: Group
- `0`: Size
- `Jan 23 19:00`: Last modified date
- `afs`: File name

### Permissions Breakdown

|Octal  |Symbol |Permission
|-------|-------|----------|
`0` | `---`| No permissions|
`1` | `--x`| Execute|
`2` | `-w-`| Write|
`3` | `-wx`| Write and execute|
`4` | `r--`| Read|
`5` | `r-x`| Read and execute|
`6` | `rw-`| Read and write|
`7` | `rwx`| Read, write and execute|


### Octal Notation
- **Octal (base-8)** notation simplifies the setting of permissions by condensing the symbolic notation into a single digit per user/group/others classification. Each octal digit can represent a combination of read, write, and execute permissions.

### Symbolic Notation
- **Symbolic** notation represents permissions using characters: `r` for read, `w` for write, and `x` for execute. A dash (`-`) represents the absence of a permission.

### Permission Categories
1. **`0` (`---`)**: No permissions. Neither the owner, nor the group, nor others can read, write, or execute the file.
2. **`1` (`--x`)**: Execute permission only. The file can be executed but not read or written.
3. **`2` (`-w-`)**: Write permission only. The file can be modified but not executed or read.
4. **`3` (`-wx`)**: Write and execute permissions. The file can be modified and executed but not read.
5. **`4` (`r--`)**: Read permission only. The file can be read but not written to or executed.
6. **`5` (`r-x`)**: Read and execute permissions. The file can be executed and read but not written to.
7. **`6` (`rw-`)**: Read and write permissions. The file can be modified and read but not executed.
8. **`7` (`rwx`)**: Full permissions. The file can be read, written to, and executed.

### Practical Use
Permissions are typically set for three categories: owner, group, and others. An octal code for each category determines the permissions, typically shown as three digits. For example, `755` in Unix permissions would translate to `rwx` for the owner, and `r-x` for both the group and others. This setup is common for web servers where the owner needs full control over the files, but the files only need to be readable and executable by others.

These permissions are crucial for security and functionality in a Unix-like system, allowing fine-grained control over who can do what with a file or directory. Understanding and correctly setting these permissions is key to managing a secure and efficient system.

In Unix and Unix-like systems, file permissions are depicted in both symbolic notation (like `dr-xr-xr-x`) and can also be represented in octal notation, but they describe two different aspects of how permissions are stored and displayed.

### Symbolic Notation (`dr-xr-xr-x`)
- The first character (`d` in your example) indicates the type of file. Here, `d` stands for directory. Other common types include `-` for a regular file and `l` for a symlink.
- The next nine characters represent the permissions for three different categories in three sets of three:
  - The first set (`r-x`) is for the owner (user) permissions.
  - The second set (`r-x`) is for the group permissions.
  - The third set (`r-x`) is for others (world) permissions.
- Each set consists of three positions:
  - `r` (read)
  - `w` (write)
  - `x` (execute)
- A dash (`-`) indicates the absence of a permission.

### Octal Notation
- The octal notation simplifies the symbolic notation into a three-digit number, each digit corresponding to one of the user categories (user, group, others).
- Each digit is the sum of its constituent permissions, calculated as follows:
  - Read (`r`) has a value of 4.
  - Write (`w`) has a value of 2.
  - Execute (`x`) has a value of 1.

### Converting `dr-xr-xr-x` to Octal
- For each set of `r-x`:
  - `r` = 4
  - `-` = 0 (no write permission)
  - `x` = 1
- So, `r-x` translates to `4 + 0 + 1 = 5`.

Therefore, `dr-xr-xr-x` corresponds to the octal permissions `555`. Each `5` represents `r-x`, which you can confirm by adding up the values for each permission in the sets (Read + Execute).

In summary, the octal notation comes from a method of summarizing the binary values of the permissions (where each permission is a binary flag) into more compact, base-8 digits, which is useful for quickly setting and understanding file permissions at a glance in command-line operations.

## `sudo` Command

The `sudo` command allows users to run programs with the security privileges of another user (by default, the superuser). It is used to execute a command as another user, typically the superuser.

The `sudo` command is used to run a command with the security privileges of another user (by default, the superuser). It is typically used to perform administrative tasks that require root access.

The sudo command, which stands for "superuser do", is a powerful command in Unix and Linux-based systems that allows a permitted user to execute a command as the superuser or another user, as specified in the sudoers file.

Here are some important points about sudo:

- It's often used for commands that require elevated permissions, such as installing software or changing system configurations.
- The sudo command provides an audit trail of the commands run with superuser privileges. This can be useful for system administrators to track changes made to the system.
- When you use sudo, you'll be prompted for your password, not the root password. This is a security feature.
- The sudo command has a timeout feature. By default, once you've entered your password, you won't be asked for it again for a period of time (usually 15 minutes).
- The sudo command can be configured to provide certain users with specific permissions to certain commands, providing fine-grained control over user permissions.

Here's an example of using sudo:

```bash
sudo apt-get update
```

We can add users to the sudo group to grant them sudo privileges:

```bash
usermod -aG sudo username
```

And we can also add them to the sudoers file:

```bash
echo "username ALL=(ALL) ALL" >> /etc/sudoers
```

This line of code is a command that is typically run in a Unix-like operating system's terminal. It's written in shell script, which is a scripting language used for system administration.

The `echo` command is used to output the strings that are passed to it. In this case, the string is "username ALL=(ALL) ALL".

The `>>` operator is used to append the output of the command on its left to the file on its right. If the file doesn't exist, it will be created.

The /etc/sudoers file is a configuration file for the sudo command. sudo stands for "superuser do", and it's used to run commands with the privileges of another user, typically the superuser (or root).

The string `"username ALL=(ALL) ALL"` is a rule that's being added to the sudoers file. This rule means that the **user username is allowed to run any command as any user on any host**.

`username` is `the user` this rule applies to. Replace this with the actual username.
The first ALL is the hosts this rule applies to. In this case, it's all hosts.
The `=(ALL)` part specifies the users the commands can be run as. Again, it's all users.
The last ALL is the commands this rule applies to. Yet again, it's all commands.
This is a very permissive rule. In a real-world scenario, you'd likely want to limit the commands a user can run with sudo, the users they can run commands as, or the hosts they can run commands on.

Please note that editing the sudoers file directly can be risky. If you make a mistake, you could lock yourself out of your system. It's generally recommended to use the visudo command to edit the sudoers file, as it includes syntax checking to prevent you from saving a file with errors.
