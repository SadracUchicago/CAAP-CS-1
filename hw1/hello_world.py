###Hello World###
###By Jesus Almaraz Argueta###

#A function that writes a short poem based on inputs given by the user

def hello_world():
  name, state, color, pronouns = str(input('What is your name?\n>>')), str(input('What state are you from?\n>>')), str(input('What is your favorite color?\n>>')), str(input('What are your prefered pronouns?\n>>'))
  pronouns = str.lower(pronouns) #I am making sure the program can handle non-binary inputs
  if ('he' in pronouns) and ('she' not in pronouns):
    pronouns = 'he'
    possessive = 'his'
  elif ('she' in pronouns):
    pronouns = 'she'
    possessive = 'her'
  elif ('ze' in pronouns):
    pronouns = 'ze'
    possessive = 'zir'
  elif ('xe' in pronouns):
    pronouns = 'xe'
    possessive = 'xyr'
  elif ('ey' in pronouns):
    pronouns = 'ey'
    possessive = 'eir'
  elif ('ne' in pronouns):
    pronouns = 'ne'
    possessive = 'nir'
  elif ('they' in pronouns):
    pronouns = 'they'
    possessive = 'their'
  else:
    pronouns = 'they'
    possessive = 'their'
  print('\nI met a person, a nice person,\nBy the name of ' + name + '.\n' + color + ' ' + pronouns + ', told me,\nWas ' + possessive + ' favorite color.')
  if (str.lower(state) == 'california') or (str.lower(state) == 'louisiana') or (str.lower(state) == 'south carolina') or (str.lower(state) == 'north carolina'):
    if (pronouns == 'they'):
      print('From ' + state + ' they were.')
    else:
      print('From ' + state + ', ' + pronouns + ' was.')
  else:
    print('Oh, from ' + state + ' ' + pronouns + ' came.')