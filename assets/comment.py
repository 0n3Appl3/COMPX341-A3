import glob

# Save existing contents of a given file.
file_contents = []
# Determine if file already has the commented line.
commented = False
# Line to prepend in a .ts file.
line = "/* Jedd Lupoy (1536884) */\n"

def insert_line(text):
    # Get all .ts files.
    #files = glob.glob("./src/**/*[!.d].ts", recursive=True)
    files = glob.glob("./src/test/*.txt", recursive=True)
    print(files)

    # Check if there are any files to comment.
    if len(files) == 0:
        print("ERROR: There are no files to comment!")
        return

    # Iterate through all .ts files.
    for i in files:
        commented = False
        original_file = open(i, 'r')
        # Save contents of original file into a list.
        for j in original_file:
            # Does the original file already have the comment line?
            if j == line: 
                commented = True
                break
            file_contents.append(j)
        # Skip this file and move to the next if it already has the comment line..
        if commented == True:
            print("NOTE: " + i + " has already been commented!")
        else:
            with open(i, 'w') as write_obj:
                # Begin writing line to file.
                write_obj.write(text)
                # Append original file contents.
                for ln in file_contents:
                    write_obj.write(ln)
            # Clear file contents list.
            file_contents.clear()
            print(i + " commented!")

if __name__ == "__main__":
    # Begin script.
    insert_line(line)