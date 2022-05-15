# Popular Coding Problem Solving Patterns

* [Sliding Window](sliding-window.py)
* [Fast & Slow Pointers](fast-slow.py)
* [Merge Interval](merge-interval.py)
* [Bitwise XOR](bitwise-xor.py)
* [In Place Reversal](in-place-reversal.py)
* [Top K Element](top-k-elem.py)
* [Two Pointers](two-pointers.py)

## Data Structures Overview
<details>
    <summary><strong>Array</strong> </summary>
    
## Array

- A list of similar values
- Can be used to store anything
- Stores values of the same data type
- Every item in an array is called an **element**
- 3 attributes:
    - Name
    - Type
    - Size
        - set integer that is fixed upon the creation of an array
        - **CAN'T** be changed once created
- Parallel arrays
    - 2 or more arrays which
        - contain the same # of elements
        - have corresponding values in the same position
- Creating an array
    - populate with elements
    - set a specific size
    - Python - array = [1, 2, 3]
- To get information, we use a **numerical index**
    - An integer which corresponds to an element within the array
- A two-dimensional array is an array with an array at each index
</details>

<details>
    <summary><strong>Stack</strong> </summary>
    
## Stack

- A data structure in which we add elements and remove elements according to the LIFO (last in first out) principle
    - only one way in and one way out for the data
- Common Stack Methods
    - push - adds an object into the top of the stack (Push(Object))
    - pop - remove an element from the top of the stack (Pop())
    - peek - allows you to get the value at the top of the list without removing it
    - contains - searching throughout the stack (Contains(Object)) - w/o having to take elements off the stack
</details>

<details>
    <summary><strong>Queue</strong> </summary>
    
## Queue

- The sequential access data structure which follows the FIFO methodology (First In First Out)
- Add to the back and remove from the front
- Queue methods
    - Enqueue - Adds element to the tail of the queue
    - Dequeue - Removes element from the head of the queue
    - Peek - returns the object that's at the forefront of the queue without removing it
    - Contains - returns whether or not the queue contains an object (boolean)
</details>

# [Problem Solving Patterns](https://seanprashad.com/leetcode-patterns/)

## Sliding Window

<details>

<summary><img id="sliding-window" src="https://img.shields.io/badge/Sliding Window-10-brightgreen?style=for-the-badge"></summary>


| S.No.    | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| -------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1        | `Sliding Window`               | [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)                                                                                    |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_01)_Reverse_String.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 2        | `Array`               | Find the maximum and minimum element in an array                                                     |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_02)_Max_Min_Element.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 3        | `Array`               | Find the "Kth" max and min element of an array                                                       |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_03)_Kth_Max_Min_Element.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_03)_kth_max_min.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 4        | `Array`               | Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo      |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C++/01%5D.%20Array/_04)_Sort_an_Array_012.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_04)_Sort_an_Array_012.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 5        | `Array`               | Move all the negative elements to one side of the array                                              |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_05)_Move_All_Negative_Elements.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_05)_MOve_all_neg_elements.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 6        | `Array`               | Find the Union and Intersection of the two sorted arrays.                                            |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_06)%20Union_of_two_arrays.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_06)_Union_intersection_ofSorted_Arrays.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 7        | `Array`               | Write a program to cyclically rotate an array by one.                                                |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_07)_Cyclically_rotate_an_array_by_one.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_07)_rotate_array_by%20one.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 8        | `Array`               | find Largest sum contiguous Subarray [V. IMP]                                                        |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_08)_Kadane's_Algorithm.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_08)_Largest_sum_contiguous_subarray.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 9        | `Array`               | Minimise the maximum difference between heights [V.IMP]                                              |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_09)_Minimize_the_Height.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 10       | `Array`               | Minimum no. of Jumps to reach end of an array                                                        |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/01%5D.%20Array/_10)_Minimum_number_of_jumps.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/01%5D.%20Array/_10)_min_jumps_to_reach_end.java"><img src="https://img.shields.io/badge/Solution-green"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>


  
## Two Pointers

<details>

<summary><img id="two-pointers" src="https://img.shields.io/badge/Two Pointers-11-yellow?style=for-the-badge"></summary>      

