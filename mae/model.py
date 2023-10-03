# model settings
model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes = 3,
        mean=[134.96, 87.27, 71.29],
        std=[86.63, 60.93, 58.15],
        to_rgb=True
        ),
    backbone=dict(
        type='mmcls.LinearVisionTransformer', 
        img_size = 320,
        arch='b', 
        patch_size=10, 
        #frozen_stages = 8, 
        init_cfg = dict(type='Xavier')
        ),
    #neck=dict(type='mmcls.GlobalAveragePooling'),
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=6,
        in_channels=768,
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        init_cfg = dict(type = 'Xavier'),
        topk=(1, 1)
        )
    )