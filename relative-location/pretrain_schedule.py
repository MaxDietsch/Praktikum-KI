# optimizer wrapper
optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=1e-4)
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=optimizer,
    paramwise_cfg=dict(custom_keys={
        'neck': dict(decay_mult=5.0),
        'head': dict(decay_mult=5.0)
    }))


# learning rate scheduler
param_scheduler = [dict(type='MultiStepLR', by_epoch=True, milestones=[15, 25, 35], gamma = 0.1)]


# runtime settings
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=50)
