# File-Finder

A command-line program that removes the hassle of finding and opening files and directories.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Contributing](#contributing)

## Installation

Installation is most easily done using the setup.py file that can be found in this repository. However, installation does depend on the [Click library](https://github.com/pallets/click) for user configuration options (common file paths, favorite text editor, etc.). If you haven't already installed it, then go ahead and install that before proceeding with the following commands on the command line:

```
$ python3 setup.py
```

## Usage

The structure of most all commands will be roughly as follows:

```
$ ff [file or directory name] [-flag]
```
Note that every command works with both files and directories. If you issue a command that feels unnatural, such as changing directories to a file called helloWorld.js, the program will intelligently change to the directory in which helloWorld.js is contained since changing directories to helloWorld.js makes no sense.

There are 4 main flags you can use: --change-directory (aliased as -c), --open-editor (-e), --open-finder (-f), and --duplicated (-d).
Changing directories is fairly straightforward and can be done as follows:

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

You'll notice that there's a folder on my Desktop called Find Me, which the program is able to find with ease, despite the fact that it's in a different directory from the one I'm currently in.

Opening a file or directory in your favorite editor has similar syntax:

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")


Lastly, I can open any file or directory in a new window in the Mac Finder application using the flag -f:



You can add the duplicated flag to any command if you think there's a chance that you might have two files or directories of the same name in your file system. If you only have one, it will assume that it's the one you want and will perform the relevant action like it would without the duplicated flag. If you have multiple, you will be given the opportunity to specify the file that you would like the action to be performed on.

The file or directory name option should be self evident.

You can also always type
```
$ ff --help
```
to remind yourself of the available commands if you ever forget.

## Support

Please note that this is application is currently only funcitonal on OS X. [Open an issue](https://github.com/fraction/readme-boilerplate/issues/new) for support.

## Contributing

Please contribute using [Github Flow](https://guides.github.com/introduction/flow/). Create a branch, add commits, and [open a pull request](https://github.com/fraction/readme-boilerplate/compare/).
