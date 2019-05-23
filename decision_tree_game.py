import numpy as np
from game import Game
import pickle

model = pickle.load(open('models/decision_tree.sav', 'rb'))

games = 10

won = 0
for _ in range(games):
    game = Game()

    weather_input = game.get_encoded_weather_representation()
    knight_input = [game.attack, game.armor, game.agility, game.endurance]

    model_input = np.concatenate([weather_input, knight_input]).reshape((1,9))

    prediction = model.predict(model_input)

    dragon = {
        'scaleThickness': int(prediction[0][0]),
        'clawSharpness': int(prediction[0][1]),
        'wingStrength': int(prediction[0][2]),
        'fireBreath': int(prediction[0][3]),
    }

    # All zeroes, send empty dragon
    if np.all(prediction[0]==0):
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