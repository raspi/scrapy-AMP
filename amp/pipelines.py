import os
from pathlib import Path
from shutil import move
from tempfile import NamedTemporaryFile

import scrapy

from amp.items import *


def validatechars(s: str) -> str:
    """
    Filesystem friendly
    :param s:
    :return:
    """

    s = s.replace(r"\\", "_")
    s = s.replace(r"/", "_")
    s = s.replace(r"?", "_")
    return s


class AmpPipeline:
    def process_item(self, item: Item, spider: scrapy.Spider):

        if not isinstance(item, Item):
            spider.log("Invalid item type")
            return

        filename = None
        basepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'items'))

        if isinstance(item, Tune):
            basepath = os.path.join(basepath, item.artistId)

        if not os.path.isdir(basepath):
            Path(basepath).mkdir(parents=True, exist_ok=True)

        if isinstance(item, Tune):
            nitem = item
            # Remove filesystem unfriendly characters
            nitem.artist = validatechars(nitem.artist)
            nitem.title = validatechars(nitem.title)
            filename = f"{nitem.artist} - {nitem.title}.{nitem.format}"

        if filename is None:
            raise ValueError("No filename")

        # Save to temporary file
        tmpf = NamedTemporaryFile("wb", prefix="amp-", suffix=f".bin", delete=False)
        with tmpf as f:
            f.write(item.data)
            f.flush()
            spider.logger.info(f"saved as {f.name}")

        # Rename and move the temporary file to actual file
        newpath = move(tmpf.name, os.path.join(basepath, filename))
        spider.logger.info(f"renamed {tmpf.name} to {newpath}")
