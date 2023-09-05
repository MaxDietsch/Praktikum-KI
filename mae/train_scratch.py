from mmengine.config import Config
from mmengine.runner import Runner
import torch
import os

benchmark_cfg = Config.fromfile('configs.py')

benchmark_cfg.work_dir = './work_dirs/train_scratch/vit_p16'

benchmark_cfg.randomness = dict(seed=0, deterministic=True)

if torch.cuda.is_available():
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

runner = Runner.from_cfg(benchmark_cfg)
runner.train()

