from pathlib import Path


CONNECTOR_SOURCE = Path("beyondtrust_connector.py").read_text()


def test_user_ids_are_coerced_to_integers_before_path_use():
    assert CONNECTOR_SOURCE.count("_parse_user_id(param.get(\"user_id\"), action_result)") == 2
    assert "User ID must be an integer" in CONNECTOR_SOURCE
