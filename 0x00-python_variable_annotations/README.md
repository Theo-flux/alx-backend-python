# 0x00-Python-Variable-Annotation

## Resources
- [python typing docs](https://docs.python.org/3/library/typing.html#)

### Iterable Type:
Imagine you have a toy box filled with different toys. Each toy is unique and special. Now, let's say you want to go through all the toys in the toy box and play with each one of them. How would you do that?

In Python, an iterable is like a toy box that contains a collection of things, just like your toy box. It can be a list of toys, a group of numbers, or even a string of letters. You can think of an iterable as a way to organize and store a bunch of items.

When you want to play with each toy in your toy box, you take them out one by one. In Python, you can do something similar with an iterable. You can use a loop, like a magic hand, to go through each item in the iterable and do something with it.

The magic hand is called a "for loop" in Python. It helps you go through each item in the iterable and perform some action. It's like taking out each toy from the toy box and playing with it before moving on to the next one.

Now, the cool thing about Iterable typing in Python is that it helps you know what kind of things are inside the iterable. Just like your toy box can contain different types of toys, an iterable in Python can contain different types of items, like numbers, words, or even other collections.

By using Iterable typing, you can tell Python what kind of items are inside the iterable. It's like putting labels on the toy box to indicate what kinds of toys are inside. This helps Python understand the types of items in the iterable and allows it to give you helpful suggestions and catch any mistakes you might make.

So, Iterable typing in Python is like having a special toy box that lets you play with each item in a collection and helps you know what types of items are inside. It makes it easier to work with collections of things and helps Python be a good friend to you when you're coding.

### Sequence
Imagine you have a box of crayons. Each crayon has a different color, and you can use them to draw beautiful pictures. Now, let's say you want to organize your crayons in a specific order. How would you do that?

In Python, a sequence is like a special order for your crayons. It helps you keep your crayons in a particular arrangement, so you can find them easily and use them in a specific way.

A sequence in Python is like a line of crayons where each crayon has a number. The first crayon is number 1, the second one is number 2, and so on. Just like in a line, the order of the crayons in a sequence is very important.

With a sequence, you can access each crayon by its number. For example, if you want to use the third crayon in the sequence, you say "Give me crayon number 3." It helps you find the crayon you want without searching through the whole box.

Now, Sequence typing in Python is like telling Python that you have a special line of things, just like your crayons. By using Sequence typing, you can tell Python that you have a specific order of items and that you can access each item by its number.

This helps Python understand the order of things in the sequence and allows it to give you helpful suggestions and catch any mistakes you might make when working with sequences.

So, Sequence typing in Python is like having a special order for your crayons, where each crayon has a number. It helps you keep things organized and makes it easier for Python to understand how you want to use the items in the sequence.

## When to use Iterable and Sequence
The decision to use Iterable typing or Sequence typing depends on how you plan to use the data and what operations you want to perform on it. Let's break it down:

    Iterable typing: Use Iterable typing when you want to indicate that you have a collection of items and you want to iterate over them one by one. Iterable typing is more general and can be used for any kind of collection, like lists, sets, dictionaries, and more.

For example, if you have a list of toys and you want to go through each toy to count how many you have, you would use Iterable typing. The focus is on going through each item without specifying their order.

    Sequence typing: Use Sequence typing when you want to indicate that you have a specific order of items, and you want to access them by their index or position. Sequence typing is more specific and is typically used for ordered collections like lists, tuples, and strings.

For example, if you have a string of letters and you want to access the letter at a particular position, like the third letter in the string, you would use Sequence typing. The order of the items is important, and you can refer to them by their positions in the sequence.

In summary, use Iterable typing when you just want to go through a collection of items without worrying about their order, and use Sequence typing when you have a specific order and want to access items by their positions.

It's worth noting that Iterable typing is more general and can be used in many cases, while Sequence typing is more specific to ordered collections. However, Python is quite flexible, so sometimes you can use Iterable typing even if you have a sequence, and it will still work.