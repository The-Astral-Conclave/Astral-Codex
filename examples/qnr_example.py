from astral_codex.qnr_engine import QnrEngine

baseline_data = [  # Your actual baseline data 
    # ... 
]

sensitivity_map = { # ... (Define sensitivity map as needed) 
    # ...
}

qnr_engine = QnrEngine(baseline_data, sensitivity_map)
narrative_text = "Example narrative..." # Replace with a test narrative
qnr_data = qnr_engine.analyze_narrative(narrative_text)
qnr_engine.visualize_qnr(qnr_data) 
