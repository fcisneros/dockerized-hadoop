#!/usr/bin/env bash

WORKDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${WORKDIR}

: "${INPUT_1:?Need to set INPUT_1 non-empty}"
: "${INPUT_2:?Need to set INPUT_1 non-empty}"
: "${OUTPUT:?Need to set OUTPUT non-empty}"


hdfs dfs -rm -r ${OUTPUT}
hadoop jar ${HADOOP_PREFIX}/share/hadoop/tools/lib/hadoop-*streaming*.jar \
    -Dmapred.reduce.tasks=1 -Dmapred.map.tasks=1 \
    -file mapper.py -mapper mapper.py \
    -file reducer.py -reducer reducer.py \
    -input ${INPUT_1} -input ${INPUT_2} -output ${OUTPUT}