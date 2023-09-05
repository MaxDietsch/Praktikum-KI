# model settings
model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes = 3,
        mean=[141.46, 95.78, 85.52],
        std=[81.42, 61.04, 58.85],
        bgr_to_rgb=True
        ),
    backbone=dict(type='VisionTransformer', arch='b', patch_size=16),
    neck=None,
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=3,
        in_channels=3072,
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 1),
    ))
