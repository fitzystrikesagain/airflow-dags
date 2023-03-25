from helpers import dagbag

DAG_ID = "sleep_ten_seconds"
dag = dagbag.get_dag(DAG_ID)
task_ids = ['start', 'task_1', 'task_2', 'task_3', 'all_done']
num_tasks = len(task_ids)

def test_catchup_disabled():
    """Catchup should not be enabled"""
    assert not dag.catchup


def test_dagrun_timeout_exists():
    """DagrunTimeout must be set"""
    assert dag.dagrun_timeout


def test_description_exists():
    """Dag must have a description"""
    assert dag.description


def test_doc_md_exists():
    """Dag must have a docstring"""
    assert dag.doc_md


def test_is_not_paused():
    """Dag should not be paused"""
    assert not dag.is_paused


def test_owner_exists():
    """Dag must have an owner"""
    assert dag.owner


def test_task_count():
    f"""Task count should equal {num_tasks}"""
    assert dag.task_count == num_tasks


def test_task_ids_match_expected_task_ids():
    """Task IDs must match expected task ids"""
    assert dag.task_ids == task_ids
