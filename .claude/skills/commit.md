---
description: 按照项目规范创建 git commit
---

# Git Commit 工作流

遵循以下原则创建高质量的 git commit：

## 核心原则

1. **少量多次提交**
   - 每完成一个小功能或修改就提交
   - 保持每个 commit 的改动范围小而聚焦
   - 便于代码审查和问题追溯

2. **详细的 commit message**
   - 清晰描述改动的内容和原因
   - 使用多行格式：标题 + 空行 + 详细说明
   - 标题简洁（< 70 字符），详细说明在 body 中展开

3. **只做 commit，不 push**
   - 只执行 `git add` 和 `git commit`
   - 不要自动执行 `git push`
   - 由用户手动决定何时推送到远程

## Commit Message 格式

```
<type>: <subject>

<body>

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

### Type 类型

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `refactor`: 重构代码
- `test`: 添加或修改测试
- `chore`: 构建过程或辅助工具的变动
- `style`: 代码格式调整（不影响功能）

### 示例

```
feat: Add learning notes directory structure

- Create learning-notes/ folder for storing study summaries
- Add claude-code-memory-system.md with comprehensive guide
- Include examples and best practices

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

## 执行步骤

1. 查看当前状态：`git status`
2. 查看改动内容：`git diff`
3. 添加文件到暂存区：`git add <files>`
4. 创建 commit：`git commit -m "message"`
5. 提醒用户可以手动 push

## 注意事项

- 提交前检查是否有未追踪的重要文件
- 避免提交敏感信息（.env, credentials 等）
- 确保 commit message 准确反映改动内容
- 每次只提交相关的改动，不要混合不相关的修改
