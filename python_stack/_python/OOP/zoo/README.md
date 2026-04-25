# Zoo Management System 🐾

## Overview

This project is a simple Object-Oriented Programming (OOP) example in Python that simulates a zoo.
It demonstrates key OOP concepts like:

* Inheritance
* Polymorphism
* Method overriding

## Classes

### 1. Animal (Base Class)

Represents a general animal with:

* name
* age
* health_care
* happiness_level

### 2. Animal Subclasses

Each animal has its own behavior for feeding:

* **Lion**
* **Monkey**
* **Bear**
* **Tiger**

Each subclass overrides the `feed()` method to simulate different effects.

### 3. Zoo

Manages a collection of animals:

* `add_animal()` → adds animals
* `print_all_info()` → displays all animals
* `feed_all()` → feeds all animals (polymorphism in action)

## Key Concept: Polymorphism

The `feed_all()` method calls `feed()` on each animal,
but each animal behaves differently depending on its class.

## Example Flow

1. Create animals
2. Add them to the zoo
3. Print their info
4. Feed all animals
5. Print updated info

## ⚠️ Note

There is a small bug in the `Tiger` class:

```python
self.health_care = +15
```

This resets the value instead of increasing it.
It should be:

```python
self.health_care += 15
```

## How to Run

Simply run the Python file:

```bash
python your_file.py
```

---

## Author

Shams ✨
