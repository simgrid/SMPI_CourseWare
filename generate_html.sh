#!/bin/bash

( set -x ; /bin/rm -rf ./gh-pages )
( set -x ; mkdir ./gh-pages )
( set -x ; cd ./gh-pages; git clone -b gh-pages https://github.com/simgrid/SMPI_CourseWare.git )
( set -x ; jekyll build --source ./content --destination ./gh-pages)
( set -x; cd gh-pages; git pull; git add --all . ; git commit -a -m "updated content"; git push origin gh-pages)
