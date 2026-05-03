import tiktoken
# encode convert text into toknen-id

enc = tiktoken.encoding_for_model("gpt-4o")
print(enc.encode("hello"))
text="hey there!! my name is sam"
token=enc.encode(text)

print("tokens",token)