
# Open the input file for reading
with open("input.txt","r") as input_file:
    # Read the content of the input file
    input_content = input_file.read()

# Open the output file for writing
with open("output.txt","w") as output_file:
    # Write the content to the output file
    output_file.write(input_content)

# Open the input file for appending
with open("output.txt","a") as append_output_file:
    # Append "hello world" to the file
    append_output_file.write("hello world\n")


'''
This code reads the contents of the file 'input.txt'
 using a with statement, which automatically closes the 
 file after we're done with it. We then create a new file
   called 'output.txt' using another with statement,
     but this time we open the file for writing using 
     the 'w' mode.

Finally, we write the content of the input file to the
 output file using the write method of the output file 
 object. This code should create a new file called 
 'output.txt' with the same content as 'input.txt'.
'''