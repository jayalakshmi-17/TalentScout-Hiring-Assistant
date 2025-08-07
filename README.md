TalentScout Hiring Assistant 🤖
An intelligent Streamlit-based chatbot that assists recruiters in screening candidates by collecting key information and generating technical questions based on their tech stack.
 
•	Friendly chatbot interface using Streamlit
•	Step-by-step candidate data collection
•	Auto-generated technical questions from OpenRouter (free GPT alternative)
•	Clean, readable UI with chat history
 
To launch locally:
 
Live hosting: [Optional if deployed]
 
•	Python
•	Streamlit (Frontend UI)
•	OpenRouter API (LLM backend)
•	dotenv (for secure token management)
 
1.	Clone the repository or unzip the folder
2.	Install dependencies
 
(Or manually install)
 
 
Prompts are dynamically constructed using candidate responses. Example:
Generate 3 technical interview questions for someone skilled in: Python, Django, MySQL
 
Generated Questions:
1.	How does Django handle database migrations?
2.	What are Python decorators and how are they used?
3.	Explain different types of SQL joins.
 
•	Hugging Face 404s: Switched to OpenRouter for better stability.
•	Quota Limits on OpenAI: Bypassed by using free LLM alternatives.
•	Prompt Formatting: Used simple structured prompts for accurate question generation.
 
	Criteria	How It's Addressed
	Technical Proficiency	Clean code, full session handling, LLM use
	Criteria	How It's Addressed
Prompt Engineering	Dynamic prompt generation based on input
UI & UX	Simple, friendly Streamlit chat interface
Documentation & Presentation	This README + possible video walkthrough
Enhancements	External API + dotenv + token security
 
📆 Submission
-
 
Built by Jaya Lakshmi Prasanna Patnala for the AI/ML Internship Assignment ✨
