---
layout: post
title: "A puzzle for you today"
permalink: /a-puzzle-for-you-today/
description: "Brain gymkhana in the form of puzzle"
tags: ["puzzle", "binary", "brain-teaser", "gymkhana"]
share: true
comments: true
---

This puzzle is from my mentor and I like how it is very pragmatic and not just a brain-teaser. So the official language of the puzzle is as below


>*Matter of Life or Death*

> An evil wizard imprisoned 64
mathematicians. The wizard announces: “Tomorrow I will have you all
stand in a line, one behind the other, and put a hat on each of your
heads. The hat will be either black or white. You can see the hats of
everyone in front of you but you can’t see your own and you can’t turn
behind. Starting from the last person in the line, I will ask the color of
the hat that is on your head. You are allowed to say aloud single word
answer: “white” or “black”. If you get it right, you will be released. Else
you will be shot dead”. The geeks have a night to discuss their strategy.
What strategy should the geeks develop so that largest number of them can survive!

Some clarifications:
1. One don't know what happened to previous person, all you can do is see in-front of you and "hear the response of all other people".
2. You can't see the shadow of person behind you.
3. Any other social hack, you might think of.

Let's focus on the question again.

### What strategy should the geeks develop so that largest number of them can survive!

The obvious possibility of surviving is 50% without doubt, how??. Well a group of 2 can save one of the person for sure i.e one person from the group has to tell right color to other person.

### Now first the hint for better solution:

> You can save significantly high number of people.

Rang a bell??

Let's draw the scenario 
```
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

|-64-|-63-|-62-|-61-|-60-|-59-|-58-|-57-|-56-|-55-|-54-|-53-|-52-|-51-|-50-|-49-|-48-|-47-|-46-|-45-|-44-|-43-|-42-|-41-|-40-|-39-|-38-|-37-|-36-|-35-|-34-|-33-|-32-|-31-|-30-|-29-|-28-|-27-|-26-|-25-|-24-|-23-|-22-|-21-|-20-|-19-|-18-|-17-|-16-|-15-|-14-|-13-|-12-|-11-|-10-|-9-|-8-|-7-|
|-6-|-5-|-4-|-3-|-2-|-1-|
```
64 people, think of it as an array.

We have signal other people, what's better than unity and forming a group? So we group people and try to signal more than one people at once.

### Another hint:
> Black and white! Two variables, can do anything with bits, binary? 

### 2 people signal group
A group of two people can signal 4 four people using 2 bits. 00, 01, 10, 11.
1. So they can signal if all people's hat have same color using 00
2. They can count no. of color of either pre-decided color, let's white is the color. 
3. If the signal is black-black i.e 00, it means everyone is white so the all four people will say white.
4. If the signal is white-black i.e 10, it means the first person can count no of white and black infront of him, if there are 2 white hats then he will say black, if there is one white hat in front of him, he way say white.
5. Next person will account the choice of previous and do the calculation similarly.

Whoaa! never thought of it before, thought whatever is in destiny will happen. LOL.

So out of 64, 6 people can form the signal group and can give 64 kinds of signals i.e counting/numbers.

### 6 people signal group
Can save at-least 58 people.

So now that's a life saving puzzle, should put enough interest to solve more puzzles.

### Humor
> There are 10 types of people in the world, one who understands binary and the rest who doesn't.

Till next time.
