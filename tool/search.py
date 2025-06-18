# from dotenv import load_dotenv
# import os
# import time
# from openai import OpenAI, RateLimitError, APIError, APIConnectionError

# load_dotenv(dotenv_path="openai.env")
# load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# print("Loaded API key:", os.getenv("OPENAI_API_KEY"))
# # print(client.models.list()) 

# def search(query: str, max_retries: int = 3) -> str:
#     """
#     Search function with exponential backoff retry logic for handling rate limits
#     and other API errors.
    
#     Args:
#         query (str): The search query
#         max_retries (int): Maximum number of retry attempts
    
#     Returns:
#         str: The response from the model or an error message
#     """
#     for attempt in range(max_retries):
#         try:
#             response = client.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[{"role": "user", "content": query}],
#                 max_tokens=200
#             )
#             return response.choices[0].message.content.strip()
            
#         except RateLimitError as e:
#             if attempt == max_retries - 1:
#                 print(f"⚠️ Rate limit hit after {max_retries} attempts:", e)
#                 return "Rate limit exceeded. Please try again in a few minutes."
            
#             wait_time = (2 ** attempt) * 1  # Exponential backoff: 1s, 2s, 4s
#             print(f"⚠️ Rate limit hit, retrying in {wait_time} seconds...")
#             time.sleep(wait_time)
            
#         except APIConnectionError as e:
#             if attempt == max_retries - 1:
#                 print(f"⚠️ API Connection error after {max_retries} attempts:", e)
#                 return "Connection error. Please check your internet connection."
            
#             wait_time = (2 ** attempt) * 1
#             print(f"⚠️ Connection error, retrying in {wait_time} seconds...")
#             time.sleep(wait_time)
            
#         except APIError as e:
#             print(f"❌ API Error:", e)
#             return f"API Error: {str(e)}"
            
#         except Exception as e:
#             print(f"❌ Unexpected error:", e)
#             return f"An unexpected error occurred: {str(e)}"

# # Test the function
# if __name__ == "__main__":
#     test_query = "What is the capital of France?"
#     result = search(test_query)
#     print(f"Query: {test_query}")
#     print(f"Result: {result}")



from dotenv import load_dotenv
import os
import time
from openai import OpenAI, RateLimitError, APIError, APIConnectionError

load_dotenv(dotenv_path="openai.env")
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("Loaded API key:", os.getenv("OPENAI_API_KEY"))

def search(query: str, max_retries: int = 3) -> str:
    """
    Search function with exponential backoff retry logic for handling rate limits
    and other API errors.
    
    Args:
        query (str): The search query
        max_retries (int): Maximum number of retry attempts
    
    Returns:
        str: The response from the model or an error message
    """
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}],
                max_tokens=200
            )
            return response.choices[0].message.content.strip()
            
        except RateLimitError as e:
            if attempt == max_retries - 1:
                print(f"⚠️ Rate limit hit after {max_retries} attempts:", e)
                return "Rate limit exceeded. Please try again in a few minutes."
            
            wait_time = (2 ** attempt) * 1  # Exponential backoff: 1s, 2s, 4s
            print(f"⚠️ Rate limit hit, retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            
        except APIConnectionError as e:
            if attempt == max_retries - 1:
                print(f"⚠️ API Connection error after {max_retries} attempts:", e)
                return "Connection error. Please check your internet connection."
            
            wait_time = (2 ** attempt) * 1
            print(f"⚠️ Connection error, retrying in {wait_time} seconds...")
            time.sleep(wait_time)
            
        except APIError as e:
            print(f"❌ API Error:", e)
            return f"API Error: {str(e)}"
            
        except Exception as e:
            print(f"❌ Unexpected error:", e)
            return f"An unexpected error occurred: {str(e)}"

# Test the function
if __name__ == "__main__":
    test_query = "What is the capital of France?"
    result = search(test_query)
    print(f"Query: {test_query}")
    print(f"Result: {result}")
