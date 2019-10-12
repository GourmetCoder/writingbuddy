import logic.word_generator as word_generator
import utility.argument_not_defined_error as argument_not_defined_error
import sys
import logic.file_loader as file_loader

if __name__ == '__main__':

    try:
        cleaner = []
        if len(sys.argv) < 3:
            raise argument_not_defined_error.ArgumentNotDefinedError
        if len(sys.argv) > 3:
            loader = file_loader.FileLoader(sys.argv[3])
            split_cleaner_file = loader.load_file().split("\n")
            cleaner = [pair.split("|||") for pair in split_cleaner_file]
        generator = word_generator.WordGenerator(sys.argv[1], clean_list=cleaner)
        generated_text = generator.generate_text(int(sys.argv[2]))
        print(generated_text)
    except argument_not_defined_error.ArgumentNotDefinedError:
        print(
            "The program did not recieve required amount of arguments!/n" +
            "    Run the program with following command app.py 'Path_to.file' 'Length of generation'"
        )