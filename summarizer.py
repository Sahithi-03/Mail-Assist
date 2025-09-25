import google.generativeai as genai   # type: ignore
  
# Configure the API key  
genai.configure(api_key="AIzaSyCASJRVu3CLx3aEzezAgMO9FaX9PleZcto")  
  
# Initialize the GenerativeModel with the model name as a positional argument  
model = genai.GenerativeModel("models/gemma-3-1b-it")  


def summary(email_text):
    # Generate summary content for the mail
    summary_prompt = f"Summarize this email in 2-3 sentences:\n\n{email_text}"
    summary = model.generate_content(summary_prompt).text
    
    # Generate reply
    reply_prompt = f"""
    Read the following email and write a reply in the **same tone and style** as the sender.
    Keep it natural, not overly formal. 

    Email:
    {email_text}

    Summary of the email: {summary}
    """
    reply = model.generate_content(reply_prompt).text

    return [summary, reply]
