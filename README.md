# Clat_cb
Project Overview
This project is a conversational chatbot named Clexa 👩‍⚖️, designed to assist law aspirants by answering queries related to the CLAT exam using a rule-based NLP approach.

🛠️ Approach
Built using **Flask (Python backend)** and **HTML/CSS **for frontend.

A **JSON knowledge base** stores answers to frequently asked CLAT-related questions.

Used **Flask sessions**to maintain chat history across user interactions.

Implemented a modern chat UI with user/bot bubbles and responsive design.

Added a **greeting message** on first visit: “Hey! I’m Clexa 👩‍⚖️ — your CLAT Assistant. How can I help you?”

Included a reset option to clear chat and restart fresh.

✅ Features
**Dynamic question**-answer chat experience.

Full chat history displayed during interaction.

Responsive and visually appealing frontend using glassmorphism styling.

**Edge case handling** for unrecognized queries.

Easily extensible knowledge base.

🧪 Test Cases
Test Case Description	 Input	                                                 Expected Output
Syllabus query	What is the syllabus for CLAT 2025?	                           CLAT 2025 syllabus includes English, GK, Legal, Logic, and Quant
Question count query	How many questions are there in English?	               There are 30 questions in the English section.
Cut-off info	Last year’s cut-off for NLSIU Bangalore?	                       The cut-off was 85 marks.
Exam duration	What is the duration of the exam?	                               CLAT exam duration is 2 hours.
Eligibility check	Am I eligible with 44% in 12th?	                             It requires at least 45% (40% for SC/ST).
Unknown question (edge case)	What is the capital of France?	                 Sorry, I couldn't find an answer to that.


Greeting on first load	Page opens for the first time	Clexa greets with a welcome message.
Reset functionality	Clicked on Reset Chat	Chat cleared; shows only greeting on refresh
