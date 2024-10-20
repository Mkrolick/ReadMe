import openai
import os
import dotenv
import pandas as pd

dotenv.load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


# here is the question, take the input from the data and split based on time gap

df = pd.read_csv("messages.csv")

df["date"] = pd.to_datetime(df["date"])

df.sort_values(by="date", inplace = True)

# _ is index 
message_list = [f"{row['author']}: {row['message']}" for _, row in df.iterrows() if row["author"] != "Quoter"]


#GPT-4 has a 32,768 total token limit.

max_tokens = 4077


token_lists = [len(x.split(" ")) for x in message_list]

break_index = []
token_sum = 0

for i in token_lists:
    token_sum += i
    if token_sum > max_tokens:
        break_index.append(token_lists.index(i))
        token_sum = 0



print("Users in this conversation: ", [x for x in df["author"].unique() if x != "Quoter"])
target_name = input("Who is the target? ")


previous_index = 0

break_index.append(len(message_list) + 1)

for index in break_index:
    converstation_message_list = message_list[previous_index:index]
    converstation_text = "\n\n".join(converstation_message_list)

    # print(converstation_text)


    #system_intel = "You are Psychological-Profiler-GPT, you are designed to pychologically profile people."
    #prompt = f"Given the conversation below, develop a psychological profile of {target_name}: {converstation_text}"

    system_intel = "You are Psychological-Profiler-GPT, you are designed to pychologically profile people."
    prompt = f"Given the text channel below, develop a psychological profile of {target_name} in a bulleted list with catagories of Behavioral Traits, Emotional Traits, Possible Motivations, Potential Issues, and an overall summary: {converstation_text}"

    # Function that calls the GPT API
    def ask_GPT(system_intel, prompt): 
        
        result = openai.ChatCompletion.create(model="gpt-3.5-turbo-0301",
                                    messages=[{"role": "system", "content": system_intel},
                                            {"role": "user", "content": prompt}])
        
        print(f"Profile: {target_name} \n")
        print(result['choices'][0]['message']['content'])

        with open("Output.txt", "w") as text_file:

            print(f"Profile: {target_name} \n", file=text_file)
            print(result['choices'][0]['message']['content'], file=text_file)
            

    # Call the function above
    ask_GPT(system_intel, prompt)