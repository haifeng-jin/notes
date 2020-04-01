# Screen
#tech/tool
This is used for keep the process running on the machine you ssh to,
even you disconnected from the ssh and shutdown your local computer.

First ssh to the machine normally.
Type "screen".
It would open a empty shell for you.
Run the process in this shell.
Press "Ctrl + A, Ctrl + D" to switch back to the normal shell.
You can log off, shutdown or anything.
When you want to see that process again, ssh to the machine and type "screen -r".