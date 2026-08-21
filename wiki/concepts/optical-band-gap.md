---
tags: [concept]
title: 'optical-band-gap'
type: concept
status: developing
papers: ['songEvidenceSinglelayerVan2022', 'Blessing2026optical', 'Delley2000', 'Tobeiha2025optical']
updated: 2026-08-18
---

# optical-band-gap

光学带隙（optical band gap）指**材料在光学跃迁中允许的最小光子能量**，即吸收/发射光谱中由电子从价带到导带直接跃迁（或激子吸收）决定的能量阈值。它决定材料对光的吸收与发射特性，是光伏、光电探测、发光与光催化材料设计与筛选的核心参数，常与电子带隙（band-gap）有别（激子束缚能与间接跃迁修正）。

## 👵 太奶导读

太奶啊，光学带隙就是"材料开始能吸光的最低光子能量"。光子能量太小（光太"软"）材料"看都不看"直接放过；能量一够（光够"硬"），电子就被"踢"上去、光被吸收。测出这个"门槛能量"，就知道材料吸不吸光、发什么颜色的光、适不适合做太阳能电池。它是材料"光学身份证"上最重要的数字。

## 🧩 核心内容与机制 (Core Content)

- **定义与测量**：由 Tauc 作图、吸收边（Kubelka-Munk）等从光谱提取；E_opt = E_g(电子带隙) - E_b(激子束缚能)（本库二维材料光学带隙论文）。
- **与电子带隙的区别**：光学带隙常小于 DFT 电子带隙（激子效应、间接-直接跃迁差异）；二维材料激子束缚能大，差异显著（本库 WSe₂/MoS₂ 激子论文）。
- **应用**：光伏材料需光学带隙匹配太阳光谱（约 1.1–1.6 eV），发光材料需窄而直接带隙，光催化需兼顾能带位置（本库钙钛矿、TMD 光电论文）。
- **调控手段**：组分、尺寸（量子限域）、应变（strain-engineering）与异质结构调控光学带隙。
- **表征**：UV-Vis 吸收/漫反射光谱、光致发光（PL）、椭偏光谱（配合 refractive-index）。

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/band-gap|带隙]]：电子带隙与光学带隙的关系。
- [[../concepts/dielectric-function|介电函数]]：光学响应的微观描述。
- [[../concepts/refractive-index|折射率]]：与带隙相关的光学常数。
- [[../concepts/2d-materials|二维材料]]：强激子效应的光学带隙。
- [[../concepts/linear-response|线性响应]]：光学跃迁的理论框架。

## 📚 相关论文 (Related Papers)

- [[../papers/songEvidenceSinglelayerVan2022]] — Evidence for a single-layer van der Waals multiferroic
- [[../papers/Blessing2026optical]] — Optical investigation of tin telluride (SnTe) thin films grown at different deposition voltage
- [[../papers/Delley2000]] — From molecules to solids with the DMol3 approach
- [[../papers/Tobeiha2025optical]] — Optical humidity sensor based on G/GO nanosheets

## 🏷️ 专业名词别名

- `optical-bandgap`（concepts）
