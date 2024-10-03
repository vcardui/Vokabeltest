from Words import vocabulary_test
import random

empty_list = []
all_words = []
available_categories = []
available_keys = []

user_score = 0
taken_questions = 0

ready_to_start = False

while ready_to_start == False:
  
  print("Select vocabulary categories to test: ")
  print("all: test all vocabulary")
  
  for key in vocabulary_test:
    available_categories.append(key)
    available_keys.append(str(available_categories.index(key)))
    print(f"{available_categories.index(key)}: {key} - ({len(vocabulary_test[key])})")
  
  #print(available_categories)
  #print(available_keys)
  
  user_choice_string = input("")

  if user_choice_string == "all":
    for category in vocabulary_test:
      for word in vocabulary_test[category]:
        all_words.append(word)
  
  else:
    user_choice = user_choice_string.split(", ")
    #print(f"user_choice = {user_choice}")
  
    for item in user_choice:
      if item in available_keys:
        for word in vocabulary_test[available_categories[int(item)]]:
          #print(item)
          all_words.append(word)

    #print(all_words)

  if all_words != empty_list:
    ready_to_start = True
  else:
    print("    Please type in valid arguments")

while all_words != empty_list:
  
  random_route = random.randint(0,1)
  
  current_word = random.choice(all_words)
  
  if random_route == 0:
    print(f"English: {current_word['english']}")
    user_answer = input(f"Deutsch: ")

    taken_questions += 1
  
    if user_answer == str(current_word['deutsch']):
      print(":D\n")
      all_words.remove(current_word)
      user_score += 1
    else:
      print("X")
      print(f"{current_word['deutsch']}")

    print(f"{user_score}/{taken_questions} \n")
  
  elif random_route == 1:
    print(f"Deutsch: {current_word['deutsch']}")
    user_answer = input(f"English: ")

    taken_questions += 1
  
    if user_answer == str(current_word['english']):
      print(":D\n")
      all_words.remove(current_word)
      user_score += 1
    else:
      print("X")
      print(f"{current_word['english']}")

    print(f"{user_score}/{taken_questions} \n")

  if user_answer == 'exit test':
    all_words = empty_list

if all_words == empty_list:
  print("No more words left")
  print(f"{user_score} correct answers out of {taken_questions} questions")