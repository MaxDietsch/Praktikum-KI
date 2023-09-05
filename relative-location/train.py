from mmengine.config import Config
from mmengine.runner import Runner
import torch
import os

benchmark_cfg = Config.fromfile('configs.py')

checkpoint_file = './work_dirs/selfsup/relative-loc_resnet50_8xb64-steplr-70e_in1k_colab/relative-loc_backbone-weights.pth'

benchmark_cfg.model.backbone.frozen_stages=4
benchmark_cfg.model.backbone.init_cfg = dict(type='Pretrained', checkpoint=checkpoint_file)

benchmark_cfg.work_dir = './work_dirs/benchmarks/classification/imagenet/resnet50_8xb32-steplr-100e_in1k_colab'

benchmark_cfg.randomness = dict(seed=0, deterministic=True)

if torch.cuda.is_available():
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

runner = Runner.from_cfg(benchmark_cfg)
runner.train()

