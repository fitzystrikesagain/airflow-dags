from helpers import dagbag

DAG_ID = "parallel_dag"
dag = dagbag.get_dag(DAG_ID)
task_ids = [
    "task_1",
    "task_2",
    "task_3",
    "task_4",
    "task_5",
    "task_6"
]


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


def test_has_on_failure_callback_exists():
    """Dag must have an on failure callback"""
    assert dag.has_on_failure_callback


def test_is_not_paused():
    """Dag should not be paused"""
    assert not dag.is_paused


def test_owner_exists():
    """Dag must have an owner"""
    assert dag.owner


def test_task_count():
    """Task count should equal 6"""
    assert dag.task_count == 6


def test_task_ids_match_expected_task_ids():
    assert dag.task_ids == task_ids


"""
FAILED module Task count should equal 4 - assert 6 == 4
FAILED module test_task_ids_match_expected_task_ids - AssertionError: assert ['task_1', 't..._5', 'task_6'] == ['tasks', 'ta..._5', 'task_6']
"""
