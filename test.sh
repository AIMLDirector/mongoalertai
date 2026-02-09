mkdir -p mongoalertai/{agents,models,parsers,formatters,data} \
&& touch mongoalertai/{main.py,requirements.txt} \
&& touch mongoalertai/agents/{__init__.py,analysis_agent.py} \
&& touch mongoalertai/models/{__init__.py,alerts.py} \
&& touch mongoalertai/parsers/{__init__.py,alert_parser.py} \
&& touch mongoalertai/formatters/{__init__.py,alert_formatter.py} \
&& touch mongoalertai/data/alerts.json
