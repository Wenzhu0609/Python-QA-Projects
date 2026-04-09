# To write:

# Write the reversed list back to the file

# with open('test.txt', 'r') as reader:
#     content = reader.readlines()            # 1. Read
#     # reversed(content)                     # 2. Reverse - but here it doesn't seem to do anything. Even commented out, running the code still gives expected result d/t reversed function used in later part
#     with open('test.txt', 'w') as writer:   # 3. Open file in write mode
#         for line in reversed(content):      # 4. Write each line of the reversed file content
#             writer.write(line)

# Industry standard:
with open('test.txt', 'r') as reader:
    content = reader.readlines()
with open('test.txt', 'w') as writer:
    for line in reversed(content):
        writer.write(line)