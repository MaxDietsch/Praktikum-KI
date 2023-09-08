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
    backbone=dict(
        depth=50,
        in_channels=3,
        norm_cfg=dict(type='BN'),
        out_indices=[
            4,
        ],
        type='ResNet'),
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
        ],
        type='mmselfsup.RelativeLocDataPreprocessor'),
    head=dict(
        in_channels=4096,
        init_cfg=[
            dict(layer='Linear', std=0.005, type='Normal'),
            dict(layer=[
                '_BatchNorm',
                'GroupNorm',
            ], type='Constant', val=1),
        ],
        loss=dict(type='mmcls.CrossEntropyLoss'),
        num_classes=8,
        type='ClsHead',
        with_avg_pool=False),
    neck=dict(
        in_channels=2048,
        out_channels=4096,
        type='RelativeLocNeck',
        with_avg_pool=True),
    type='RelativeLoc')
optim_wrapper = dict(
    optimizer=dict(lr=0.1, momentum=0.9, type='SGD', weight_decay=0.0001),
    paramwise_cfg=dict(
        custom_keys=dict(head=dict(decay_mult=5.0), neck=dict(
            decay_mult=5.0))),
    type='OptimWrapper')
optimizer = dict(lr=0.1, momentum=0.9, type='SGD', weight_decay=0.0001)
param_scheduler = [
    dict(
        by_epoch=True,
        gamma=0.1,
        milestones=[
            15,
            25,
            35,
        ],
        type='MultiStepLR'),
]
randomness = dict(deterministic=True, seed=0)
resume = False
train_cfg = dict(max_epochs=50, type='EpochBasedTrainLoop')
train_dataloader = dict(
    batch_size=64,
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        data_prefix='',
        data_root='../data_dir/kvasir/',
        pipeline=[
            dict(type='LoadImageFromFile'),
            dict(scale=292, type='Resize'),
            dict(size=255, type='RandomCrop'),
            dict(keep_channels=True, prob=0.66, type='RandomGrayscale'),
            dict(type='RandomPatchWithLabels'),
            dict(
                meta_keys=[
                    'img_path',
                ],
                pseudo_label_keys=[
                    'patch_box',
                    'patch_label',
                    'unpatched_img',
                ],
                type='PackSelfSupInputs'),
        ],
        type='mmcls.CustomDataset'),
    num_workers=4,
    persistent_workers=True,
    sampler=dict(shuffle=True, type='DefaultSampler'))
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(scale=292, type='Resize'),
    dict(size=255, type='RandomCrop'),
    dict(keep_channels=True, prob=0.66, type='RandomGrayscale'),
    dict(type='RandomPatchWithLabels'),
    dict(
        meta_keys=[
            'img_path',
        ],
        pseudo_label_keys=[
            'patch_box',
            'patch_label',
            'unpatched_img',
        ],
        type='PackSelfSupInputs'),
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
work_dir = 'relative-location/results_pretrain'
