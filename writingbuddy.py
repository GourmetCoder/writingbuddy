import logic.word_generator as word_generator
import utility.argument_not_defined_error as argument_not_defined_error
import sys

if __name__ == '__main__':
    try:
        if len(sys.argv) < 3:
            raise argument_not_defined_error.ArgumentNotDefinedError
        generator = word_generator.WordGenerator(sys.argv[1])
        generated_text = generator.generate_text(int(sys.argv[2]))
        print(generated_text)
    except argument_not_defined_error.ArgumentNotDefinedError:
        print(
            "The program did not recieve required amount of arguments!\n" +
            "    Run the program with following command app.py 'Path_to.file' 'Length of generation'"
        )