import requests
import os

def load_story_prompt():
    prompt_path = os.path.join(os.path.dirname(__file__), "prompts", "story_qa_prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def get_llm_response(messages, system_prompt=None):
    """
    Get response from the custom deployed LLM endpoint.
    """
    try:
        api_key = "OMxArANmOKYKVt2RtKFw5-iTAmTr0lDu3aOeCUp6G3U"
        sys_prompt = system_prompt

        # Convert messages into a readable conversation string
        conversation = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in messages])
        full_prompt = f"System: {sys_prompt}\n{conversation}"

        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json"
        }

        params = {"question": full_prompt}

        response = requests.post("https://ai.sugarlabs.org/ask-llm", headers=headers, params=params)
        response.raise_for_status()

        data = response.json()
        return data.get("answer", "No answer found in response.")
    
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"
      
story_prompt = load_story_prompt()
response = get_llm_response(
    messages=[
        {"role": "user", "content": "My story is about a gardener"},
        {"role": "assistant", "content": "Wonderful work. This will be a nice story"},
        {"role": "user", "content": "Thank you"},
    ],
    system_prompt=story_prompt
)
print(response)