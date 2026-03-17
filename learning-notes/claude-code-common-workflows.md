# Claude Code 常见工作流程

> 来源：https://code.claude.com/docs/en/common-workflows
> 学习日期：2026-03-17

---

## 代码探索

```
give me an overview of this codebase
find the files that handle user authentication
trace the login process from front-end to database
```

---

## 调试

```
I'm seeing an error when I run npm test
suggest a few ways to fix the @ts-ignore in user.ts
```

---

## 重构

```
find deprecated API usage in our codebase
refactor utils.js to use ES2024 features while maintaining the same behavior
```

---

## 测试

```
find functions in NotificationsService.swift that are not covered by tests
add test cases for edge conditions in the notification service
```

---

## 文档 & PR

```
add JSDoc comments to the undocumented functions in auth.js
create a pr
```

---

## 文件引用

| 语法 | 用途 |
|------|------|
| `@src/utils/auth.js` | 引用单个文件 |
| `@src/components/` | 引用目录 |
| `@server:resource` | 引用 MCP 资源 |

---

## Plan Mode

```bash
# 启动时进入 Plan Mode（只读分析，不修改代码）
claude --permission-mode plan

# 会话中切换：Shift+Tab 循环切换模式
# Normal → Auto-Accept → Plan Mode
```

---

## Subagents

```bash
/agents                                          # 查看/创建 subagents
use the code-reviewer subagent to check auth     # 明确调用
review my recent code changes for security       # 自动委派
```

自定义 subagent 放在 `.claude/agents/` 供团队共享。

---

## 会话管理

```bash
claude --continue              # 继续最近的会话
claude --resume auth-refactor  # 按名称恢复
claude --from-pr 123           # 从 PR 恢复

/rename auth-refactor          # 命名当前会话
/resume                        # 打开会话选择器
```

---

## Worktrees（并行开发）

```bash
claude --worktree feature-auth   # 创建隔离 worktree
claude --worktree bugfix-123     # 另一个并行会话
```

- Worktree 在 `.claude/worktrees/<name>` 创建
- 无更改时自动清理，有更改时提示保留/删除
- 将 `.claude/worktrees/` 加入 `.gitignore`

---

## Thinking Mode

| 方式 | 说明 |
|------|------|
| `Option+T` / `Alt+T` | 切换当前会话的思考开关 |
| 提示中加 `ultrathink` | 为该轮设置最高推理深度 |
| `Ctrl+O` | 查看思考过程（灰色斜体） |
| `CLAUDE_CODE_EFFORT_LEVEL` | 设置推理深度：low/medium/high |

---

## Unix 管道集成

```bash
# 管道输入
cat build-error.txt | claude -p 'explain the root cause' > output.txt

# 输出格式
--output-format text         # 纯文本（默认）
--output-format json         # JSON（含元数据）
--output-format stream-json  # 流式 JSON

# 作为 linter 集成到 package.json
"lint:claude": "claude -p 'you are a linter. look at changes vs. main and report typos.'"
```

---

## 通知（长任务时）

```bash
/hooks  # 选择 Notification 事件

# macOS 通知命令
osascript -e 'display notification "Claude needs attention" with title "Claude Code"'
```

触发时机：`permission_prompt` / `idle_prompt` / `auth_success`
