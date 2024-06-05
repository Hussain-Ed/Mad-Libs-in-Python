story = "Today I went to the [adjective] zoo. I saw a [noun] swinging from a [noun]. I also saw a [noun] eating a [noun]. It was a very [adjective] day at the zoo!"

words_needed = ["adjective", "noun", "noun", "noun", "noun", "adjective"]

print(story)

for word in words_needed:
  replacement = input(f"Enter a(n) {word}: ")
  story = story.replace(f"[{word}]", replacement)

print(story)
