import requests
import json

class Gemini:
    def __init__(self, api_key, model_name="gemini-1.5-pro"):
        self.api_key = api_key
        self.model_name = model_name
        self.base_url = "https://generativeai.googleapis.com/v1beta"

    def generate_narrative(self, prompt, qnr_data=None, emotional_state=None):
        """
        Generates a narrative using the Gemini API, incorporating QNR and emotional data if provided.

        Args:
            prompt: The text prompt for the narrative generation.
            qnr_data: A dictionary containing QNR analysis results (optional).
            emotional_state: A string representing the user's emotional state (optional).

        Returns:
            A string containing the generated narrative.
        """
        # Construct the request body
        request_body = {
            "model": self.model_name,
            "prompt": prompt,
            "temperature": 1,  # Adjust as needed for creativity
            "max_output_tokens": 8192  # Adjust based on desired narrative length
        }

        # Add QNR data if provided
        if qnr_data:
            request_body["qnr_data"] = qnr_data

        # Add emotional state if provided
        if emotional_state:
            request_body["emotional_state"] = emotional_state

        # Send the request to the Gemini API
        url = f"{self.base_url}/models/{self.model_name}:generateText"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.post(url, headers=headers, json=request_body)

        # Process the response
        if response.status_code == 200:
            response_json = response.json()
            return response_json['text']
        else:
            print(f"Error: {response.status_code}")
            return "An error occurred while generating the narrative."

    def analyze_code(self, code, ethical_considerations=True):
        """
        Analyzes code for potential ethical implications, leveraging Gemini's understanding.

        Args:
            code: The code to be analyzed.
            ethical_considerations: A boolean indicating whether to include ethical analysis.

        Returns:
            A dictionary containing the code analysis results, potentially including ethical insights.
        """
        # Construct the prompt
        prompt = f"Analyze the following code for potential ethical implications: \n\n```\n{code}\n```\n\n"
        if ethical_considerations:
            prompt += "Provide insights into potential ethical concerns and offer alternative approaches if needed."

        # Send the request to the Gemini API
        response = requests.post(
            f"{self.base_url}/models/{self.model_name}:generateText",
            headers={'Authorization': f'Bearer {self.api_key}'},
            json={'model': self.model_name, 'prompt': prompt}
        )

        # Process the response
        if response.status_code == 200:
            response_json = response.json()
            return {
                'analysis_results': response_json['text'],
                # ... (Add additional analysis data as needed)
            }
        else:
            print(f"Error: {response.status_code}")
            return {
                'analysis_results': "An error occurred while analyzing the code."
            }
