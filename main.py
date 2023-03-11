import requests
token='15951e4e4f9896da66a7e30b976f4135'
response=requests.post('https://pokemonbattle.me:9104/pokemons', headers = {'trainer_token' : token, 'Content-Type': 'application/json' } , 
                       json={"name": "Бульбазавр", "photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print (response.text)
name_pokemons_response=requests.put('https://pokemonbattle.me:9104/pokemons', headers = {'trainer_token' : token, 'Content-Type': 'application/json' } , 
                      json={"pokemon_id": 6121,"name": "Пикачу","photo": "https://dolnikov.ru/pokemons/albums/010.png"})
print(name_pokemons_response.text)
pokeball_response=requests.post('https://pokemonbattle.me:9104//trainers/add_pokeball',headers = {'trainer_token' : token, 'Content-Type': 'application/json' } , 
                                json= {"pokemon_id": 6121})
print(pokeball_response.text)