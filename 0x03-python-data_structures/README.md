0x03. Python - Data Structures: Lists, Tuples

# Python Programming

Python is an awesome programming language known for its simplicity, readability, and versatility. It is widely used for various purposes such as web development, data analysis, scientific computing, artificial intelligence, and more. Here, we will explore some key concepts and features of Python programming.

## Lists

Lists are one of the fundamental data structures in Python. They are used to store a collection of items, which can be of different types. Lists are mutable, meaning you can modify their contents after they are created. To define a list, you enclose the items in square brackets `[ ]` and separate them with commas.

Example:
```python
fruits = ['apple', 'banana', 'orange', 'mango']
```

In the above example, we have created a list called `fruits` containing four elements.

## Differences and Similarities between Strings and Lists

Strings and lists are both sequence types in Python, but they have some differences and similarities.

Differences:
- Strings are immutable, meaning you cannot change individual characters once a string is created, while lists are mutable.
- Strings store a sequence of characters, whereas lists can store elements of any type.

Similarities:
- Both strings and lists can be indexed and sliced to access individual elements or sub-sequences.
- They support common sequence operations such as concatenation (`+`), repetition (`*`), and membership (`in` or `not in`) checks.

## Common List Methods

Python provides several built-in methods to manipulate lists. Here are some commonly used methods:

- `append()`: Adds an element to the end of the list.
- `extend()`: Appends the elements of another list to the current list.
- `insert()`: Inserts an element at a specified position in the list.
- `remove()`: Removes the first occurrence of a specified element from the list.
- `pop()`: Removes and returns the element at a specified index.
- `index()`: Returns the index of the first occurrence of a specified element.
- `count()`: Returns the count of a specified element in the list.
- `sort()`: Sorts the elements of the list in ascending order.
- `reverse()`: Reverses the order of the elements in the list.

Example:
```python
numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]

numbers.extend([7, 8, 9])
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.insert(0, 0)
print(numbers)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers.remove(3)
print(numbers)  # Output: [0, 1, 2, 4, 5, 6, 7, 8, 9]

popped_element = numbers.pop(5)
print(popped_element)  # Output: 6
print(numbers)         # Output: [0, 1, 2, 4, 5, 7, 8, 9]

index = numbers.index(5)
print(index)  # Output: 4

count = numbers.count(2)
print(count)  # Output: 1

numbers.sort()
print(numbers)  # Output: [0, 1, 2, 4, 5, 7, 8, 9]

numbers.reverse()
print(numbers)  # Output: [9, 8, 7, 5, 4, 2, 1, 0]
```

## Using Lists as Stacks and Queues

Lists can be used as simple implementations of stacks and queues.

Stacks:
- To implement a stack, you can use the `append()` method to add elements to the end of the list and the `pop()` method to remove elements from the end.

```python
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]

popped_element = stack.pop()
print(popped_element)  # Output: 3
print(stack)          # Output: [1, 2]
```

Queues:
- To implement a queue, you can use the `append()` method to add elements to the end of the list and the `pop()` method with index 0 to remove elements from the beginning.

```python
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print(queue)  # Output: ['a', 'b', 'c']

dequeued_element = queue.pop(0)
print(dequeued_element)  # Output: 'a'
print(queue)            # Output: ['b', 'c']
```

## List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists or other iterable objects. They consist of square brackets `[ ]` containing an expression followed by a `for` loop and optional `if` conditions.

Example:
```python
numbers = [1, 2, 3, 4, 5]

squared_numbers = [n**2 for n in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # Output: [2, 4]
```

## Tuples

Tuples are similar to lists but are immutable, meaning you cannot modify their elements after creation. Tuples are defined by enclosing comma-separated values in parentheses `( )`.

Example:
```python
point = (3, 4)
```

In the above example, we have created a tuple called `point` representing a coordinate.

## When to Use Tuples versus Lists

Use tuples when:
- You need an immutable sequence of elements that should not be modified.
- You want to use a collection of values as keys in a dictionary (since tuples are hashable, unlike lists).

Use lists when:
- You need a mutable sequence that allows modification of elements.
- You want to store a collection of homogeneous or heterogeneous elements that can be modified.

## Sequence

A sequence is an ordered collection of items in Python. Lists, tuples, and strings are examples of sequence types. Sequences support common operations such as indexing, slicing, concatenation, repetition, and more.

## Tuple Packing

Tuple packing is the process of combining multiple values into a single tuple. It allows you to assign multiple values to multiple variables in a single statement.

Example:
```python
coordinates = 3, 4
x, y = coordinates

print(x)  # Output: 3
print(y)  # Output: 4
```

In the above example, the values `3` and `4` are packed into the tuple `coordinates`, and then unpacked into the variables `x` and `y`.

## Sequence Unpacking

Sequence unpacking is the process of separating a sequence into individual variables. It allows you to assign the elements of a sequence to multiple variables simultaneously.

Example:
```python
fruits = ['apple', 'banana', 'orange']

fruit1, fruit2, fruit3 = fruits

print(fruit1)  # Output: 'apple'
print(fruit2)  # Output: 'banana'
print(fruit3)  # Output: 'orange'
```

In the above example, the elements of the `fruits` list are unpacked into the variables `fruit1`, `fruit2`, and `fruit3`.

## The `del` Statement

The `del` statement is used to delete objects or elements in Python. It can be used to remove elements from a list, delete variables, or delete entire objects.

Example:
```python
numbers = [1, 2, 3, 4, 5]

del numbers[2]
print(numbers)  # Output: [1, 2, 4, 5]

x = 10
del x  # Deletes the variable x

# Deleting an object
class MyClass:
    pass

obj = MyClass()
del obj  # Deletes the object
```

In the above example, we use the `del` statement to remove an element from the `numbers` list, delete the variable `x`, and delete the `obj` object.

## Recommended Resources

To further enhance your understanding and skills in Python programming, here are some recommended resources:

- Python documentation: The official Python documentation provides comprehensive information and examples for Python programming. You can find it at [docs.python.org](https://docs.python.org).
- Python tutorials and courses: Online platforms like [Coursera](https://www.coursera.org) and [Udemy](https://www.udemy.com) offer various Python tutorials and courses for beginners and advanced learners.
- "Python Crash Course" by Eric Matthes: This book provides a beginner-friendly introduction to Python programming with practical examples and projects.
- "Fluent Python" by Luciano Ramalho: This book is recommended for intermediate to advanced Python programmers who want to deepen their understanding of the language and its features.