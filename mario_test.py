from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
import time
import gym

# env = gym_super_mario_bros.make('SuperMarioBros-v0')
# env = JoypadSpace(env, SIMPLE_MOVEMENT)

# done = True
# for step in range(9000):
#     if done:
#         state = env.reset()
#     state, reward, done, info = env.step(env.action_space.sample())
#     env.render()

# env.close()

# 保存路径
video_dir_path = 'video/mario_test'
# 创建游戏环境
env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)

# 使用 strftime 生成不带冒号的时间格式，例如: 20251125-161728
timestamp = time.strftime("%Y%m%d-%H%M%S")
env = gym.wrappers.RecordVideo(
 env,
 video_folder=video_dir_path,
 episode_trigger=lambda episode_id: True,
 name_prefix='mario-video-{}'.format(timestamp)
)

# 开始运行一局
print("开始录制...")
env.reset()
while True:
    state, reward, done, info = env.step(env.action_space.sample())
    if done or info['time'] < 250:
        break
print("Your mario video is saved in {}".format(video_dir_path))
try:
    del env
except Exception:
    pass