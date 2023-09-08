import argparse
import os
import os.path as osp

from mmengine.config import Config, DictAction
from mmengine.runner import Runner


def parse_args():
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('work_dir', help='the dir to contain config')
    parser.add_argument('--job', default='pretrain', help='specify if pretrain job or train job should be done')
    parser.add_argument('--save_dir', help='the dir to save logs and models')
    parser.add_argument(
        '--resume',
        nargs='?',
        type=str,
        const='auto',
        help='If specify checkpint path, resume from it, while if not '
        'specify, try to auto resume from the latest checkpoint '
        'in the work directory.')
    parser.add_argument(
        '--amp',
        action='store_true',
        help='enable automatic-mixed-precision training')
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        help='override some settings in the used config, the key-value pair '
        'in xxx=yyy format will be merged into config file. If the value to '
        'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
        'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
        'Note that the quotation marks are necessary and that no white space '
        'is allowed.')
    parser.add_argument(
        '--load_bb',
        nargs='?',
        type=str,
        help='specify checkpoint path, from which weights for the backbone should be loaded')
    parser.add_argument(
        '--launcher',
        choices=['none', 'pytorch', 'slurm', 'mpi'],
        default='none',
        help='job launcher')
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

    # load config
    if args.job == 'pretrain':
        cfg_path = osp.join(args.work_dir, args.job + "_configs.py")
    else: 
        cfg_path = osp.join(args.work_dir, "configs.py")

    cfg = Config.fromfile(cfg_path)
    if args.cfg_options is not None:
        cfg.merge_from_dict(args.cfg_options)

    # work_dir is determined in this priority: CLI > segment in file > filename
    if args.save_dir is not None:
        cfg.work_dir = osp.join(args.work_dir, args.save_dir)
    elif cfg.get('save_dir', None) is None:
        cfg.work_dir = osp.join(args.work_dir, "results_" + args.job)

    # resume training from another checkpoint
    if args.resume == 'auto':
        cfg.resume = True
        cfg.load_from = None
    elif args.resume is not None:
        cfg.resume = True
        cfg.load_from = args.resume

    # load backbone weights
    if args.load_bb is not None:
        cfg.model.backbone.init_cfg = dict(type='Pretrained', checkpoint=args.load_bb)

    # enable automatic-mixed-precision training
    if args.amp is True:
        optim_wrapper = cfg.optim_wrapper.get('type', 'OptimWrapper')
        assert optim_wrapper in ['OptimWrapper', 'AmpOptimWrapper'], \
            '`--amp` is not supported custom optimizer wrapper type ' \
            f'`{optim_wrapper}.'
        cfg.optim_wrapper.type = 'AmpOptimWrapper'
        cfg.optim_wrapper.setdefault('loss_scale', 'dynamic')

    # build the runner from config
    runner = Runner.from_cfg(cfg)
    # start training
    #runner.train()


if __name__ == '__main__':
    main()
