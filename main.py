def text_to_morse(text):
    # Character to Morse decoder
    char_to_morse = {'A': "._", 'B': "_...", 'C': ".. .", 'D': "_..", 'E': ".", 'F': "._.",
                     'G': "__.", 'H': "....", 'I': "..", 'J': "_._.", 'K': "_._", 'L': "._..",
                     'M': "__", 'N': "_.", 'O': "___", 'P': ".__.", 'Q': "__._", 'R': "._.",
                     'S': "...", 'T': "_", 'U': ".._", 'V': "..._", 'W': ".__", 'X': "_.._",
                     'Y': "_.__", 'Z': "__..",

                     '0': "_____", '1': ".____", '2': "..___",
                     '3': "...__", '4': "...._", '5': ".....", '6': "_....", '7': "__...",
                     '8': "___..", '9': "____.",

                     ',': ",__..__", '.': "._._._", '?': "..__..", ';': "_._._.", ':': "___...",
                     '/': "_.._.", '-': "_...._", "'": ".____.", '"': "._.._.", '_': "..__._",
                     '(': "_.__.", ')': "_.__._", '=': "_..._", '+': "._._.", '*': "_.._",
                     '@': ".__._.", ' ': "/",

                     'Á': ".__._", 'Ä': "._._", 'É': ".._..", 'Ñ': "__.__",
                     'Ö': "___.", 'Ü': "..__"}
    morse = ''
    for i in range(0, len(text)):
        # Convert possible letter to uppercase
        char = str.upper(text[i])

        # Find corresponding Morse Code character and add to string
        morse += char_to_morse[char]
        morse += ' '
    print(f"{text} in Morse Code is:\n {morse}")

if __name__ == '__main__':
    text = input("Please enter a string text: ")
    text_to_morse(text)