# optimizer wrapper
optimizer = dict(
    type='AdamW', lr=1.5e-4 * 4096 / 256, betas=(0.9, 0.95), weight_decay=0.05)
optim_wrapper = dict(
    type='OptimWrapper',
    optimizer=optimizer,
    paramwise_cfg=dict(
        custom_keys={
            'ln': dict(decay_mult=0.0),
            'bias': dict(decay_mult=0.0),
            'pos_embed': dict(decay_mult=0.),
            'mask_token': dict(decay_mult=0.),
            'cls_token': dict(decay_mult=0.)
        }))



# learning rate scheduler
param_scheduler = [
    dict(
        type='LinearLR',
        start_factor=0.0001,
        by_epoch=True,
        begin=0,
        end=20,
        convert_to_iter_based=True),
    dict(
        type='CosineAnnealingLR',
        T_max=260,
        by_epoch=True,
        begin=20,
        end=50,
        convert_to_iter_based=True)
]



# runtime settings
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=50)
