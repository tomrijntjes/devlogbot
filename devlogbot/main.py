import os
import sys
from openai import OpenAI
from devlogbot.devlogvectordb import query_devlogbook

os.environ["TOKENIZERS_PARALLELISM"] = "true"


def main():
    """Main function to process the query and display results."""
    # Parse command-line arguments
    query_string = ' '.join(sys.argv[1:])
    if len(query_string) < 1:
        raise ValueError("Please provide a query string.")

    print(f"Processing query: {query_string}")

    try:
        # Query the ChromaDB collection using the provided query string
        logs = query_devlogbook(query_string)
        
        if not logs:
            print("No documents matched the query.")
            return
        
        # Format the query results into a prompt for the LLM model
        prompt = f"""Examine this list of log entries and identify relevant information to answer: 
                     {query_string}

                     Log entries:
                     {logs}
                 
                     Based on the above information, provide a concise and accurate response.
                     """
        
        # Initialize OpenAI client
        openai_client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio", )
        
        try:
            # Send the prompt to the LLM model using completions API
            completion = openai_client.chat.completions.create(
                model="qwen2.5-7b-instruct-1m",
                max_tokens=8192,
                messages=[{
                    "role": "user",
                    "content": prompt
                }],


            )
            
            response = completion.choices[0].message.content
            
            print("Response from the LLM:")
            print(response)
        except Exception as e:
            print(f"Error making API call: {str(e)}")
    
    except Exception as e:
        print(f"Error parsing command line argument: {str(e)}")

if __name__ == "__main__":
    main()
