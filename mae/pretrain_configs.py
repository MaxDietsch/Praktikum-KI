_base_ = [
    './pretrain_model.py', 
    './pretrain_data.py',
    './pretrain_schedule.py',
    './runtime.py'
]

default_hooks = dict(logger=dict(type='LoggerHook', interval=10))
default_hooks = dict(checkpoint=dict(type='CheckpointHook', interval=1, max_keep_ckpts=3))

work_dir = './work_dirs/selfsup/vit_p16'

randomness = dict(seed=0, deterministic=True)
