#!/usr/bin/env bash

WORKDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${WORKDIR}

: "${INPUT:?Need to set INPUT non-empty}"
: "${OUTPUT:?Need to set OUTPUT non-empty}"


hdfs dfs -rm -r ${OUTPUT}
hadoop jar ${HADOOP_PREFIX}/share/hadoop/tools/lib/hadoop-*streaming*.jar \
    -file mapper.py -mapper mapper.py \
    -file reducer.py -reducer reducer.py \
    -input ${INPUT} -output ${OUTPUT}