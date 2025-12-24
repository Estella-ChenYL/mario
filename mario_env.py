import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import numpy as np

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

print("="*30)
print(f"1. 观测空间 (Observation Space): {env.observation_space}")
print(f"   数据类型: {env.observation_space.dtype}")
print(f"   上下限: [{env.observation_space.low.min()}, {env.observation_space.high.max()}]")
print("-" * 30)
print(f"2. 动作空间 (Action Space): {env.action_space}")
print(f"   动作含义 (SIMPLE_MOVEMENT): {SIMPLE_MOVEMENT}")
print("-" * 30)
print(f"3. 奖励范围 (Reward Range): {env.reward_range}")
print("="*30)