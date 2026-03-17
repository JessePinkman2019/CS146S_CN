# Claude Code 记忆系统速查

> 来源：https://code.claude.com/docs/en/memory
> 学习日期：2026-03-17

---

## 双重记忆系统

| | CLAUDE.md | 自动记忆 |
|--|-----------|---------|
| 编写者 | 你 | Claude |
| 内容 | 指令和规则 | 学习和模式 |
| 加载 | 每个会话完整加载 | 前 200 行 |

---

## CLAUDE.md 文件位置（优先级从低到高）

```
~/.claude/CLAUDE.md                          # 用户级（个人偏好）
./CLAUDE.md 或 ./.claude/CLAUDE.md           # 项目级（团队共享）
/etc/claude-code/CLAUDE.md                   # 组织级（IT 管理，不可排除）
```

**快速生成**：`/init`

**编写原则**：
- 目标 200 行以下
- 写具体可验证的指令，不写模糊描述
- 避免冲突规则
- 用 `@path/to/file` 导入其他文件

---

## .claude/rules/ 规则系统

```
.claude/rules/
├── code-style.md    # 无 paths → 启动时加载
├── testing.md
└── api.md           # 有 paths → 读取匹配文件时加载
```

**路径范围规则**（按需加载，节省上下文）：
```yaml
---
paths:
  - "src/api/**/*.ts"
---
# 仅对匹配文件生效的规则
```

---

## 自动记忆

**存储位置**：`~/.claude/projects/<project>/memory/`

```
memory/
├── MEMORY.md       # 索引，前 200 行自动加载
├── debugging.md    # 主题文件，按需加载
└── patterns.md
```

**管理**：
```bash
/memory             # 查看/编辑记忆文件，切换开关
```

**配置**：
```json
{ "autoMemoryEnabled": false }
```

**应该记录**：稳定模式、架构决策、用户偏好、重复问题的解决方案

**不应该记录**：临时状态、未验证的结论、与 CLAUDE.md 重复的内容

---

## 故障排除

| 问题 | 解决 |
|------|------|
| Claude 不遵循指令 | `/memory` 确认文件已加载；指令更具体；查找冲突规则 |
| 不知道记了什么 | `/memory` 浏览自动记忆文件夹 |
| CLAUDE.md 太大 | 用 `@path` 导入或拆分到 `.claude/rules/` |
| 压缩后指令丢失 | 指令只在对话中，需写入 CLAUDE.md 才能持久化 |

---

## 分层设计原则

- **组织级**：公司编码标准、安全策略（强制）
- **项目级**：构建命令、架构决策、团队约定（版本控制共享）
- **用户级**：个人偏好、工具快捷方式（仅本机）
- **自动记忆**：Claude 从交互中学习的内容（机器本地）
