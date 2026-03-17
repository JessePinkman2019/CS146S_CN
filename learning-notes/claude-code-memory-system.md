# Claude Code 记忆系统完整指南

> 来源：https://code.claude.com/docs/en/memory
> 学习日期：2026-03-17

## 核心概念

Claude Code 使用**双重记忆系统**在会话间传递知识：

| 系统 | CLAUDE.md 文件 | 自动记忆 |
|------|---------------|---------|
| **编写者** | 你手动编写 | Claude 自动学习 |
| **内容** | 指令和规则 | 学习和模式 |
| **范围** | 项目/用户/组织 | 每个工作树 |
| **加载时机** | 每个会话完整加载 | 每个会话（前 200 行） |
| **用途** | 编码标准、工作流、架构 | 构建命令、调试见解、偏好 |

---

## 一、CLAUDE.md 文件系统

### 1.1 文件位置层级

从高到低的优先级：

```
托管策略（组织级）
├── macOS: /Library/Application Support/ClaudeCode/CLAUDE.md
├── Linux/WSL: /etc/claude-code/CLAUDE.md
└── Windows: C:\Program Files\ClaudeCode\CLAUDE.md

项目级（团队共享）
├── ./CLAUDE.md
└── ./.claude/CLAUDE.md

用户级（个人偏好）
└── ~/.claude/CLAUDE.md
```

**加载规则**：
- 从当前工作目录向上遍历，加载所有祖先目录的 CLAUDE.md
- 子目录中的 CLAUDE.md 在读取该目录文件时按需加载
- 更具体的位置优先级更高

### 1.2 快速开始

```bash
# 自动生成初始 CLAUDE.md
/init
```

Claude 会分析代码库并创建包含构建命令、测试指令和项目约定的文件。

### 1.3 编写有效指令

**核心原则**：
- **大小**：目标 200 行以下（更长会降低遵守度）
- **结构**：使用 markdown 标题和列表组织
- **具体性**：写可验证的具体指令
- **一致性**：避免冲突规则

**示例对比**：

❌ 模糊：
```markdown
- 正确格式化代码
- 测试您的更改
- 保持文件有组织
```

✅ 具体：
```markdown
- 使用 2 空格缩进
- 在提交前运行 npm test
- API 处理程序位于 src/api/handlers/
```

### 1.4 导入其他文件

使用 `@path/to/file` 语法：

```markdown
# 项目概述
有关项目概述，请参阅 @README.md
有关可用命令，请参阅 @package.json

# 工作流指南
- Git 工作流 @docs/git-instructions.md

# 个人偏好（不签入版本控制）
- @~/.claude/my-project-instructions.md
```

**特性**：
- 支持相对路径和绝对路径
- 最大递归深度 5 层
- 首次遇到外部导入需要批准

---

## 二、.claude/rules/ 规则系统

### 2.1 组织结构

```
your-project/
├── .claude/
│   ├── CLAUDE.md           # 主项目指令
│   └── rules/
│       ├── code-style.md   # 代码样式指南
│       ├── testing.md      # 测试约定
│       ├── security.md     # 安全要求
│       └── frontend/       # 可以使用子目录
│           └── react.md
```

### 2.2 路径范围规则

使用 YAML frontmatter 限定作用范围：

```yaml
---
paths:
  - "src/api/**/*.ts"
  - "lib/**/*.ts"
---

# API 开发规则

- 所有 API 端点必须包括输入验证
- 使用标准错误响应格式
- 包括 OpenAPI 文档注释
```

**Glob 模式示例**：

| 模式 | 匹配 |
|------|------|
| `**/*.ts` | 任何目录中的所有 TypeScript 文件 |
| `src/**/*` | src/ 目录下的所有文件 |
| `*.md` | 项目根目录中的 Markdown 文件 |
| `src/**/*.{ts,tsx}` | src/ 下的 TS 和 TSX 文件 |

**加载时机**：
- 无 `paths` 字段：启动时加载
- 有 `paths` 字段：读取匹配文件时加载

### 2.3 跨项目共享规则

使用符号链接：

```bash
# 链接共享目录
ln -s ~/shared-claude-rules .claude/rules/shared

# 链接单个文件
ln -s ~/company-standards/security.md .claude/rules/security.md
```

### 2.4 用户级规则

```
~/.claude/rules/
├── preferences.md    # 个人编码偏好
└── workflows.md      # 首选工作流
```

用户级规则在项目规则之前加载，项目规则优先级更高。

---

## 三、自动记忆系统

### 3.1 工作原理