| S.No.    | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| -------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1        | `Matrix`              | Spiral traversal on a Matrix                                                                         |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_01)_Spirally_traversing_a_matrix.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2        | `Matrix`              | Search an element in a matriix                                                                       |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_02)_1)_Search_a_2D_Matrix.cpp"><img src="https://img.shields.io/badge/Solution-1-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_02)_2)_Search_a_2D_Matrix.cpp"><img src="https://img.shields.io/badge/Solution-2-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3        | `Matrix`              | Find median in a row wise sorted matrix                                                              |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_03)_Median_in_a_row_wise_sorted_Matrix.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4        | `Matrix`              | Find row with maximum no. of 1's                                                                     |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_04)_Row_with_max_1s.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5        | `Matrix`              | Print elements in sorted order using row-column wise sorted matrix                                   |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_05)_Sorted_matrix.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6        | `Matrix`              | Maximum size rectangle                                                                               |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_06)_Max_Rectangle.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 7        | `Matrix`              | Find a specific pair in matrix                                                                       |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_07)_Find_a_Specific_Pair_in_Matrix.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 8        | `Matrix`              | Rotate matrix by 90 degrees                                                                          |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_08)_Rotate_a_Matrix_by_90_Degree_in_Clockwise_without_Extra_Space.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 9        | `Matrix`              | Kth smallest element in a row-cpumn wise sorted matrix                                               |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_09)_Kth_element_in_Matrix.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 10       | `Matrix`              | Common elements in all rows of a given matrix                                                        |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/02%5D.%20Matrix/_10)_Common_elements_in_all_rows_of_matrix.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#450-dsa-sheet">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Fast & Slow Pointers

<details>

<summary><img id="string" src="https://img.shields.io/badge/Fast & Slow Pointers-10-orange?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `String`              | Reverse a String                                                                                     |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/03%5D.%20Strings/_01)_Reverse_String.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `String`              | Check whether a String is Palindrome or not                                                          |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/03%5D.%20Strings/_02)_Palindrome_String.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `String`              | Find Duplicate characters in a string                                                                |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/03%5D.%20Strings/_03)_Print_all_Duplicates_String.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `String`              | Why strings are immutable in Java?                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Answer-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Answer-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Answer-red"></a> |
| 5         | `String`              | Write a Code to check whether one string is a rotation of another                                    |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/03%5D.%20Strings/_05)_Check_String_are_Rotations_of_Each_Other.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `String`              | Write a Program to check whether a string is a valid shuffle of two strings or not                   |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/03%5D.%20Strings/_06)_Check_String_is_valid_Suffle_of_two_different_Strings.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/03%5D.%20Strings/_06)_Check_String_is_valid_Suffle_of_two_different_Strings.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 7         | `String`              | Count and Say problem                                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 8         | `String`              | Write a program to find the longest Palindrome in a string.[ Longest palindromic Substring]          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 9         | `String`              | Find Longest Recurring Subsequence in String                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 10        | `String`              | Print all Subsequences of a string.                                                                  |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Merge Intervals

<details>

<summary><img id="mergeintervals" src="https://img.shields.io/badge/Merge_Intervals-6-red?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Searching & Sorting` | Find first and last positions of an element in a sorted array                                        |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/04%5D.%20Searching%20%26%20Sorting/_01)_First_and_Last_Position_of_an_Element.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Searching & Sorting` | Find a Fixed Point (Value equal to index) in a given array                                           |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/04%5D.%20Searching%20%26%20Sorting/_02)_find_fixed_point(value%20equals%20to%20index).cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Searching & Sorting` | Search in a rotated sorted array                                                                     |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/04%5D.%20Searching%20%26%20Sorting/_03)_Search_in_Rotated_Sorted_Array.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Searching & Sorting` | square root of an integer                                                                            |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/04%5D.%20Searching%20%26%20Sorting/_04)_Count_Squares.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Searching & Sorting` | Maximum and minimum of an array using minimum number of comparisons                                  |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/04%5D.%20Searching%20%26%20Sorting/_05)_Middle-of_Three.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Searching & Sorting` | Optimum location of point to minimize total distance                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Cyclic Sort

