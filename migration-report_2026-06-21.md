# SA 目录迁移 — 最终报告

## 已完成

### 文件迁移（7 篇 → 6 个子板块）
- `guide/`: planet-order-guide.md, vulcanus-guide.md
- `fulgora/`: fulgora-recycling-guide.md
- `gleba/`: gleba-survival-guide.md
- `aquilo/`: aquilo-guide.md
- `platform/`: space-platform-guide.md
- `quality/`: quality-module-guide.md

每篇文件添加了 `aliases: - /space-age/<slug>/` 确保旧 URL 自动 301 重定向。

### 子板块 _index.md（6 个）
每个子板块目录下创建了 `_index.md`，含 title 和 description。

### 模板更新
- `baseof.html`: `nav-btn-space-age` → `nav-btn`（取消高亮区别）
- `home.html`: 无需修改，`where .Site.RegularPages "Section" "space-age"` 跨子目录正确收集
- `list.html`: 子板块渲染正常
- `single.html`: `.Parent.Pages` 仅显示同板块的兄弟文章

### Hugo 构建
- 119 页面，7 aliases，0 错误
- 首页、子板块页、文章页、旧 URL 重定向均验证通过

### 跨引用（ref shortcode）修复
更新了 10 个文件中的 `{{< ref >}}` 短代码，指向新路径。

### `space-age/_index.md` 链接修复
7 个手动链接从旧路径改为子目录路径。

## 已知问题

### 7 篇丢失文章（从未提交到 git）
以下文章在本会话中因文件操作失误永久丢失，需要重新编写：
1. vulcanus-lava-processing.md
2. fulgora-scrap-overflow.md
3. gleba-bioflux-production.md
4. gleba-pentapod-defense.md
5. space-platform-ship-design.md
6. cross-planet-logistics.md
7. quality-module-upcycling.md
