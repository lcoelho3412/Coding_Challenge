import httpx
from app.schemas.schemas import QuestionRequest, AnswerResponse
from datetime import datetime


class OllamaClient:
    def __init__(self):
        self.base_url = "http://localhost:11434/api/generate"
        self.model = "llama2"  # Changed from mistral to your available model
        self.timeout = 60.0  # Increased timeout for slower responses

    async def ask_marketing_question(self, question: QuestionRequest) -> AnswerResponse:
        """Send question to local Ollama instance with marketing context"""
        prompt = f"""You are a senior digital marketing expert. Answer this question specifically about marketing:
        Question: {question.question}

        Requirements:
        - Respond in under 150 words
        - Use bullet points when appropriate
        - Include 1-2 practical examples
        - Maintain professional tone"""

        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.base_url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0.7},  # Balances creativity and focus
                },
                timeout=self.timeout,
            )
            response.raise_for_status()
            result = response.json()

            return AnswerResponse(
                answer=result["response"],
                model_used=self.model,
                timestamp=datetime.now(),
            )
