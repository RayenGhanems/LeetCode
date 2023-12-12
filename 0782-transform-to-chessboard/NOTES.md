## movesToChessboard Function Explanation

The `movesToChessboard` function takes a binary chessboard represented by a 2D list and calculates the minimum number of moves required to convert it into a valid chessboard. If conversion is not possible, the function returns -1.

### Logic Overview:

1. **XOR Check:**
   - Ensures the XOR of the top-left element with other elements in the first row and column is zero, indicating a valid chessboard.

2. **Row and Column Sum Check:**
   - Verifies if the sum of values in the first row and column falls within the valid range for a chessboard.

3. **Counting Mismatches:**
   - Counts the mismatches between the first row and column elements and their expected values.

4. **Adjustment for Even-sized Board:**
   - If the board size is even, adjusts counts to represent the minimum moves needed to fix the board.

5. **Calculation and Return:**
   - Returns the average of the adjusted row and column counts divided by 2.

### Usage Example:

```python
# Example Usage
board = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
result = movesToChessboard(board)
print(f"Minimum moves required: {result}")
​
