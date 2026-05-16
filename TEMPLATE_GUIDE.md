# Steam 攻略站 Hugo 模板 — Agent 使用指南

> **基于 DSP_Site (Dyson Sphere Program Guide) 结构提炼的标准化模板**
> 用途：Agent 读取此文档后，通过替换美术资源、CSS 变量、内容即可生成结构一致的攻略站

---

## 一、快速开始

### 1. 模板复制

将整个 `steam-guide-template/` 目录复制为新站点目录，例如：

```
新站点名称/         ← 新的 Hugo 站点根目录
├── hugo.toml
├── themes/guide-theme/
├── layouts/
├── static/
├── content/
├── data/
└── .github/workflows/
```

### 2. 必须替换的项（6 处）

| # | 文件 | 替换内容 | 说明 |
|---|------|---------|------|
| 1 | `hugo.toml` | `baseURL`, `title`, `params` | 站点基本信息 |
| 2 | `themes/guide-theme/layouts/_default/baseof.html` | Logo 文字、导航链接、字体、页脚 | 全局外壳 |
| 3 | `static/css/main.css` | CSS 变量 (`:root`) | 全部颜色/字体/间距 |
| 4 | `static/images/` | hero-bg.jpg, logo.png, favicon.ico | 美术资源 |
| 5 | `data/materials.toml` | 物品图标映射表 | 游戏特定素材 |
| 6 | `content/*.md` | 攻略文章内容 | 页面内容 |

### 3. 可选替换

| 文件 | 说明 |
|------|------|
| `layouts/shortcodes/*.html` | 短代码模板（一般不改结构，只改游戏特定逻辑） |
| `static/js/main.js` | TOC 生成逻辑（一般不改） |
| `.github/workflows/hugo-deploy.yml` | CI/CD 配置 |

---

## 二、站点结构详解

```
steam-guide-template/
├── hugo.toml                          # 站点配置（baseURL, title, SEO参数）
├── TEMPLATE_GUIDE.md                  # ← 你正在读的这个文件
├── CONTENT_ARCHITECTURE.md            # 内容架构规划模板
│
├── themes/guide-theme/                # Hugo 主题（全局布局）
│   ├── hugo.toml                      # 主题元数据
│   ├── theme.toml                     # 主题描述
│   ├── archetypes/default.md          # 新文章模板
│   ├── assets/
│   │   ├── css/main.css               # 主题默认 CSS（占位，实际用 static/css/main.css）
│   │   └── js/main.js                 # 主题默认 JS（占位）
│   ├── static/favicon.ico             # 站点图标
│   └── layouts/
│       ├── _default/
│       │   ├── baseof.html            # ★ 全局 HTML 外壳（head + nav + footer）
│       │   ├── home.html              # ★ 首页模板
│       │   ├── single.html            # ★ 文章页模板
│       │   └── list.html              # 列表页模板
│       └── partials/                  # 可复用片段
│           ├── head.html
│           ├── header.html
│           ├── footer.html
│           ├── menu.html
│           ├── terms.html
│           └── head/
│               ├── css.html
│               └── js.html
│
├── layouts/                           # 站点级布局覆盖
│   └── shortcodes/                    # ★ 短代码组件（文章内嵌 UI 组件）
│       ├── box.html                   # 内容容器
│       ├── callout.html               # 提示/警告框
│       ├── check.html                 # 物品清单项
│       ├── diagram.html               # SVG 说明图
│       ├── material.html              # 物品图标卡
│       ├── mat.html                   # 物品卡（旧版兼容）
│       ├── mat-row.html               # 材料行
│       ├── plus.html                  # 加号/等号分隔
│       ├── rawhtml.html               # 原始 HTML
│       ├── recipe.html                # 配方展示（物品 A + B → C）
│       └── section.html               # 章节标题
│
├── static/                            # 静态资源（直接复制到输出）
│   ├── CNAME                          # 自定义域名（如 dsp-guide.com）
│   ├── css/main.css                   # ★ 主样式表（所有视觉风格在此）
│   ├── js/main.js                     # ★ TOC 生成 + 滚动监听
│   └── images/                        # 图片资源
│       ├── hero-bg.jpg                # 首页 + 文章页背景大图
│       ├── game-logo.png              # 游戏Logo
│       └── game-icons/                # 游戏物品图标 PNG
│           └── (游戏物品图标文件)
│
├── content/                           # Markdown 内容
│   ├── _index.md                      # 首页数据
│   └── guide-slug.md                  # 攻略文章（每篇一个 .md 文件）
│
├── data/
│   └── materials.toml                 # 物品图标名称映射
│
└── .github/workflows/
    └── hugo-deploy.yml                # GitHub Pages 自动部署
```

