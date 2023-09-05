model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes=3,
        mean=[123.675, 116.28, 103.53],
        std=[58.395, 57.12, 57.375],
        to_rgb=True,
    ),
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        num_stages=4,
        norm_cfg=dict(type='BN'),
        frozen_stages=-1),
    neck=dict(type='mmcls.GlobalAveragePooling'),
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=3,
        in_channels=2048,
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 1),
    ))
