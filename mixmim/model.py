model = dict(
    type='MixMIM',
    data_preprocessor=dict(
        mean=[22.58, 12.83, 9.29],
        std=[55.03, 34.93, 25.90],
        bgr_to_rgb=True),
    backbone=dict(
        type='MixMIMTransformerPretrain',
        arch='b',
        drop_rate=0.0,
        drop_path_rate=0.0, 
        init_cfg=dict(type='Xavier'),
    ),
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=2,
        in_channels=128,
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        init_cfg = dict(type = 'Xavier'),
        topk=(1, 1)
        ))
