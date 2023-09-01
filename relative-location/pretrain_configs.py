_base_ = [
    './pretrain_model.py', 
    './pretrain_data.py',
    './schedule.py',
    './runtime.py'
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
param_scheduler = [dict(type='MultiStepLR', by_epoch=True, milestones=[10, 15, 23])]

# runtime settings
# pre-train for 30 epochs
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=30)
# the max_keep_ckpts controls the max number of ckpt file in your work_dirs
# if it is 3, when CheckpointHook (in mmcv) saves the 4th ckpt
# it will remove the oldest one to keep the number of total ckpts as 3
default_hooks = dict(
    checkpoint=dict(type='CheckpointHook', interval=1, max_keep_ckpts=3))

work_dir = './work_dirs/selfsup/relative-loc_resnet50_8xb64-steplr-70e_in1k_colab'

# Output logs for every 10 iterations
default_hooks.logger.interval = 10
# Set the random seed and enable the deterministic option of cuDNN
# to keep the results' reproducible.
randomness = dict(seed=0, deterministic=True)
