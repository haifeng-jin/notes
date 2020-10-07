# Git
#tech/software engineering#

## Basics
* The normal way to contribute to a public repo with git.
[https://github.com/junit-team/junit4/blob/e848a97320851c8614cf9712fa5e2b5092d82925/CONTRIBUTING.md](https://github.com/junit-team/junit4/blob/e848a97320851c8614cf9712fa5e2b5092d82925/CONTRIBUTING.md)

* Forked sync changes in the upstream repo:
[https://help.github.com/articles/configuring-a-remote-for-a-fork/](https://help.github.com/articles/configuring-a-remote-for-a-fork/)
[https://help.github.com/articles/syncing-a-fork](https://help.github.com/articles/syncing-a-fork/) [/](https://help.github.com/articles/syncing-a-fork/)

* Delete a branch.
`git branch -d branch_name`

* List all the branches.
`git branch`

* Switch to a branch
`git checkout branch_name`

* Git make the current branch exactly the same as upstream.
`git fetch upstream`
`git reset --hard upstream/master`
`git push -f origin [current_branch_name]`

* Delete a branch remotely
`git push origin --delete <branchName>`

* How to checkout a remote branch that doesn't exist locally?

`git branch -v -a` To see all the branches available for checkout.
`git fetch`
`git checkout <branch_name>` The branch name should not contain origin/ or remotes/.

* How to deal with a detached HEAD?

It is caused by checking out a remote branch directly like `git checkout origin/devel`
Or caused by checkout a commit with SHA1.
It is starting a new route from a previous node (commit).
So you need to create a branch to save the changes on the detached HEAD.
Just use `git checkout -b <branch_name>` is good enough.

* Show remote URL.
`git remote show origin`

## Tags

List the tags
```
git tag
```

Get pull the tags
```
git fetch
```

Add a tag
```
git tag -a tag_name
git push origin tag_name
```

## Undo Things
* How to undo a commit (not pushed to remote) to unstagged?
`git reset HEAD~`

* How to revert the last several commits?
First you can use `git reset <SHA1>` 
and `git push origin <branch_name> -f`.
However, this is not recommended, since it lost the information of those commits in the commit history.
You should use revert.
If only revert one commit, just `git revert <SHA>`. This command will directly fire a new commit for you to reverse the changes.
If multiple revert, use `git revert -n <SHA>` multiple times for different commits in the latest to the oldest order. `-n` means do not auto fire a commit for it.
If the commit to be reverted is a merge commit, use `git revert -n <SHA> -m 1` to revert to the 1st branch or `-m 2` to revert to the second branch.
Then make a commit.
It can only revert the last changes, instead of jumping over some commits and revert the previous ones.

* How to revert commits in the middle of the history?
If we have commit A B C D E, and you want to revert B and C.
You first `git checkout -b <new_branch_name> <SHA of A>`.
Then cherry-pick the commits from D to E with `git cherry-pick <SHA of D>..<SHA of E>`.

* how to delete a tag?
`git tag -d [tag_name]`
`git push origin :[tag_name]`

* how to delete a release?
click the release name. The delete button is on the top right.

* How to stash?
We stash the uncommited changes and pull from remote and unstash them to apply.
`git stash`
`git stash pop`

## Clean Up
`rebase master -i`

## Sync with Remote
Force push the local changes.

`git push origin branch_name --force-with-lease`

Force pull.

```shell
git checkout branch_name
git fetch --all
git reset --hard origin/branch_name
```
## Across Branches
### How to merge two branches?
You can use git merge but not recommended.
git rebase is more professional.
For example, you are rebasing the master branch when you are on a feature branch.
It would start from the current master branch head,
and add the commits of your feature branch one by one to it.
So that in the log of the current branch (feature) the commits from master would before the commits of the feature branch.
If there is a conflict, it would stop and ask you to solve.
You just solve it and git add the files with conflicts.
and no commit is needed just use `git rebase --continue` to continue the rebase process.
When push to the remote branch, it needs to use 
`git push --force-with-release origin branch_name` .

### How to cherry-pick?

Just find the commit in other branch you need.
And on the branch you want to add the commit, execute `git cherry-pick <SHA>`.


### Working on a branch with a dependence on another branch that is being reviewed

feature_b is created like this
`git checkout feature_a`
`git checkout -b feature_b`

update feature_b for the latest changes in feature_a
`git checkout feature_b`
`git rebase feature_a`

When feature_a has been merged into master, you simply get the new master and rebase feature_a onto it a last time:
`git checkout master`
`git pull origin master`
`git checkout feature_b`
`git rebase --onto master feature_a feature_b`
