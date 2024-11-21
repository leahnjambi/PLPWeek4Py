def modify_file(input_filename, output_filename):
    try:
        # Open the input file read mode
        with open(input_filename, "r") as file:
            content = file.read() 
            
        # Modify the content
        modified_content = content.upper()  # Example modification: making the text uppercase
        
        # Open the output file in write mode and write the modified content
        with open(output_filename, "w") as new_file:
            new_file.write(modified_content)
            
        print(f"The file has been successfully modified and saved as {output_filename}.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: There was a problem reading or writing to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Ask the user for the filename to read and the output filename to write
input_filename = input("Enter the name of the file to read from: ")
output_filename = input("Enter the name of the new file to save the modified content: ")

# Call the function to modify the file
modify_file(input_filename, output_filename)
