Why to use tinycmd?
=============

Have you ever been in situation where you wanted to help a friend or relative to install or configure something on their computer, but they didn’t really have a computer background?

If you did it, you know that in many cases it is not simple in the graphical interface, as you have to imagine another person’s desktop, which can greatly vary on different computers.

In these cases, it is much simpler to just ask the person to open up a terminal window and type a command string. However, will it be easy for the person without a computer background to type what you say?

If you use phone, it can be hard for them to find the special characters on the keyboard, and they can also put whitespaces in the wrong places of the command string.

When using text, in another hand, it can be necessary to first explain them how the clipboard works (and how they can copy the command string), and to then understand why the command is not working correctly (they can, for example, copy everything except the last character of the string).

The solution is to use command string shortening — tinycmd.

You can simply save your command right here, and then, for running it (if tinycmd is installed on the computer), the person just needs to type this in the terminal and press return:

    t 2b3

Where `t` is the tinycmd command and `2b3` is an unique shortcut for the command.

You can also use it for presentations and master classes, or if you need to use a piece of paper to write a manual for someone.

Theoretical feature ideas
=============

1. Adding command strings from the command line, using the t command.
2. Viewing the command before execution, and canceling the execution
in a short period of time (for example, 5 seconds before execution).
3. Commenting (maybe even with threads) the command strings on the website.
