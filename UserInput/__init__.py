# informacion que el usuario ingreso se guarda en userInput que es un diccionario!
# https://www.w3schools.com/python/python_dictionaries.asp
# esta variable permite la comunicación entre distintos Frames

userInput = dict.fromkeys(['order', 'type', 'frequency', 'frequency2', 'gain', 'epsilon', 'inputFunction',
                          'inputAmplitude', 'inputFreq', 'poles' , 'zeros', 'transf'])

#THINGS INSIDE userInput

#"order" : 1, 2             Describes order of chosen filter
#"type": "low", "high", "band", "all", "notch", "guess"           Describes filter type
#"frequency"                List of key frequencies
#"poles"
#"zeros"
#"epsilon"
#'inputFunction'            "Bode", "Distribution", "Sine", "Step"
#'transf'                   Transfer function H
#
#
