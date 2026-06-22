# SA 内容选题规划（serper API 验证版）

> 验证工具: serper API (Google 全球搜索)
> 红线: SVG ✓ 表格 ✓ 图标 ✓ 内链 ✓
> 禁止: 3词以下泛词、未经验证的选题、国内搜索引擎

---

## 一、现状评估

| 现有文章 | 字数 | 表格 | SVG图 | 材料图标 | 内链 | 状态 |
|----------|------|------|-------|----------|------|------|
| vulcanus-guide | 85w | 0 | 0 | 0 | 0 | 极薄，需重写 |
| fulgora-recycling-guide | 131w | 0 | 0 | 0 | 0 | 极薄，需重写 |
| gleba-survival-guide | 146w | 0 | 0 | 0 | 0 | 极薄，需重写 |
| aquilo-guide | 141w | 0 | 0 | 0 | 0 | 极薄，需重写 |
| planet-order-guide | 108w | 0 | 0 | 0 | 0 | 可保留骨架 |
| quality-module-guide | 41w | 0 | 0 | 0 | 0 | 极薄，需重写 |
| space-platform-guide | 110w | 0 | 0 | 0 | 0 | 极薄，需重写 |

**结论：7 篇全部未过 QA 红线，需要深度重写 + 补新。**

---

## 二、选题矩阵

### Phase 1（首批 8 篇，最高搜索量 + 最急需）

| # | 选题（长尾关键词） | 行星 | serper 验证证据 | SVG图 | 表格 | 图标 | 内链 | 优先级 |
|---|-------------------|------|-----------------|-------|------|------|------|--------|
| 1 | **Fulgora Scrap Overflow — How to Void Excess Items and Keep Production Running** | Fulgora | 红迪热帖 "How do you deal with overflowing items" + Steam讨论 | 溢料处理流程图：分拣→缓冲→销毁 | 各物品消耗/产出配比 | Recycler, belt, chest, inserter | vulcanus-guide (浇铸对比) | ⭐⭐⭐ |
| 2 | **Gleba Bioflux Production — Fruit Ratio, Nutrients Loop, and Spoilage Control** | Gleba | 搜索密集，红迪 "A Guide to Gleba" 高赞，论坛普遍困惑 | 果→果酱→生物质→生物通量流程图 | 果/果酱/生物通量产出配比 | Fruit, bioflux, nutrient, spoilage | gleba-survival-guide | ⭐⭐⭐ |
| 3 | **Vulcanus Lava Processing — Molten Iron and Copper Without Miners** | Vulcanus | 论坛帖 "Molten iron/copper on Nauvis"、"lava processing" | 熔岩→铁液/铜液→铸件流程 | 各铸件配比、模块数量 | Foundry, lava pump, pipe, calcite | vulcanus-guide | ⭐⭐⭐ |
| 4 | **Aquilo Heating Grid Design — Heat Pipe Distance and Power Generation Guide** | Aquilo | 论坛帖 "Heat Pipe Math for Aquilo" 搜索量高，玩家集体困惑 | 加热管布局方案（直线/分支/多热源） | 热量衰减表、不同管线配置油/热交换器比 | Heat pipe, heat exchanger, heating tower | aquilo-guide | ⭐⭐⭐ |
| 5 | **Quality Module Upcycling Loop — From Uncommon to Legendary Without Waste** | Quality | serper结果4/5直接相关，"legendary upcycling"、"comprehensive quality guide"热点 | 质量循环：回收→加工→再筛选流程图 | 各质量等级概率、投入产出比 | Quality module, recycler, assembler | quality-module-guide, fulgora-recycling-guide | ⭐⭐⭐ |
| 6 | **Space Platform Ship Design for All Planets — Asteroid Defense and Fuel Ratios** | Platform | serper "ship design for all planets" 搜索密集，YouTube+红迪讨论活跃 | 飞船布局模板（通道/防御区/加工区） | 各星球航线防御需求对照表、燃料配比 | Thruster, asteroid collector, turret, crusher | space-platform-guide | ⭐⭐⭐ |
| 7 | **Gleba Pentapod Defense — Turret Placement and Spore Management Strategy** | Gleba | "Gleba defense"、"pentapod"反复出现，玩家卡关热点 | 孢子扩散→虫巢生成→进攻波次示意图 | 各防御方案成本与效率对比 | Gun turret, rocket turret, landmine, spore | gleba-survival-guide, gleba bioflux article | ⭐⭐ |
| 8 | **Cross-Planet Logistics — What to Ship Between Planets and Cargo Rocket Automation** | Cross | serper "what to ship" + "interplanetary logistics" 高热度、红迪抱怨 QoL | 各行星货运清单示意图 | 各行星可出口/需进口物品表 | Cargo rocket, rocket silo, space platform | 全部行星文章 | ⭐⭐ |