<details>

<summary><img id="cyclicsort" src="https://img.shields.io/badge/Cyclic_Sort-5-blue?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `LinkedList`          | Write a Program to reverse the Linked List. (Both Iterative and recursive)                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `LinkedList`          | Reverse a Linked List in group of Given Size. [Very Imp]                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `LinkedList`          | Write a program to Detect loop in a linked list.                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `LinkedList`          | Write a program to Delete loop in a linked list.                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `LinkedList`          | Find the starting point of the loop.                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## In-place Reversal of a LinkedList

<details>

<summary><img id="linkedlist" src="https://img.shields.io/badge/Inplace_Reversal_LinkedList-6-bluevoilet?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Binary Trees`        | level order traversal                                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Binary Trees`        | Reverse Level Order traversal                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Binary Trees`        | Height of a tree                                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Binary Trees`        | Diameter of a tree                                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Binary Trees`        | Mirror of a tree                                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Binary Trees`        | Inorder Traversal of a tree both using recursion and Iteration                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Tree Breadth First Search

<details>

<summary><img id="bfs" src="https://img.shields.io/badge/Tree_Breadth_First_Search-17-yellowgreen?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Binary Search Trees` | Fina a value in a BST                                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Binary Search Trees` | Deletion of a node in a BST                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Binary Search Trees` | Find min and max value in a BST                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Binary Search Trees` | Find inorder successor and inorder predecessor in a BST                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Binary Search Trees` | Check if a tree is a BST or not                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Binary Search Trees` | Populate Inorder successor of all nodes                                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 7         | `Binary Search Trees` | Find LCA  of 2 nodes in a BST                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 8         | `Binary Search Trees` | Construct BST from preorder traversal                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 9         | `Binary Search Trees` | Convert Binary tree into BST                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 10        | `Binary Search Trees` | Convert a normal BST into a Balanced BST                                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 11        | `Binary Search Trees` | Merge two BST [ V.V.V>IMP ]                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 12        | `Binary Search Trees` | Find Kth largest element in a BST                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 13        | `Binary Search Trees` | Find Kth smallest element in a BST                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 14        | `Binary Search Trees` | Count pairs from 2 BST whose sum is equal to given value "X"                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 15        | `Binary Search Trees` | Find the median of BST in O(n) time and O(1) space                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 16        | `Binary Search Trees` | Count BST ndoes that lie in a given range                                                            |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 17        | `Binary Search Trees` | Replace every element with the least greater element on its right                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
    
<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Tree Depth First Search

<details>

<summary><img id="greedy" src="https://img.shields.io/badge/Tree_Depth_First_Search-30-green?style=for-the-badge"> </summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Greedy`              | Activity Selection Problem                                                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Greedy`              | Job SequencingProblem                                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Greedy`              | Huffman Coding                                                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Greedy`              | Water Connection Problem                                                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Greedy`              | Fractional Knapsack Problem                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Greedy`              | Greedy Algorithm to find Minimum number of Coins                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 7         | `Greedy`              | Maximum trains for which stoppage can be provided                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 8         | `Greedy`              | Minimum Platforms Problem                                                                            |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 9         | `Greedy`              | Buy Maximum Stocks if i stocks can be bought on i-th day                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 10        | `Greedy`              | Find the minimum and maximum amount to buy all N candies                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 11        | `Greedy`              | Minimize Cash Flow among a given set of friends who have borrowed money from each other              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 12        | `Greedy`              | Minimum Cost to cut a board into squares                                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 13        | `Greedy`              | Check if it is possible to survive on Island                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 14        | `Greedy`              | Find maximum meetings in one room                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 15        | `Greedy`              | Maximum product subset of an array                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 16        | `Greedy`              | Maximize array sum after K negations                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 17        | `Greedy`              | Maximize the sum of arr[i]*i                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 18        | `Greedy`              | Maximum sum of absolute difference of an array                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 19        | `Greedy`              | Maximize sum of consecutive differences in a circular array                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 20        | `Greedy`              | Minimum sum of absolute difference of pairs of two arrays                                            |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 21        | `Greedy`              | Program for Shortest Job First (or SJF) CPU Scheduling                                               |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 22        | `Greedy`              | Program for Least Recently Used (LRU) Page Replacement algorithm                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 23        | `Greedy`              | Smallest subset with sum greater than all other elements                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 24        | `Greedy`              | Chocolate Distribution Problem                                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 25        | `Greedy`              | DEFKIN -Defense of a Kingdom                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 26        | `Greedy`              | DIEHARD -DIE HARD                                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 27        | `Greedy`              | GERGOVIA -Wine trading in Gergovia                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 28        | `Greedy`              | Picking Up Chicks                                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 29        | `Greedy`              | CHOCOLA –Chocolate                                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 30        | `Greedy`              | ARRANGE -Arranging Amplifiers                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Two Heaps

