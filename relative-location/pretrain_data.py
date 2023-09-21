# dataset settings
dataset_type = 'mmcls.CustomDataset'
data_root = '../data_dir/kvasir/'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(320, 320), interpolation='bicubic'),
    dict(type='RandomPatchWithLabels'),
    dict(type='PackSelfSupInputs', meta_keys=['img_path'])]

train_dataloader = dict(
    batch_size=32,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/train.txt',
        data_prefix=dict(img_path='train/'),
        pipeline=train_pipeline))
