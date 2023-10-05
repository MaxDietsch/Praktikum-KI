from mmengine.config import Config
from mmengine.runner import Runner
import torch
import os

cfg = Config.fromfile('configs.py')
cfg.work_dir = './work_dirs/train_scratch/5000'

runner = Runner.from_cfg(cfg)
runner.train()

