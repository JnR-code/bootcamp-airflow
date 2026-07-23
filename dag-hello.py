from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.trigger_rule import TriggerRule
 
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
        bash_command="echo 'Hello 2 - simulation erreur'; exit 1"  # force l'échec
    )

    hello3 = BashOperator(
        task_id="hello3",
        bash_command="echo 'Hello 3'",
        trigger_rule=TriggerRule.ALL_SUCCESS  # s'exécute seulement si hello a réussi (c'est le défaut, explicite ici pour la clarté)
    )

    hello4 = BashOperator(
        task_id="hello4",
        bash_command="echo 'Hello 4'",
        trigger_rule=TriggerRule.ALL_FAILED  # s'exécute seulement si hello2 a échoué
    )

    hello >> hello3
    hello2 >> hello4