<details>

<summary><img id="twoheaps" src="https://img.shields.io/badge/Two_Heaps-3-yellow?style=for-the-badge"> </summary>

| S.No.     | Topic:             | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `BackTracking`     | Rat in a maze Problem                                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `BackTracking`     | Printing all solutions in N-Queen Problem                                                            |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `BackTracking`     | Word Break Problem using Backtracking                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Subsets

<details>

<summary><img id="subsets" src="https://img.shields.io/badge/Subsets-6-red?style=for-the-badge"> </summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Stacks & Queues`     | Implement Stack from Scratch                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Stacks & Queues`     | Implement Queue from Scratch                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Stacks & Queues`     | Implement 2 stack in an array                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Stacks & Queues`     | find the middle element of a stack                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Stacks & Queues`     | Implement "N" stacks in an Array                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Stacks & Queues`     | Check the expression has valid or Balanced parenthesis or not.                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Modified Binary Search

<details>

<summary><img id="bs" src="https://img.shields.io/badge/Modified_Binary_Search-7-orange?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Heap`                | Implement a Maxheap/MinHeap using arrays and recursion.                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Heap`                | Sort an Array using heap. (HeapSort)                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Heap`                | Maximum of all subarrays of size k.                                                                  |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Heap`                | “k” largest element in an array                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Heap`                | Kth smallest and largest element in an unsorted array                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Heap`                | Merge “K” sorted arrays. [ IMP ]                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 7         | `Heap`                | Merge 2 Binary Max Heaps                                                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |


<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Bitwise XOR

<details>

<summary><img id="graph" src="https://img.shields.io/badge/Bitwise_XOR-3-orange?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Graph`               | Create a Graph, print it                                                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Graph`               | Implement BFS algorithm                                                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Graph`               | Implement DFS Algo                                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |


<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Top K Elements

<details>

<summary><img id="topk" src="https://img.shields.io/badge/Top_K_Elements-11-blue?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Trie`                | Construct a trie from scratch                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Trie`                | Find shortest unique prefix for every word in a given list                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Trie`                | Word Break Problem \| (Trie solution)                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Trie`                | Given a sequence of words, print all anagrams together                                               |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Trie`                | Implement a Phone Directory                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Trie`                | Print unique rows in a given boolean matrix                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#problem-solving-patterns">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## K-Way Merge

<details>

