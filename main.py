import json
from pathlib import Path

from parsers.alert_parser import parse_alert
from formatters.alert_formatter import format_alert_for_llm
from agents.analysis_agent import analysis_agent


def main():
    alerts = json.loads(Path("data/alerts.json").read_text())

    for idx, raw in enumerate(alerts, start=1):
        print(f"\n========== ALERT {idx} ==========")

        alert = parse_alert(raw)
        llm_input = format_alert_for_llm(alert)

        print("📄 LLM Input:\n", llm_input)

        result = analysis_agent.invoke({
            "input": llm_input
        })
        analysis =(result.get("output") or result.get("final_output") or result["messages"][-1].content
           
        )
        print("🤖 AI Analysis:\n", analysis)


if __name__ == "__main__":
    main()
