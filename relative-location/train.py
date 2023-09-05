from mmengine.config import Config
from mmengine.runner import Runner
import torch
import os

benchmark_cfg = Config.fromfile('configs.py')

checkpoint_file = './work_dirs/selfsup/resnet50/resnet_backbone-weights.pth'

benchmark_cfg.model.backbone.frozen_stages=1
benchmark_cfg.model.backbone.init_cfg = dict(type='Pretrained', checkpoint=checkpoint_file)

benchmark_cfg.work_dir = './work_dirs/train/kvasir/resnet50'

benchmark_cfg.randomness = dict(seed=0, deterministic=True)

if torch.cuda.is_available():
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

runner = Runner.from_cfg(benchmark_cfg)
runner.train()

