# 文档说明
## 创建环境
```python
conda env create -f mario_environments_utf8.yaml # linux/mac
conda env create -f mario_environments.yaml # win
conda activate mario
```
## 大数据
运行文件在`DI-adventure/mario-dqn`
- 修改DQN为Dueling DQN （25.12.24）
## 飞行
文件为mario-dqn/DQN-mario-xiaoyao
- 修改了`main.py`（训练）逻辑结构，通过函数封装等使代码具有可读性
- 修改了`replay.py`（评估），增加了seed的功能，并通过函数封装等使代码具有可读性
- 修改了`wrappers.py`(环境)，增加了稀疏奖励、硬币奖励、FinalEvalRewardEnv
- 目前训练的速度很慢，如果需要提速，需增加`ding.envs.SyncSubprocessEnvManager`并行环境管理器、`cuda`加速
  
