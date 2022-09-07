# 0x02-shell_redirections
## 0-hello_world
This script prints "Hello, World", followed by a new line to the standard output.
## 1-confused_smiley
This script displays a confused smiley ***"(Ôo)'***
## 2-hellofile
This script displays the content of the ***/etc/passwd*** file
## 3-twofiles
This script displays the content of ***/etc/passwd*** and ***/etc/hosts***
## 4-lastlines
This script displays the last 10 lines of ***/etc/passwd***
## 5-firstlines
This script displays the first 10 lines of ***/etc/passwd***
## 6-third_line
This script displays the third line of the file ***iacta***
## 7-file
This script creates a file named exactly ***\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)*** containing the text Best School ending by a new line
## 8-cwd_state
This script writes into the file ls_cwd_content the result of the command ***ls -la*** and overwrites the file if it already exists
## 9-duplicate_last_line
This script duplicates the last line of the file ***iacta***
## 10-no_more_js
This script deletes all the regular files (not the directories) with a ***.js*** extension that are present in the current directory and all its subfolders
## 11-directories
This script counts the number of directories and sub-directories in the current directory
- The current and parent directories are taken into account
- Hidden directories are counted
## 12-newest_files
This script displays the 10 newest files in the current directory
- One file per line
- Sorted from the newest to the oldest
## 13-unique
This script takes a list of words as input and prints only words that appear exactly once
- Input format: One line, one word
- Output format: One line, one word
- Words should be sorted
## 14-findthatword
This script displays lines containing the pattern ***root*** from the file ***/etc/passwd***
## 15-countthatword
This script displays the number of lines containing the pattern ***bin*** in the file ***/etc/passwd***
## 16-whatsnext
This script displays lines containing the pattern ***root*** and 3 lines after them in the file ***/etc/passwd***
## 17-hidethisword
This script displays all the lines in the file ***/etc/passwd*** that do not contain the pattern ***bin***
## 18-letteronly
This script displays all lines of the file ***/etc/ssh/sshd_config*** starting with a letter
- Capital letters are included as well
## 19-AZ
This script replaces all characters ***A*** and ***c*** from input to ***Z*** and ***e*** respectively
## 20-hiago
This script removes all letters ***c*** and ***C*** from input
## 21-reverse
This script reverses its input
## 22-users_and_homes
This script displays all users and their home directories, sorted by users
- Based on the the ***/etc/passwd*** file
## 100-empty_casks
This script finds all empty files and directories in the current directory and all sub-directories
- Only the names of the files and directories are displayed (not the entire path)
- Hidden files are listed
- One file name per line
- The listing ends with a new line
## 101-gifs
This script lists all the files with a ***.gif*** extension in the current directory and all its subdirectories
- Hidden files are listed
- Only regular files (not directories) are listed
- The names of the files are displayed without their extensions
- The files are sorted by byte values, but case-insensitive
- One file name per line
- The listing ends with a new line
## 102-acrostic
This script decodes acrostics that use the first letter of each line
- The ***decoded*** message ends with a new line
## 103-the_biggest_fan
This script parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests
- Ordered by number of requests, most active host or IP at the top
