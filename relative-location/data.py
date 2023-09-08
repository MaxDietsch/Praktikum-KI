# dataset settings
dataset_type = 'Kvasir'
data_root = 'data_dir/kvasir/'

"""
data_preprocessor = dict(
    num_classes=3,
    # RGB format normalization parameters
    mean=[141.46, 95.78, 85.52],
    std=[81.42, 61.04, 58.85],
    # convert image from BGR to RGB
    to_rgb=True,
)
"""

train_pipeline = [
    dict(type='LoadImageFromFile'),
    #dict(type='RandomResizedCrop', scale=224, backend='pillow'),
    dict(type='RandomFlip', prob=0.5, direction='horizontal'),
    dict(type='mmcls.PackClsInputs'),
]

test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='mmcls.ResizeEdge', scale=256, edge='short', backend='pillow'),
    #dict(type='CenterCrop', crop_size=224),
    dict(type='mmcls.PackClsInputs'),
]

train_dataloader = dict(
    batch_size=2,
    num_workers=4,
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/train.txt',
        data_prefix='train',
        pipeline=train_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=True),
    collate_fn=dict(type='default_collate'),
    persistent_workers=True,
    pin_memory=True,
)

val_dataloader = dict(
    batch_size=2,
    num_workers=4,
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/val.txt',
        data_prefix='val',
        pipeline=test_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
    persistent_workers=True,
)
val_evaluator = dict(type='mmcls.Accuracy', topk=(1, 1))

# If you want standard test, please manually configure the test dataset
test_dataloader = val_dataloader
test_evaluator = val_evaluator
