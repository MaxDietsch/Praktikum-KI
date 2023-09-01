from mmengine.config import Config
from mmengine.runner import Runner
import os 
import torch

if torch.cuda.is_available():
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

cfg = Config.fromfile("./pretrain_configs.py")

runner = Runner.from_cfg(cfg)
runner.train()