_base_ = [
    'model.py',
    'runtime.py']

dataset_type = 'Kvasir'
data_root = 'data_dir/kvasir/'
extract_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='mmcls.ResizeEdge', scale=256, edge='short', backend='pillow'),
    dict(type='mmcls.PackClsInputs'),
]
extract_dataloader = dict(
    batch_size=8,
    num_workers=4,
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        ann_file='meta/val.txt',
        data_prefix='val',
        pipeline=extract_pipeline),
    sampler=dict(type='DefaultSampler', shuffle=False),
)
