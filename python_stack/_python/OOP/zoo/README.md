# 🐾 Zoo Management System (OOP in Python)

## 📌 Overview

This project is a simple Zoo Management System built using **Object-Oriented Programming (OOP)** in Python.
It demonstrates how different animal types can share common behavior while also having their own unique actions.

---

## 🎯 Concepts Covered

* **Classes & Objects**
* **Inheritance**
* **Method Overriding**
* **Polymorphism**

---

## 🏗️ Project Structure

### 🔹 Base Class: `Animal`

Represents a general animal with shared attributes:

* `name`
* `age`
* `health`
* `happiness`

**Methods:**

* `display_info()` → prints animal details
* `feed()` → default behavior (can be overridden)

---

### 🔹 Subclasses (Inheritance)

Each animal inherits from `Animal` and overrides `feed()`:

* **Lion**
* **Monkey**
* **Bear**
* **Tiger**

Each class defines its own feeding behavior, affecting health and happiness differently.

---

### 🔹 Zoo Class

Manages a collection of animals.

**Methods:**

* `add_animal(animal)` → adds an animal to the zoo
* `show_animals()` → displays all animals
* `feed_all()` → feeds all animals (**polymorphism happens here**)

---

## 🔥 Polymorphism Explained

The `feed_all()` method loops through all animals:

```python
for animal in self.animals:
    animal.feed()
```

Even though the same method is called, each animal behaves differently based on its class.

👉 This is **polymorphism**.

---

## ▶️ Example Usage

```python
zoo = Zoo("John's Zoo")

zoo.add_animal(Lion("Simba", 5, 50, 40, 80))
zoo.add_animal(Monkey("George", 3, 40, 60, "Banana"))
zoo.add_animal(Bear("Baloo", 7, 70, 50, 300))
zoo.add_animal(Tiger("Rajah", 6, 65, 45, "Orange"))

zoo.show_animals()
zoo.feed_all()
zoo.show_animals()
```

---

## ⚙️ How to Run

1. Make sure Python is installed
2. Run the file:

```bash
python zoo.py
```

---

## ✅ Improvements from Original Version

* Removed redundant methods
* Fixed logical bugs
* Simplified class design
* Applied **clean polymorphism**
* Improved readability

---

## 📌 Notes

* The base `Animal` class provides a default `feed()` method.
* Subclasses override it to create unique behaviors.
* The system is easily extendable (you can add new animals anytime).

---

## 👨‍💻 Author

Shams
