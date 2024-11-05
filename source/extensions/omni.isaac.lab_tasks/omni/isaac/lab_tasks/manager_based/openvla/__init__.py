'''
Author: jamefrank 42687222+jamefrank@users.noreply.github.com
Date: 2024-11-04 14:32:27
LastEditors: jamefrank 42687222+jamefrank@users.noreply.github.com
LastEditTime: 2024-11-04 15:20:22
FilePath: /IsaacLab/source/extensions/omni.isaac.lab_tasks/omni/isaac/lab_tasks/manager_based/openvla/__init__.py
Description: 

Copyright (c) 2024 by Frank, All Rights Reserved. 
'''

import gymnasium as gym
from .franka_camera_env_cfg import FrankaRGBCamEnvCfg


gym.register(
    id="Isaac-FrankaOpenval-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": FrankaRGBCamEnvCfg
    },
)
