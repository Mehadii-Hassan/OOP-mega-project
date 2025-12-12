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
                        
                1. Press 1 for Registration.
                2. Press 2 for Login.
                3. Press 3 for Exit.
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
            4. Text Summarization
            5. Keyword Extraction
            6. Named Entity Recognition
            7. Part-of-Speech Tagging
            8. Topic Modeling
            9. Text Classification
            10. Question Answering
            11. Text Generation
            12. Emotion Detection
            13. Intent Detection
            14. Paraphrase Detection
        """
    )
        if second_input == "1":
            self.__sentiment_analysis()
        elif second_input == "2":
            self.__language_translation()
        elif second_input == "3":
            self.__language_detection()
        elif second_input == "4":
            self.__text_summarization()
        elif second_input == "5":
            self.__keyword_extraction()
        elif second_input == "6":
            self.__named_entity_recognition()
        elif second_input == "7":
            self.__part_of_speech_tagging()
        elif second_input == "8":
            self.__topic_modeling()
        elif second_input == "9":
            self.__text_classification()
        elif second_input == "10":
            self.__question_answering()
        elif second_input == "11":
            self.__text_generation()
        elif second_input == "12":
            self.__emotion_detection()
        elif second_input == "13":
            self.__intent_detection()
        elif second_input == "14":
            self.__paraphrase_detection()
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

    def __text_summarization(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Summarize of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __keyword_extraction(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Extract the important keywords from this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __named_entity_recognition(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Identify named entities (like person, place, organization) in this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __part_of_speech_tagging(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Tag each word in this sentence with its part of speech: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __topic_modeling(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Identify the main topic of this sentence: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __text_classification(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Classify this sentence into a category (e.g. sports, politics, technology): {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __question_answering(self):
        user_text = input("Enter your question: ")
        model = self.getmodel()
        response = model.generate_content(f"Answer the question based on the user question: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __text_generation(self):
        user_text = input("Enter a prompt: ")
        model = self.getmodel()
        response = model.generate_content(f"Generate a short text based on this prompt: {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __emotion_detection(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Detect the emotion expressed in this sentence (happy, sad, angry, etc.): {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __intent_detection(self):
        user_text = input("Enter your text: ")
        model = self.getmodel()
        response = model.generate_content(f"Detect the intent of this sentence (e.g. booking, inquiry, complaint): {user_text}")
        results = response.text
        print(results)
        self.second_menu()

    def __paraphrase_detection(self):
        text1 = input("Enter first sentence: ")
        text2 = input("Enter second sentence: ")
        model = self.getmodel()
        response = model.generate_content(f"Check if these two sentences mean the same thing:\n1. {text1}\n2. {text2}")
        results = response.text
        print(results)
        self.second_menu()

app = AppFeatures() 