Shitpost Bot (Version 4: The open source one)

Shitpost bot is a robot designed for Twitter that allows for random "Cards Against Humanity" style tweets.

Shitpost bot takes input from 4 files:

questions.txt -- the fill-in-the-blank style questions that the robot uses as a template. The space where the word will be added must be replaced by %s in order to allow for correct formatting, and each question should be on its own line. Not all questions have to have a blank. Some can be considered Stand alone questions, that require no blanks to be added.

blanks.txt -- the text that goes in the blanks from questions.txt Each blank must be on its own line.

hashtags.txt -- hashtags that can be appended to the end of tweets. Each hashtag must be on it's own line

mentions.txt -- list of @ usernames that can be appended to the end of tweets. Each mention must be on it's own line and begin with @
