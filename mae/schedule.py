
# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
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

param_scheduler = [
    dict(type='MultiStepLR', by_epoch=True, milestones=[7, 15], gamma=0.1)
]

# runtime settings
train_cfg = dict(type='EpochBasedTrainLoop', max_epochs=20)
#val_cfg = dict()
#test_cfg = dict()

