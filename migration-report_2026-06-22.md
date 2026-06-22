# SA 目录迁移 & 文章恢复 — 最终报告

## 目录结构（7 个子板块，14 篇文章）

```
content/space-age/
├── _index.md        Space Age Expansion Guide
├── guide/           星球顺序 + 第一站攻略 (2篇)
│   ├── _index.md
│   ├── planet-order-guide.md
│   └── vulcanus-guide.md
├── vulcanus/        熔岩处理 (1篇)  ← 新增
│   ├── _index.md
│   └── lava-processing.md (aliases: /space-age/vulcanus-lava-processing/)
├── fulgora/         废料回收 + 溢出管理 (2篇)
│   ├── _index.md
│   ├── fulgora-recycling-guide.md
│   └── scrap-overflow.md (aliases: /space-age/fulgora-scrap-overflow/)
├── gleba/           腐烂生存 + 生物通量 + 虫族防御 (3篇)
│   ├── _index.md
│   ├── gleba-survival-guide.md
│   ├── bioflux-production.md (aliases: /space-age/gleba-bioflux-production/)
│   └── pentapod-defense.md (aliases: /space-age/gleba-pentapod-defense/)
├── aquilo/          冰冻生存 (1篇)
│   ├── _index.md
│   └── aquilo-guide.md
├── platform/        飞船设计 + 跨行星物流 (3篇)
│   ├── _index.md
│   ├── space-platform-guide.md
│   ├── ship-design.md (aliases: /space-age/space-platform-ship-design/)
│   └── cross-planet-logistics.md (aliases: /space-age/cross-planet-logistics/)
└── quality/         品质模块 + 上循环 (2篇)
    ├── _index.md
    ├── quality-module-guide.md
    └── upcycling-loop.md (aliases: /space-age/quality-module-upcycling/)
```

## SVG 图解（7 个）

全部位于 `static/images/diagrams/space-age/`：
- `lava-processing-flow.svg` — 熔岩→铁液/铜液→铸造流程图
- `scrap-overflow-sorter.svg` — 优先级分拣器设计
- `bioflux-chain.svg` — 水果→生物通量生产链
- `pentapod-defense-layout.svg` — 孢子管理 + 三层防御布局
- `ship-layout-templates.svg` — 3种飞船布局（脊骨/宽体/紧凑）
- `planet-logistics-matrix.svg` — 5行星物流矩阵
- `quality-upcycling-loop.svg` — 品质上循环回路

## 构建验证

- Hugo build: 132 pages, 14 aliases, 0 errors
- 首页、子板块页、文章页：全部 200
- 所有旧 URL 通过 alias 重定向到新路径
