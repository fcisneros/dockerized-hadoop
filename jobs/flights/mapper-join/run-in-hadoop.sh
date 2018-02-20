#!/usr/bin/env bash

WORKDIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd ${WORKDIR}

: "${INPUT:?Need to set INPUT_1 non-empty}"
: "${OUTPUT:?Need to set OUTPUT non-empty}"

echo "workdir = $(pwd)"
echo "content = $(ls -ltrha)"

hdfs dfs -rm -r ${OUTPUT}
hadoop jar ${HADOOP_PREFIX}/share/hadoop/tools/lib/hadoop-*streaming*.jar \
    -Dmapred.reduce.tasks=1 \
    -files mapper.py,reducer.py,airlines.csv \
    -mapper mapper.py \
    -reducer reducer.py \
    -input ${INPUT} -output ${OUTPUT}