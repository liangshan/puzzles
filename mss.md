## 长城以外
> Across the Great Wall, we can reach every corner in the world

由于众所周知的原因，我们的网站需要过滤屏蔽词。我们的屏蔽词库大约有3万个，如何实现就是一个难题，相信大家也很好奇我们是怎么做到每分钟处理集团超过20万次的屏蔽词过滤需求。

把这个问题抽象一下：
```
给定一个词库A，每当传入一个字符串B，返回B包含了A中的哪些词
```

先给一个不适用的答案，时间复杂度O(m * n):
```
for (word in A) {
    if (word is part of B) {
        result.append(word)
    }    
}
```




