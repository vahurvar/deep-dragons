import numpy as np
from game import Game
from keras.models import load_model

model = load_model('models/neural_network.h5')

games = 10

won = 0
for _ in range(games):
    game = Game()

    weather_input = game.get_encoded_weather_representation()
    knight_input = [game.attack, game.armor, game.agility, game.endurance]

    model_input = np.concatenate([weather_input, knight_input]).reshape((1,9))

    prediction = np.round(model.predict(model_input))[0]

    dragon = {
        'scaleThickness': int(prediction[0]),
        'clawSharpness': int(prediction[1]),
        'wingStrength': int(prediction[2]),
        'fireBreath': int(prediction[3]),
    }

    # All zeroes, send empty dragon
    if np.all(prediction==0):
        dragon = None

    print('Trained dragon: ', dragon)

    result = game.submit(dragon)
    print('Result: ', result)
    
    if result == 'Victory':
        won += 1

    print('------------')

print('Won: ', won)
print('Total: ', games)
print('Accuracy: ', won/games)