---

## 三、页面类型与模板对应

### 3.1 首页 (home.html)

**结构**：
1. Hero 区域 — 全屏背景图 + 游戏Logo + 标题 + CTA按钮
2. Latest Guides 卡片网格 — 自动列出所有文章
3. By Topic 分类卡 — 按主题分组
4. Newsletter CTA — 底部号召
5. Disclaimer — 免责声明

**Agent 操作**：修改 `home.html` 中的文字和链接即可。

### 3.2 文章页 (single.html)

**结构**：
1. Hero 条 — 背景图 + 文章标题 + 更新日期
2. 左侧浮动 TOC — 自动从 h2 生成，JS 驱动
3. 文章主体 — Markdown 渲染的内容

**Agent 操作**：
- 写 `content/xxx.md` 文件，Hugo 自动渲染
- 使用短代码插入游戏物品图标、配方、提示框等

### 3.3 列表页 (list.html)

简单的标题+摘要列表，一般用于 tags/categories。

---

## 四、短代码使用手册

### `{{< section "标题" >}}`
章节大标题，带左侧琥珀色边框 + 深色背景。

```markdown
{{< section "⚡ What Just Happened" >}}
这里是内容...
```

### `{{< diagram "filename.svg" "Alt text" "760" >}}`
插入 SVG 说明图。文件放在 `static/images/`。

```markdown
{{< diagram "power-cascade.svg" "The power cascade diagram" "760" >}}
```

### `{{< callout tip >}}...{{< /callout >}}`
提示/警告框。类型：`tip`（默认，青色）、`warning`（琥珀色）、`info`（蓝色）。

```markdown
{{< callout tip >}}
**TL;DR** — Your factory needs more power.
{{< /callout >}}
```

### `{{< box >}}...{{< /box >}}`
通用内容容器，带边框和圆角。

```markdown
{{< box >}}
这里放任意内容，支持 Markdown。
{{< /box >}}
```

### `{{< material "processor" "1x" >}}` / `{{< material "processor" "1x" result=true >}}`
物品图标卡。名称对应 `data/materials.toml` 中的 key。`result=true` 加绿色发光边框。

```markdown
{{< material "processor" "2x" >}}
```

### `{{< recipe name1="X" qty1="1x" name2="Y" qty2="1x" result="Z" rqty="1x" >}}`
配方展示：多个材料 + 结果。箭头自动显示。

```markdown
{{< recipe name1="processor" qty1="1x" name2="circuit" qty2="2x" result="green-matrix" rqty="1x" >}}
```

### `{{< check "processor" 8 "Assembling Machine M2" >}}`
清单项：图标 + 数量 + 描述。

```markdown
{{< check "processor" 8 "Assembling Machine M2" >}}
```

### `{{< plus >}}` / `{{< plus type="eq" >}}`
加号或等号分隔符。

---

## 五、CSS 主题定制指南

### 5.1 变量系统 (static/css/main.css)

所有颜色、字体、间距通过 CSS 变量控制。Agent 只需修改 `:root` 即可完全改变视觉风格：

```css
:root {
  /* 背景色 */
  --bg-deep: #080c14;          /* 页面最深背景 */
  --bg-card: #0e1726;          /* 卡片/容器背景 */
  --bg-hero: #0a1020;          /* Hero 区域背景 */

  /* 边框色 */
  --border-dim: #1a2a3e;       /* 弱边框 */
  --border-accent: #2d4a6b;    /* 强调边框 */

  /* 文字色 */
  --text-primary: #e0e8f0;     /* 主文字 */
  --text-secondary: #8a9bb5;   /* 次文字 */
  --text-dim: #5a6a8a;         /* 弱文字 */

  /* 强调色 — 改变这4个就能完全换风格 */
  --accent-cyan: #22d3ee;      /* 主强调色 */
  --accent-blue: #60a5fa;      /* 链接色 */
  --accent-amber: #f59e0b;     /* 标题/警告色 */
  --accent-green: #22c55e;     /* 成功/结果色 */
  --accent-red: #ef4444;       /* 错误/危险色 */

  /* 布局 */
  --nav-height: 56px;          /* 导航栏高度 */
  --max-width: 1100px;         /* 内容最大宽度 */
}
```

