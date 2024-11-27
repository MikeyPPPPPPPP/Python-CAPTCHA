# This is a CAPTCHA made with the python module PIL

## This is for a website I'm making so I don't have to worry about bots.


## How to solve it?

The key is printed the same way you read a book.
There are 3 horizontal lines that have four charectors each, you need to combine the lines to make one big line. 

# captcha.py
```
botDetectionCaptcha = customCaptcha(".")
answare, new_image = botDetectionCaptcha.newCaptch()
```


