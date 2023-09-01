from mmengine.config import Config
from mmengine.runner import Runner



cfg = Config.fromfile("./configs.py")

runner = Runner.from_cfg(cfg)
runner.train()

