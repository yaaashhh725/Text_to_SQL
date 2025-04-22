# Text to SQL agent
An AI agent to translate and execute natural language queries into SQL queries

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)

## Installation
1. Clone the repository:
```bash
 git clone https://github.com/yaaashhh725/Text_to_SQl.git
```
2. Create a virtual environment (optional):
```bash
python -m venv environment_name
```
 For windows:
```bash
.environment_name\scripts\activate
```
 For Mac/Linux:
```bash
source environment_name/bin/activate
```
3. Install dependencies:
```bash
 pip install -r requirements.txt
 ```

## Usage
To run the project, use the following command:
```bash
python -m streamlit run app.py
```
OR
```bash
streamlit run app.py
```
## Customization
- You can create your own database and work with it.
- After creating your own database you will also need to edit the prompt string being supplied to the model
