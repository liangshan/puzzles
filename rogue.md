## 聪明的小偷
有一个贼在偷窃一家商店时发现有n件物品。第i件物品值v(i)元，重w(i)磅，此处v(i)和w(i)都是整数。他当然希望带走的东西越值钱越好，但他的背包中至多只能装下W磅的东西，W为一整数。那么他应该带哪几样东西呢？考虑2种情形：

1. 每件物品必须整体带走
2. 每件物品可以只带一部分

给出每种情形的解答，并讲出其中的区别

## 解答
这里面包含了2个问题。先说第二种情况，即可以只带一部分，也是大多数人立刻就能给出解答的情形：只要用v(i)/w(i)算出每一个物品的性价比，从单价最高的开始拿，依次拿满W即可。这种算法有一个很贴切的名字：**贪心算法**

再说每件物品必须整体带走。我们可以将这个问题稍微抽象一下：

```
设V[i][j]表示前i件物品，装入限重j的包中的最大价值。
```
很显然的一个性质是，对于任意的i和j，`V[0][j] = V[i][0] = 0`。

而本题的解其实就是求`V[n][W]`。

那么对于给定的j，每个第i个物品而言只有拿与不拿两种选择。如果拿，那么`V[i][j] = V[i-1][j-w(i)] + v(i)`；不拿，那么`V[i][j] = V[i-1][j]`。于是得到如下公式:

```
V[i][j] = max(V[i-1][j-w(i)] + v(i), V[i-1][j])
```

那么从`V[0][0]`使用两层循环即可得到每一个`V[i][j]`的值。最终得到的`V[n][W]`即为可以偷到的最大价值。

但我对这个题目做了一点伸展，要求算出具体拿了哪些物品。这也很简单，在V这个`n*W`的矩阵中，具有`V[i][j] >= V[i-1][j]`的特性。所以只要从`V[n][W]`开始往前逐层检查，如果`v[i][W] > v[i-1][W]`，那么第i件物品就是要拿的。

这道题目同时是一个很典型的 **动态规划** 问题。即运算只关注当前遇到的子问题，通过逐步解决子问题来得到最终的解。相同的算法还应用于 **动态导航** 以及 **查找最长公共子字符串** 等问题上。另外，从本题中还能注意到每一个子问题`V[i][j]`在整个过程中需要重复利用，这也是动态规划问题很重要的特征。

最后 **贪心算法** 本质上也是一种动态规划，不同的是，贪心算法的每个子问题都有确定的最优解。比如在本题中，每次直接拿当前单价最贵的即可。而在压缩编码领域， **赫夫曼编码** 正是贪心算法的一个应用。

以下附上Python代码

### Code
```python
# -*- coding: utf-8 -*-
import sys
from getopt import getopt

def package(items,limit):
	print "Items list:"
	for i in items:
		item = items.get(i)
		print "%s weight:%s value:%s" % (item['n'],item['w'],item['v'])

	print "weight limit:%s" % limit	

	N = len(items)
	F = [[0 for col in range(limit+1)] for row in range(N+1)]
	P = [[0 for col in range(limit+1)] for row in range(N+1)]
	result = []

	print "stealing..."
	for i in range(1,N+1):
		for j in range(0,limit+1):
			if j >= items.get(i).get('w'):
				if F[i-1][j-items.get(i).get('w')] + items.get(i).get('v') > F[i-1][j]:
					F[i][j] = F[i-1][j-items.get(i).get('w')] + items.get(i).get('v')
					P[i][j] = 1
				else:
					F[i][j] = F[i-1][j]

	print "max value:%s" % F[N][limit]

	i = N
	j = limit 
	while i > 0:
		if P[i][j] == 1:
			result.append(i)
			j = j-items.get(i).get('w')
		
		i = i-1

	print "Items picked:"
	for i in result[::-1]:
		print items.get(i)['n']

if __name__ == '__main__':
    items = {1:{'n':'A','w':240,'v':5000},2:{'n':'B','w':200,'v':4300},3:{'n':'C','w':100,'v':8000}}
    weight = 500

    opts, args = getopt(sys.argv[1:], 'w:', ['weight='])
    for o, a in opts:
        if o in ('-w', '--weight'):
            weight = int(a)
        else:
            pass
            
    package(items, weight)
```


