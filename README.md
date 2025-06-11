# List_and_Set_python
Data structures implemented in Python (lists and sets)

---
# List and Set in Data Structures

## 📋 List

A **list** is an ordered collection of elements that allows duplicates. Lists maintain the insertion order, meaning elements are stored in the order in which they were added.

---

### Characteristics:
- Ordered
- Allows duplicate elements
- Indexable (elements can be accessed via their position)

---

### Example (Python):
```python
my_list = [1, 2, 3, 2, 4]
print(my_list[0])  # Output: 1
```

---

### Use Cases:
Storing items in a specific order
Accessing elements by index
Performing operations like sorting, slicing, appending, etc.

---

## 🔢 Set

A **set** is an unordered collection of unique elements. It does not allow duplicates, and it does not maintain insertion order (although in Python 3.7+, sets preserve insertion order as an implementation detail, but this should not be relied upon for logic).

---

### Characteristics:
- Unordered
- Does not allow duplicate elements
- Not indexable (you cannot access items by position)

---

### Example (Python):
```python
my_set = {1, 2, 3, 2, 4}
print(my_set)  # Output: {1, 2, 3, 4}
```

---

### Use Cases:
Ensuring all elements are unique
Performing mathematical set operations (union, intersection, difference)
Fast membership testing

---

## 🚀 Summary

| Feature    | List        | Set           |
|------------|-------------|---------------|
| Ordered    | ✅ Yes      | ❌ No         |
| Duplicates | ✅ Allowed  | ❌ Not allowed |
| Indexable  | ✅ Yes      | ❌ No         |
| Use Case   | Sequence data | Unique data  |

---
The attached codes are lists and sets implemented in Python including List using array (function version and class), line editor using list, set class using array.

