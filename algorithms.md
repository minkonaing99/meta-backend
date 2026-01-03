break into smaller parts

palindrome
optimum

An algorithms is a set of insturctions that is completed in a step-by-step way to solve a particular problem.

Recursion refers to a method or a function that will call itself. It is used to resolve problems by breaking the problem down into sub-problems.

- Divide and conquer

- Dynamic programming

* mainly use for optimization problems.
* split problems into sub problems

- Greeedy algorithm

* locally optimal choices
  A greedy algorithm solves a problem step by step by always picking the best-looking choice right now, without worrying too much about the future.

Greedy algorithms work only for certain problems, where:

Making the best choice now never causes regret later

A big problem can be broken into smaller similar problem

Planning is key with any algorithm. Make sure you have all the steps neatly laid out.

Refactoring - a standard part of the software development cycle.

Measured by Time (how long it take) and space (how much memory it takes)

Big O notation
Constant time (run under the same time and space) O(1)
Example: Accessing an element in an array by its index.

Linear time (grow depending on the size of input) O(n)
Example: Searching for a specific value in an unsorted list.

Logarithmic time (grow logarithmically with the size of the input data.) (O(log(n)))
Example: Binary search in a sorted list.

Quadratic time (grow with the square of the input size) O(n^2)
Example: Bubble Sort, a simple sorting algorithm.

Exponential time (fibonacci)

Big O notation is written as "O(f(n))," where "f(n)" is a function that represents the relationship between the input size (usually denoted as "n") and the algorithm's runtime or resource usage.

Why Big O Notation Matter

- Algorithm Comparison
- Performance Optimization
- Scalability
- Resource Management
- Coding Interviews

Analyzing Code with Big O Notation

- Identify the input size - determine what "n" represents in your code, often related to the soze of the input data
- Identify loops and iterations - determine the primary factors affecting time complexity
- ciount operations inside loops
- combine complexity - if you have nested loop, multiply their complexities to determine the overall time complexity
- choose the dominatnt term
- simplify
