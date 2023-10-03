from mmengine.config import Config
from mmengine.runner import Runner
import torch
import os

if torch.cuda.is_available():
    os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

cfg = Config.fromfile('configs.py')
checkpoint_file = './work_dirs/pretrain/vit_p16_backbone-weights.pth'
cfg.model.backbone.init_cfg = dict(type='Pretrained', checkpoint=checkpoint_file)
cfg.work_dir = './work_dirs/train/100%'

runner = Runner.from_cfg(cfg)
runner.train()

