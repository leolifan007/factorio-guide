# Session Summary — 2026-05-23 ~ 2026-05-24

## 已完成的工作

### 1. SVG 字体 QA 与批量修复（上一轮延续，本轮汇总）
- 编写了 QA 脚本 `scripts/run_svg_qa.py` 和批量修复脚本 `scripts/batch_fix_svg_fonts.py`
- 修复 25 个 SVG 文件中的字体过小问题（viewBox 缩放导致渲染 < 12px）
- 策略：round → ceil 避免欠调，最终 0 个字号 FAIL
- 剩余 256 个重叠/布局 FAIL（文字增大后与相邻元素重叠），需人工调整布局
- `artillery-outpost.svg` 因 XML 损坏已重写

### 2. 全站乱码修复（本轮完成）
- **问题根因**：UTF-8 双重编码导致 em dash `—` 变成 `鈥?`，箭头 `→` 变成 `鈫?`
- **范围**：扫描 134 个文件，修复 36 个文件
- **文件**：
  - `content/` 下 5 个 .md 文件（ltn-mod-guide.md, artillery-guide.md, beacon-module-guide.md, kovarex-enrichment-guide.md, vulcanus-guide.md）
  - `docs/` 下 31 个 .html 文件（对应页面 + 所有标签页）
- **修复脚本**：`scripts/fix_garbled_chars.py`（最终版本）

### 3. game-slot 组件图标放大 + 优化
- **变更**：`static/css/main.css` 和 `docs/css/main.css`
- `.game-img`：40px → **70px**
- `.game-slot`：padding 加大，min-width 64→80px
- `.game-name`：font-size 0.68→0.78rem，max-width 64→90px
- `.game-row`：gap 0.5rem（不变，配合 70px 图标视觉平衡）

### 4. 文章页面布局修复
- **根因**：`.article-center` 缺少 `display: flex`
- **影响**：TOC（220px sticky）和正文垂直堆叠而非左右并排
- **修复**：`.article-center` 添加 `display: flex; gap: 2rem; align-items: flex-start`
- **响应式**：≤768px 时 column 布局，TOC 在上正文在下
- 已同步到 `static/css/main.css` 和 `docs/css/main.css`

## 创建的脚本
| 文件 | 用途 |
|------|------|
| `scripts/run_svg_qa.py` | SVG 质量检查（字号、布局、重叠等） |
| `scripts/batch_fix_svg_fonts.py` | 批量修复 SVG 字体大小 |
| `scripts/fix_garbled_chars.py` | 全站乱码字符修复 |
| `scripts/_check_result.py` | 检查修复结果（临时） |
| `scripts/_sync_css.py` | 同步 CSS 到 docs（临时） |
| `scripts/check_garbled.py` | 验证乱码字节状态（临时） |

## 开放问题（需继续）
1. **部分 h2 标题缺少 `<div class="section-head">` 包装**——red-science-guide、quality-module-guide、main-bus-guide 等页面 h2 样式与其他页面不一致
2. **SVG 剩余 256 个重叠 FAIL**——文字增大后与相邻元素重叠，需人工调整布局
3. **之前 6 张截图的具体视觉缺陷**尚未逐张排查
4. **QA 流程固化**——用户要求将 QA 流程文档化为可复用 checklist

## 文件修改汇总
- `static/css/main.css` — game-slot 图标尺寸 + article-center flex 布局
- `docs/css/main.css` — 同上同步
- `layouts/_default/single.html` — 未修改（TOC 位置确认正确，之前的问题在 CSS）
- `static/js/main.js` — 未修改（TOC 生成逻辑确认正确，浏览器端执行）
- 5 个 content/ .md 文件 — 乱码修复
- 31 个 docs/ .html 文件 — 乱码修复
- SVG 文件见上一轮概要

## Hugo 服务
- Dev server running at `:1319`
- Static server at `:1323`
- 均指向 `factorio-guide/` 目录
