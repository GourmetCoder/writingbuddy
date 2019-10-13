import logic.sentence_generator as sentence_generator
import utility.argument_not_defined_error as argument_not_defined_error
import sys
import logic.file_loader as file_loader

if __name__ == '__main__':

    try:
        cleaner = []
        if len(sys.argv) < 3:
            raise argument_not_defined_error.ArgumentNotDefinedError
        loader = file_loader.FileLoader(sys.argv[2])
        split_cleaner_file = loader.load_file().split("\n")
        cleaner = [pair.split("|||") for pair in split_cleaner_file]
        generator = sentence_generator.SenteceGenerator(sys.argv[1], clean_list=cleaner)
        exceptions_list = [
            "mr.",
            "mrs.",
            "mx.",
            "ms.",
            '"mr.',
            '"mrs.',
            '"mx.',
            '"ms.',
            '“mr.',
            '“mrs.',
            '“mx.',
            '‘ms.',
            '‘mr.',
            '‘mrs.',
            '‘mx.',
            '‘ms.',
            'jr.'
        ]
        final_out_put = []
        start_word = None
        while True:
            generated_text = generator.generate_sentence(final_exceptions=exceptions_list, start_word=start_word)
            print(generated_text)
            keep = input("Keep line y/n (q - quit) ")
            if keep == 'y':
                start_word = generated_text.split(" ")[len(generated_text.split(" "))-1]
                final_out_put.append(generated_text)
                generator.record_names_from_sentence(generated_text)
            elif keep == 'q':
                break
            print("\n")
        print("\n\n".join(final_out_put))
    except argument_not_defined_error.ArgumentNotDefinedError:
        print("The program did not recieve required amount of arguments!/n")
        print("    Run the program with following command 'writingbuddy.py path_to.data path_to.cleaner'")