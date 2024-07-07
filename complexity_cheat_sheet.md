# Complexity Analysis Cheat Sheet

1. **Simple operation:** O(1)  - Constant time, regardless of input size.

2. **Single loop:** O(n)  - Linear time, where the complexity increases linearly with the input size n .

3. **Multiple O(n)  operations:** O(n) + O(n) + O(n)  is still O(n)  - The overall complexity is determined by the dominant term, which remains O(n) .

4. **Single nested loop:** O(n^2)  - Quadratic time, where each iteration of the outer loop triggers n  iterations of the inner loop.

5. **Three nested loops:** O(n^3)  - Cubic time, where each iteration of the outermost loop triggers n^2  iterations of the second loop, and so on.

6. **O(1)  + O(1)  = O(1) ** - Multiple constant-time operations are still constant time.

7. **O(1)  + O(n)  = O(n) ** - Constant time operations followed by linear time operations result in linear time complexity.

8. **O(n)  * O(n)  = O(n^2) ** - Multiplying complexities indicates nested operations or operations dependent on two variables.

9. **O(n^k)  (where k  is a constant) + O(n^m)  (where m > k ) = O(n^m) ** - The higher power dominates the complexity.
