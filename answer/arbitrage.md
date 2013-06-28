# 套汇
套汇是指利用货币兑率的差异，把一个单位的某种货币转换为大于一个单位同种货币的方法。比如，假设1美元可以兑换46.4印度卢比，1印度卢比可以买2.5日元，1日元可以买0.0091美元。如果不考虑手续费，一个人可以从1美元开始买入，得到`46.4*2.5*0.0091=1.0556`美元，从而获得5.56%的利润。

假设已知n种货币c1,c2,...,cn和有关兑换率的n^2的表R，那么一个单位的货币ci可以买入`R[i,j]`单位的货币cj。写出一个有效算法，以确定是否存在一个货币序列可以实现套汇。

## 解答
这道题目需要用到图的相关知识。由题目可知，答案可等价为：确定是否存在一个货币序列可以满足

```
R[i1,i2] * R[i2,i3] ... R[i(k-1),i(k)] * R[i(k),i1] > 1
```

这里需要一点基础的数学知识了，上述条件需要经过2次推导

```
1 / (R[i1,i2] * R[i2,i3] ... R[i(k-1),i(k)] * R[i(k),i1]) < 1

lg(1/R[i1,i2]) + lg(1/R[i2,i3]) + ... + lg(1/R[i(k),i1]) < 0
```

对于图算法熟悉的同学到这里就能看端倪了。到这里，要求已经转化为：以每种货币为节点，(ci,cj)为边，lg(1/R[i,j])为权值的图里，是否存在一个负权值回路。

可以使用最标准的 [Bellman-Ford算法](http://zh.wikipedia.org/zh-cn/%E8%B4%9D%E5%B0%94%E6%9B%BC-%E7%A6%8F%E7%89%B9%E7%AE%97%E6%B3%95) 即可有解。

那么思考题就是：写出一个有效算法来输出该序列(如果存在)，并分析算法的时间复杂度。