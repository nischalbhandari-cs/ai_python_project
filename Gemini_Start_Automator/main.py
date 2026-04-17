import os 
import google.generativeai as genai 
from dotenv import load_dotenv 

def start_task_automator(): 
    # SET UP 
    load_dotenv() 
    api_key=os.getenv("GEMINI_API_KEY") 
    api_password=os.getenv("API_PASSWORD") 

    #2. asking for password 
    user_input= input("Please Enter the Password to Access: ") 

    #If password is incorrect, end the function
    if user_input!= api_password: 
        print("Incorrect password.Access is denied") 
        return 
     
    else:
        print("Access Granted. Starting Task Automator") #password correct 

    #3 configure gemini ai 
    genai.configure(api_key=api_key)
    model= genai.GenerativeModel("gemini-2.0-flash") 

    #4 read taks from file 
    try:
        with open("tasks.txt","r") as file:
            tasks=file.read()  

    except FileNotFoundError: 
        print("tasks.txt file is not found.")
        return 
    
    #5 generate responses from gemini ai  

    prompt= f" Please generate a response of the follong tasks: {tasks}"
    try:
        ai_response=model.generate_content(prompt)
        print("\n your organized tasks are :") 
        print (ai_response.text)
    except Exception as e: 
        print(f"An error as occured {e}") 

    #The main entry point of the program 
if __name__ =="__main__":
    start_task_automator()


    
