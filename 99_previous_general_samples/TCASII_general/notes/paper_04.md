# paper_04 - Self-Adaptive Intermediate Resonator in a 3-Coil Inductive Link

## 一句话定位
这篇提出可自适应中间谐振器，在三线圈感应链路中兼顾高效功率传输和数据通信。

## 摘要写法
摘要先说明同一 inductive link 同时传功率和数据的矛盾：功率传输要高 Q，数据通信又需要响应可调整。本文提出两个策略：降低 Q 或 detune resonator，并用原型验证。

## Introduction 写法
引言从短距离无线能量传输、植入设备和 RFID 应用说起，随后指出 intermediate resonator 提高功率效率但会妨碍半双工数据传输。gap 非常具体。

## 方法/架构写法
方法围绕工作相位切换：充电阶段 tuned high-Q，通信阶段自适应改变响应。写法像一个电路操作时序说明，而不是长篇理论。

## 实验/测量写法
实验展示 power transfer efficiency、通信可读性以及两种响应调整方式。它的重点是动态切换是否真的在同一硬件上成立。

## 图表套路
图表包括链路结构、半双工时序、谐振响应和测量波形。Brief 中图要把“何时高 Q、何时低 Q/失谐”讲明白。

## 可模仿写法
如果你的电路解决的是“两个工作模式冲突”，可以模仿它把模式切换机制作为论文中心。
