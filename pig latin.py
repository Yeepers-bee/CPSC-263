
def to_pig_latin(word):
    # Remove punctuation
    punctuation = ''
    while word and not word[-1].isalnum():
        punctuation = word[-1] + punctuation
        word = word[:-1]
    
    if not word:
        return punctuation
    
    # Check if word starts with vowel
    if word[0].lower() in 'aeiou':
        result = word + 'way'
    else:
        vowel_pos = 0
        word_chars = list(word.lower())
        found_vowel = False

        for i in range(len(word_chars)):
            char = word_chars[i]
            if char in 'aeiou':
                vowel_pos = i
                found_vowel = True
                break

        
    
        result = word[vowel_pos:] + word[:vowel_pos] + 'ay' 
    return result

def translate_text(text):
    words = text.split()
    translated_words = [to_pig_latin(word) for word in words]
    return ' '.join(translated_words)

def main():
    print("Pig Latin Translator\n")
    
    while True:
        text = input("Enter text: ")
        english_text = text.lower()
        pig_latin = translate_text(english_text)
        print(f"English:\t{english_text}")
        print(f"Pig Latin:\t{pig_latin} \n")
        continue_choice = input("Continue? (y/n): ")
        if continue_choice != 'y':
            print("\nBye!")
            break
        print()

if __name__ == "__main__":
    main()










