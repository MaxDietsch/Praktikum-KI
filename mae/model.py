# model settings
model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes = 3,
        mean=[141.46, 95.78, 85.52],
        std=[81.42, 61.04, 58.85],
        to_rgb=True
        ),
    backbone=dict(type='mmcls.VisionTransformer', arch='s', patch_size=16),
    #neck=dict(type='LinearNeck', in_channels = 2304, out_channels = 500),
    #neck=dict(type='mmcls.GlobalAveragePooling'),
    head=dict(
        type='MultiLabelLinearClsHead',
        num_classes=3,
        in_channels=768,
        loss=dict(
            type='CrossEntropyLoss',
            use_sigmoid=True,
            reduction='mean',
            loss_weight=1.0),
    ))

"""
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=3,
        in_channels=500,
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 1),
    ))"""
