# Factorio Guide - 文章发布状态与样式对比报告

**生成时间**: 2026-05-24 22:36 GMT+8  
**当前分支**: content-polishing  
**产线分支**: main  

---

## 一、未发布到产线的新文章（6篇）

这些文章在 `main` 分支**不存在**，仅在 `content-polishing` 分支存在，且设置了 `hidden: true` 和未来的 `publishDate`。

| 序号 | 文章路径 | 标题 | 状态 | hidden | publishDate | 样式差异 |
|------|----------|------|------|---------|-------------|----------|
| 1 | `content/blueprints/ltn-mod-guide.md` | LTN Mod Guide | ✅ 新建 | true | 2026-05-27 | ⚠️ **全新样式** |
| 2 | `content/defense/artillery-guide.md` | Artillery Guide | ✅ 新建 | true | 2026-05-27 | ⚠️ **全新样式** |
| 3 | `content/production-ratios/beacon-module-guide.md` | Beacon Module Guide | ✅ 新建 | true | 2026-05-27 | ⚠️ **全新样式** |
| 4 | `content/production-ratios/kovarex-enrichment-guide.md` | Kovarex Enrichment Guide | ✅ 新建 | true | 2026-05-27 | ⚠️ **全新样式** |
| 5 | `content/space-age/aquilo-guide.md` | Aquilo Guide | ✅ 新建 | true | 2026-05-27 | ⚠️ **全新样式** |
| 6 | `content/space-age/vulcanus-guide.md` | Vulcanus Guide | ✅ 新建 | true | 2026-05-27 | ⚠️ **全新样式** |

---

## 二、重构文章（10篇）- 内容已修改但存在于产线

这些文章在 `main` 分支**已存在**，但在 `content-polishing` 分支经过了**沙漏结构重构**（commit `11c86c6`）。

| 序号 | 文章路径 | 标题 | 修改行数 | 样式差异 |
|------|----------|------|----------|----------|
| 1 | `content/base-design/nuclear-power-guide.md` | Nuclear Power Guide | +169 | ✅ **有差异** |
| 2 | `content/blueprints/circuit-network-guide.md` | Circuit Network Guide | -187 | ✅ **有差异** |
| 3 | `content/defense/flamethrower-defense-guide.md` | Flamethrower Defense | -160 | ✅ **有差异** |
| 4 | `content/getting-started/green-science-guide.md` | Green Science Guide | +109 | ✅ **有差异** |
| 5 | `content/getting-started/your-first-factory.md` | Your First Factory | +113 | ✅ **有差异** |
| 6 | `content/production-ratios/oil-processing-guide.md` | Oil Processing Guide | -173 | ✅ **有差异** |
| 7 | `content/space-age/fulgora-recycling-guide.md` | Fulgora Recycling | -184 | ✅ **有差异** |
| 8 | `content/space-age/gleba-survival-guide.md` | Gleba Survival Guide | +165 | ✅ **有差异** |
| 9 | `content/space-age/space-platform-guide.md` | Space Platform Guide | -208 | ✅ **有差异** |
| 10 | `content/trains-logistics/basic-rail-network.md` | Basic Rail Network | +116 | ✅ **有差异** |

---

## 三、CSS 样式变更（影响所有文章）

`static/css/main.css` 在 `content-polishing` 分支有**重大更新**，这些变更会影响**所有文章**的渲染效果。

### 3.1 文章布局修复

**变更前 (main)**:
```css
.article-center {
  flex: 1;
  min-width: 0;
  max-width: var(--content-w);
}
```

**变更后 (content-polishing)**:
```css
.article-center {
  display: flex;           /* ✅ 新增 */
  gap: 2rem;               /* ✅ 新增 */
  align-items: flex-start;  /* ✅ 新增 */
  flex: 1;
  min-width: 0;
  max-width: var(--content-w);
}
```

**影响**:
- ✅ **TOC（目录）现在会正确显示在左侧**，与正文并排
- ✅ 修复了之前 TOC 垂直堆叠在正文上方的问题
- ✅ 响应式设计：≤768px 时自动切换为垂直布局

---

### 3.2 Game Slot 图标放大

