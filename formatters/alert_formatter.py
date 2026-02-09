from models.alerts import (
    NetworkAlert,
    QueryPerformanceAlert,
    ReplicationAlert,
    StorageAlert,
    AccessControlAlert,
)


def format_alert_for_llm(alert) -> str:

    if isinstance(alert, NetworkAlert):
        return f"""
Alert Type: Network Alert
Context: Listener or connection issue

Message:
{alert.msg}

Address:
{alert.attr.get("address")}
"""

    if isinstance(alert, QueryPerformanceAlert):
        cmd = alert.attr.get("command", {})
        return f"""
Alert Type: Query Performance Alert
Context: Slow query execution

Message:
{alert.msg}

Duration (ms): {alert.attr.get("durationMillis")}
Query:
{cmd}
"""

    if isinstance(alert, ReplicationAlert):
        return f"""
Alert Type: Replication Alert
Context: Replication lag or heartbeat failure

Message:
{alert.msg}

Target:
{alert.attr.get("target")}

Error:
{alert.attr.get("error")}
"""

    if isinstance(alert, StorageAlert):
        return f"""
Alert Type: Storage / WiredTiger Alert
Context: Disk or cache pressure

Message:
{alert.msg}

Error Code:
{alert.attr.get("error")}

Details:
{alert.attr.get("message")}
"""

    if isinstance(alert, AccessControlAlert):
        return f"""
Alert Type: Access Control Alert
Context: Authentication or authorization failure

Message:
{alert.msg}

User: {alert.attr.get("user")}
Database: {alert.attr.get("db")}
Client IP: {alert.attr.get("client")}
"""

    return f"""
Alert Type: Unknown
Message:
{alert.msg}

Attributes:
{alert.attr}
"""