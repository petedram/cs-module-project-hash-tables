"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)


q is ordered set of numbers, no dups
example: q = (1, 3, 4, 7, 12)

function: f(x) = x * 4 + 6

If you choose 4 numbers from `q`, call them `a`, `b`, `c`, and `d`:

What are the combinations of `f(a) + f(b)` that are algebraically
equivalent to the combinations of `f(c) - f(d)`?

That is, show all `a`, `b`, `c`, `d` for which this is true:
f(a) + f(b) = f(c) - f(d)

For the above `q`, we get this sample output:

```
f(1) + f(1) = f(12) - f(7)    10 + 10 = 54 - 34
f(1) + f(4) = f(12) - f(4)    10 + 22 = 54 - 22
f(4) + f(1) = f(12) - f(4)    22 + 10 = 54 - 22
f(1) + f(7) = f(12) - f(1)    10 + 34 = 54 - 10
f(4) + f(4) = f(12) - f(1)    22 + 22 = 54 - 10
f(7) + f(1) = f(12) - f(1)    34 + 10 = 54 - 10
f(3) + f(3) = f(12) - f(3)    18 + 18 = 54 - 18
```

UPER

looks like can reuse a number more than once
try every combination?
    try every pair to see the result then match results?
    if 5 nums and can reuse, num against every other and itself = 5 pairs for each num?

    take a num, use it as f(a) then for each num (including itself) get the result for f(b)
    do the same for f(c) - f(d)

    Use dictionary?
        each combo as a key e.g. "num1+num2", value is result
        key as a string: "+,num1,num2"?
        need to know if + or - to match them
            first char is indication of type
            cycle through finding matching values with opposite types
            return strings in array: "f{num1} + f{num2} = f{num1} - f{num2}     {res1} + {res2} = {res1} - {res2}" 

    create object instead of dictionary?

        if use an object:
            self.type = '+' or '-'
            self.num1 = num1
            self.num2 = num2
            self.res1 = res1
            self.res2 = res2
            self.result = result

        Once all combos loaded into objects, iterate over them to find type '+' which has same result as type '-'
        Then load them into return array as strings per above.

        This could take a long time:
            create node for every combo: n^2
            cycle through each node to find opposite types with same result
            construct array of strings to return

"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

def f(x):
    return x * 4 + 6

# Your code here
class Node:
    def __init__(self, nodeType, num1, num2):
        self.nodeType = nodeType
        self.num1 = num1
        self.num2 = num2
        self.res1 = None
        self.res2 = None
        self.result = None

nodeArrayAB = []
nodeArrayCD = []

#a+b
for num in q:
    num1 = num
    for num in q:
        num2 = num
        newNode = Node('+',num1,num2)
        newNode.res1 = f(num1)
        newNode.res2 = f(num2)
        newNode.result = newNode.res1 + newNode.res2
        nodeArrayAB.append(newNode)

#c-d
for num in q:
    num1 = num
    for num in q:
        num2 = num
        newNode = Node('-',num1,num2)
        newNode.res1 = f(num1)
        newNode.res2 = f(num2)
        newNode.result = newNode.res1 - newNode.res2
        nodeArrayCD.append(newNode)

# Once all combos loaded into objects, iterate over them to find type '+' which has same result as type '-'
# return string if true
for node in nodeArrayAB:
    nodeType = node.nodeType
    result = node.result
    num1 = node.num1
    num2 = node.num2
    res1 = node.res1
    res2 = node.res2
    for node in nodeArrayCD:
        if node.result == result:
            if node.nodeType != nodeType:
                print(f'f({num1}) + f({num2}) = f({node.num1}) - f({node.num2})     {res1} + {res2} = {node.res1} - {node.res2}')



