---
tags: [concept]
title: '可变弹性常数（复数）/ Variable Spring Constants'
type: concept
status: developing
papers: ['henkelmanClimbingImageNudged2000c']
updated: 2026-08-18
---

# 可变弹性常数（复数）/ Variable Spring Constants

可变弹性常数（variable spring constants）是**可变弹性常数（[[../concepts/variable-spring-constant|variable-spring-constant]]）**的复数形式，指弹性带方法（NEB）中随路径位置变化的弹簧常数设定，用于控制相邻图像间间距以稳定最小能量路径（MEP）搜索。

## 👵 太奶导读

太奶，算材料里原子"翻山越岭"的最低能量路径时，要用一根根"弹簧"把沿途的中间态串起来。可变弹性常数就是让弹簧"松紧可调"——该紧的地方紧、该松的地方松，这样找出来的路径才准。

## 📛 名称与使用范围

- **规范名**：variable-spring-constant（concepts 页）
- **别名**：variable-spring-constants（复数形式）
- **使用范围**：爬坡弹性带方法（CI-NEB）等过渡态搜索算法的实现与文献描述中，常以复数泛指各图像间的弹簧常数。

## ⚠️ 容易混淆的对象

- **固定弹性常数 NEB**：所有图像弹簧常数相同，路径分辨率控制较弱。
- **spring force（弹簧力）**：NEB 中连接相邻图像的有心力，与常数取值相关但不同概念。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/variable-spring-constant|可变弹性常数]]：本页的规范名（单数形式）。
- [[../concepts/minimum-energy-path|最小能量路径]]：可变弹簧常数所服务的 NEB 搜索目标。
- [[../concepts/nudged-elastic-band|NEB 方法]]：使用可变弹簧常数稳定路径搜索的弹性带算法。

## 📚 相关论文 (Related Papers)

- [[../papers/henkelmanClimbingImageNudged2000c]] — A climbing image nudged elastic band method for finding saddle points and minimum energy paths（CI-NEB 方法引入可变弹簧常数改进收敛）

## 🔗 规范页 (Canonical Page)

- [[../concepts/variable-spring-constant|variable-spring-constant]]：本页所指的标准条目。
