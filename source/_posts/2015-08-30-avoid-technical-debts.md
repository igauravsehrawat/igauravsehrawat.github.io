---
layout: post
permalink: /avoid-technical-debts/
title: How to avoid technical debts
description: "Some tips on good technical credits and bad technical debts"
tags: [code, refactor, design, debt, technical debt]
comments: true
share: true
---

Writing code can be scary especially in a collaborative environment and when you have to avoid techical debts.  


### But first what is <b>technical debt</b>?
Have a look at gif below and imagine you are coding instead of driving


<img src="/images/technical_debts.gif" style="margin-left:40%">



#### In simple words : code you wrote isn't maintable, hard to understand and does not follow code conventions of others.

So the first rule for writing code is understanding who is going to maintain it, who is going to add further code to it. And even that doesn't matter, writing good code should be a habit and shouldn't be broken at any cost. 

## Solution to bad code
+ Follow code conventions.
- For eg. while writing python follow pep8 conventions and while writing js code follow jslint conventions

+ How granular or modular code should be?
- For eg. There should be separate function for separate task. It may depend on number lines of code for that function.

+ How often comments should appear and on what severity?

## THE TRUTH
> One can't write perfect code in one go.
Refactoring, pruning is the key. May be you need to burn all your sphagetti code and it would definitely pay off.

## More concrete steps
+ Bad habits doesn't go easily. So there is pair programming for that. Pair programming reduces effort on new learning and makes new learning easy and fast. Key to good coding is good discussion. Look at the code written already and discuss about it and rewrite if needed.

+ DESIGN : Technical debts can also be attributed to wrong code designs. Design is not just about visual art, it is also the architecture of code. Fitting code is no joke. 
	+ Agility comes from good code design.

+ REFACTOR : Refactoring code brings new features to the application in current development, so refactor more and often.

> Technical debt is like karma, gonna kick you soon or later.

That's enough of water-cooler side talk. Keep avoiding technical debts.

<b>Notes</b>

Thanks <a href="https://twitter.com/trssnd" target="_blank">Shyam Sundar</a> for reading the draft.