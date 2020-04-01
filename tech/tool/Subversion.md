# Subversion
svn list: show contents
svn mkdir [address] -m "discription of the repository": create a new repository
svn co [address]: check out a directory to local
svn add [file/directory]: add to the server
svn commit -m "discription of the transaction": push changes to the server
svn up: update to the newest version
svn log: show all the changes

how to create a local repository

```
$ mkdir /home/user/svnrep
$ cd ~/svnrep
$ svnadmin create project1
```

#tech/tool