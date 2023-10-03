# model settings
model = dict(
    type='MAE',
    data_preprocessor=dict(
        mean=[7.18, 4.85, 3.47],
        std=[34.02, 22.52, 16.46],
        bgr_to_rgb=True),
    backbone=dict(type='MAEViT', arch='s', img_size=(320, 320), patch_size=9, mask_ratio=0.75),
    neck=dict(
        type='MAEPretrainDecoder',
        num_patches = 1296,
        patch_size=9,
        in_chans=3,
        embed_dim=768,
        decoder_embed_dim=512,
        decoder_depth=8,
        decoder_num_heads=16,
        mlp_ratio=4.,
    ),
    head=dict(
        type='MAEPretrainHead',
        norm_pix=True,
        patch_size=9,
        loss=dict(type='MAEReconstructionLoss')),
    init_cfg=[
        dict(type='Xavier', distribution='uniform', layer='Linear'),
        dict(type='Constant', layer='LayerNorm', val=1.0, bias=0.0)
    ])
