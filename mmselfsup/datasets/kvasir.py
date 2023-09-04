from typing import List, Optional, Union
from mmcls.datasets import CustomDataset
from mmselfsup.registry import DATASETS
from mmengine.fileio import join_path

@DATASETS.register_module()
class Kvasir(CustomDataset):

    IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif')

    def __init__(self,
                 ann_file: str = '',
                 metainfo: Optional[dict] = None,
                 data_root: str = '',
                 data_prefix: Union[str, dict] = '',
                 **kwargs) -> None:
        kwargs = {'extensions': self.IMG_EXTENSIONS, **kwargs}
        super().__init__(
            ann_file=ann_file,
            metainfo=metainfo,
            data_root=data_root,
            data_prefix=data_prefix,
            **kwargs)

    def load_data_list(self) -> List[dict]:
        assert self.ann_file != ''
        with open(self.ann_file, 'r') as f:
            self.samples = f.readlines()
        self.has_labels = len(self.samples[0].split()) == 2

        data_list = []
        for sample in self.samples:
            info = {'img_prefix': self.img_prefix}
            sample = sample.split()
            info['img_path'] = join_path(self.img_prefix, sample[0])
            info['img_info'] = {'filename': sample[0]}
            labels = sample[1] if self.has_labels else -1
            info['gt_label'] = np.array(labels, dtype=np.int64)
            data_list.append(info)
        return data_list

