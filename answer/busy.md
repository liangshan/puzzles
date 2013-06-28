# 招聘很忙

## 题目概述
应聘者与项目的双选会，假设有M个项目，编号1～M，另有N名应聘者，编号1～N，每个应聘者能选择最多三个，最少一个感兴趣的项目。
选定以后，HR就会安排项目负责人和相应感兴趣的应聘者一一面谈，每次面谈持续半小时。请你按照以下要求，设计一个算法，帮助面试各方尽量节约时间。

1. 应聘者很忙，假设应聘者在第一个面试开始时到达，最后一个面试结束后离开。在一个项目的面试后，不能立刻参加下一个项目组面试，就必须等待。所以请尽量让应聘者面试集中，减少他们的等待时间。
2. 项目负责人很忙，请在保证1的前提下，使得项目负责人等待时间最少。
3. HR很忙。HR需要从第一轮面试开始，待到最后一轮面试结束。请在保证1，2的前提下让整体面试时间最短。

## 输入
文件方式输入，文件名iw.in，每行格式：应聘者编号 项目编号

样例：
```
    1 1
    1 2
    1 3
    2 1
    3 1
    3 2
    0 0
```
这表示M=3，N=3，编号1的应聘者选择了1，2，3项目，编号2的应聘者选择了1项目，编号3的应聘者选择了1，2项目

## 输出
文件方式输出，文件名iw.out，每行格式：行号为项目编号，每行为依次面试的应聘者编号序列。

样例：
```
    1 3 2
    3 1 0
    0 0 1
```
这表示1项目，第一轮面试1号应聘者，第二轮3号，第三轮2号。依次类推。

## 解答
这个题目因为是从招聘信息中看到，所以我也没有标准答案。只说说我的解法。

当然首先可以想到的解是把所有安排方式都列出来，然后找出满足条件最省时间的解法。而我的解法和随机有关。

我认为这道题目可以通过 [模拟退火算法](http://zh.wikipedia.org/wiki/%E6%A8%A1%E6%8B%9F%E9%80%80%E7%81%AB) 来找到局部最优解。

1. 定义评价函数。按照题目要求，我们评价一个方案的好坏依据评聘者，项目负责人，HR等待的时间。所以我们使用`pow(waste_of_user, 2) + waste_of_projects + sqrt(hr)`来评估一组解的好坏。
2. 随机找到一组可能的解，通过上面的公式算出评价。此时整个算法有一个较高的“温度”
3. 修改这组解中的任意一个值，从而得出一个新的解，再次算出评价。如果结果更好，则重复这个过程并给算法“降温”，如果结果更差则利用退火公式决定是否接受这个更差的结果。
4. 反复第3步直到算法“温度为0”

附上 [代码](https://github.com/liangshan/puzzles/blob/master/code/busy.py)