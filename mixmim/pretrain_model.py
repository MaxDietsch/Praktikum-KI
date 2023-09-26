model = dict(
    type='MixMIM',
    data_preprocessor=dict(
        mean=[7.18, 4.85, 3.47],
        std=[34.02, 22.52, 16.46],
        bgr_to_rgb=True),
    backbone=dict(
        type='MixMIMTransformerPretrain',
        arch='B',
        drop_rate=0.0,
        drop_path_rate=0.0, 
    ),
    neck=dict(
        type='MixMIMPretrainDecoder',
        num_patches=49,
        encoder_stride=32,
        embed_dim=1024,
        decoder_embed_dim=512,
        decoder_depth=8,
        decoder_num_heads=16),
    head=dict(
        type='MixMIMPretrainHead',
        norm_pix=True,
        loss=dict(type='PixelReconstructionLoss', criterion='L2')))
