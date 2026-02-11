
# AI Article Processor (Groq Version)

This version replaces OpenAI with Groq API.

Groq Endpoint:
POST https://api.groq.com/openai/v1/chat/completions

Model Recommended:
llama-3.1-8b-instant

Add to .env:
GROQ_API_KEY=your_key_here

Inside n8n HTTP Node:
Authorization: Bearer {{$env.GROQ_API_KEY}}

Then extract response:
{{$json["choices"][0]["message"]["content"]}}

Run with Docker:
docker-compose up --build
