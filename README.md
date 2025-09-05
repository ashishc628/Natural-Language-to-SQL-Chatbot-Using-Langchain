# NL2SQL with LangChain


<p align="center">
  <img src="flow.png" alt="NL2SQL Workflow" width="600"/>
</p>



Interact with databases using **natural language** instead of SQL. This project demonstrates how to build an NL2SQL system using **LangChain**, allowing users to ask questions in plain English and get accurate answers from their database.

## Key Features

- **Basic NL2SQL Queries**: Translate natural language questions into SQL commands.
- **Few-Shot Learning**: Improve query accuracy with examples.
- **Dynamic Example Selection**: Pick relevant examples based on the current question.
- **Relevant Table Selection**: Focus only on tables needed for a query, improving speed and accuracy.
- **Clear Responses**: Rephrase raw SQL results into human-readable answers.
- **Conversation Memory**: Handle follow-up questions by remembering previous interactions.

## Example Workflow

1. Ask a question in plain English.  
2. The model selects relevant tables and examples.  
3. SQL query is generated and executed.  
4. Results are presented in a clear, natural format.  
5. Follow-up questions are handled using conversation history.

## Why NL2SQL?

- Makes database access **easier for non-technical users**.  
- Reduces **errors in query generation**.  
- Saves time and improves **data accessibility**.  

Unlock your data with a **conversational interface** and get answers without writing SQL.
