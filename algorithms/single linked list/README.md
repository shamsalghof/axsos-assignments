# 🔗 Singly Linked List (Python)

## 📌 Overview

This project implements a **Singly Linked List** from scratch in Python without using built-in data structures.

---

## 🧠 Concepts Covered

* Nodes & pointers
* Linked list traversal
* Dynamic memory structure
* Basic data structure operations

---

## 🏗️ Structure

### Node

Represents a single element:

* `value` → stored data
* `next` → pointer to next node

---

### SLinkedList

Manages the linked list using a `head` pointer.

---

## ⚙️ Available Methods

* `add_to_front(value)` → add node at beginning
* `add_to_back(value)` → add node at end
* `remove_from_front()` → remove first node
* `remove_from_last()` → remove last node
* `remove_val(value)` → remove specific value
* `insert_at(value, index)` → insert at position
* `print_values()` → display all values

---

## ▶️ Example Usage

```python
myList = SLinkedList()

myList.add_to_front(4)
myList.add_to_front(3)
myList.add_to_front(1)

myList.remove_val(3)
myList.print_values()
```

---

## 📌 Example Output

```
1
4
```

---

## ⚠️ Notes

* Index-based insertion does nothing if index is out of range
* No tail pointer is used (traversal required for last operations)
* Duplicate values are allowed

---

## 🚀 Future Improvements

* Add `length()` method
* Add `find()` method
* Add tail pointer for faster insertions
* Convert to Doubly Linked List

---

## 👨‍💻 Author

Shams
