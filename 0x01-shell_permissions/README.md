# 0x01-shell_permissions
## 0-iam_betty
This script switches the current user to the user named betty
## 1-who_am_i
This script prints the effective username of the current user
## 2-groups
This script prints all the groups the current user is part of
## 3-new_owner
This script changes the owner of the file 'hello' to the user 'betty'
## 4-empty
This script creates an empty file called 'hello'
## 5-execute
This script adds execute permission to the owner of the file 'hello'
## 6-multiple_permissions
This script adds execute permission to the owner and group owner, and read permission to other users to the file 'hello'
## 7-everybody
This script adds execution permission to the owner, group owner and the other users, to the file 'hello'
## 8-James_Bond
This script sets owner and group permission to no permission at all and gives other users all the permissions
## 9-John_Doe
This script sets the mode of the file 'hello' to '-rwxr-x-wx'
## 10-mirror_permissions
This is a script that sets the mode of the file 'hello' the same as 'olleh''s mode
## 11-directories_permissions
This script adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users
## 12-directory_permissions
This script creates a directory called 'my_dir' with permissions '751' in the working directory 
