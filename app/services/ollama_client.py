import httpx
from app.schemas.schemas import QuestionRequest, AnswerResponse
from datetime import datetime


class OllamaClient:
    def __init__(self):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = "llama2"  # Changed from mistral to your available model
        self.timeout = 180.0  # Increased timeout for slower responses

    async def ask_marketing_question(self, question: QuestionRequest) -> AnswerResponse:
        """Send question to local Ollama instance with marketing context"""

        # Use a simple prompt for testing
        prompt = f"{question.question}\n\nOnly answer if this is related to marketing. Otherwise state you can only answer marketing questions."

        print(">>> Sending request to Ollama...")  # Debug print

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.base_url,
                    json={
                        "model": self.model,
                        "prompt": prompt,
                        "stream": False,
                        "options": {
                            "temperature": 0.7
                        },  # Balances creativity and focus
                    },
                    timeout=self.timeout,
                )

                # Check if the request was successful
                response.raise_for_status()

                print(">>> Response received from Ollama")  # Debug print

                # Assuming the response contains a 'response' key
                result = response.json()

                return AnswerResponse(
                    answer=result["response"],
                    model_used=self.model,
                    timestamp=datetime.now(),
                )
            except httpx.ReadTimeout:
                print(
                    ">>> Request timed out. Try increasing the timeout further or check server status."
                )
                return None
            except httpx.RequestError as e:
                print(f">>> An error occurred: {e}")
                return None
            except Exception as e:
                print(f">>> Unexpected error: {e}")
                return None


# Example of calling the function
async def main():
    client = OllamaClient()
    question = QuestionRequest(
        question="What is the best strategy for digital marketing?"
    )
    response = await client.ask_marketing_question(question)

    if response:
        print(f"Answer: {response.answer}")
        print(f"Model Used: {response.model_used}")
        print(f"Timestamp: {response.timestamp}")
    else:
        print("No response received")
