# taken from https://github.com/jupyter/docker-stacks/blob/master/pyspark-notebook/Dockerfile
FROM jupyter/pyspark-notebook:spark-3.4.1

LABEL authors="AdrianJ"

ARG DELTA_SPARK_VERSION="2.4.0"
RUN pip install --quiet --no-cache-dir delta-spark==${DELTA_SPARK_VERSION} && \
     fix-permissions "${HOME}" && \
     fix-permissions "${CONDA_DIR}"

ARG PYTEST_VERSION="7.1.2" 
RUN pip install --quiet --no-cache-dir pytest==${PYTEST_VERSION} && \
     fix-permissions "${HOME}" && \
     fix-permissions "${CONDA_DIR}"

USER root

#set spark default config for delta and spark-cassandra connector
RUN echo 'spark.sql.extensions io.delta.sql.DeltaSparkSessionExtension' >> "${SPARK_HOME}/conf/spark-defaults.conf" && \
    echo 'spark.sql.catalog.spark_catalog org.apache.spark.sql.delta.catalog.DeltaCatalog' >> "${SPARK_HOME}/conf/spark-defaults.conf"

USER ${NB_UID}