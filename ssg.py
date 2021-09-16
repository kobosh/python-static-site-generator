import typer
from ssg.site import Site
import ssg.parsers
def main(source="content", dest="dist"):
    config={"parsers":[ssg.parsers.ResourceParser(),ssg.parsers.MarkdownParser(),ssg.parsers.RestructuredTextParser()] ,   "source": source,    "dest":dest  }
    Site(**config).build()

typer.run(main)
