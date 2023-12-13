## Counting Good Nodes in Binary Matrix

The provided code defines a function that counts the number of "good" nodes in a binary matrix. A "good" node is one with the value 1, and it is considered good if there are no other 1s in its row or column.

### Code Overview:

1. **Initialization:**
   - The code initializes `ans` to 0, representing the count of good nodes.
   - `m` and `n` store the dimensions of the binary matrix.

2. **Nested Loops:**
   - Two nested loops iterate through each element in the matrix.

3. **Checking Good Nodes:**
   - If the current element is 1, the code checks if there are no other 1s in the same row or column. If true, the node is considered "good," and the count (`ans`) is incremented.

4. **Return:**
   - The function returns the final count of good nodes in the binary matrix.

### Usage Example:

```python
# Example Usage
matrix = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
result = count_good_nodes(matrix)
print(f"Number of good nodes: {result}")
​
