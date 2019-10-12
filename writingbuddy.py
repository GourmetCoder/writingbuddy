import logic.sentence_generator as sentence_generator
import utility.argument_not_defined_error as argument_not_defined_error
import sys
import logic.file_loader as file_loader

if __name__ == '__main__':

    try:
        cleaner = []
        if len(sys.argv) < 2:
            raise argument_not_defined_error.ArgumentNotDefinedError
        if len(sys.argv) > 2:
            loader = file_loader.FileLoader(sys.argv[2])
            split_cleaner_file = loader.load_file().split("\n")
            cleaner = [pair.split("|||") for pair in split_cleaner_file]
        generator = sentence_generator.SenteceGenerator(sys.argv[1], clean_list=cleaner)
        exceptions_list = [
            "mr.",
            "mrs.",
            "mx.",
            "ms.",
        ]
        final_out_put = []
        while True:
            generated_text = generator.generate_sentence(final_exceptions=exceptions_list)
            print(generated_text)
            keep = input("Keep line y/n (q - quit) ")
            if keep == 'y':
                final_out_put.append(generated_text)
            elif keep == 'q':
                break
            print("")
        print("\n\n".join(final_out_put))
    except argument_not_defined_error.ArgumentNotDefinedError:
        print("The program did not recieve required amount of arguments!/n")
        print("    Run the program with following command app.py 'Path_to.file' 'cleaner file'")