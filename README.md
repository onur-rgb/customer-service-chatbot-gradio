# Customer Service Chatbot

## Overview

This project implements a customer service chatbot that provides information about products in different categories. Users can ask questions related to products, and the chatbot will provide relevant information based on the queries. The chat interface is powered by Gradio, and the chatbot itself uses OpenAI's GPT-3.5 Turbo model for natural language understanding.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/onur-rgb/customer-service-chatbot-gradio.git
   cd customer-service-chatbot-gradio
   ```

2. Set up your OpenAI API key by replacing `"YOUR_API_KEY"` in the code with your actual API key. You can obtain an API key by signing up at [OpenAI's platform](https://platform.openai.com/).

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
4. Create and configure `products.json` with product information. You can customize this JSON file to match your specific product database.

   Make sure to add products and categories relevant to your use case.

5. Run the chatbot:

   ```bash
   python main.py
   ```

## Usage

- Interact with the chatbot by entering queries or questions related to products.
- The chatbot will process your queries and provide information about products and categories.

## Rate Limiting

To prevent rate limit errors from OpenAI, a rate-limiting mechanism has been implemented in the code. The rate limit is set based on your OpenAI organization's specific rate limit policy. You can adjust the rate limit parameters in the code to match your rate limit requirements.

## Gradio Chat Interface

The chat interface is powered by Gradio, a Python library that simplifies the creation of interactive interfaces for machine learning models. You can customize the interface's appearance and behavior by modifying the Gradio components in the code.

## Prompt Engineering

This chatbot uses prompt engineering to guide user interactions and generate responses. You can enhance the chatbot's capabilities by refining the prompts used for different types of queries.

Feel free to explore and customize this code to meet your specific requirements. If you have any questions or need further assistance, please don't hesitate to reach out.

Happy chatting!
