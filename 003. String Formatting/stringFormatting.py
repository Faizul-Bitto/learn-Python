"""
String Formatting
"""

firstName = "John"
print(f"Hi {firstName}")

sentence = "Hi {}"
print(sentence.format(firstName))

sentence2 = "Hi {} {}"
lastName = "Doe"
print(sentence2.format(firstName, lastName))

print(f"Hi {firstName} {lastName}. Hope you are well.")
