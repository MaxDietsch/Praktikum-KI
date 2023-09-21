# model settings
model = dict(
    type='RelativeLoc',
    data_preprocessor=dict(
        type='mmselfsup.RelativeLocDataPreprocessor',
        mean=[141.46, 95.78, 85.52],
        std=[81.42, 61.04, 58.85],
        bgr_to_rgb=True),
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        out_indices=[4],  
        norm_cfg=dict(type='BN')),
        frozen_stages = -1, 
    neck=dict(
        type='RelativeLocNeck',
        in_channels=2048,
        out_channels=4096,
        with_avg_pool=True),
    head=dict(
        type='ClsHead',
        loss=dict(type='mmcls.CrossEntropyLoss'),
        with_avg_pool=False,
        in_channels=4096,
        num_classes=8,
        init_cfg=[
            dict(type='Normal', std=0.005, layer='Linear'),
            dict(type='Constant', val=1, layer=['_BatchNorm', 'GroupNorm'])
        ]))
