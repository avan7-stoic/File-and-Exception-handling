def read_and_modify_file():
    filename = input("Enter the filename to read from: ")

    try:
        with open(filename, 'r') as file:
            content = file.readlines()
        
        # Modify content (e.g., make all lines uppercase)
        modified_content = [line.upper() for line in content]

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_content)

        print(f"✅ File was successfully read and written to '{new_filename}'.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except IOError:
        print("❌ Error: The file could not be read or written to.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
