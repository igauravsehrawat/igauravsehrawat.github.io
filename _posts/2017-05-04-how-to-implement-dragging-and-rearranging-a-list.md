---
layout: post
permalink: /how-to-implement-dragging-and-rearranging-a-list
title: "How to implement dragging and rearranging a list"
description: "Using vanilla Javascript for the implementation."
tags: [vanilla javascript, HTML5, js, drag and drop]
comments: true
share: true
---

So first technical blog of the year. It's simple blog as it seems from the title. UX is important here too, that will also be the focus apart from code. This blog is from a task given to me by my mentor.

So let's see the flow.
1. We want to have two lists and item can be added and deleted in each list.  
2. An item can also be moved to other list by dragging it over to other list's place.  
3. We want to create a placeholder where the item is going to be placed.  
4. We want to slightly tilt the item being dragged to show distinction.  

So we need to know drag and drop API's from [MDN](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)(a good documentation place). There are multiple API's but we just need 4 of those. Those 4 are `ondrag`, 'ondragover', 'ondragleave', 'ondragend'. We don't need `ondrop` since we are using placeholder to mark the position to place the elements.

So let's define the behavior.  
1. What happens when your start dragging?  

> Visual clue from rest of items present there(like tilted).  

2. How to show the place when an item is going to be dropped.  

> Show a visual clue like placeholder.  

3. What happens if drag fails(i.e it goes out of browser)?  

> It should come to the last visual clue it is supposed to come.   

So our drag-able element/item looks like:
{% highlight javascript linenos %}
        <div id="item-template-container" class="item-template-container" draggable="true" ondragstart="listItemDragStartHandler(event);" ondragover="dragoverHandler(event);" ondragend="dragEndHandler(event);" ondragleave="dragLeaveHandler(event);" ondrop="onDropHandler(event);">
            <div class="item-list-element">
                <div class="item-text"></div>
                <div class="delete-item-div">
                    <button class="delete-item" onclick="delete_item(event);">Delete</button>
                </div>
            </div>
        </div>
{% endhighlight %}

And the 4 drag function looks like below
{% highlight javascript linenos %}

function removePlaceholder() {
    if(document.getElementById('grayed-empty-node') !== null) {
        document.getElementById('grayed-empty-node').remove();
    }
}

function insertPlaceholder(currentElement, which) {
    var isGrayEmptyNodeThere = document.getElementById('grayed-empty-node');
    if(isGrayEmptyNodeThere === null) {
        var listContainer = currentElement.parentNode;
        var emptyNode = document.getElementById('empty-node').cloneNode(true);
        emptyNode.removeAttribute('id');
        emptyNode.setAttribute('id', 'grayed-empty-node');
        emptyNode.setAttribute('class', 'fade-in');
        emptyNode.style.height = String(heightWidth[0]) + 'px';
        emptyNode.style.width = String(heightWidth[1]) + 'px';
        if (which == 'over')
            listContainer.insertBefore(emptyNode, currentElement);
        else if (which == 'leave')
            listContainer.insertBefore(emptyNode, null);
    }
}
{% endhighlight %}

The above ones are 2 helper functions for removing and inserting placeholder as the name suggests. Also you will notice there is `event.preventDefault` used because some OS browsers have other behaviors for dragging an object. So we will avoid that.


`listItemDragStartHandler` (funny name) is an `ondrag` method, here we want to save the dragged item in global var `source` and height & width of dragged element for placeholder. Then we attach a custom image for dragging which is bit tilted to show some relevance which is also stored in a global var `dragImageSource`.

{% highlight javascript linenos %}
function listItemDragStartHandler(event) {
    source = event.currentTarget;
    heightWidth = [];
    heightWidth.push(source.offsetHeight);
    heightWidth.push(source.offsetWidth);
    event.dataTransfer.setData('text/html', event.currentTarget.innerHTML);
    event.dataTransfer.effectAllowed = 'move';
    // Drag image logic
    dragImageSource = source.cloneNode(true);
    dragImageSource.style.position = 'absolute';
    // Don't show the element
    dragImageSource.style.top = '0px';
    dragImageSource.style.left = '-' + String(window.innerWidth) + 'px';
    // dragImageSource.style.left = '-100px';
    var toTiltElement = dragImageSource.getElementsByClassName('item-list-element')[0];
    toTiltElement.style.transform = 'rotate(5deg)';
    document.body.append(dragImageSource);
    event.dataTransfer.setDragImage(dragImageSource, heightWidth[1]/2, heightWidth[0]/2);
}
{% endhighlight %}

