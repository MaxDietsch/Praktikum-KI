# dataset settings
dataset_type = 'Ld'
data_root = '../data_dir/LD'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(640, 640), interpolation='bicubic'),
    dict(type='PackSelfSupInputs', meta_keys=['img_path'])]

train_dataloader = dict(
    batch_size=16,
    num_workers=32,
    persistent_workers=True,
    pin_memory=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/train.txt',
        data_prefix=dict(img_path='train/'),
        pipeline=train_pipeline))
