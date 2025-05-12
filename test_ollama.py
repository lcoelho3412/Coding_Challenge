import asyncio
import traceback  # <-- Add this import
from app.services.ollama_client import OllamaClient
from app.schemas.schemas import QuestionRequest


async def main():
    try:
        client = OllamaClient()
        response = await client.ask_marketing_question(
            QuestionRequest(
                question="What's the best time to post on LinkedIn?", user_id="test"
            )
        )
        print("SUCCESS!")
        print("Answer:", response.answer)
    except Exception as e:
        print("FULL ERROR TRACEBACK:")  
        traceback.print_exc()  


if __name__ == "__main__":
    asyncio.run(main())
