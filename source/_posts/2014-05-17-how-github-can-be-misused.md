---
layout: post
permalink: /how-github-can-be-misused/
title: how-github-can-be-misused
description: "knowledge of github tricks"
tags: [github,git]
comments: true
share: true
---

Github can land you in trouble if you don't know some hacks of it .

+ For example using  a hack ,one can add any collaborator to repository without acknowledgement of the collaborator . Yes , any  collaborator. The commit wil appear as if that person just contributed to the code base. 

How ? 

{% highlight bash %}
git -config user.name <any_user_in_the_world>
git -config user.email <email_of_that_user>
{% endhighlight bash %}

so now when you push the user would not be you but the user you specified. 

+ Apart from that one can also host website without getting tracked or traced ,and that too for free.  

+ One more bad trick is changing git commit time , which is very misleading for bad purpose . One can check gitcheatsheet <b><a href="https://github.com/igauravsehrawat/Utility-scripts/blob/master/productivity/git_cheatsheet">here</a></b>.

