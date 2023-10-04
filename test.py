import argparse
import os
import os.path as osp

from mmengine.config import Config, DictAction
from mmengine.runner import Runner
import torch

def parse_args():
    parser = argparse.ArgumentParser(description='Test a model')
    parser.add_argument('algorithm', help='the algorithm which was used for SSL')
    parser.add_argument('job', default='train', help='specify if train job or train_scratch (no SSL training) job should be done')
    parser.add_argument('dataset', help='the dataset which was used for training')
    
    # When using PyTorch version >= 2.0.0, the `torch.distributed.launch`
    # will pass the `--local-rank` parameter to `tools/train.py` instead
    # of `--local_rank`.
    parser.add_argument('--local_rank', '--local-rank', type=int, default=0)
    args = parser.parse_args()
    if 'LOCAL_RANK' not in os.environ:
        os.environ['LOCAL_RANK'] = str(args.local_rank)

    return args


def main():
    args = parse_args()

    cfg_path = osp.join(args.algorithm, "configs.py")
    cfg = Config.fromfile(cfg_path)

    model_path = osp.join(args.algorithm, "work_dirs", args.job, args.dataset, "epoch_20.pth")
    cfg.model.init_cfg = dict(type = "Pretrained", checkpoint = model_path)

    # work_dir is determined in this priority: CLI > segment in file > filename
    cfg.work_dir = osp.join(args.algorithm, "work_dirs", args.job, "results_" + args.dataset)

    cfg.test_dataloader =  dict(
    batch_size=32,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type="Sun",
        data_root="./data_dir/SUN",
        ann_file='meta/test.txt',
        data_prefix='test',
        pipeline=cfg.test_pipeline)
    )

    cfg.train_dataloader = None
    cfg.train_cfg = None
    cfg.optim_wrapper = None
    cfg.param_scheduler = None

    # build the runner from config
    runner = Runner.from_cfg(cfg)
    if torch.cuda.is_available():
        os.environ['CUBLAS_WORKSPACE_CONFIG'] = ':16:8'

    # start testing
    print(model_path)
    runner.test()


if __name__ == '__main__':
    main()

#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