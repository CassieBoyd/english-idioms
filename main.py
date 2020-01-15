# Create a new Python file and paste the following code into it. At the end write a for in loop to produce the output below.

# OUTPUT
# Penny: A penny for your thoughts
# Injury: Add insult to injury
# Moon: Once in a blue moon
# Grape: I heard it through the grapevine
# Murder: Kill two birds with one stone
# Limbs: It costs an arm and a leg
# Grain: Take what someone says with a grain of salt
# Fences: I'm on the fence about it
# Sheep: Pulled the wool over his eyes
# Lucifer: Speak of the devil

# Make sure you join the strings

idioms = {
    "Penny": ["A", "penny", "for", "your", "thoughts"],
    "Injury": ["Add", "insult", "to", "injury"],
    "Moon": ["Once", "in", "a", "blue", "moon"],
    "Grape": ["I", "heard", "it", "through", "the", "grapevine"],
    "Murder": ["Kill", "two", "birds", "with", "one", "stone"],
    "Limbs": ["It", "costs", "an", "arm", "and", "a", "leg"],
    "Grain": ["Take", "what", "someone", "says", "with", "a", "grain", "of", "salt"],
    "Fences": ["I'm", "on", "the", "fence", "about", "it"],
    "Sheep": ["Pulled", "the", "wool", "over", "his", "eyes"],
    "Lucifer": ["Speak", "of", "the", "devil"],
}

# For/in loop uses .join to join all items in a dictionary into a string, using a separator (in this case either noSpace or space) to join the items together. The f in the print statement is an f-string. F-strings provide a concise and convenient way to embed python expressions inside string literals for formatting.
noSpace = ""
space = " "
for word in idioms:
    print(f"{noSpace.join(word)}: {space.join(idioms[word])}")