### 5.2 主题风格示例

**科幻深空风（当前 DSP 默认）**：
```css
--bg-deep: #080c14; --accent-cyan: #22d3ee; --accent-amber: #f59e0b;
```

**末日废土风**：
```css
--bg-deep: #1a1410; --accent-cyan: #d4a574; --accent-amber: #c45e2c;
--text-primary: #e8dcc8; --border-accent: #4a3520;
```

**奇幻魔法风**：
```css
--bg-deep: #0f0a1a; --accent-cyan: #a78bfa; --accent-amber: #fbbf24;
--text-primary: #e8e0f0; --border-accent: #3d2a5c;
```

**明亮清新风（浅色）**：
```css
--bg-deep: #f8fafc; --bg-card: #ffffff; --text-primary: #1a202c;
--text-secondary: #4a5568; --border-dim: #e2e8f0;
--accent-cyan: #0891b2; --accent-amber: #d97706;
```

### 5.3 字体

在 `baseof.html` 的 `<head>` 中替换 Google Fonts 链接：
```html
<link href="https://fonts.googleapis.com/css2?family=Font1:wght@400;700&family=Font2:wght@500;700&display=swap" rel="stylesheet">
```
然后在 `main.css` 中更新：
```css
body { font-family: 'Font1', sans-serif; }
h1, h2, h3 { font-family: 'Font2', sans-serif; }
```

---

## 六、内容创建工作流

### Agent 生成新文章的步骤：

1. **确定文章 slug**（如 `power-fix-guide`）
2. **创建 `content/<slug>.md`**，Front Matter 格式：

```yaml
---
title: "Article Title (H1)"
description: "Meta description, <160 chars"
date: "2026-05-15"
---
```

3. **使用短代码组织内容**：
   - `{{< section >}}` 分章节
   - `{{< diagram >}}` 插图
   - `{{< callout >}}` 提示
   - `{{< recipe >}}` 配方
   - `{{< material >}}` 物品图标
4. **在 `baseof.html` 的导航中添加链接**
5. **创建 SVG 说明图** → `static/images/`

---

## 七、部署配置

### GitHub Pages（推荐）

1. 创建 GitHub 仓库
2. 将站点推送到 `main` 分支
3. `.github/workflows/hugo-deploy.yml` 自动构建部署
4. 在仓库 Settings → Pages 选择 GitHub Actions
5. 自定义域名：修改 `static/CNAME` + Cloudflare DNS

### 本地预览

```bash
hugo server -p 1616
# 访问 http://localhost:1616/
```

---

## 八、不可修改的结构规则

以下结构规则 Agent **不得**修改，否则会导致布局崩坏：

1. `baseof.html` 必须包含 `{{ block "main" . }}{{ end }}`
2. `single.html` 的 `.article-layout` 必须是 flex 布局（TOC + body）
3. `floating-toc` 的 JS 依赖 `#floatingToc` ID 和 `.article-body h2` 选择器
4. `.game-slot` 的固定宽度（64px / 52px mobile）不可改
5. `.schema-diagram` 类名是 diagram 短代码输出的标识，不可改名
6. CSS 中 `.article-body > h2` 的样式是章节标题的核心样式
7. `data/materials.toml` 的 key 名必须和 `recipe.html` 中的 JSON 映射保持同步

---

## 九、检查清单（Agent 生成新站时必查）

- [ ] `hugo.toml` 的 `baseURL` 和 `title` 已替换
- [ ] `baseof.html` 的 Logo、导航链接、页脚文字已替换
- [ ] `main.css` 的 `:root` CSS 变量已按目标风格修改
- [ ] Google Fonts 链接已替换（如需要换字体）
- [ ] `hero-bg.jpg` 已替换为目标游戏的背景图
- [ ] `game-logo.png` 已替换
- [ ] `data/materials.toml` 已替换为目标游戏的物品映射
- [ ] `static/images/game-icons/` 已放入目标游戏的物品图标
- [ ] 至少 1 篇 `content/*.md` 文章已创建
- [ ] `CNAME` 已设置（如使用自定义域名）
- [ ] `hugo server` 本地预览正常
- [ ] 导航链接全部可点击
- [ ] TOC 自动生成且可跳转
- [ ] 移动端响应式正常
