# dataset settings
dataset_type = 'CustomDataset'
data_root = 'data_dir/kvasir'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=292),
    dict(type='RandomCrop', size=255),
    dict(type='RandomGrayscale', prob=0.66, keep_channels=True),
    dict(type='RandomPatchWithLabels'),
    dict(
        type='PackSelfSupInputs',
        pseudo_label_keys=['patch_box', 'patch_label', 'unpatched_img'],
        meta_keys=['img_path'])
]

train_dataloader = dict(
    batch_size=64,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='',
        data_prefix='',
        pipeline=train_pipeline))
