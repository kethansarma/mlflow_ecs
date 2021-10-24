FROM continuumio/miniconda:latest

RUN conda install python=3.6 \
    && pip install mlflow \
    && pip install numpy\
    && pip install scipy \
    && pip install pandas \
    && pip install scikit-learn
# RUN apk add git
COPY MLproject /tmp
# COPY trainecs.py /tmp
COPY setup_experiment.py /tmp
COPY wine-quality.csv /tmp
COPY train.py /tmp
CMD  cd /tmp && python setup_experiment.py exp1 && mlflow run . --no-conda --experiment-name exp1
