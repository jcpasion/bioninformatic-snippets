#!/bin/bash
 
#move empty files in directory to another directory 

dir=$(echo /path/to/dir)
empty=$(find ${dir} -empty)
 
echo $empty
 
for i in $empty; do
    echo $i
    mv ${dir}/${i} /path/to/empty_dir
done
