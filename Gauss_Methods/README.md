# Explanation for Simple Gauss algorithm (without numpy)

__This is the explanation for the file [`Gauss.py`](https://github.com/Jumaruba/MNUM/blob/master/Gauss_Methods/Gauss.py)__.

To understant the _Simple Gauss Algorithm_ it's important you to know how to do the  Gaussian Elimination.  
If you don't know, brilliant website explains it very well: [`gauss-elimination`](https://brilliant.org/wiki/gaussian-elimination/).

The first function at the file is rowOp. It basically subtracts one line from the other multiplied by a constant k: 
```python
def rowOp(down, up, k):
    global matrix
    for p in range(len(matrix[0])):
        matrix[down][p] -= k * matrix[up][p]
```

So, let's suppose we have the following matrix: 

![matrix](https://github.com/Jumaruba/MNUM/blob/master/Images/mainMatrix.gif)

And we want to put `d` as zero. To do so, we call `rowOp` with the arguments `down = 1` _(because the target is at the line 1)_, `up = 0` _(because a is at line 0)_ and we need to calculate a: 

![](https://github.com/Jumaruba/MNUM/blob/master/Images/d-ka.gif)  
![](https://github.com/Jumaruba/MNUM/blob/master/Images/k.gif)  

Then we will have this:  
  
![](https://github.com/Jumaruba/MNUM/blob/master/Images/CodeCogsEqn.gif)
  
Since it's clear how `rowOp` works, let's analyse the second function:  
  
```python
def gauss():
    global matrix
    for i in range(len(matrix)):   
        rowOp(i, i, (1 - 1 / matrix[i][i]))  
        for j in range(i, len(matrix)): 
            if i != j:
                rowOp(j, i, matrix[j][i])  
```

In the firt lines we have:  
  
```python
for i in range(len(matrix)):    #for each column of the matrix
        rowOp(i, i, (1 - 1 / matrix[i][i]))    # set the diagonal to 1
```
  
Then for the next for cicle:  

```python
for j in range(i, len(matrix)): #for each line of the column i
            if i != j:
            #put each line of the column i (below the diagonal line)
            #to zero
                rowOp(j, i, matrix[j][i]) 
                
```
