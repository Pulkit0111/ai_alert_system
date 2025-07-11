from agent_utils import (
    read_log_file,
    summarize_alert_log,
    send_telegram_message
)

def alert_agent(log_path):
    log_content = read_log_file(log_path)
    log_summary = summarize_alert_log(log_content)
    send_telegram_message(log_summary)