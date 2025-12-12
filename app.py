import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class BaseModel:
    def getmodel(self):
        try:
            genai.configure(api_key = os.getenv("GEMINI_API__KEY"))
            model = genai.GenerativeModel("gemini-2.5-flash")
            return model
        except Exception as e:
            print(e)

class AppFeatures(BaseModel):
    def __init__(self):
        self.__database = {} 
        self.first_menu()

    def first_menu(self):
        first_input = input(
            """
            Hi! How would you like to proceed?
            
                1. Not a member? Register
                2. Alreadey a member? Login
                3. Nothing? Exit
            """
        )

        if first_input == "1":
            #Register
            self.__register()
        elif first_input == "2":
            #Login
            self.__login()
        else:
            exit()

    def second_menu(self):
        second_input = input(
        """
        Hi! How would you like to proceed?

            1. Sentiment Analysis
            2. Language Translation
            3. Language Detection
        """
        )
        if second_input == "1":
            #sentiment
            self.__sentiment_analysis()
        elif second_input == "2":
            #translation
            self.__language_translation()
        elif second_input == "3":
            #detection
            self.__language_detection()
        else:
            exit()

    def __register(self):
        name = input("Enter your Name: ")
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")

        if email in self.__database:
            print("Email already exists.")
        else:
            self.__database[email] = [name, password]
            print("Registration successful. Now you can login!")
        self.first_menu()

    def __login(self):
        email = input("Enter your Email: ")
        password = input("Enter your Password: ")

        if email in self.__database:
            if self.__database[email][1] == password:
                print("Login Successfull!")
                #second menu
                self.second_menu()
            else:
                print("Your password is incorrect! Please try again.")
                self.__login()
        else:
            print("Email not found! Please register first.")
            self.first_menu()




    def __sentiment_analysis(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Give me the sentiment of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __language_translation(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Give me Bangla transilation of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()
    
    def __language_detection(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Detect the language of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

app = AppFeatures()
