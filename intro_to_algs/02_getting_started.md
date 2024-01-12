# 2.1 Insertion Sort

## Loop Invariant
"A tool used for proving statements about the properties of our algorithms" \
Often used to prove correctness

To prove correctness, we need to show three things:

### Initialization
"If it is true prior to the first iteration of the loop"

### Maintenance
"If it is true before an iteration of the loop, it remains true before the next iteration"

### Termination
"The loop terminates, and when it terminations, the invariant - usually along with the reason that the loop termianted - gives us a useful property that helps show that the algorithm is correct."

## Exercises

### 2.1-2
Initialization: The value is 0 because nothing is added in yet \
Maintenance: Determine what the value after the operation should be and check whether the operation gave the correct answer \
Termination: If the iteration is finite and every maintenance check ended in success, then the operation gave a correct answer

### 2.1-4
linear_search(A, n, x)
    for i = 0 to n
        if A[i] == x
            return i
    return NIL

###  2.1-5
ADD-BINARY-INTEGERS(A, B, n)
    C = [] size n
    c = 0
    a = 0
    b = 0
    for i = 0 to n - 1
        a += A[i]
        b += B[i]
    a *= 2^i
    b *= 2^i
    c = a + b
    store c in binary to C
    

# 2.2 Analyzing algorithms

## Exercises

### 2.2-1
O(n^3)

### 2.2-2
Selection sort pseudocode: 

SELECTION-SORT(A, n)
    max = 0
    temp = 0
    for curr = 0 to n - 1
        for i = curr to n - 1
            if A[i] > A[max]
                max = i
        temp = A[max]
        A[max] = A[curr]
        A[curr] = A[max]
    return A

Time complexity: O(n^2) for best and worse time complexity

Loop invariant of selection sort:\
Initialization: Initially, our sorted array is empty, so sorted?\
Maintenance: After each iteration, A[1:current] gives us a sorted array\
Termination: At the end, A[1:n] gives us a sorted array

### 2.2-3
- After many iterations, it'll average out to about n/2
- Worse case is that the item is not present and that it'll have to go through n items
- Best: O(1) if it's the first item, O(n) if the item is last or not present, which means it has to check all n elements before comming to a conclusion

### 2.2-4
Taking advantage of any ways to not repeat any work?

# 2.3 Designing algorithms