### Phase 2（第二轮 7 篇，深度补充）

| # | 选题 | 行星 | 选定理由 | 必备组件 | 优先级 |
|---|------|------|----------|----------|--------|
| 9 | **Fulgora Holmium Processing — From Scrap to EM Science and Electromagnetic Plants** | Fulgora | EM science 是终局需求，现有文章无覆盖 | 钬液产线图、电力消耗/产出表 | ⭐⭐ |
| 10 | **Vulcanus Demolisher Worm Killing Guide — Turret Strategies and Weakness Analysis** | Vulcanus | "demolisher killing"是红迪高频提问 | 大小虫血条对比图、各武器伤害表 | ⭐⭐ |
| 11 | **Aquilo Cryogenic Factory — Ice Platform Starting and Fluid Handling at -100°C** | Aquilo | "cryogenic factory"专用需求，现有文章仅涉及登陆 | 冰平台→冰→水→氧流程图、冰冻管线处理方案 | ⭐⭐ |
| 12 | **Quality Armor and Equipment — Legendary Personal Equipment Priority Order** | Quality | 传奇品质做哪些装备最划算，玩家决策痛点 | 各装备传奇vs普通数值对比表 | ⭐⭐ |
| 13 | **Space Platform Asteroid Reprocessing — Crusher Recipes and Resource Self-Sufficiency** | Platform | serper 第三位 "Asteroid Reprocessing"，中级进阶 | 小行星种类→碎片→处理流程图 | ⭐⭐ |
| 14 | **Gleba Agricultural Science Pack — Full Automation Blueprint Walkthrough** | Gleba | 农业科学的配套是终局强迫需求，当前无文章覆盖 | 农科全自动产线图 | ⭐⭐ |
| 15 | **Vulcanus to Nauvis Supply Chain — Calcite Shipping and Foundry Integration** | Vulcanus/Cross | 论坛帖 "calcite demand"高热度，跨行星物流高频卡点 | 钙运回Nauvis后产线改造对比图 | ⭐⭐ |

### Phase 3（第三轮 8 篇，锦上添花）

| # | 选题 | 行星 | 选定理由 | 必备组件 | 优先级 |
|---|------|------|----------|----------|--------|
| 16 | **Fulgora Lightning Protection — Rod Placement and Substation Grid Design** | Fulgora | "lightning" 防御是特有机制，老文章无覆盖 | 防雷网格布局、覆盖范围表 | ⭐ |
| 17 | **Gleba Spoil Loop — Bacteria Cultivation and Nutrient Recycling at Scale** | Gleba | 细菌培养+孢子循环是Gleba独特机制 | 细菌培养工艺流程图 | ⭐ |
| 18 | **Quality in Production — Assembler Quality vs Module Quality Tradeoff Analysis** | Quality | "quality in modules" 搜索结果密集，高意向 | 不同策略产出对比表 | ⭐ |
| 19 | **Aquilo Fusion Power — Building the First Fusion Reactor in Space Age** | Aquilo | 融合是最终能源，玩家问"fusion reactor setup" | 融合发电厂布局图 | ⭐ |
| 20 | **Space Platform Thruster Fuel Optimization — Asteroid Chunk to Fuel Ratio** | Platform | "thruster fuel consumption" 有专门论坛帖，技术细节 | 推动器燃料配比计算图 | ⭐ |
| 21 | **Advanced Interplanetary Logistics — Circuit-Controlled Rocket Requests** | Cross | 红迪帖 "space logistics QoL is horrible" 证明有高级需求 | 电路控制火箭示例图 | ⭐ |
| 22 | **Promethium Science Pack — Endgame Infinite Research Setup** | Cross | SA最终科学包，理论上需要 | 终局科学产线全图 | ⭐ |
| 23 | **Planet Order Revisited — Updated Route After 100 Hours of Space Age** | Strategy | 现有planet-order太薄，更新版带实战验证 | 各路线通关时间线对比 | ⭐ |

