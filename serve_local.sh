#!/bin/bash
#
# This script simply serves the site locally


( set -x ; jekyll serve --source . --destination /tmp/gh-pages)
( set -x ; /bin/rm -rf /tmp/gh-pages )
