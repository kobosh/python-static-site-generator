from ssg.site import Parser
class ResourceParser(Parser):
    extensions=[".jpg", ".png", ".gif", ".css",".html"]
    def parse(self,path:Path,source:Path,dest:Path):
        copy(path,source,dest)
