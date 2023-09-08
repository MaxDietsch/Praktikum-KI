data_root = '../data_dir/kvasir/'
dataset_type = 'mmcls.CustomDataset'
default_hooks = dict(
    checkpoint=dict(interval=1, max_keep_ckpts=3, type='CheckpointHook'),
    logger=dict(interval=1200, type='LoggerHook'),
    param_scheduler=dict(type='ParamSchedulerHook'),
    runtime_info=dict(type='RuntimeInfoHook'),
    sampler_seed=dict(type='DistSamplerSeedHook'),
    timer=dict(type='IterTimerHook'))
default_scope = 'mmselfsup'
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
load_from = None
log_level = 'INFO'
log_processor = dict(
    custom_cfg=[
        dict(data_src='', method='mean', window_size='global'),
    ],
    window_size=10)
model = dict(
    backbone=dict(arch='s', mask_ratio=0.75, patch_size=16, type='MAEViT'),
    data_preprocessor=dict(
        bgr_to_rgb=True,
        mean=[
            141.46,
            95.78,
            85.52,
        ],
        std=[
            81.42,
            61.04,
            58.85,
        ]),
    head=dict(
        loss=dict(type='MAEReconstructionLoss'),
        norm_pix=True,
        patch_size=16,
        type='MAEPretrainHead'),
    init_cfg=[
        dict(distribution='uniform', layer='Linear', type='Xavier'),
        dict(bias=0.0, layer='LayerNorm', type='Constant', val=1.0),
    ],
    neck=dict(
        decoder_depth=8,
        decoder_embed_dim=512,
        decoder_num_heads=16,
        embed_dim=768,
        in_chans=3,
        mlp_ratio=4.0,
        patch_size=16,
        type='MAEPretrainDecoder'),
    type='MAE')
optim_wrapper = dict(
    optimizer=dict(
        betas=(
            0.9,
            0.95,
        ), lr=0.0024, type='AdamW', weight_decay=0.05),
    paramwise_cfg=dict(
        custom_keys=dict(
            bias=dict(decay_mult=0.0),
            cls_token=dict(decay_mult=0.0),
            ln=dict(decay_mult=0.0),
            mask_token=dict(decay_mult=0.0),
            pos_embed=dict(decay_mult=0.0))),
    type='OptimWrapper')
optimizer = dict(
    betas=(
        0.9,
        0.95,
    ), lr=0.0024, type='AdamW', weight_decay=0.05)
param_scheduler = [
    dict(
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=20,
        start_factor=0.0001,
        type='LinearLR'),
    dict(
        T_max=260,
        begin=20,
        by_epoch=True,
        convert_to_iter_based=True,
        end=50,
        type='CosineAnnealingLR'),
]
randomness = dict(deterministic=True, seed=0)
resume = False
train_cfg = dict(max_epochs=50, type='EpochBasedTrainLoop')
train_dataloader = dict(
    batch_size=64,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        ann_file='meta/train.txt',
        data_prefix=dict(img_path='train/'),
        data_root='../data_dir/kvasir/',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(
                backend='pillow',
                interpolation='bicubic',
                scale=(
                    0.2,
                    1.0,
                ),
                size=224,
                type='RandomResizedCrop'),
            dict(prob=0.5, type='RandomFlip'),
            dict(meta_keys=[
                'img_path',
            ], type='PackSelfSupInputs'),
        ],
        type='mmcls.CustomDataset'),
    num_workers=8,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        backend='pillow',
        interpolation='bicubic',
        scale=(
            0.2,
            1.0,
        ),
        size=224,
        type='RandomResizedCrop'),
    dict(prob=0.5, type='RandomFlip'),
    dict(meta_keys=[
        'img_path',
    ], type='PackSelfSupInputs'),
]
vis_backends = [
    dict(type='LocalVisBackend'),
]
visualizer = dict(
    name='visualizer',
    type='SelfSupVisualizer',
    vis_backends=[
        dict(type='LocalVisBackend'),
    ])
work_dir = 'mae/results_pretrain'
