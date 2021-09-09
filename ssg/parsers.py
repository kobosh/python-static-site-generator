from typing import List
from pathlib import Path
from shutil import copy2

class Parser:

    extensions:List[str]=[]
    def valid_extension(self,extension):
        if extension in self.extensions:
            return True
        return False
    def parse(self,path:Path,source:Path,dest:Path):
         raise NotImplementedError
    def read(self, path):
        with  open(path) as file:
            bts=file.read()
        return bts
    def write(self,path,dest,content,ext=".html"):
        if self.valid_extension(ext):
            extn=ext
        destination=self.parse(path,None,dest)
        full_path=destination/path.with_suffix(extn).name
        with open(full_path) as file:
            file.write(content)
    def copy(self,path,source,dest):
        relpath=dest/path.relative_to(source)
        copy2(path,relpath)
