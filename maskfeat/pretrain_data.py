# dataset settings
dataset_type = 'Ld'
data_root = '../data_dir/LD'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(640, 640), interpolation='bicubic'),
     dict(type='BEiTMaskGenerator', input_size=14, num_masking_patches=78, min_num_patches=15),
    dict(type='PackSelfSupInputs', algorithm_keys=['mask'], meta_keys=['img_path'])]

train_dataloader = dict(
    batch_size=1,
    num_workers=6,
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
