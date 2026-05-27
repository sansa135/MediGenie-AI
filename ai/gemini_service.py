def ask_chatbot(question):

    question = question.lower()

    if "fever" in question:
        return """
        AI Analysis:

        Possible Infection Detected

        Recommendations:
        - Drink more water
        - Take proper rest
        - Monitor body temperature
        - Consult doctor if fever increases
        """

    elif "cough" in question:
        return """
        AI Analysis:

        Mild respiratory symptoms detected.

        Recommendations:
        - Stay hydrated
        - Steam inhalation recommended
        - Avoid cold food
        """

    elif "chest pain" in question:
        return """
        AI Analysis:

        Warning:
        Chest pain may require medical attention.

        Recommendation:
        Consult physician immediately.
        """

    else:
        return """
        AI Analysis:

        General Health Recommendation:
        Maintain healthy diet, exercise regularly and sleep properly.
        """