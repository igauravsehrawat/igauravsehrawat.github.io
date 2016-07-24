---
layout: post
permalink: /productive-tips-for-command-interface/
title: productive tips for command interface particularly shell
description: "how to be a productive developer, optimizing the command line interface"
tags: [shell, bash, productive, tips, command-line]
comments: true
share: true

---


Imagine a scenario where you would prefer to type instead of clicking. That day would be epic. As a developer, it's our job to use and spend time on command interface it can be shell, bash, or it can be a editor like vim, emacs etc. Lot of optimization has been made since the beginning of these things. Today i will specifically talking about shell/bash prompt.

We generally use 20% of the features available there, to attain maximum efficiency in long term it learning rest 80% will help tremendously. So let's get down to business.

I. Using search in prompt
------------------------------
One can search through the commands one has previously typed. Just use

{%highlight bash%} Ctrl + R{%endhighlight%}

, this would enable backward search such that one can search through logged commands.



II. Using alias for long commands or shortcuts
------------------------------
For this one needs to use .bashrc or .zshrc(more about this later) file in the

{%highlight bash%}   ~/{%endhighlight%}

directory which is

{%highlight bash%} /home/username{%endhighlight%}

. There you have to add a `alias <alias_name>=<your long command>`
for eg. for using p for python use

{%highlight bash%} 'alias p='python'{%endhighlight%}

 now you can just use p python_script.py to run the python script, or you can add your ssh command to   server ip,which are pretty long. Isn't that handy!



III. Configuring rsa key for auto pushing to github/git network.
------------------------------
You might be typing username and password every time you want to push to github. There is an easy way to do this automatic. One need to paste the key from `~/.ssh/ ` directory, keep in mind the key ends in .rsa . If you have one already generated and configured with ssh-agent then paste the key in github profile settings under SSH realted area.

If you haven't done it yet, do it by using key-gen utility

{%highlight bash%} key-gen -t rsa -C "your_email_id"{%endhighlight%}

`-t` is for defining the type of key which rsa in this case
`-C` is to providing commenting so that you can identify different keys for what we are using email id.
then add generated keys to ssh-agent using

{%highlight bash%} eval "$(ssh-agent -s)"{%endhighlight%}
{%highlight bash%}ssh-add ~/.ssh/<key_id.rsa> '''{%endhighlight%}

And then follow the procedure to add it on github profile
Additonal link: [github-ssh](https://help.github.com/articles/generating-ssh-keys/){:target="_blank"}




IV. Using zsh instead of bash
------------------------------
zsh is an shell designed for interactive use, most of its features are from bash, so one can easily use as bash replacement.

+ One of most fruitful feature is one don't need to type `cd` for changing the directory. Just type directory and enter & you are in directory.

+  Other feature is intelligent autocorrection, supposedly you made some type in case, zsh would auto correct it. For modifying the configuration use file at `~/.zshrc` like adding alias or export or path.
Additional link:[zsh-link](http://zsh.sourceforge.net/)



V. Using oh-my-zsh framework for zsh
------------------------------
oh-my-zsh is most popular command line utility framework on github. It has premade zsh configuration which you would have to write otherwise in bashrc/zshrc files. you can use lot of themes from lot of community themes.

A screenshot of my terminal using oh-my-zsh is given below
![oh-my-zsh-screenshot](http://s2.postimg.org/47mlvy4nt/oh_my_zsh_screenshot.png)
Some useful mentions

+ I can see full path of my working directory

+  I can see git repository branch, i am working upon

+  I can see time stamp for each command

+  also if my git repos has been modified and there are uncommitment changes, i see all that on one terminal.

Isn't that wonderful!
Additional link:[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)



VI. Mutliple tabs instead of mulitple windows
------------------------------
Lot of people bring a new command window for different task. Using tabs is recommended since you can switch easily and also see what is running on different tab.

Just use `Alt + T ` for new tab and `Alt + <tab_number for eg.1,2 >` for switching the tab.

That's all for now. For more detailed information follow the links provided in the post

Next time it will be productive while being python developer.





