from models.alerts import (
    NetworkAlert,
    QueryPerformanceAlert,
    ReplicationAlert,
    StorageAlert,
    AccessControlAlert,
    GenericAlert,
)


def parse_alert(data: dict):
    category = data.get("c")

    if category == "NETWORK":
        return NetworkAlert.model_validate(data)
    if category == "COMMAND":
        return QueryPerformanceAlert.model_validate(data)
    if category == "REPL":
        return ReplicationAlert.model_validate(data)
    if category == "STORAGE":
        return StorageAlert.model_validate(data)
    if category == "ACCESS":
        return AccessControlAlert.model_validate(data)

    return GenericAlert.model_validate(data)