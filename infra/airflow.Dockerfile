FROM apache/airflow:2.9.3

USER root
RUN apt-get update && apt-get install -y \
    libgdal-dev libgeos-dev libproj-dev \
    && rm -rf /var/lib/apt/lists/*

USER airflow

ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-2.9.3/constraints-3.12.txt"

RUN pip install --no-cache-dir \
    "geopandas<0.15.0" "pandas<2.2.0" rapidfuzz sqlalchemy psycopg2-binary \
    camelot-py[cv] beautifulsoup4 requests openpyxl pyarrow \
    bcrypt geoalchemy2 \
    --constraint "${CONSTRAINT_URL}"