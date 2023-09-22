model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes=3,
        mean=[22.58, 12.83, 9.29],
        std=[55.03, 34.93, 25.90],
        to_rgb=True,
    ),
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        out_indices=[4],  
        norm_cfg=dict(type='BN'),
        init_cfg=dict(type='Xavier')),
    #neck=dict(type='mmcls.GlobalAveragePooling'),
    neck=dict(
        type='RelativeLocNeck',
        in_channels=1024,
        out_channels=1024,
        with_avg_pool=True,
        init_cfg=dict(type='Xavier')),
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=2,
        in_channels=1024,
        init_cfg=dict(type='Xavier'),
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 1),
    ))