'''
Author: jamefrank 42687222+jamefrank@users.noreply.github.com
Date: 2024-11-04 09:54:15
LastEditors: jamefrank 42687222+jamefrank@users.noreply.github.com
LastEditTime: 2024-11-04 15:15:15
FilePath: /IsaacLab/source/dev/openvla.py
Description: 测试使用openvla

Copyright (c) 2024 by Frank, All Rights Reserved.
'''


import argparse

from omni.isaac.lab.app import AppLauncher

# add argparse arguments
parser = argparse.ArgumentParser(description="openvla with isaaclab.")
parser.add_argument("--num_envs", type=int, default=1, help="Number of environments to spawn.")
# append AppLauncher cli args
AppLauncher.add_app_launcher_args(parser)
# parse the arguments
args_cli = parser.parse_args()

# launch omniverse app
app_launcher = AppLauncher(args_cli)
simulation_app = app_launcher.app

# --------------------------
import gymnasium as gym
import torch

import omni.isaac.lab_tasks  # noqa: F401
from omni.isaac.lab_tasks.utils import parse_env_cfg


def main():
    task_name = "Isaac-FrankaOpenval-v0"
    env_cfg = parse_env_cfg(task_name)
    env = gym.make(task_name, cfg=env_cfg)
    env.reset()
    cnt = 0
    # # simulate environment
    while simulation_app.is_running():
        # run everything in inference mode
        with torch.inference_mode():
            # # sample actions from -1 to 1
            # actions = 2 * torch.rand(env.action_space.shape, device=env.unwrapped.device) - 1
            # # apply actions
            # env.step(actions)
            cnt += 1

    # env.close()


if __name__ == '__main__':
    main()
    pass
