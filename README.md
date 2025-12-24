# MARIO 工作区说明

本仓库包含多个外部项目作为 Git 子模块：

- DI-adventure（opendilab/DI-adventure）
- DI-engine（opendilab/DI-engine）
- DQN-mario-xiaoyao（likemango/DQN-mario-xiaoyao）

## 克隆与初始化

首次克隆本仓库后，请执行子模块初始化与更新：

```bash
git clone https://github.com/Estella-ChenYL/mario.git
cd mario
git submodule update --init --recursive
```

如果子模块需要同步到最新版本：

```bash
git submodule update --remote --recursive
```

## 备注

之前的目录以快捷方式/嵌套仓库形式存在，现已统一为标准 Git 子模块，便于版本管理与协作。
