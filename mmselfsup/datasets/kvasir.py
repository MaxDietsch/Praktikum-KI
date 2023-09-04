from typing import List, Optional, Union
from mmcls.datasets import CustomDataset
from mmselfsup.registry import DATASETS
from mmcls.datasets import BaseDataset
from PIL import Image
import torchvision.transforms as transforms

@DATASETS.register_module()
class Kvasir(BaseDataset):

    IMG_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.ppm', '.bmp', '.pgm', '.tif')

    def __init__(self,
                 ann_file: str = '',
                 metainfo: Optional[dict] = None,
                 data_root: str = '',
                 data_prefix: Union[str, dict] = '',
                 **kwargs) -> None:
        #kwargs = {'extensions': self.IMG_EXTENSIONS, **kwargs}
        super().__init__(
            ann_file=ann_file,
            metainfo=metainfo,
            data_root=data_root,
            data_prefix=data_prefix)
            #**kwargs)

    def load_data_list(self) -> List[dict]:
        assert isinstance(self.ann_file, str)
        data_list = []

        transform = transforms.Compose([transforms.ToTensor()])

        with open(self.ann_file) as f:
            samples = [x.strip().split(' ') for x in f.readlines()]
            for filename, gt_label in samples:
                #img_path = add_prefix(filename, self.img_prefix)
                img_path = self.img_prefix + "/" + filename
                info = {'img_path': img_path, 'gt_label': int(gt_label)}

                img = Image.open(img_path)
                inputs = transform(img)
                info = {'inputs': inputs, 'gt_label': int(gt_label)}

                data_list.append(info)
        print(data_list)
        return data_list

