# ♎️

# <font face="Comic Sans MS" color=#666666>所以你也来看我了?🧐</font>
<br><br>

> <font face="Noto Serif SC" color=#00DDAA>相识 漫长 了解 靠近 倾心 惊讶 窃喜 慌张 担忧 逃避 试探 渴望 纠结 快乐 小心 假装 疑惑 关于 决定 真心 勇气 承认 庆幸 期待 相信 沉迷 疯狂 幻境 极致 依赖 冷淡 哽咽 心酸 错过 自嘲 痛苦 绝境 极端 迷茫 无奈 摧毁 失败 失望 狠心 缓解 否定 浮沉 人海 真实 早睡 祝好 所谓 爱情 皆与此</font>

<br><br>

# <font face="Comic Sans MS" color=#87CEFA>This is the <font face="Computer Modern" color=#FF0000>Recording File </font>of my life since <font face="Comic Sans MS" color=#77FF00>1969</font>.😗😢</font>

[![HitCount](http://hits.dwyl.com/ExcaliburEX/KeMo.svg)](http://hits.dwyl.com/ExcaliburEX/KeMo)

[![GitHub Issues](https://img.shields.io/github/issues/ExcaliburEX/KeMo)](https://github.com/ExcaliburEX/KeMo/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/ExcaliburEX/KeMo.svg)](https://github.com/ExcaliburEX/KeMo/pulls)
![forks](https://img.shields.io/github/forks/ExcaliburEX/KeMo)
![stars](	https://img.shields.io/github/stars/ExcaliburEX/KeMo)
![repo size](https://img.shields.io/github/repo-size/ExcaliburEX/KeMo)
![](https://img.shields.io/badge/Followers-6666-brightgreen)  ![](https://img.shields.io/badge/Rating-10000-orange)  ![](https://img.shields.io/badge/chat-9999-blue)
![Copyright](https://img.shields.io/static/v1.svg?label=My%20cool%20project%20©️%20&message=%202020%20Name&labelColor=informational&color=033450) 
[![Follow us on AngelList](https://img.shields.io/static/v1.svg?label=Follow%20us&message=😇&color=black&logo=angellist&logoColor=white&labelColor=black)](https://angel.co/company/thumbtack) 
[![Buy me a coffee](https://img.shields.io/static/v1.svg?label=Buy%20me%20a%20coffee&message=🥨&color=black&logo=buy%20me%20a%20coffee&logoColor=white&labelColor=6f4e37)](https://your-donate-link)
[![Add to Chrome](https://img.shields.io/static/v1.svg?label=Add%20to&message=Chrome%20🧘)](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd) 
[![Email me](https://img.shields.io/static/v1.svg?label=Email%20me&labelColor=blueviolet&message=📧)](mailto:912011727@qq.com) 
![MIT License](https://img.shields.io/static/v1.svg?label=📜%20License&message=MIT&color=informational) 
[![Listen to the podcast](https://img.shields.io/static/v1.svg?label=%F0%9F%8E%A7%20Listen%20to%20the%20&message=podcast&labelColor=d83a0c&color=381206)](https://dcs.megaphone.fm/KM1909355062.mp3?key=08b1b80a1b7d75383e6da1a741aedfdb) 




# <font face="Times New Roman" color=#0044BB >20.7.4~7.13</font>
##  基于P2P的分布式存储的研究与实现

### 基本信息

- 硕士论文

- 2004年

- 关键词：`P2P 模型`；`资源查找`；`冗余` 

- 摘要

  > “基于 P2P 的分布式存储系统”是四川省科技厅“青年软件创新工程”资助项目。 
  >
  > 
  >
  > 本系统在 P2P 的基础上采用了 Server-to-Server 的模型，各个 Server 之间完全对等，通过路由关系连接起来。客户从任何一个 Server 上都可以查询并访问系统中的所有文件，同时每一个 Server 上的文件及其存储信息都被冗余备份到其他Server 上，提供了较高的容错性。此外，本系统的文件存储信息采用 XML 方式存放，有利于 WEB 方式发布和查询信息。 
  >
  > 
  >
  > 在基础理论中，首先介绍了 I/O 模型，并对几种网络服务器内部架构进行了分析和比较，最后介绍了 XML 语言的基本概念和相关语法。随后，我们讨论了P2P 的各种资源查找算法，并详细描述了本系统使用的基于关键字的路由模型的主要算法和设计。在对网络分布存储及其技术研究的基础上，我们设计了一个基于 P2P 模型的分布式存储系统。本系统采用分层结构，以路由层作为基础，在其上实现了对象传输层和命令解释层。在命令解释层实现了一个基于线程池的任务驱动的服务器框架模型，它监听 UDP 端口，并维护一个全局任务队列，所有收到的命令都作为一个任务放到任务队列中由处理线程进行命令分发，调用对象传输层处理；在对象传输层实现了资源查找算法，设计并实现了一套基于 UDP 的传输协议用于客户与服务器之间，以及服务器内部之间的命令交互，同时还设计了以 XML 方式存放的文件存储指针格式；最后，实现了一个定时模块，使得各种网络延时较大的任务可以通过定时队列得到异步响应，从而释放相应的处理线程，并且对于延时太久的任务可以实现超时重发。
  >
  > 
  >
  >  通过对本系统的初步测试，表明该系统实现了设计目标并具有较好的性能。

- 引用格式

    > 陈刚, 基于P2P的分布式存储的研究与实现, 2004, 电子科技大学.

### 摘录

- `Server-to-Server`模型，各个Server之间完全对等，通过路由关系连接起来，同时每一个 Server 上的文件及其存储信息都被冗余备份到其他Server 上。
-  在本系统中**冗余备份**主要包括：**实际文件的冗余**和**文件存储指针的冗余**。
-  实际文件的冗余包括**分片冗余**和**拷贝冗余**。这部分工作是上传服务器在文件上传成功后，调用冗余备份模块，进行冗余存储，并将冗余信息记录在文件存储指针中，这些对于用户来说都是透明的。
- 如果是分片存储，在下载时需要客户端的支持。文件存储指针的冗余则分为三个层次。
  - 第一个层次是在通过文件名哈希算法计算出文件 $ID$ 值时，对这个 $ID$ 值加上两个偏移量，从而得到另外两个 $ID$，这样文件存储指针按照三个 $ID$ 值分别存放在三个不同的服务器上，从而实现冗余。偏移量的选取跟 $ID$值的取值空间有关，假设取值空间中最大值为$ID_{max}$，则两个偏移量为$\dfrac{1}{3}ID_{max}$，$\dfrac{2}{3}ID_{max}$，由于本系统的路由算法跟距离相关，$ID$ 值相差越大，节点的实际距离也越大，因此这样取值的偏移量可以使的三个拷贝尽量存放在相隔较远的节点。
  - 第二个层次的冗余是当文件存储指针存放到某个节点服务器后，它会再备份到跟它 $ID$ 值最相近的两个节点上，一个是 $ID$ 值比它大，一个 $ID$ 值比它小，因为如果这个节点出现故障时，那么原来那些把它作为相关节点的文件，当再次进行路由定位时将会定位到跟它 $ID$ 值最接近的两个节点上，而这两个节点就接替它成为那些文件的相关节点。
  - 第三个层次是通过高速缓存来冗余备份，具体来说就是，每个节点都建立自己的高速缓存，在一个文件存储指针从初始节点到目的节点的路由过程中，所经过的所有节点都把该存储指针在自己的高速缓存中留一份拷贝。这样当某个节点查询一个文件时，查询报文在路由过程中将会在每个路由节点的高速缓存中查找，如果发现有匹配项，就可以立刻返回，最坏的情况是直到相关节点才找到。当然，如果查找高速缓存没有命中的话反而会延缓查找过程，为了防止这种情况出现，我们采用**旁路技术**，即在每个路由节点查找高速缓存的时候，不管是否命中缓存，都直接把查询报文向下一个节点转发。<u>这样就不会因为没有命中缓存而延缓查询过程，但是如果有多个节点命中缓存的话，就会产生多份冗余报文发送给请求服务器。</u>不过对于路由节点不多的情况下，是可以忍受的。 
  - 如图 3-2所示，当文件 Myfile 存储到 A 节点后，根据资源定位算法，它的文件存储指针被存放到 F 节点上。当我们在 B 节点访问 Myfile 时，如果没有高速缓存，则需要从 B 路由到 F，才能从 F 节点上获得 Myfile 的文件存储指针，然后 B 再跟 A连接，访问到 Myfile；而引入高速缓存后，在从 A 路由到 F 节点的过程中，  C、D 节点上的高速缓存中就保存了 Myfile 的文件存储指针拷贝，此时 B 在路由到C 时就在 C 的高速缓存中发现了 Myfile 的存储指针，从而立刻返回到 B，然后 B就可以直接从 A 中访问到 Myfile 了。 
  - <img src='https://i.loli.net/2020/07/10/PElVTvwtR86ofzK.png' title='quicker_9f1a2917-2d82-4260-bf2a-2d8e4ca87f84.png' />
- 在系统设计的时候我们的目标是在存放文件存储指针的服务器故障的时候，通过冗余备份信息获得文件存储指针。 

### 思考




## Peer-to-Peer存储系统中一种高效的数据维护方案

### 基本信息

- 软件学报

- 2009年

- 关键词：`对等网络存储`;`数据维护`;`永久失效`;`暂时失效`;`失效检测`;`带宽优化`  

- 摘要

  > 提出一套完整的数据维护方案.该方案建立在 P2P 环境动态性特点的基础上.一方面,该方案考虑了节点动态性差异,它基于不同的动态性作相应的数据冗余,能够用更少的冗余开销来保证数据的目标可用性;
  >
  > 另一方面,该方案给出如何利用判别器来区分永久失效和暂时失效,以减少由于不必要的数据修复而带来的额外修复开销.通过在真实 P2P 系统 Maze 上的实验结果表明,该方案比目前主流的方案能够节省大约 80%的数据维护带宽。
  
- 引用格式

    > 杨智, 朱君与代亚非, Peer-to-Peer存储系统中一种高效的数据维护方案. 软件学报, 2009. 20(01): 第80-95页.

### 摘录

- 本文基于 P2P 系统节点的动态性规律,研究存储节点的选择方案,以降低系统屏蔽暂时失效所需的数据冗余度,同时;本文将研究如何使用永久失效判别器来检测系统中节点的永久失效,以降低由于系统无法区分暂时失效和永久失效所带来的额外开销.本文的主要贡献如下:  
  - 本文考虑了节点的动态性差异,提出一种基于节点动态性的数据分发算法,它把数据放在动态性相近的节点上,并精确计算出相应的冗余度.相对于传统的随机分发算法,能够在 P2P 这种高动态环境下用更少的冗余开销达到数据的目标可用性.  
  - 如何在时间阈值判别器中设置时间阈值来区分永久和暂时失效是当前 P2P 存储系统研究中的一个难题,本文基于漏判抵消误判的思想,给出了永久失效判别器中参数设置的统一原则,使得时间阈值判别器的性能接近于最优的理想判别器.  
  - 为了提高判别器精度,本文提出了一种新的永久失效判别器:基于节点离开概率的判别器.它在不同的离线长度下给出相应的永久失效概率,而不是只用一个阈值来确定性地判别永久失效,因此,本文提出的判别器比时间阈值判别器更为精确.  
  
- 冗余方式主要包含两类:副本和纠删码(erasure code).  
  - 参数是$(m,n)$的纠删码将原始文件分成$ m$ 个碎片,然后编码成$ n(n>m)$  个碎片,并保证其中任意 $m$个碎片都可以重构文件.最早人们用量化的方法分析了纠删码和副本方式冗余对系统可靠性的影响,但考虑的是较为稳定的环境.之后,研究者重新考察了纠删码对 P2P 存储
    系统可用性的影响,更关注高动态性的系统,指出对于节点可用性比较低的系统,用副本的方式较好,但并没有考虑修复带宽开销[14].关注在 P2P 系统中两种冗余方式下的修复开销,指出副本方式在高动态系统中更为有效.更为复杂的方式是采用副本和纠删码结合的方式,文献[15]的研究表明,这种方式能够更好地优化修复带宽 .
  
- 数据放置策略决定一个数据对象的副本存放在哪些节点上.数据放置策略可以分为两类:**随机放置策略**和**选择放置策略**  

- 目前,主流的数据冗余策略是**随机分发数据**,然后利用节点在线概率的平均值计算出数据的目标冗余度. 但这种方法却忽略了节点间动态性的差异.  
  - 冗余度定义为冗余后的数据量与原始数据量的比值.对于副本方式,冗余度就等于数据副本的个数.对于参数是(m,n)的纠删码,冗余度为 n/m.  
  - 目标冗余度是指能够达到数据目标可用性的最小冗余度  
  
- 本文提出一种基于节点动态性的数据分发算法,它采用与主流方法相同的可用性计算模型,但根据不同的节点动态性产生不同的冗余度,更好地适用于节点动态性差异较大的 P2P 系统.

- 时间阈值判别器，本文将回答如何自动、合理地设置时间阈值τ的难题.另外,还提出一种新的永久错误判别器:**基于概率的判别器**.基于真实 P2P 系统运行日志的模拟实验表明,这两种判别器的性能都接近最优的理想判断器(没有误判和漏判的判断器).  

- **系统的开销模型** ：冗余和修复会耗费系统的资源,从而产生冗余数据或修复数据,这种开销称为系统维护开销。作出如下假设

  - 假设节点间是相互独立的；
  - 节点加入和永久离开系统的平均速率是恒定的；
  - 系统中节点的数量是稳定的。

- **系统的开销模型具体细节**<img src='https://i.loli.net/2020/07/13/SqEQkvyim6dp1Zu.png' title='quicker_f45de31f-2d0d-4df7-b500-badf3cffb308.png' /><img src='https://i.loli.net/2020/07/13/dkgbJ2sm7XvojfG.png' title='quicker_f2054db0-2b3a-4958-aa21-6f204a4caac9.png' />

- **数据的冗余优化**：目前,主流的数据冗余算法是在整个系统里随机选择节点分发数据,然后利用节点在线概率的平均值计算出数据的目标冗余度 ，本节提出的优化算法仍能保证系统中节点的负载平衡(即分发后每个节点上存储相等的数据量),而不是通过不断将负载移向高可用节点来减少冗余度。

  - 节点动态性差异对$k_L$的影响：提出一种新的衡量目标冗余度的算法，相对主流算法在理论上能够节省 30%左右的带宽  
    $$
    I=1-\frac{\tilde{k}_{L}}{k_{L}}=1-\frac{\int_{0}^{1} h f(h) \mathrm{d} h}{\int_{0}^{1}-\log (1-h) f(h) \mathrm{d} h}
    $$
    

  - 基于节点动态性的概率放置算法：<img src='https://i.loli.net/2020/07/13/saDpQUmr3YoHlVK.png' title='quicker_8a3f29e8-2a20-420e-bde2-253f8c3cb1cb.png' />

- **数据修复优化**

  - 基于判别器的数据修复算法

    - Timeout($\tau$) ,时间阈值判别器，属于确定型永久判别器
      $$
      f(\text {node,t})=\left\{\begin{array}{ll}
      A, & \text { if } d(t)=0 \\
      U, & \text { if } 0<d(t)<\tau \\
      D, & \text { if } d(t) \geq \tau
      \end{array}\right.
      $$

    - Probability($f(\xi)$)，概率判别器，$f(\xi)$)是一个以节点离线时间$\xi$为 自 变 量 的 概 率 函 数  
      $$
      f(\text {node,t})=\left\{\begin{array}{ll}
      Z=A, & \text { if } d(t)=0 \\
      P(Z=U)=1-f(d(t)), & \text { if } d(t)>0 \\
      P(Z=D)=f(d(t)), & \text { if } d(t)>0
      \end{array}\right.
      $$

    - <img src='https://i.loli.net/2020/07/13/tEmgSTJC3Uuceok.png' title='quicker_0814d921-50a4-46da-ab6c-c9cfe95df77d.png' />

  - 误判和漏判对$k_R$的影响

  - 两类永久判别器中参数的设置

- <img src='https://i.loli.net/2020/07/13/BhiZ1F2SabMALdl.png' title='quicker_729d0a97-67b4-4dbb-81b1-ff4b72148fb6.png' />

- <img src='https://i.loli.net/2020/07/13/orXE5bIaVYleZGk.png' title='quicker_fdd08dbe-e88f-4339-9a1c-bc81ef374a30.png' />

- <img src='https://i.loli.net/2020/07/13/U4QniIsNOH83cE6.png' title='quicker_674cc7d6-2460-48f1-880a-41346d96fb61.png' />


### 思考
- 算法构件：
  - 冗余算法
    - 纠删码Erasure code
    - 副本冗余方式
    - 数据的随机分发方式
  - 修复算法
    - 积极修复
    - 懒惰修复
- 服务构件：
  - 数据目录服务：Total Recall 中,每个对象都由一个节点来负责,称为 Master.Master 知道它所负责的对象的每个副本存放在哪个节点上,维护了副本与系统中节点的映射关系.当用户(对应图中的 client)读取数据时,首先联系 Master,获取副本的位置,然后再联系存储副本的节点(对应图中的 Data storage hosts)下载 。
  - 节点监控目录：系统中存储每个存储副本的节点向其对应的存储索引的 Master 节点定期发送心跳信息,汇报自己的在线状态.因此,Master 也维护了节点的在线状态,它同时是目录服务和监控服务的提供者.当用户读取数据时,Master 可以用这两种信息告诉用户一个
    当前可用的副本的位置.  
  - <img src='https://i.loli.net/2020/07/11/tbjWHoUyaxmugl7.png' title='quicker_22b7c65e-c1d7-4bad-a44e-d2cbc906ffd8.png' />
- 系统的运行过程如下:数据对象最初存入系统时,冗余算法被调用.冗余算法根据数据的目标可用性并通过监控服务统计出的节点动态性为对象产生一个配置,包括冗余方式、冗余度和放置策略.当数据存入系统后,系统通过目录服务建立副本和节点的对应关系.对于每个数据对象,系统定期地通过目录服务和监控服务查看存放其副本的节点失效情况,以评估对象的冗余度.如果冗余度低于能够保证目标可用性的最低冗余度,则系统触发修复并调用修复算法产生新的副本。



# <font face="Times New Roman" color=#0044BB >20.6.6~7.3</font>
> <font face="Noto Serif SC">到公司后这个项目的更新就有点迟缓了，按理说到公司后大量的工作涌来应该有更多关于各种研究工作的内容可以记录，但事实恰恰相反，心事太多，做了不少事情，但更多地只是想写一旦心事。近来的事情大致可以罗列一下吧。</font>

<font face="Noto Serif SC">1️⃣&emsp;</font>[`博客`](https://kemo.xyz/)又重新修缮了一下，更多地更重要的是对这个[`相识`](https://kemo.xyz/%E7%9B%B8%E8%AF%86.html)的增加更新。说道博客，也帮小治整了老久的博客，我们已经无聊到这种地步了吗？


<font face="Noto Serif SC">2️⃣&emsp;</font>2号下午，新认了个Ai的徒弟，顺便大家一起花了一下午设计了实验室的各种版本的图标。如下：

<img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-07-02-1.png height="200"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-07-02-2.png height="200"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-07-02-3.png height="200"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-07-02-4.png width="200"/>

<img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-07-02-5.png height="150"/>

<font face="Noto Serif SC">3️⃣&emsp;</font>在overleaf上创造了我们实验室的专属[`Latex模板`](https://www.google.com/url?q=https://www.overleaf.com/latex/templates/su-zhou-da-xue-wang-luo-kong-jian-an-quan-shi-yan-shi-latexmo-ban-soochow-university-cyber-security-lab-report-template/zqzfbyjcrtbr&source=gmail&ust=1593880891336000&usg=AFQjCNHtfKA-LnmDHjVrjG_MHnck-IJkyg)。


# <font face="Times New Roman" color=#0044BB >20.5.13~6.5</font>
> <font face="Noto Serif SC">待续</font>
> 
<font face="Noto Serif SC">1️⃣&emsp;[用PySimpleGUI实现一个简易的分布式计算系统——简易多机协同计算原型系统(Simply Multi-Machine Collaborative Computing)](https://blog.csdn.net/ExcaliburUlimited/article/details/106317529)</font>


<font face="Noto Serif SC">2️⃣&emsp;[Adobe Illustrator自制苏大计科院院徽](https://blog.csdn.net/ExcaliburUlimited/article/details/106495298)</font>

<font face="Noto Serif SC">3️⃣&emsp;[全国人社窗口单位业务技能在线自动答题——全国人社自动学习机](https://blog.csdn.net/ExcaliburUlimited/article/details/106569427)</font>




# <font face="Times New Roman" color=#0044BB >20.5.1~5.12</font>
> <font face="Noto Serif SC">少年不识愁滋味，爱上层楼。爱上层楼。为赋新词强说愁。<br>而今识尽愁滋味，欲说还休。欲说还休。却道天凉好个秋。<br><br>真的难，是真的难。<br><br>这半个月过的是真的辛酸，一忽疹疾缠身，一忽又骑车飞摔，蹭的皮开肉绽。身体动弹不得，疹疾又致全身不得按宁。着实不知如何是好，现如今母上也奔赴都市生活，不知不觉，这段儿时至现在都未曾体验过的与母上一起生活这么久的时光已然结束了。激动的三月，慵懒的四月，以前未曾想到会有这样的一段怀念终身的生活，原以为这样的生活只有很多年后的年老之时才可体验。如今只因其过于美好，但终究是要结束的，即使我迷恋这样的生活，但内心的忧虑却也不断地在增加，再美好的时光，但总也要面对现实的压迫的。它的日复一日，每天的日常又是如此的重复，母亲终日看着小说，而我终日地在楼上看着电脑，虽然不舍，但这样的生活终究是不平衡的，我们都不应该被束缚在这里，虽然我们幸福地平平淡淡地陪伴在彼此左右，但此时的它应该是短暂的，我们彼此都有应该去做的事情，于当前，它只是看上去那么平静罢了，可我们还未实现的东西太多了，这样的生活提前来到了，幸福了但也徒增了很多不安。</font>


<font face="Noto Serif SC">1️⃣&emsp;接的爬虫作业(￥500)，应该是利兹大学的，爬取既定网站的所有网页，为每次单词创造包含出现位置以及词频的反向索引等等，写了篇文章：[简单地打造一个搜索工具——爬取所有网页并创造单词的反向索引](https://blog.csdn.net/ExcaliburUlimited/article/details/106087957)</font>

<font face="Noto Serif SC">2️⃣&emsp;帮学妹写了一个遗传算法，[地铁大小交路优化模型的遗传算法求解](https://blog.csdn.net/ExcaliburUlimited/article/details/106088598)</font>

<font face="Noto Serif SC">3️⃣&emsp;接了法学院关于垃圾分类的视频剪辑(￥500)，改的头有点发晕，反馈还是很Nice的。链接: [垃圾分类](https://pan.baidu.com/s/1ixRlLQmwLwLFosRLKcgxaA) 提取码: 2hbi</font>

<font face="Noto Serif SC">4️⃣&emsp;近期讲座汇总：<br>
- [人工智能前沿与交叉_李凡长_2020-05-08](https://pan.baidu.com/s/1LDGeTghYJYbo8kt7rjwoQg) 提取码: tre6
- [功能纳米与软物质研究院讲座_仲启轩_2020-05-10](https://pan.baidu.com/s/1Ds1eqVpc0bTuGF26yOuHsA) 提取码: k5u5
- [知识图谱讲座_李直旭_2020-05-11](https://pan.baidu.com/s/1V2CHLHNpiu37hu_fw4K84Q) 提取码: pzaj </font>










## <font face="Times New Roman" color=#0044BB >20.4.20~4.30</font>
> <font face="Noto Serif SC">时间过的真快，不知不觉，已经来到了这充满谎言的时代的终点。干了点什么呢，记忆逐渐有些模糊不清了。哦，对，因为之前我参加了一个组队学习的活动，因此认识了一些队友，最近队友接单发现没时间做，就拜托我完成。我因此也发现一个代写各种算法作业的地方，第一份任务很满意，从零写一个朴素贝叶斯分类器，一天写完赚了400，还是挺酸爽的。后来又干了什么呢？不记得就是大概是各种琐事缠身，也许这就是孤独的常态。完成了HPC的三个作业，做了一个视频，录了一个演讲。</font>

<font face="Noto Serif SC">1️⃣&emsp;实现了三个作业，[高性能分布式计算(HPC)作业1——节点实时通信](https://blog.csdn.net/ExcaliburUlimited/article/details/105873287)、[高性能分布式计算(HPC)作业2——节点通信，发布计算任务](https://blog.csdn.net/ExcaliburUlimited/article/details/105873303)、[高性能分布式计算(HPC)作业3——节点通信，发布计算任务，并在计算任务中阻塞](https://blog.csdn.net/ExcaliburUlimited/article/details/105873315)。</font>

<font face="Noto Serif SC">2️⃣&emsp;从零实现一个朴素贝叶斯分类器为学生分班，发了CSDN，[从零实现朴素贝叶斯分类器(离散情况)——以学生分班为例](https://blog.csdn.net/ExcaliburUlimited/article/details/105873378)</font>

<font face="Noto Serif SC">3️⃣&emsp;最近pyq充斥了各种问卷星调查问卷，所以写了个秒填爬虫。[利用Selenium秒填朋友圈各种问卷星调查问卷](https://blog.csdn.net/ExcaliburUlimited/article/details/105873424)</font>

<font face="Noto Serif SC">4️⃣&emsp;关于剪的研会的云采访视频，已经上传到B站，点击下方图片跳转。</font>
[![](https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-05-01-%E8%A7%86%E9%A2%91%E6%88%AA%E5%9B%BE.png)](https://www.bilibili.com/video/BV1TZ4y147ZP)

<font face="Noto Serif SC">5️⃣&emsp;近期的一些图片。</font>

<img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/3c6c8298-8967-11ea-a02d-fa163e1f3304.png height="500"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/2020-5-01-ONE%E5%B7%A5%E4%BD%9C%E8%AF%81.jpg height="500"/>


## <font face="Times New Roman" color=#0044BB >20.4.14~4.19</font>
> <font face="Noto Serif SC">至此，一周的「ONE」的线上实习也接近了尾声。<br><br>这次活动，很明显是一个双赢的活动。有几个点想表达一下：<br>1️⃣ 作为一个「ONE」8年的老用户，还是挺激动能有这样的机会的。那是在高中语文课上，“遥远”的语文老师推荐给我们的，至那以后它就陪伴在我周围。<br><br>2️⃣ 这次活动所有人也经历了一开始的满腔热情，到后来在日常生活中，没有声息的交流后面渐渐失去热情的过程。当然这是所有小组活动的通病，更别提一群互不相识的陌生人之间的合作了。<br><br>3️⃣ 虽然我对新媒体的热情并不是那么高涨，我内心只不过希望我的文字能得到少部分人的共鸣反应就足够了。「ONE」的有些内容于我有强烈的共鸣，自然我也想通过它来理解如何获得产生网络时代持续不断共鸣文字的能力。<br><br>4️⃣ 最后一个任务我们没有完成的很好，因为最后坚持下来的人越来越少，大家你一言我一语，甚至出现有人觉得自己被冷落了，拒绝交流，开小窗交流，然后让组长转达的骚操作。不过至少跟以往学校的小组活动一样，我完成了大部分工作，以往是这样，以后亦是如此。<br><br>最后感谢那些与我一同坚持到最后的队友，感谢「ONE」！有缘，江湖见！ </font>

<img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E3%80%8CONE%E3%80%8DDay3.png height="500"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E3%80%8CONE%E3%80%8DDay4.png height="500"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E3%80%8CONE%E3%80%8DEND.png height="500"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E3%80%8CONE%E3%80%8DEND_GROWN.png height="500"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E4%B8%AD%E6%96%87ONE%E8%AF%81%E4%B9%A6.png height="400"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E8%8B%B1%E6%96%87ONE%E8%AF%81%E4%B9%A6.jpg height="400"/>



## <font face="Times New Roman" color=#0044BB >20.4.2~4.13</font>
> <font face="Noto Serif SC">时光匆匆，又过了许多个日夜。感觉也没干啥，除了搞了个有颜色的项目外，刚参加了「one」线上实习已经开始了，希望这一周能有所收获吧。</font>

<font face="Noto Serif SC">1️⃣&emsp;[AutoS&D](https://github.com/ExcaliburEX/GHS)</font>

<font face="Noto Serif SC">2️⃣&emsp;[「one」](http://wufazhuce.com/article/4270)的实习活动，第一个任务是活动策划分析报告。我选取了一个心理测试和一个Datawhale的线上组队学习项目，写在了简书上[「one」线上实习任务一 活动策划分析报告](https://www.jianshu.com/p/4c3228e19c01)</font>


<img src=https://uploader.shimo.im/f/dRcaukhaynfGwAqS.PNG!thumbnail height="500"/>
<br><br>

<font face="Noto Serif SC">3️⃣&emsp;天池比赛也结束了，得了一些虚名。</font>

<img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/award1.jpg width="250"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/award2.jpg width="250"/><img src=https://blog-1259799643.cos.ap-shanghai.myqcloud.com/award3.jpg width="250"/>

## <font face="Times New Roman" color=#0044BB >20.3.30~4.1</font>
<font face="Noto Serif SC">1️⃣&emsp;天池比赛的第二个任务搞定，写完文章[天池_二手车价格预测_Task3_特征工程](https://editor.csdn.net/md/?articleId=105170015)<br>关于本任务总结的脑图：</font>

![特征工程](https://img-blog.csdnimg.cn/20200402004507865.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0V4Y2FsaWJ1clVsaW1pdGVk,size_16,color_FFFFFF,t_70#pic_center)

<font face="Noto Serif SC">2️⃣&emsp;3天工作总结
- [x] 天池比赛 ❎3️⃣
- [x] [Daily-Plan-In-Graduate-Life](https://github.com/ExcaliburEX/Daily-Plan-In-Graduate-Life#2033041)项目的更新 ❎3️⃣
</font>

<font face="Noto Serif SC">3️⃣&emsp;明日计划</font>

<img src = "https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E5%BE%AE%E4%BF%A1%E6%88%AA%E5%9B%BE_20200402013850.png" height = "450"/>

## <font face="Times New Roman" color=#0044BB >20.3.22~3.29</font>
> <font face="Noto Serif SC">终于有机会更新了，这后面的5天里，我只做了一件事，就是改造[个人博客网站](https://kemo.xyz)。改到天昏地暗，改到海枯石烂，改到脾气逐渐暴躁，发髻逐渐凌乱，面目逐渐可憎，键盘逐渐散架(砸的)。</font>

<font face="Noto Serif SC">1️⃣&emsp;最近重新修缮鼓捣个人博客，首先大刀阔斧地改造背景以及动态效果，移除那些没有用的js动画，当代世界的快节奏，人们已经不再喜欢复杂，充斥颗粒的东西了，内容至上，简约独特，这是永远的核心。其次加入友链，虽然朋友们没有什么博客，但他们有qq空间和B站啊。最重要的是加入具有大师锋范的相册，qq空间的相册太难看，微信又没有相册，B站又不适合，简书，csdn，github都是技术，也不适合，还是这里最安全最炫酷。学习了不少css的知识，最重要的是自己给自己增加了更新的动力与压力吧。——发自于3.25号的打卡</font>

<font face="Noto Serif SC">2️⃣&emsp;8天工作总结
- [x] 博客修缮完毕
  - 改变了样式，渐变色，动画，背景，评论等外观
  - 加入了[相册](https://kemo.xyz/photos/)，[运动记录](https://kemo.xyz/sports/)，[豆瓣读书](http://kemo.xyz/books/)，[豆瓣电影](http://kemo.xyz/movies/)，[友链](http://kemo.xyz/movies/)等页面
  - 以及各种不知缘由的BUG，以及总结了其中最复杂的一个BUG，发了一篇关于`css`本地预览与部署不同的文章：[柯摩のblog](http://kemo.xyz/%E5%AE%8C%E7%BE%8E%E8%A7%A3%E5%86%B3%EF%BC%9AHexo-Next%E4%B8%BB%E9%A2%98%E6%9C%AC%E5%9C%B0%E5%8F%AF%E9%A2%84%E8%A7%88CSS%EF%BC%8C%E4%BD%86%E9%83%A8%E7%BD%B2%E5%88%B0%E7%BD%91%E7%AB%99CSS%E5%A4%B1%E6%95%88%E9%97%AE%E9%A2%98.html),[CSDN](https://blog.csdn.net/ExcaliburUlimited/article/details/105161761)

- [x] 天池比赛的特征工程做了一半，勉强打卡，还得继续磕 ❎2️⃣
- [x] [Daily-Plan-In-Graduate-Life](https://github.com/ExcaliburEX/Daily-Plan-In-Graduate-Life#2032129)项目的更新 ❎2️⃣




## <font face="Times New Roman" color=#0044BB >20.3.21</font>

<font face="Noto Serif SC">1️⃣  花了一天时间完成了比赛项目的数据分析工作，写了blog分别在[kemo](https://kemo.xyz/%E5%A4%A9%E6%B1%A0_%E4%BA%8C%E6%89%8B%E8%BD%A6%E4%BB%B7%E6%A0%BC%E9%A2%84%E6%B5%8B_Task1-2_%E8%B5%9B%E9%A2%98%E7%90%86%E8%A7%A3%E4%B8%8E%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90.html)以及[csdn](https://blog.csdn.net/ExcaliburUlimited/article/details/105021630)。

2️⃣  工作总结
- [x] [Daily-Plan-In-Graduate-Life](https://github.com/ExcaliburEX/Daily-Plan-In-Graduate-Life#20320)项目的更新 ❎1️⃣
- [x] 天池比赛的研究，数据分析 ❎1️⃣
</font>  



## <font face="Times New Roman" color=#0044BB >20.3.19~20</font>
> 这两天没顾得上学`go`，总觉得有些事没思考清楚。

<font face="Noto Serif SC">1️⃣  忧心论文，所以看了知网研学的[哈工大专场-论文阅读写作与学术规范](https://www.bilibili.com/video/av96719855?t=53)，要算收获的话是以前没注意到的知网的分析分类功能，主要问题还是怎样找自己的研究方向吧。

2️⃣  有点想拍点vlog记录生活，为每一天赋予意义。所以看了一下[小苏的vlog相机](https://www.bilibili.com/video/av97724226)
  - 大疆Osmo pocket
  - G7XMark2
  - GoPro7
  - Mac ✈️
<br>嗯，买不起，刚不动。

3️⃣  关于文献管理工具，目前想用NoteExpress，知网研学以及Mendeley的组合。

4️⃣  参与了datawhale与天池举办的一个天池[新手入门赛](https://github.com/datawhalechina/team-learning)，组了个小队，希望这半个月能在这个完整的流程中有所收获。



## <font face="Times New Roman" color=#0044BB >20.3.18</font>
<font face="Noto Serif SC">1️⃣  继续[`go`](https://github.com/ExcaliburEX/Go-Learning#-20317)的学习<br>
今日学习的思维导图：

![图](https://blog-1259799643.cos.ap-shanghai.myqcloud.com/Go_2020.3.18.png)

具体内容如下：
- 容器
  - 数组
  - 多维数组
  - 切片
  - map
  - 列表list
  - nil

**具体内容移步到实时更新的**[Go-Learning-20200318](https://github.com/ExcaliburEX/Go-Learning#-20318)
</font>  

## <font face="Times New Roman" color=#0044BB >20.3.17</font>
<font face="Noto Serif SC">1️⃣  开始了[`go`](https://github.com/ExcaliburEX/Go-Learning#-20317)的学习<br>今日学习的思维导图：

![图](https://blog-1259799643.cos.ap-shanghai.myqcloud.com/Go.png)
<br>
具体如下：
- 基本语法 
  - 变量声明
  - 变量的初始化
  - 多变量同时赋值
  - 匿名变量：下划线“_”
  - 变量作用域(没什么好讲的，跟`python`类似)
  - 浮点类型
  - 字符串（一个不可改变的字节序列）
  - 指针
  - 常量（`const`）
  - `type`关键字（类型别名）
  - 关键字
  - 运算优先级

**具体内容移步到实时更新的**[Go-Learning-20200317](https://github.com/ExcaliburEX/Go-Learning#-20317)
</font>

## <font face="Times New Roman" color=#0044BB >20.3.13~3.16</font>
<font face="Noto Serif SC">1️⃣  把毕设以及代码以及毕设期间代写毕设的代码上传到[Graduation-Design-and-MATLAB-Code](https://github.com/ExcaliburEX/Graduation-Design-and-MATLAB-Code-)
</font>


## <font face="Times New Roman" color=#0044BB >20.3.9~3.12</font>
<font face="Noto Serif SC">1️⃣  !!!∑(ﾟДﾟノ)ノ参与了一个Github上近一周Trending排名第一的项目(**[fucking-algorithm](https://github.com/labuladong/fucking-algorithm)**)的翻译工作。

该项目主要是将Leetcode上的算法进行结构化，框架化的解读，项目作者将自己一年刷题的经验与心得整合为一份gitbook并持续更新，用动图，编码，通俗的语言对各种经典的动态规划，数据结构，算法思维，并引经据典，旁征博引《算法4》等经典算法著作。

我参与了项目的KMP算法的翻译工作，KMP算法是字符串匹配算法的高效算法，由三位计算机科学界的大佬提出，所以全名为Knuth-Morris-Pratt 算法，它与传统的暴力匹配不同的是，它利用记忆数组存储匹配记忆，以达到快速匹配的目的。目前我已经将我的翻译工作commit，并对该项目进行了pull request并且已经merged，成为了一名Contributor。😊 

2️⃣  写了一下午的HPC作业，在这里[HPC_Homework](https://github.com/ExcaliburEX/KeMo/blob/master/HPC_Homework.py)。

- 主要涉及了文件数据的处理工作。在进行高性能分布式计算时，一个最基本的工作就是将数据集成化，有序化，准确地输入到工作流中。
- 在分割文件时会出现很多种情况：如相应的文件不存在，相应的sheet不存在或者无法打开；相应的id出现了重复情况，无法判断何者为原始数据；在sheetn(n>=2)中出现的id不是id的子集；抑或是其余等等情况。所以在处理数据时需要提前考虑到大部分的失败情况，对每一种情况都做相应的措施然后继续推进任务。
</font>

<img src = "https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200312203415.jpg" height = "350"/>




## <font face="Times New Roman" color=#0044BB >20.3.4~3.8</font>
<font face="Noto Serif SC">1️⃣  搭建了go的环境包括[`VScode` 以及 `Goland`]，😫 完成了基本语法的学习，亦即：
- **「数据类型」**
- **「循环选择结构」**
- **「函数」**
- **「等」**

2️⃣  get😆到了一个科研神器`Grammarly`以及`Linggle`。<br>
3️⃣  `Aixcoder` 北大出品，必属精品。😈利用DL技术，以历史编码模式为输入，进行智能补全提示。<br>
4️⃣  比较了好几款文献管理工具， 包括 `NoteExpress`(适合中文)，以及`Mendeley`, `Zotero`。三款软件常用的功能都具备，如文献标签整理，快速导入参考文献，自带阅读器，浏览器插件等等，都可用于日常阅读工作。😎<br>
5️⃣  通过落拓的系列视频[是落拓啊-区块链](https://www.bilibili.com/video/av88477333)，复习了`POW`工作量证明机制，哈希碰撞，并且快速实现了一个小型的区块系统。<br>
6️⃣ 「等」,暂时想不来了，哪天想起来再更。🙋‍♂️</font>

<img src = "https://blog-1259799643.cos.ap-shanghai.myqcloud.com/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20200312203426.jpg" height = "350"/>







