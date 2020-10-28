from _test_class import AnonymouSurvey

def get_formatted_name(first,last):
	complete_name = f"{first} {last}"
	return complete_name.title()

def get_name():
	print("Enter 'q' at any time to quit")
	while True:
		first = input("\n Please give me a first name: ")
		if first == 'q':
			break
		last = input("\n Please give me a last name: ")
		if last == 'q':
			break
			
		complete = get_formatted_name(first,last)
		print(f"\n Neatly formatted name: {complete}")

# 定义一个问题 并创建一个问卷
question = "What's your name?"
survey = AnonymouSurvey(question)

# 显示问题并存储答案
survey.show_question()
print("(Enter 'q' at any time to quit.)\n")

while True:
	response = input("name: ")
	if response == 'q':
		break
	survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in the survey!\n")
survey.show_results()


