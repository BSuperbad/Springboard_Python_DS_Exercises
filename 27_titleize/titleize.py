def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_phrase = ''
    for word in phrase.split():
        new_word = word[0].upper() + word[1:].lower()
        new_phrase += new_word + ' '
    return new_phrase[:-1]

# return phrase.title()
