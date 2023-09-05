# optimizer wrapper
optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=1e-4)
optim_wrapper = dict(type='AmpOptimWrapper', loss_scale='dynamic')


# learning rate scheduler
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.0001,
        by_epoch=True,
        begin=0,
        end=10,
        convert_to_iter_based=True),
    dict(
        type='CosineAnnealingLR',
        T_max=260,
        by_epoch=True,
        begin=10,
        end=20,
        convert_to_iter_based=True)
]



# runtime settings
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=20)
