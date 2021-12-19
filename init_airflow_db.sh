airflow db reset

# airflow users create \
#     --username admin \
#     --firstname Mobasshir \
#     --lastname Bhuiyan \
#     --role Admin \
#     --email mobasshirbhuiyan.shagor@gmail.com

airflow users  create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
airflow users  create --role Admin --username airflow --email airflow --firstname airflow --lastname airflow --password airflow