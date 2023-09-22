# model settings
model = dict(
    type='SimSiam',
    data_preprocessor=dict(
        mean=[7.18, 4.85, 3.47],
        std=[34.02, 22.52, 16.46],
        bgr_to_rgb=True),
    backbone=dict(
        type='ResNet',
        depth=50,
        in_channels=3,
        out_indices=[4],  # 0: conv-1, x: stage-x
        norm_cfg=dict(type='SyncBN'),
        zero_init_residual=True),
    neck=dict(
        type='NonLinearNeck',
        in_channels=2048,
        hid_channels=2048,
        out_channels=2048,
        num_layers=3,
        with_last_bn_affine=False,
        with_avg_pool=True),
    head=dict(
        type='LatentPredictHead',
        loss=dict(type='CosineSimilarityLoss'),
        predictor=dict(
            type='NonLinearNeck',
            in_channels=2048,
            hid_channels=512,
            out_channels=2048,
            with_avg_pool=False,
            with_last_bn=False,
            with_last_bias=True)),
)
