from ai.gemini_service import ask_chatbot


def analyze_report(report_text):
    prompt = f"""
    Analyze this medical report.

    Give:
    1. Summary
    2. Risks
    3. Recommendations

    Report:
    {report_text}
    """

    response = ask_chatbot(prompt)
    return {
        'analysis': response
    }
