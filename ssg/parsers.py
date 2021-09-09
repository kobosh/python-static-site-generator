from typing import List
from pathlib import pathlib

class Parser:

    extensions:List[str]=[]
    def valid_extension(self,extension):
        if extension is in self.extensions:
            return True
        return False
    def parse(self,path:Path,source:Path,dest:Path):
         raise NotImplementedError
    def read(self path):
        with  open(path) as f
        bytes=f.read()
        return bytes
    def write(self,path,dest,content,ext=".html"):
        if valid_extension(ext):
            extn=ext
        destination=parse(path,source=None,dest)
        full_path=destination/path.with_suffix(ext).name
