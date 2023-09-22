model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes=3,
        mean=[7.18, 4.85, 3.47],
        std=[34.02, 22.52, 16.46],
        to_rgb=True,
    ),
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        out_indices=[4],  
        norm_cfg=dict(type='BN')),
    #neck=dict(type='mmcls.GlobalAveragePooling'),
    neck=dict(
        type='RelativeLocNeck',
        in_channels=4096,
        out_channels=1024,
        with_avg_pool=True),
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=2,
        in_channels=1024,
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 1),
    ))