from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.sensors.time_delta import TimeDeltaSensor
from datetime import timedelta
 
with DAG(
    dag_id="dag_formation",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["guide"],
) as dag:
    hello = BashOperator(
        task_id="hello",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date"
    )
    
    hello2 = BashOperator(
        task_id="hello2",
        bash_command="echo 'Hello 2'"
    )
    hello3= BashOperator(
        task_id="hello3",
        bash_command="echo 'Hello 3'"
    )
    
    wait = TimeDeltaSensor(
    task_id="attendre_10s",
    delta=timedelta(seconds=10),
    mode="reschedule"  # libère le slot pendant l'attente
)
    
    hello >> wait >> [hello2, hello3]