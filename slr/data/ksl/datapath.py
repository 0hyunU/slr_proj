from collections import defaultdict
from dataclasses import dataclass, field
from pickle import DICT
import numpy as np
import os,sys
from pathlib import Path

# sys.path.append(Path(".."))
# from ...static.const import *
# from BodyPoint import BodyPoint
from pathlib import Path
from typing import List, Dict
from slr.static.const import ROOT


@dataclass
class DataPath():
    _users_dir: List[Path] = field(default_factory=list)
    class_dict: Dict[str,List[Path]] = field(default_factory=lambda:defaultdict(list))

    def __init__(self, class_limit = 1e10):
        self._users_dir = [next(i.iterdir()) for i in ROOT.iterdir() if i.is_dir()]
        self.cls_limit = class_limit
        self.class_dict = self._set_class_dir()
        # for k,v in self.class_dir.items():
        #     print(k,v)

    def _set_class_dir(self):
        class_dict = defaultdict(list)

        for p in self._users_dir:
            for i in p.iterdir():
                if self._cls_num(i) > self.cls_limit: break
                class_dict[self._cls_name(i)].append(i)

        return class_dict

    def _cls_num(self, i:Path) -> str:
        return int(i.name[11:15])
    
    
    def _cls_name(self, i:Path) -> str:
        return i.name[:15]

    @property
    def data(self):
        x,y = [],[]
        for k,v in self.class_dict.items():
            x.extend(v)
            y.extend([k]*len(v))
        
        return x,y

def main():
    print(DataPath(class_limit=10))

# main()

# if __name__ == '__main__':
#     print(DataPath(class_limit=10))