<summary><img id="dp" src="https://img.shields.io/badge/ Dynamic_Programming-60-ff69b4?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Dynamic Programming` | Coin ChangeProblem                                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 2         | `Dynamic Programming` | Knapsack Problem                                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 3         | `Dynamic Programming` | Binomial CoefficientProblem                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 4         | `Dynamic Programming` | Permutation CoefficientProblem                                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 5         | `Dynamic Programming` | Program for nth Catalan Number                                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 6         | `Dynamic Programming` | Matrix Chain Multiplication                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 7         | `Dynamic Programming` | Edit Distance                                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 8         | `Dynamic Programming` | Subset Sum Problem                                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 9         | `Dynamic Programming` | Friends Pairing Problem                                                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 10        | `Dynamic Programming` | Gold Mine Problem                                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 11        | `Dynamic Programming` | Assembly Line SchedulingProblem                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 12        | `Dynamic Programming` | Painting the Fenceproblem                                                                            |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 13        | `Dynamic Programming` | Maximize The Cut Segments                                                                            |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 14        | `Dynamic Programming` | Longest Common Subsequence                                                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 15        | `Dynamic Programming` | Longest Repeated Subsequence                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 16        | `Dynamic Programming` | Longest Increasing Subsequence                                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 17        | `Dynamic Programming` | Space Optimized Solution of LCS                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 18        | `Dynamic Programming` | LCS (Longest Common Subsequence) of three strings                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 19        | `Dynamic Programming` | Maximum Sum Increasing Subsequence                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 20        | `Dynamic Programming` | Count all subsequences having product less than K                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 21        | `Dynamic Programming` | Longest subsequence such that difference between adjacent is one                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 22        | `Dynamic Programming` | Maximum subsequence sum such that no three are consecutive                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 23        | `Dynamic Programming` | Egg Dropping Problem                                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 24        | `Dynamic Programming` | Maximum Length Chain of Pairs                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 25        | `Dynamic Programming` | Maximum size square sub-matrix with all 1s                                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 26        | `Dynamic Programming` | Maximum sum of pairs with specific difference                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 27        | `Dynamic Programming` | Min Cost PathProblem                                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 28        | `Dynamic Programming` | Maximum difference of zeros and ones in binary string                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 29        | `Dynamic Programming` | Minimum number of jumps to reach end                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 30        | `Dynamic Programming` | Minimum cost to fill given weight in a bag                                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 31        | `Dynamic Programming` | Minimum removals from array to make max –min <= K                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 32        | `Dynamic Programming` | Longest Common Substring                                                                             |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 33        | `Dynamic Programming` | Count number of ways to reacha given score in a game                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 34        | `Dynamic Programming` | Count Balanced Binary Trees of Height h                                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 35        | `Dynamic Programming` | LargestSum Contiguous Subarray [V>V>V>V IMP ]                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 36        | `Dynamic Programming` | Smallest sum contiguous subarray                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 37        | `Dynamic Programming` | Unbounded Knapsack (Repetition of items allowed)                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 38        | `Dynamic Programming` | Word Break Problem                                                                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 39        | `Dynamic Programming` | Largest Independent Set Problem                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 40        | `Dynamic Programming` | Partition problem                                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 41        | `Dynamic Programming` | Longest Palindromic Subsequence                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 42        | `Dynamic Programming` | Count All Palindromic Subsequence in a given String                                                  |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 43        | `Dynamic Programming` | Longest Palindromic Substring                                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 44        | `Dynamic Programming` | Longest alternating subsequence                                                                      |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 45        | `Dynamic Programming` | Weighted Job Scheduling                                                                              |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 46        | `Dynamic Programming` | Coin game winner where every player has three choices                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 47        | `Dynamic Programming` | Count Derangements (Permutation such that no element appears in its original position) [ IMPORTANT ] |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 48        | `Dynamic Programming` | Maximum profit by buying and selling a share at most twice [ IMP ]                                   |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 49        | `Dynamic Programming` | Optimal Strategy for a Game                                                                          |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 50        | `Dynamic Programming` | Optimal Binary Search Tree                                                                           |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 51        | `Dynamic Programming` | Palindrome PartitioningProblem                                                                       |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 52        | `Dynamic Programming` | Word Wrap Problem                                                                                    |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 53        | `Dynamic Programming` | Mobile Numeric Keypad Problem [ IMP ]                                                                |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 54        | `Dynamic Programming` | Boolean Parenthesization Problem                                                                     |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 55        | `Dynamic Programming` | Largest rectangular sub-matrix whose sum is 0                                                        |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 56        | `Dynamic Programming` | Largest area rectangular sub-matrix with equal number of 1’s and 0’s [ IMP ]                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 57        | `Dynamic Programming` | Maximum sum rectangle in a 2D matrix                                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 58        | `Dynamic Programming` | Maximum profit by buying and selling a share at most k times                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 59        | `Dynamic Programming` | Find if a string is interleaved of two other strings                                                 |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |
| 60        | `Dynamic Programming` | Maximum Length of Pair Chain                                                                         |❌         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a> |