We have `ondragover` and `ondragleave` methods below which basically insert placeholder according to latest movement. In `dragoverHandler` we hide the existing item from it's original place and check if we are dragging over a new element using `lastDragOverElementId`, only then we remove existing placeholder and insert new placeholder.

{% highlight javascript linenos %}
function dragoverHandler(event) {
    event.preventDefault();
    event.dataTransfer.dropEffect = 'move';
    source.style.display = 'none';
    var currentElement = event.currentTarget;
    var listContainer = currentElement.parentNode;
    if (lastDragOverElementId != currentElement.getAttribute('id')) {
        lastDragOverElementId = currentElement.getAttribute('id');
        removePlaceholder();
        insertPlaceholder(currentElement, 'over');
    }
}
{% endhighlight %}

In `dragLeaveHandler`, this is specifically needed to have a placeholder at the end of the list because we are always appending above existing drag over element. But when element exit the list it's place should be at end. So here we check if it has left the last visible element(remember we still have one hidden original element in the list).

Also you will notice we have a timeout here for disabling `ondragleave` for few moments, this is for stop a chain reaction between `ondragover` and `ondragleave` since a list element passes through the dragged element when placing the placeholder. Then at-last we set `lastDragOverElementId` to null since a new dragged element will hover over other element now or re-enter.

{% highlight javascript linenos %}
function dragLeaveHandler(event) {
    event.preventDefault();
    var currentElement = event.currentTarget;
    var listContainer = currentElement.parentNode;
    var elementList = listContainer.getElementsByClassName('item-template-container');
    var visibleElementList = [];
    var i = 0;
    for (i=0; i<elementList.length; i++) {
        if (elementList[i].style.display !== 'none') {
            visibleElementList.push(elementList[i]);
        }
    }
    // Last element ondragleave handler should be delayed, otherwise it
    // would spin off chain reaction.
    var lastVisibleElement = visibleElementList[visibleElementList.length - 1];
    // Basically last element
    if (currentElement.id === lastVisibleElement.getAttribute('id')) {
        lastVisibleElement.removeAttribute('ondragleave');
        removePlaceholder();
        insertPlaceholder(currentElement, 'leave');
        // This delayed the chain reaction
        setTimeout(function() {
            visibleElementList[visibleElementList.length - 1].setAttribute('ondragleave', 'dragLeaveHandler(event);');
        }, 500);
    // When event is on last element set the lastDragOverElementId to null
    // then dragover to lastVisibleElement(second last element) can be handled
    // otherwise dragover to second last element won't show placeholder.
    lastDragOverElementId = null;
    }
}
{% endhighlight %}

This handler is needed to place the dragged element to placeholder place irrespective of drop, so drop is mouse release operation here. 
{% highlight javascript linenos %}
function dragEndHandler(event) {
    event.preventDefault();
    // Check the dropEffect
    dragImageSource.remove();
    var listElement = document.getElementById('grayed-empty-node')
    var listContainer = listElement.parentNode;
    if (event.dataTransfer.dropEffect === 'none' ||
        event.dataTransfer.dropEffect === 'move') {
        var grayEmptyNode = document.getElementById('grayed-empty-node');
        // When grayEmptyNode is null, that will append at the end.
        listContainer.insertBefore(source, grayEmptyNode);
        source.style.display = '';
        removePlaceholder();
    }
}
{% endhighlight %}

Ahoy!! I can't understand without a demo. I have a [demo here](https://codepen.io/igaurav/pen/pPWwXR). There are few things I haven't mentioned like fading of placeholder and using livereload while developing this.

That's all for today.
