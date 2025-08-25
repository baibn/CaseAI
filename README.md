# CaseAI - AI 辅助测试用例生成系统

CaseAI 是一个基于 AI 技术的测试用例生成系统，通过分析软件需求文档，自动生成相应的测试用例，提高测试效率和质量。

## 项目特性

- 🚀 基于 AI 的测试用例自动生成
- 📊 直观的数据统计和可视化
- 🎯 项目管理和需求跟踪
- 💡 智能需求分析和测试点提取
- 🔄 实时更新和多线程处理

## 技术栈

### 后端
- Django (Python Web 框架)
- SQLite 数据库
- AI API 集成
- 多线程处理机制

### 前端
- Vue.js
- Element UI
- Axios
- Echarts (数据可视化)

## 系统架构

```
CaseAI/
├── 后端 (Django)
│   ├── Myapp/
│   │   ├── AIapi.py     # AI 功能核心实现
│   │   ├── models.py    # 数据模型
│   │   └── views.py     # 接口实现
│   └── CaseAI/          # Django 项目配置
└── 前端 (Vue.js)
    ├── src/
    │   ├── components/  # 组件
    │   ├── views/       # 页面
    │   └── router/      # 路由配置
    └── public/
```

## 核心功能

1. **项目管理**
   - 项目创建和配置
   - 项目详情查看和编辑
   - 项目统计数据展示

2. **需求管理**
   - 需求文档导入
   - 需求分析和分类
   - 需求变更跟踪

3. **AI 测试用例生成**
   - 基于需求的测试点提取
   - 智能测试用例生成
   - 多线程并行处理

4. **数据可视化**
   - 项目统计数据展示
   - 需求覆盖率分析
   - 测试用例分布展示

## 快速开始

### 环境要求
- Python 3.x
- Node.js
- npm 或 yarn

### 后端设置
```bash
# 安装依赖
pip install -r requirements.txt

# 运行数据库迁移
python manage.py migrate

# 启动服务器
python manage.py runserver
```

### 前端设置
```bash
# 进入前端目录
cd client

# 安装依赖
npm install

# 启动开发服务器
npm run serve
```

## API 接口

主要接口包括：
- `/get_project_detail/` - 获取项目详情
- `/update_project_detail/` - 更新项目信息
- `/get_news/` - 获取系统公告

## AI 功能说明

系统集成了 AI 接口，通过 `AIapi.py` 实现，主要功能：
- 需求文档智能分析
- 测试点自动提取
- 多线程并行处理提高效率

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

[MIT License](LICENSE)