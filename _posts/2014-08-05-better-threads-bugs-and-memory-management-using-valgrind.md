---
layout: post
permalink: better-threads-bug-and-memory-management-using-valgrind
title: better threads bug and memory management using valgrind
description: "how to efficiently handle c and c++ memory management,thread bugs & profiling programs in detail"
tags: [debugging , better-errors, c , c++ ]
comments: true
share: true

---

### Problem ?

Problem arises when you don't get to know why my program dysfunctional , inspite of correct logic . The problem may be with memory handling or in the thread handling . Learning syntax is half part , gaining proficiency is another part .

### What exactly is memory management ?

In C/C++ assigning memory & handling threads can PITA until one reach a level of experience .
Let's go by an example:

{%highlight c%}
#include <stdlib.h>

void bad_memory(void){

	int* array_alloc = malloc(20 * sizeof(int));
	array_alloc[20] = 10 ;
}

int main(void){

	bad_memory();
	return 0 ;
}

{% endhighlight c %}
The above code has two errors . It doesn't pops up during compilation and during execution .
First one : assigning out of bound index of array_alloc a value i.e array_alloc[20]
Second one : not freeing the allocated memory resulting in memory leak .

###Valgrind to rescue !
By definition : The <a href="valgrind.org">Valgrind</a> tool suite provides a number of debugging and profiling tools that help you make your programs faster and more correct. The most popular of these tools is called Memcheck. It can detect many memory-related errors that are common in C and C++ programs and that can lead to crashes and unpredictable behaviour.

To rescue onself run the executable using valgrind command

{% highlight c %}

valgrind --leak-check=full ./a.out

{% endhighlight  c %}
The result is as following
{%highlight bash %}

valgrind --leak-check=full ./a.out
==25516== Memcheck, a memory error detector
==25516== Copyright (C) 2002-2011, and GNU GPL'd, by Julian Seward et al.
==25516== Using Valgrind-3.7.0 and LibVEX; rerun with -h for copyright info
==25516== Command: ./a.out
==25516==
==25516== Invalid write of size 4
==25516==    at 0x400512: bad_memory (in /home/rooted/Documents/git-repos/workshop/code/a.out)
==25516==    by 0x400522: main (in /home/rooted/Documents/git-repos/workshop/code/a.out)
==25516==  Address 0x51f2068 is 0 bytes after a block of size 40 alloc'd
==25516==    at 0x4C2B6CD: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==25516==    by 0x400505: bad_memory (in /home/rooted/Documents/git-repos/workshop/code/a.out)
==25516==    by 0x400522: main (in /home/rooted/Documents/git-repos/workshop/code/a.out)
==25516==
==25516==
==25516== HEAP SUMMARY:
==25516==     in use at exit: 40 bytes in 1 blocks
==25516==   total heap usage: 1 allocs, 0 frees, 40 bytes allocated
==25516==
==25516== 40 bytes in 1 blocks are definitely lost in loss record 1 of 1
==25516==    at 0x4C2B6CD: malloc (in /usr/lib/valgrind/vgpreload_memcheck-amd64-linux.so)
==25516==    by 0x400505: bad_memory (in /home/rooted/Documents/git-repos/workshop/code/a.out)
==25516==    by 0x400522: main (in /home/rooted/Documents/git-repos/workshop/code/a.out)
==25516==
==25516== LEAK SUMMARY:
==25516==    definitely lost: 40 bytes in 1 blocks
==25516==    indirectly lost: 0 bytes in 0 blocks
==25516==      possibly lost: 0 bytes in 0 blocks
==25516==    still reachable: 0 bytes in 0 blocks
==25516==         suppressed: 0 bytes in 0 blocks
==25516==
==25516== For counts of detected and suppressed errors, rerun with: -v
==25516== ERROR SUMMARY: 2 errors from 2 contexts (suppressed: 2 from 2)

{% endhighlight bash %}
There are two errors : Heap error for invalid assign & Leaks relating lost memory .

Valgrind can also be misused to profile your code (pun intended )
Further Valgrind can also be used for Bounty programs (like google chrome).

### Conclusion !

There are other tools for debugging like <a href="http://www.gnu.org/software/gdb/">GDB</a> which is very elaborate & pro-like . Apart from that Valgrind is there .
As pointed out what's better than finding out bugs as quickly without any pain .


Comments welcomed . Pros & cons ?

