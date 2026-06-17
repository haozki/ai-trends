# AIBOX 项目长期记忆

## 项目概况

- AI 科技导航站，单文件静态站点，无构建依赖
- 部署地址：https://haozki.github.io/ai-trends/
- GitHub 仓库：https://github.com/haozki/ai-trends.git（gh-pages 分支）

## 目录结构

- `dist/` — 部署目录（index.html, git-history.html, v1/, v2/）
- `assets/` — 参考数据（models.md, projects.md, coding-agents.md, companies.md）
- `ProjectsCollection/` — AI项目资料库（10个项目，面向公众号文章素材，每个含info.md+asset/）
- `AGENTS.md` — 项目级规则
- `.workbuddy/skills/` — 项目级别 skills（frontend-design、web-design-guidelines、ui-ux-pro-max）
- `src/content/` — Astro 内容集合（博客文章）
- `src/content.config.ts` — 集合 Schema 定义

## 技术栈

- **框架**：Astro 5（静态站点生成器）
- **内容管理**：Astro 内容集合（Content Collections）
- **构建**：`npm run build` 生成 `dist/` 目录
- **部署**：本地构建 → 推送 `dist/` 到 `gh-pages` 分支

## 数据来源

- 大模型排名：Chatbot Arena (openlm.ai)，Elo 评分
- 文生图模型：arena.ai，Elo 评分
- 文生视频模型：magichour.ai，共识评分
- AI 项目：GitHub API，按 Stars 排名
- 厂商 Logo：models.dev/logos/{id}.svg，CSS filter 反色显示

## 页面结构

- 首页：直接显示博客文章列表（极简结构）
- 博客列表页：/blog/（备用入口）
- 博客文章详情页：/blog/[id]
- 热门模型：二级导航（默认/国产/生图/生视频）
- 热门项目：二级导航（默认 + 9 大分类）
- 热门 Agent：待更新

## 项目 Skills

- 项目级别 skills 存储在 `.workbuddy/skills/` 目录
- 已安装：frontend-design、web-design-guidelines、ui-ux-pro-max
- 仅对当前项目生效，不影响全局配置

## 设计系统（AI科技极简风格）

- **配色方案**：浅紫色背景 (#FAF5FF) + 紫色主色 (#7C3AED) + 青色强调 (#06B6D4)
- **字体**：Space Grotesk（标题）+ DM Sans（正文）
- **设计风格**：极简、未来感、专业感，大量留白、细线边框、微妙发光效果
- **微交互动效**：悬停发光、平滑过渡、按钮悬停效果
- **响应式设计**：适配移动端（375px）、平板（768px）、桌面端（1024px+）
- **组件样式**：卡片、按钮、标签、代码块等统一风格
- **最后更新**：2026-06-17
- **改造完成**：已成功应用AI科技极简风格，包括配色、字体、布局、动效等
- **极简结构**：首页直接显示博客列表，移除英雄区域，实现极简布局

## 部署流程

1. `npm run build` 构建 dist 目录
2. `git add dist/` 添加 dist 目录下的所有文件
3. `git commit -m '...'` 提交更改
4. `git subtree split --prefix=dist -b gh-pages-deploy`
5. `git push origin gh-pages-deploy:gh-pages --force`
6. `git branch -D gh-pages-deploy`
