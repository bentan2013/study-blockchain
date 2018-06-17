<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. 代码实践</a>
<ul>
<li><a href="#sec-1-1">1.1. 数据结构</a></li>
<li><a href="#sec-1-2">1.2. 加密</a></li>
<li><a href="#sec-1-3">1.3. 共识机制</a>
<ul>
<li><a href="#sec-1-3-1">1.3.1. Proof of work计算量模拟</a></li>
<li><a href="#sec-1-3-2">1.3.2. 模拟双重支付</a></li>
</ul>
</li>
</ul>
</li>
</ul>
</div>
</div>

github.io地址： <https://bentan2013.github.io/study-blockchain/>
github 地址: <https://github.com/bentan2013/study-blockchain>

# 代码实践<a id="sec-1" name="sec-1"></a>

## 数据结构<a id="sec-1-1" name="sec-1-1"></a>

引用实验楼的相关代码。(具体出处不详)
代码：[struct<sub>block</sub>.py](https://github.com/bentan2013/study-blockchain/blob/master/struct_bitcoin.py)

代码中包括了区块的数据结构的模拟，和梅克尔树的相关知识。

## 加密<a id="sec-1-2" name="sec-1-2"></a>

参考: [实验楼文档](https://www.shiyanlou.com/courses/890/labs/3248/document)

[代码：encryption.py](https://github.com/bentan2013/study-blockchain/blob/master/encryption.py) 
实验楼是python2.7的，我想改成python3.5的，目前还没有完成。

## 共识机制<a id="sec-1-3" name="sec-1-3"></a>

### Proof of work计算量模拟<a id="sec-1-3-1" name="sec-1-3-1"></a>

引用: [实验楼文档](https://www.shiyanlou.com/courses/890/labs/3248/document)

代码：[proof<sub>of</sub><sub>work</sub><sub>difficulty</sub>.py](https://github.com/bentan2013/study-blockchain/blob/master/proof_of_work_difficulty.py) 

纯引用，没有修改。可以发现，随着计算出的hash值前面的0的个数的增加（即hash值要小于某一个值），
增加的计算时间是巨大的。

### 模拟双重支付<a id="sec-1-3-2" name="sec-1-3-2"></a>

在看了共识和双重支付相关的文章之后，就自己写了一段代码

代码： [double payment simulation](https://github.com/bentan2013/study-blockchain/blob/master/double_payment_simulation.py)

其中可以设置在交易完成之后，经过了多少次确认之后，evil nodes开始双重支付。
最后使用一个图来表示，有正确交易的链的增长情况和包含不正确交易的链的增长情况。

没有51%算力时，失败的双重支付

![img](https://user-images.githubusercontent.com/5510943/41500062-b67970be-71bd-11e8-894a-4e451d2fb5eb.gif)

超过51%算力时，成功的双重支付

![img](https://user-images.githubusercontent.com/5510943/41508131-6362fd90-7272-11e8-8bf1-c29987eda770.gif)