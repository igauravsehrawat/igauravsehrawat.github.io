---
layout: post
permalink: /programming-in-haskell/
title: Programming-in-haskell
description: "learning haskell & why functional language"
tags: [programming,haskell,academia]
comments: true
share: true
---

Haskell is a functional language & very different from imperative langauges such as python,ruby,c++..etc . It is also called declarative language, the reason is simple one just describe the problem in the program instead of instructions on how to solve the problem .

## Why Haskell ?

It's just not the haskell , this is about functional language , equal importance is for the Scala . The main context for functional langauge is involvement of "Academia" , which other imperative language fails to bridge . It so much fun to learn mathematics and science using functional langauge .

## Syntax

Syntax might seems very unconventional to conventional programmers , but it's just for the good . Functional programming discourages mutable variable & does not allow reassignment to variable.

Haskel limelight:
{% highlight haskell%}
"-- " is used for comments
let this = [ 1,23,42,97] -- 'this' represents variable name for the list
length this  -- length is a function
				--notice while passing arguments no brackets are used
let start = head this -- return the first element of list

let latter = tail this -- return list apart from head

let access = this !! 2 -- '!!' used to access element 2 tell the possition.
						--	ofcourse indexing begins with "0"

null this --null is function 'this ' act as argument will return true if argument is null

let loop = repeat 4 --repeat act as infinite loop and generate an infinte list
					--infinity concept is just kept in mind
let slice = take 2 this --slice first two elements from the list
let duplicate  = replicate 2 5  --finite loop for generating argument 'n' times


let append = x ++ y -- (++) appends two lists one after another

let two_dim = [[1,4,5],[2,9,7],[1,2,3]] --syntax for two dimensional list

let concatenation = concat two_dim --this would reduce two dimensional list to one dimensional by concatenating each sublist to single list
{% endhighlight haskell%}

Well if you reached so far , won't you like to evaluate yourself .
{%highlight haskell%}
expandList :: [Int] -> [Int]
expandList lst = if null lst then [] else (replicate (head lst) (head lst)) ++ expandList(tail lst)
{% endhighlight haskell%}
You have to guess the purpose of above function .

Put it in comment section .
