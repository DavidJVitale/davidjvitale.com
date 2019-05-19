!#/bin/bash

for f in *.html; do
    mv -- "$f" "${f%.txt}.md"
done
