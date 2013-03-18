#随机算法

在研究概率的相关问题时，输入参数是否是完全随机是一个重要因素。

假定一个数组A[n]包含了数字1～n，设计一个算法构造这个数组的随机序列。

##解答

一个常用的方法是为数组的每个元素A[i]赋一个随机的优先级P[i]，然后依据优先级对数组A中的元素进行排序。通常我们称这个过程为`PERMUTE-BY-SORTING`

```
n <- length[A]
for i <- 1 to n
    do P[i] = RANDOM(1, n^3)
sort A, using P as sort keys
```

显然的，上述方法需要引入一个额外的P[i]，一个更好的方法是原地排列给定数列。在第i次迭代时，元素A[i]从元素A[i]到A[n]中随机选取。这个过程我们称作`RANDOMIZE-IN-PLACE`

```
n <- length[A]
for i <- 1 to n
    do swap A[i] <-> A[RANDOM(i, n)]
```

这里有两个很有意思的地方

1. 第二种算法中，`swap A[i] <-> A[RANDOM(i, n)]` 而不是`swap A[i] <-> A[RANDOM(0, n)]`, but why?
2. 有人可能会有这样的想法，即要证明一个排列是随机均匀的，只要证明对于每个元素A[i]，其位于位置j的概率是1/n就足够了。但事实并非如此，why?
