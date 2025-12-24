from gym_super_mario_bros.actions import SIMPLE_MOVEMENT,COMPLEX_MOVEMENT
from gym_super_mario_bros import SuperMarioBrosEnv
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from nes_py.app.play_human import play_human

env = gym_super_mario_bros.make('SuperMarioBros-v0')

if __name__ == '__main__':
  
    env = JoypadSpace(env, COMPLEX_MOVEMENT)
    
    # 启动人类游玩模式
    print("请使用键盘控制 (W/A/S/D 等键)...")
    play_human(env)

# if __name__ == '__main__':
#     print("="*40)
#     print("      马里奥键盘操控说明")
#     print("="*40)
#     print("1. 请确保你的输入法是【英文模式】")
#     print("2. 运行后，请用鼠标【点击一下游戏窗口】以获取焦点")
#     print("-" * 40)
#     print("【按键列表】")
#     print("  方向键 (↑↓←→) : 移动")
#     print("  O (字母欧)    : 跳跃 (A键)")
#     print("  P (字母皮)    : 加速/攻击 (B键)")
#     print("  Enter (回车)  : 开始/暂停")
#     print("="*40)

#     # 启动人工控制
#     try:
#         play_human(env)
#     except Exception as e:
#         print(f"发生错误: {e}")