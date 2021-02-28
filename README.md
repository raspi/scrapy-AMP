# scrapy-AMP
Crawler for [Amiga Music Preservation](https://amp.dascene.net/) (AMP) site.


## Download artist X tunes:

    scrapy crawl artist -a id=2313

Downloaded tunes are saved to `items` directory:

```
% find items -type f
items/2313/Dune - novaliquid.s3m
items/2313/Dune - astral ian breakside.fst
items/2313/Dune - the determination.mod
items/2313/Dune - mindless design.mod
items/2313/Dune & Sulphur - deskTop sektoriLe(kplremix.s3m
items/2313/Dune - carnaq.s3m
items/2313/Dune - World of Saracens.s3m
items/2313/Dune - bathroom tests.xm
items/2313/Dune - syoa.s3m
... etc ...
items/2313/Dune - dance xtc.mod
items/2313/Dune - astral ian breakside.s3m
items/2313/Dune - Light.s3m
items/2313/Dune - The Sea Love of Robot.s3m
```
