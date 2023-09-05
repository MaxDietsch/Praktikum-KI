_base_ = [
    './pretrain_model.py', 
    './pretrain_data.py',
    './pretrain_schedule.py',
    './runtime.py'
]


default_hooks = dict(logger=dict(type='LoggerHook', interval=10))

optimizer = dict(type='SGD', lr=0.2, momentum=0.9, weight_decay=1e-4)
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=optimizer,
    paramwise_cfg=dict(custom_keys={
        'neck': dict(decay_mult=5.0),
        'head': dict(decay_mult=5.0)
    }))

param_scheduler = [dict(type='MultiStepLR', by_epoch=True, milestones=[10, 15, 23])]

train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=30)

default_hooks = dict(checkpoint=dict(type='CheckpointHook', interval=1, max_keep_ckpts=3))

work_dir = './work_dirs/selfsup/resnet50'

randomness = dict(seed=0, deterministic=True)
