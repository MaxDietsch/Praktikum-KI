from mmengine.config import Config
from mmengine.runner import Runner
import torch
import os

if torch.cuda.is_available():
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

cfg = Config.fromfile('configs.py')
cfg.work_dir = './work_dirs/train_scratch/10x3'

runner = Runner.from_cfg(cfg)
runner.train()

