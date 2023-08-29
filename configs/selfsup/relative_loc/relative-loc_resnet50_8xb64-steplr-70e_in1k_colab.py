_base_ = [
    '../_base_/models/relative-loc.py',
    '../_base_/datasets/imagenet_relative-loc.py',
    '../_base_/schedules/sgd_steplr-200e_in1k.py',
    '../_base_/default_runtime.py',
]

default_hooks = dict(logger=dict(type='LoggerHook', interval=10))

# optimizer wrapper
optimizer = dict(type='SGD', lr=0.2, momentum=0.9, weight_decay=1e-4)
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=optimizer,
    paramwise_cfg=dict(custom_keys={
        'neck': dict(decay_mult=5.0),
        'head': dict(decay_mult=5.0)
    }))

# learning rate scheduler
param_scheduler = [dict(type='MultiStepLR', by_epoch=True, milestones=[1, 2])]

# runtime settings
# pre-train for 70 epochs
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=70)
# the max_keep_ckpts controls the max number of ckpt file in your work_dirs
# if it is 3, when CheckpointHook (in mmcv) saves the 4th ckpt
# it will remove the oldest one to keep the number of total ckpts as 3
default_hooks = dict(
    checkpoint=dict(type='CheckpointHook', interval=1, max_keep_ckpts=3))
