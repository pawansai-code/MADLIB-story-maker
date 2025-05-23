def get_input(word_type:str):
    #function prompts the user for a specific type of word (noun, verb, adjective)

    user_input = input(f"enter a {word_type}: ")
    #Check if the input is empty

    return user_input

noun1=get_input("noun")
adjective1=get_input("adjective")
verb1=get_input("verb")
adjective2=get_input("adjective")
noun2=get_input("noun")
verb2=get_input("verb")
adjective3=get_input("adjective")
verb3=get_input("verb")
adjective4=get_input("adjective")
verb4=get_input("verb")

#instead of using noun, verb, adjective u can give alternate words

story=f"""
Robert Downey Jr. is a {adjective1} actor known for his role as Iron Man.
He started his career as a {noun1} in Hollywood, where he had to {verb1}through many challenges.
Despite facing {adjective2} times, RDJ never gave up and continued to {verb2} with passion.
He is famous for his {adjective3} performances and his ability to {verb3} different characters.
Outside of acting, he loves his {noun2} and enjoys {verb4} in his free time.
Today, Robert Downey Jr. is considered one of the most {adjective4}and successful actors in the industry.
"""
    #multilne string
    #your own story
print(story)
