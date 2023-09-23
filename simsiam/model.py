# model settings
model = dict(
    type='mmcls.ImageClassifier',
    data_preprocessor=dict(
        num_classes = 3, 
        mean=[22.58, 12.83, 9.29],
        std=[55.03, 34.93, 25.90],
        to_rgb=True),
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        out_indices=[4],  # 0: conv-1, x: stage-x
        norm_cfg=dict(type='BN'),
        zero_init_residual=True,
        init_cfg = dict(type='Xavier')),
    neck=dict(
        type='NonLinearNeck',
        in_channels=2048,
        hid_channels=2048,
        out_channels=1024,
        num_layers=3,
        with_last_bn_affine=False,
        with_avg_pool=True,
        init_cfg = dict(type='Xavier')),
    head=dict(
        type='mmcls.LinearClsHead',
        num_classes=2,
        in_channels=1024,
        init_cfg=dict(type='Xavier'),
        loss=dict(type='mmcls.CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 1),
    )
)
