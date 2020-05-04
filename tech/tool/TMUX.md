# TMUX
## Inside
c-b is the main key to trigger tmux commands.

after c-b you can use the following keys to do things.

### session
d " detach

### windows
c " create a new windown

w " list all the windows

p " previous window

n " next window

3 " jump to window 3

& " close window

, " rename window

### panes
% " vertical split

:sp " horizontally split

x " close x

## Outside
When starting tmux, you can do tmux -s name_of_session

tmux list-sessions " to show the existing session

tmux attach " to recover the session

tmux attach -b name_of_session


### Rename Session
`tmux list-sessions`

It shows in the format of `name: number of windows`.

`tmux rename-session [-t current-name] [new-name]`

if -t is not provided, the most recent one will be used.
