# 温度补偿 / Temperature Compensation

温度补偿（temperature compensation）指**通过校准算法、结构设计或参考测量，消除/修正传感器或测量系统输出中随温度变化的干扰分量，从而保证被测物理量（如湿度、应变、光强）准确性的技术手段**。光纤湿度传感器等测量设备普遍面临温度-湿度交叉敏感问题，温度补偿是其走向可靠工程应用的关键环节。

## 👵 太奶导读

很多传感器"一根筋"：它测的是湿度，可温度一变，读数也跟着漂——你以为湿度变了，其实是天热了。这不是传感器坏了，而是它"天生敏感"。温度补偿就是给传感器装"纠错机制"：要么查表把温度影响扣掉，要么选材料让它对温度"免疫"，要么直接改测更稳的量。这一扣一免之间，数据才真正可信。

## 🧩 温度补偿与光学测量原理

- **热透镜法本质测绝对湿度**：基于热透镜探测技术的光纤湿度传感器（球透镜光纤微腔）输出信号与相对湿度成线性关系；温度控制实验揭示该传感器本质上测量的是绝对湿度（水汽密度），因此要获得精确的相对湿度，必须对检测信号进行温度补偿（[[../papers/Yarai2005optical|Yarai 2005]]）。

## 🧩 温度补偿与校准方法

- **查找表校准法**：基于双层包层单模光纤、涂覆琼脂糖凝胶的湿度传感器具低插入损耗与高灵敏度，但其响应受温度和湿度耦合影响、呈非线性特征；提出的查找表校准法有效解决此问题，成功监测了混凝土硬化过程中湿度从 100% 降至 68.9%、温度先升后降的动态过程（[[../papers/XiaokangZhang2013calibrating|Zhang 2013]]）。
- **温度不敏感设计**：在本征法布里-珀罗干涉仪（IFPI）端面自组装 PAH/PSS 纳米薄膜的光纤相对湿度传感器中，实现了 0.08 dB/%RH 的高灵敏度与 5–90% RH 的良好稳定性与可逆性，响应时间 2/6 秒，且在 20–100 °C 温度范围内表现出优异的**温度不敏感性**——即通过结构/材料设计从源头消除温度补偿需求（[[../papers/Unknown2014optical|Optical Fiber Sensor 2014]]）。

## 📚 相关论文 (Related Papers)

- [[../papers/Unknown2014optical]] — Optical Fiber Relative Humidity Sensor Based on Fabry-Perot Interferometer
- [[../papers/XiaokangZhang2013calibrating]] — Calibrating an optical fiber humidity sensor and applying it in real-time monitoring of relative humidity in fresh concrete
- [[../papers/Yarai2005optical]] — Optical fiber sensor for humidity monitoring based on thermal lens detection technique

## 🔗 关联概念与实体 (Related Concepts & Entities)

- [[../concepts/solvent-relaxation|溶剂弛豫]]：湿度传感涉及的表面水分子吸附/弛豫机制。
- [[../concepts/charge-transfer|电荷转移]]：传感层对水分子的响应机制之一。
- [[../concepts/strain-relaxation|应变弛豫]]：同类"补偿-弛豫"思路的对照。
*（内容由AI生成，仅供参考）*
