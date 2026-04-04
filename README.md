# Python 实践仓库  

> **欧阳思琦** · 湘潭大学网络安全 · 大一（17岁）  
> **学习时间**：每天 1.5 小时 · **方法**：AI 出题 + LeetCode 刷题 + 项目驱动  
> **目标**： - **短期（大一下 - 大二上）**：掌握 Python、NumPy、PyTorch 基础，具备独立完成小型科研任务（数据清洗、模型复现、可视化）的能力，**争取大二进入本校 AI / 数据科学实验室**。   **长期**：在实验室中积累真实项目经验，提升算法和工程能力，为未来深造或科研打下扎实基础。
---

## 我为什么这样学？

- 不盲目看网课，用 **AI（ChatGPT/DeepSeek）出题 → 我手写 → AI 批改 → 反思** 的闭环快速掌握语法
- 所有练习围绕 **算法比赛（Codeforces/LeetCode）** 和 **AI 科研（PyTorch）** 的真实需求，不学无用知识
- 每天提交代码到 GitHub，用连续的绿色格子证明 **坚持与自律**

---

##  学习进度（实时更新）

| 模块 | 状态 | 证明 |
|------|------|------|
| 变量、输入输出、条件、循环 | ✅ | [基础练习](./day1-3/) |
| 列表、元组、字典、集合 | ✅ | [AI 练习题 + 批改](./AI_Tutor_Exercises/day01_lists/) |
| 函数、lambda、作用域 | ✅ | [AI 练习题](./AI_Tutor_Exercises/day05_functions/) |
| 常用内置函数（map/filter/zip） | ✅ | [练习+笔记](./notes/builtins.md) |
| collections & itertools | 🔄 | [进行中](./AI_Tutor_Exercises/day08_collections/) |
| NumPy 基础（数组、广播、矩阵） | 🔄 | [KNN 实现](./projects/knn_numpy/) |
| 学生管理系统（命令行+JSON） | 🔄 | [项目代码](./projects/student_management/) |
| LeetCode 刷题 | 🔥 已解 40 题 | [记录](./LeetCode_Progress/) |
| Codeforces 适应 | 🔄 | [虚拟赛日志](./Codeforces_log.md) |

> ✅ 已完成 &nbsp;&nbsp; 🔄 进行中 &nbsp;&nbsp; 🔥 持续增长

---

## 一、基础语法练习（已用 AI 辅助重构）

每一题流程：**AI 出题 → 我独立写代码 → AI 批改 → 记录反思**

| 主题 | 练习内容 | 代码 | AI 批改与反思 |
|------|----------|------|----------------|
| 变量、输入输出 | 个人信息打印、圆面积计算 | [代码](basic_syntax/day1_variables.py) | [反馈](./feedback/day1.md) |
| 条件判断 | 闰年判断、成绩等级 | [代码](basic_syntax/day2_if.py) | [反馈](./feedback/day2.md) |
| 循环 | 阶乘、九九乘法表 | [代码](./day3_loop.py) | [反馈](./feedback/day3.md) |
| 列表与元组 | 列表去重、排序、切片 | [代码](./day4_list.py) | [反馈](./feedback/day4.md) |
| 函数 | 素数判断、斐波那契数列 | [代码](./day5_function.py) | [反馈](./feedback/day5.md) |
| 文件操作 | 统计单词数、读写文件 | [代码](./day6_file.py) | [反馈](./feedback/day6.md) |

> 我原来的“学生成绩管理系统”已升级为带 JSON 持久化的命令行版本，见下方项目区。

---

## 二、算法与数据结构（LeetCode 为主）

每道题记录：思路、卡点、复杂度、多种解法。  
**已完成**（部分示例）：
- 数组：两数之和、最大子数组和、移动零  
- 哈希表：有效的字母异位词、快乐数  
- 双指针：反转字符串、三数之和（中等）  
- 栈：有效的括号、最小栈  

👉 [完整刷题记录](./LeetCode_Progress/)  
👉 [解题笔记模板](./algorithm/notes_template.md)

**计划中**：链表反转、二叉树遍历、贪心与动态规划基础。

---

## 三、项目实战（可运行 + 有截图）

| 项目 | 描述 | 技术栈 | 亮点 | 代码 |
|------|------|--------|------|------|
| 学生管理系统 | 增删改查 + JSON 存储 + 模糊搜索 | Python 标准库 | 异常处理、单元测试 | [查看](./projects/student_management/) |
| NumPy KNN（进行中） | 从零实现 K 近邻分类器 | NumPy | 向量化计算、广播机制 | [查看](./projects/knn_numpy/) |

> 每个项目都配有 README（运行方法、设计思路、测试用例）和运行截图。

---

## 四、学习笔记与沉淀

- [Python 常见坑点（可变默认参数、浅拷贝等）](./notes/common_pitfalls.md)
- [NumPy 速查表](./notes/numpy_cheatsheet.md)
- [如何用 AI 出题 + 批改（我的工作流）](./notes/AI_tutor_workflow.md)

---

##  给未来导师的话

我是一名大一学生，正在系统学习 Python 和算法。  
如果您有任何适合本科生的科研小任务（如数据清洗、复现 baseline、跑通开源项目），我非常愿意争取。

**联系方式**：202505180522@xtu.edu.cn  
**GitHub 主页**：[https://github.com/SiqiOuyang](https://github.com/SiqiOuyang)

> 感谢您花时间阅读。我会持续更新这个仓库，直到达到实验室的要求。
