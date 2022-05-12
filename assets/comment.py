import glob

# Save existing contents of a given file.
file_contents = []
# Line to prepend in a .ts file.
line = "/* Jedd Lupoy (1536884) */\n"

def insert_line(text):
    # Get all .ts files.
    #files = glob.glob("./src/**/*[!.d].ts", recursive=True)
    files = glob.glob("./src/test/*.txt", recursive=True)
    print(files)

    # Iterate through all .ts files.
    for i in files:
        original_file = open(i, 'r')
        # Save contents of original file into a list.
        for j in original_file:
            file_contents.append(j)

        with open(i, 'w') as write_obj:
            # Begin writing line to file.
            write_obj.write(text)
            # Append original file contents.
            for ln in file_contents:
                write_obj.write(ln)
        # Clear file contents list.
        file_contents.clear()

if __name__ == "__main__":
    # Begin script.
    insert_line(line)