**存储位置**：
```
~/.claude/projects/<project>/memory/
├── MEMORY.md          # 简洁索引（前 200 行自动加载）
├── debugging.md       # 调试模式详细笔记
├── api-conventions.md # API 设计决策
└── ...                # 其他主题文件
```

**关键特性**：
- 默认启用（v2.1.59+）
- 机器本地，不跨设备同步
- 同一 git 仓库的所有工作树共享记忆
- 所有文件都是纯 markdown，可随时编辑

### 3.2 Claude 自动记录的内容

✅ **应该记录**：
- 稳定的模式和约定（多次交互确认）
- 关键架构决策、重要文件路径
- 用户工作流程和工具偏好
- 重复问题的解决方案
- 用户明确要求记住的内容

❌ **不应该记录**：
- 会话特定的临时状态
- 可能不完整的信息
- 与 CLAUDE.md 重复或矛盾的内容
- 推测性或未验证的结论

### 3.3 管理记忆

**查看和编辑**：
```bash
/memory  # 列出所有加载的文件，切换自动记忆开关
```

**配置**：

```json
// .claude/settings.json
{
  "autoMemoryEnabled": false,  // 禁用自动记忆
  "autoMemoryDirectory": "~/my-custom-memory-dir"  // 自定义存储位置
}
```

**环境变量**：
```bash
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

### 3.4 记忆加载机制

- **MEMORY.md**：前 200 行在会话开始时加载
- **主题文件**：按需加载（Claude 需要时才读取）
- **更新时机**：会话期间实时读写

---

## 四、大型团队管理

### 4.1 部署组织级 CLAUDE.md

1. 在托管策略位置创建文件
2. 使用 MDM、Group Policy、Ansible 等工具分发
3. 此文件无法被个人设置排除

### 4.2 排除特定 CLAUDE.md

在大型 monorepo 中排除无关文件：

```json
// .claude/settings.local.json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```

**注意**：托管策略 CLAUDE.md 无法排除。

### 4.3 加载其他目录的 CLAUDE.md

```bash
# 默认不加载 --add-dir 目录中的 CLAUDE.md
# 要加载，设置环境变量：
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
```

---

## 五、故障排除

### 5.1 Claude 不遵循 CLAUDE.md

**原因**：CLAUDE.md 是上下文，不是强制配置。

**调试步骤**：
1. 运行 `/memory` 验证文件是否加载
2. 检查文件位置是否正确
3. 使指令更具体
4. 查找冲突指令
5. 使用 `InstructionsLoaded` hook 记录加载日志

### 5.2 不知道自动记忆保存了什么

```bash
/memory  # 选择自动记忆文件夹浏览
```

### 5.3 CLAUDE.md 太大

**解决方案**：
- 使用 `@path` 导入拆分内容
- 将指令移到 `.claude/rules/` 文件
- 使用路径范围规则按需加载

### 5.4 压缩后指令丢失

**原因**：指令只在对话中给出，未写入 CLAUDE.md。

**解决**：将指令添加到 CLAUDE.md 使其持久化。

---

## 六、关键洞察

### 设计哲学

1. **渐进式学习**：Claude 随时间了解项目
2. **分层管理**：组织/团队/个人三级指令
3. **按需加载**：优化上下文使用
4. **透明可控**：所有记忆可读可编辑

### 与 Skills 的区别

- **CLAUDE.md/Rules**：始终或条件加载到上下文
- **Skills**：仅在调用或相关时加载
- **自动记忆**：Claude 自主决定记录内容

### 最佳实践总结

```markdown
# 项目 CLAUDE.md（团队共享）
- 构建和测试命令
- 编码标准和架构决策
- 命名约定和常见工作流

# 用户 CLAUDE.md（个人偏好）
- 代码样式偏好
- 个人工具快捷方式
- 工作流习惯

# 自动记忆（Claude 学习）
- 调试见解
- 发现的模式
- 用户更正和偏好
```

---

## 七、相关资源

- **Skills**：打包按需加载的可重复工作流
- **Settings**：配置 Claude Code 行为
- **管理会话**：上下文管理、恢复对话
- **Subagent 记忆**：让 subagents 维护自己的记忆

---

## 实践建议

1. **从 `/init` 开始**：让 Claude 生成初始 CLAUDE.md
2. **保持简洁**：每个文件 < 200 行
3. **具体化指令**：写可验证的具体规则
4. **定期审查**：删除过时或冲突的指令
5. **善用分层**：项目共享 vs 个人偏好
6. **信任自动记忆**：让 Claude 学习你的习惯
7. **定期检查**：用 `/memory` 查看 Claude 学到了什么
