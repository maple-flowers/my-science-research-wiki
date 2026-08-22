---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: d1440e82f85676d2b3ce24ffb8efaf05_abdac9e39a2211f19467525400287e28
    ReservedCode1: ThpTk1BX30rDKHZNRFMvG/enmvAps9p5Jrlkzl+lmG/GW7YCfazFMYoj0hRlzQ+ZUYf4q2Z5lnNNhreqzsiWVRD9H+mHWsewy3owo1ZNVMphnBV43jziMBiUZVrzj/VKznsJ0F2ZY7IBBp8aNvOFrdVJCng2ezTYWIcCx7NvANw/ae4bMd1j92A5wvM=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: d1440e82f85676d2b3ce24ffb8efaf05_abdac9e39a2211f19467525400287e28
    ReservedCode2: ThpTk1BX30rDKHZNRFMvG/enmvAps9p5Jrlkzl+lmG/GW7YCfazFMYoj0hRlzQ+ZUYf4q2Z5lnNNhreqzsiWVRD9H+mHWsewy3owo1ZNVMphnBV43jziMBiUZVrzj/VKznsJ0F2ZY7IBBp8aNvOFrdVJCng2ezTYWIcCx7NvANw/ae4bMd1j92A5wvM=
---

# Phase C 身份解析完成汇总报告

- 完成时间：2026-08-17
- 覆盖范围：concepts 层 1173 页 + entities 层 506 页 = 1679 页，全部完成身份解析
- 批次：batch1-113（concepts 层 batch1-113，entities 层 batch71-81 等）
- 全程只读分析，未修改任何页面，未 commit/push

## 身份分布（去重统计）

| 身份类型 | 数量 | 说明 |
|----------|------|------|
| canonical | 135 | 有 frontmatter 的正式页 |
| alias | 2 | concepts/1t-phase、entities/BTO |
| ambiguous | 2 | concepts/biphoton、entities/AFM |
| misplaced | 2 | concepts/bamboo-like-N-CNTs、concepts/bedt-ttf |
| no-evidence | 1 | concepts/additive-manufacturing |
| short-aggregation | 其余 | 无 frontmatter 的短反链聚合页 |

## 关键问题清单（供后续 Phase 处理）

1. **跨层碰撞**（已知 3 对，无新增）：1t-phase、bamboo-like-N-CNTs、glassy-carbon
2. **misplaced 待迁移**：bedt-ttf、bamboo-like-N-CNTs（concepts 版）、axicon 候选、band-pass-filter 候选、carbazole-derivatives 候选
3. **ambiguous 待消歧**：AFM、biphoton
4. **no-evidence 待处理**：additive-manufacturing
5. **canonical 候选**（论文多但未升级为正式页）：topochemical-reaction、topological-defects、trap-depth、trimerization、two-photon-absorption-cross-section、two-photon-polymerization、undercooling、vdW-heterostructure、vdw-correction、voxel、wannier-function、weak-ferromagnetism 等

## 别名记录（Phase C 期间新增）

- steepest-ascent → steepest-ascent-path
- surface-termination → surface-terminations
- two-photon-absorption-cross-section → two-photon-cross-section
- type-i-multiferroic → type-i-multiferroics
- variable-spring-constant → variable-spring-constants
- vdW-heterostructure → van-der-waals-heterostructure

## 后续阶段

- Phase D：高价值 short-aggregation 页扩写
- Phase E：alias/ambiguous/no-evidence 处理
- Phase F：其余 stub 扩写
- Phase G：跨层误放迁移
- Phase H：developing 复核
- Phase I：mature 复核
- Phase J：最终验收
*（内容由AI生成，仅供参考）*
