---
layout: post
permalink: /escalating-from-octopress/
title: Escalating from octopress to jekyll
description: "Why jekyll over octopress !!"
tags: [octopress ,jekyll]
comments: true
share: true
---

Octopress is derived from jekyll itself . It is very much automated with commands but it is mainly for blogging. 
{% highlight ruby %}
    rake new_post["escalating from octopress to jekyll"]
{% endhighlight %}
but in jekyll
{% highlight ruby %}
    touch 2014-04-19-escalating-from-octopress-to-jekyll
{% endhighlight %}
#why jekyll ?
Jekyll because it has super power . Jekyll can handle having post and pages for the website , while the octopress is only able to handle only post . 

thats one only no ?

instead of 
{% highlight ruby%}
rake deploy
{% endhighlight ruby%}

one uses

{% highlight ruby%}
jekyll build
{% endhighlight ruby%} 
and push directly to github along with markdown files , which is very handy feature incase one lost blog . It can be regenerated again.

Not to mention the awesome liquid tags . and emoji {{content | emojify }} :smiley:

#what superpower-jekyll got ?

1. Behind the scene jekyll generates the html code which github.io pages can understand . 


2. Jekyll is also the wizard behind handling gh-pages on github i.e the github pages can recognize if the sites is build in jekyll so it will handle it in jekyll gem way . 

3. The best thing one can mix HTML with markdown .

4.More over it , it build with hackers tendency i.e code for everything.

#best place to learn jekyll ?

Official documentation is the best @ <a href="http://jekyllrb.com/docs/home"> jekyll docs</a>. 


