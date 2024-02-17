import os
from RegexConvFullFileRead import RegexConvFull  

class Main:
    @staticmethod
    def read():
        input_folder = os.path.join(os.path.dirname(__file__), '..', 'input')
        output_folder = os.path.join(os.path.dirname(__file__), '..', 'output')

        # Create 'input' folder if it doesn't exist
        os.makedirs(input_folder, exist_ok=True)

        # Check if 'input' folder is empty or has only non-Markdown files
        md_files = [f for f in os.listdir(input_folder) if f.endswith('.md')]
        if not md_files:
            print("A pasta 'input' está vazia ou não contém ficheiros Markdown (.md). Insira os ficheiros na pasta 'input'.")
            return

        # Create 'output' folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        for file_name in md_files:
            file_path = os.path.join(input_folder, file_name)
            try:
                with open(file_path, 'r') as file:
                    markdown_text = file.read()
                    html_output = RegexConvFull.markdown_to_html(markdown_text)
                    
                    output_path = os.path.join(output_folder, f"{os.path.splitext(file_name)[0]}.html")
                    
                    with open(output_path, "w") as output_file:
                        output_file.write(html_output)
                    print(f"Conversão bem sucedida. Ficheiro HTML guardado em '{output_path}'")
            except FileNotFoundError:
                print(f"File not found: {file_path}")
                
                
                
    def __init__(self):
        Main.read()
        

main_instance = Main()