**变更前 (main)**:
```css
.game-slot {
  display: flex;
  gap: 0.25rem;
  padding: 0.35rem 0.5rem;
  min-width: 64px;
}

.game-img {
  width: 40px;
  height: 40px;
}

.game-name {
  font-size: 0.68rem;
  max-width: 64px;
}
```

**变更后 (content-polishing)**:
```css
.game-slot {
  display: inline-flex;     /* ✅ flex → inline-flex */
  gap: 0.35rem;            /* ✅ 增大 */
  padding: 0.5rem 0.65rem; /* ✅ 增大 */
  min-width: 80px;          /* ✅ 64px → 80px */
}

.game-img {
  width: 70px;             /* ✅ 40px → 70px */
  height: 70px;
}

.game-name {
  font-size: 0.78rem;     /* ✅ 0.68rem → 0.78rem */
  max-width: 90px;         /* ✅ 64px → 90px */
}
```

**影响**:
- ✅ 游戏图标从 **40px 放大到 70px**（75% 增大）
- ✅ 图标更清晰，移动端更易于点击
- ✅ 文字区域增大，避免长名称换行问题

---

## 四、SVG 图形质量修复

`content-polishing` 分支修复了 **25 个 SVG 文件**的字体过小问题。

**修复策略**: `round()` → `ceil()` 避免欠调

**影响文章**:
- 8-beacon-layout.svg
- artillery-outpost.svg（已重写，原文件 XML 损坏）
- blue-science-flow.svg
- circuit-control.svg
- 等共 25 个文件

**剩余问题**: 256 个重叠/布局 FAIL（文字增大后与相邻元素重叠），需人工调整布局

---

## 五、全站乱码修复

`content-polishing` 分支修复了 **36 个文件**的 UTF-8 双重编码问题。

**根因**: em dash `—` (U+2014) 被错误编码为 `鈥?`，箭头 `→` 变成 `鈫?`

**修复范围**:
- `content/` 下 5 个 .md 文件
- `docs/` 下 31 个 .html 文件

**影响**: 所有文章的特殊字符（破折号、箭头等）现在会正确渲染

---

## 六、总结与建议

### 6.1 新文章（6篇）- 未发布

**状态**: ✅ 内容完成 | ⚠️ **未发布**（`hidden: true` + 未来日期）

**建议**:
1. 确认 `publishDate: 2026-05-27T16:52:00+08:00` 是否为正式发布时间
2. 发布前检查：
   - SVG 图形布局（256 个重叠 FAIL）
   - h2 标题是否缺少 `<div class="section-head">` 包装
   - 移动端响应式效果

---

### 6.2 重构文章（10篇）- 已修改但未合并到 main

**状态**: ⚠️ **样式与产线不一致**

**建议**:
1. 这些文章的 Markdown 内容已重构（沙漏结构 + H2 随机化 + 社区链接）
2. 由于 CSS 变更（`.article-center` flex 布局 + `.game-slot` 图标放大），**重构文章在 `content-polishing` 分支的渲染效果与产线不同**
3. 必须**同时发布 CSS 更新**，否则重构文章在产线上的样式会错乱

---

### 6.3 发布优先级

**P0（必须同时发布）**:
- ✅ `static/css/main.css`（文章布局 + 图标尺寸）
- ✅ 6 篇新文章（如果到了发布日期）
- ✅ 10 篇重构文章

**P1（建议发布前修复）**:
- ⚠️ SVG 重叠布局问题（256 个 FAIL）
- ⚠️ h2 标题缺少 `<div class="section-head">` 包装

---

## 七、附录：Git 分支对比命令

```bash
# 查看 content-polishing 相对于 main 的新文件
git diff main --name-status -- content/ | Select-String "^A"

# 查看 content-polishing 相对于 main 的修改文件
git diff main --name-status -- content/ | Select-String "^M"

# 查看 CSS 差异
git diff main -- static/css/main.css

# 查看某篇文章的详细差异
git diff main -- content/space-age/vulcanus-guide.md
```

---

**报告结束** | 如有疑问，请查看 `session-summary_2026-05-24.md` 了解详细技术背景。
