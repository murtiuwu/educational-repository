def find_a_palindrome(text):
    quantity = 0
    word_list = text.split(' ')
    for letter in text:
        if letter.lower() in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz ':
            pass
        else:
            print("Используются только буквы!")
            quantity = -999999999
            break
    for word in word_list:
        if len(word) == 1:
            quantity -= 1
        quantity += [1 if word[i] is word[-(i+1)] else 0 for i in range((len(word) + 1) // 2)]

    return quantity


print(find_a_palindrome('я люблю свой шалаш'))



