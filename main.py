import openai
import gradio as gr
import utils
import time

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"  # Replace with your key

# Rate limiting parameters
max_requests_per_minute = 3  # Maximum requests allowed per minute
request_interval = 60 / max_requests_per_minute  # Time interval between requests

# Initialize rate limiting variables
last_request_time = 0

# Define the predict function with rate limiting
def predict_with_rate_limit(message, history):
    global last_request_time

    # Check if enough time has passed since the last request
    current_time = time.time()
    if current_time - last_request_time < request_interval:
        return "Rate limit exceeded. Please wait before making another request."

    # Update the last request time
    last_request_time = current_time

    # Continue with the original prediction logic
    products_by_category = utils.get_products_from_query(message)
    category_and_product_list = utils.read_string_to_list(products_by_category)

    if isinstance(category_and_product_list, list):
        product_info = utils.get_mentioned_product_info(category_and_product_list)
    else:
        product_info = utils.get_mentioned_product_info([category_and_product_list])

    assistant_answer = utils.answer_user_msg(user_msg=message, product_info=product_info)

    return assistant_answer

# Create the Gradio interface
gr.ChatInterface(
    predict_with_rate_limit,  # Use the rate-limited predict function
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="You can insert your prompt here", container=False, scale=7),
    title="Customer Service Chatbot",
    description="Ask me a question about products",
    theme="soft",
    examples=[
        "What categories of devices do you have?",
        "Tell me about the smartx pro phone and the fotosnap camera, the dslr one. Also, what TVs or TV related products do you have?",
        "Show me all of your computers.",
        "Tell me about the CineView TV, the 8K one, Gamesphere console, the X one. I'm on a budget and I have 1000 dollars, what computers do you have?",
    ],
    cache_examples=False
).queue().launch(share=False)