---

## 三、数量汇总

| 区域 | 现有 | 新增 Phase 1 | 新增 Phase 2 | 新增 Phase 3 | 总数 |
|------|------|-------------|-------------|-------------|------|
| Vulcanus | 1 | 1 | 2 | 0 | 4 |
| Fulgora | 1 | 1 | 1 | 1 | 4 |
| Gleba | 1 | 2 | 1 | 1 | 5 |
| Aquilo | 1 | 1 | 1 | 1 | 4 |
| Quality | 1 | 1 | 1 | 1 | 4 |
| Space Platform | 1 | 1 | 1 | 1 | 4 |
| Cross-planet/Strategy | 1 | 1 | 1 | 2 | 5 |
| **合计** | **7** | **8** | **7** | **8** | **~30** |

---

## 四、各文章 SOP 红线检查模板

每篇文章发布前必须通过以下检查：

```
□ SVG图 ＞1 张（流程图/方案图/布局图）
□ 数据表格 ≥2 个（配比/对比/步骤）
□ 材料图标 ≥2 处（真实游戏 icon via {{< material >}}）
□ 内链 ≥2 条（指向已有 SA 或 vanilla 文章）
□ 无 emoji / 弯引号 / em-dash（首页卡片除外）
□ 无 UTF-8 BOM
□ QA 通过（9 道关卡，warnings ≤ 3）
□ Hugo build 0 错误
```

---

## 五、现有 7 篇文章重写优先级

考虑到 7 篇现有 SA 文章全部是 Thin Content（41-146w），建议按以下顺序重写：

| 文章 | 当前质量 | 重写策略 | 时机 |
|------|---------|----------|------|
| quality-module-guide | 最差（41w，0短代码） | 完全重写 → 与#5 quality upcycling合并 | Phase 1 |
| vulcanus-guide | 极薄，有含金量 | 保留骨架 → 与#3 lava processing合并或重写 | Phase 1 |
| space-platform-guide | 极薄 | 与#6 ship design合并，重写 | Phase 1 |
| gleba-survival-guide | 极薄 | 作为#2 bioflux的前置阅读，对原有内容重写 | Phase 1 |
| fulgora-recycling-guide | 极薄 | 与#1 overflow合并，重写 | Phase 1 |
| aquilo-guide | 极薄 | 与#4 heating grid合并，重写 | Phase 2 |
| planet-order-guide | 中等 | 保留，等#23更新版再替换 | Phase 3 |

---

## 六、依赖关系（必须先写谁）

```
Phase 1-A（并行，互不依赖）：
  ┌─ Fulgora Scrap Overflow
  ├─ Gleba Bioflux + 重写 gleba-survival
  ├─ Vulcanus Lava Processing + 重写 vulcanus-guide
  └─ Quality Upcycling Loop + 重写 quality-module-guide

Phase 1-B（依赖 A 完成后）：
  ├─ Space Platform Ship Design + 重写 space-platform-guide
  ├─ Cross-Planet Logistics（依赖所有行星文章完成）
  └─ Gleba Pentapod Defense（依赖 Bioflux 完成）

Phase 2（依赖 Phase 1 完成）：
  └─ Fulgora Holmium → Aquilo Cryogenic → Defense → etc.

Phase 3（所有依赖就绪后）：
  └─ 锦上添花篇
```

---

## 七、serper API 额外验证字段

发布前对每个选题再做一次 serper 搜索验证：

```powershell
# 验证模板
$body = @{ q = "Factorio Space Age <长尾关键词>" gl = "us" hl = "en" num = 5 } | ConvertTo-Json
Invoke-RestMethod -Uri "https://google.serper.dev/search" -Method Post -Body $body -ContentType "application/json" `
  -Headers @{ "X-API-KEY" = "78903b2ef656a0e0c51c9d037249223d9a8d3df1" }
```

验证目标：
- 确保选题有足够搜索意图（有 Reddit/论坛/YouTube 讨论）
- 确保我们提供的内容比搜索结果前 5 名更好
- 确认没有大站垄断（如果前 5 全是官方 Wiki + 知名 YouTuber → 需要差异化角度）