<br/>
<div align="right">
    <b><a href="#450-dsa-sheet">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

## Bit Manipulation

<details>

<summary><img id="bm" src="https://img.shields.io/badge/Bit_Manipulation-10-bluevoilet?style=for-the-badge"></summary>

| S.No.     | Topic:                | Problem                                                                                              | Solutions | Python | C++    | Java   |
| --------  |:---------------------:|------------------------------------------------------------------------------------------------------|:---------:|--------|--------|--------|
| 1         | `Bit Manipulation`    | Count set bits in an integer                                                                         |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%203%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/15%5D.%20Bit%20Manipulation/_01)_Number_of_1_Bits.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_01)_0_Count_SetBit.java"><img src="https://img.shields.io/badge/Solution-1-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_01)_1_Count_SetBits.java"><img src="https://img.shields.io/badge/Solution-2-green"></a> |
| 2         | `Bit Manipulation`    | Find the two non-repeating elements in an array of repeating elements                                |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%203%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/15%5D.%20Bit%20Manipulation/_02)_Non_Repeating_Numbers.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_02)_0_Non_Repeating_Elements.java"><img src="https://img.shields.io/badge/Solution-1-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_02)_1_Non_Repeating_Elements.java"><img src="https://img.shields.io/badge/Solution-2-green"></a> |
| 3         | `Bit Manipulation`    | Count number of bits to be flipped to convert A to B                                                 |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%203%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/15%5D.%20Bit%20Manipulation/_03)_Bit_Difference.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_03)_Bits_To_Flip.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 4         | `Bit Manipulation`    | Count total set bits in all numbers from 1 to n                                                      |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%203%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/15%5D.%20Bit%20Manipulation/_04)_Count_total_set_bits.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_04)_0_Total_SetBits_in_Range.java"><img src="https://img.shields.io/badge/Solution-1-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_04)_1_Total_SetBits_in_Range.java"><img src="https://img.shields.io/badge/Solution-2-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_04)_2_Total_SetBits_in_Range.java"><img src="https://img.shields.io/badge/Solution-3-green"></a> |
| 5         | `Bit Manipulation`    | Program to find whether a no is power of two                                                         |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%203%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/15%5D.%20Bit%20Manipulation/_05)_Power_of_2.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_05)_Power_Of_2_or_Not.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 6         | `Bit Manipulation`    | Find position of the only set bit                                                                    |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%203%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/C%2B%2B/15%5D.%20Bit%20Manipulation/_06)_Find_position_of_set_bit.cpp"><img src="https://img.shields.io/badge/Solution-green"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_06)_Position_Of_Only_SetBit.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 7         | `Bit Manipulation`    | Copy set bits in a range                                                                             |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_07)_0_Copy_SetBits_From_X_to_Y.java"><img src="https://img.shields.io/badge/Solution-1-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_07)_1_Copy_SetBits_From_X_to_Y.java"><img src="https://img.shields.io/badge/Solution-2-green"></a> |
| 8         | `Bit Manipulation`    | Divide two integers without using multiplication, division and mod operator                          |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_08)_Division.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 9         | `Bit Manipulation`    | Calculate square of a number without using *, / and pow()                                            |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_09)_Square_Of_a_Number.java"><img src="https://img.shields.io/badge/Solution-green"></a> |
| 10        | `Bit Manipulation`    | Power Set                                                                                            |✔️         |<a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="#"><img src="https://img.shields.io/badge/Solution-red"></a>  |  <a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_10)_0_Power_Set.java"><img src="https://img.shields.io/badge/Solution-1-green"></a><br><a href="https://github.com/AkashSingh3031/The-Complete-FAANG-Preparation/blob/master/1%5D.%20DSA/3%5D.%20450%20DSA%20by%20(%20Love%20Babbar%20Bhaiya%20)/Java/15%5D.%20Bit%20Manipulation/_10)_1_Power_Set.java"><img src="https://img.shields.io/badge/Solution-2-green"></a> |
<br/>
<div align="right">
    <b><a href="#450-dsa-sheet">⬆️ Back to Top</a></b>
</div>
<br/>
</details>

