# dataset settings
dataset_type = 'Sun'
data_root = '../data_dir/SUN/'

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(320, 320), interpolation='bicubic'),
    dict(type='RandomFlip', prob=0.5),
    dict(type='mmcls.PackClsInputs'),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='Resize', scale=(320, 320), interpolation='bicubic'),
    #dict(type='mmcls.ResizeEdge', scale=256, edge='short', backend='pillow'),
    dict(type='mmcls.PackClsInputs'),
]

train_dataloader = dict(
    batch_size=16,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/train1000.txt',
        data_prefix='train1000',
        pipeline=train_pipeline)
)


val_dataloader = dict(
    batch_size=16,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/val.txt',
        data_prefix='val',
        pipeline=test_pipeline)
)


val_evaluator = dict(type='mmcls.Accuracy', topk=(1, 1))

val_dataloader = None
val_evaluator = None

test_dataloader = val_dataloader
test_evaluator = val_evaluator