from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, pokemon_trainer_id):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.level = self.get_level()
        self.pokemon_trainer_id = pokemon_trainer_id
        


        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"  
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']["official-artwork"]["front_default"])
        else:
            return "https://www.google.com/imgres?q=pokemon&imgurl=https%3A%2F%2Fcdn.pixabay.com%2Fphoto%2F2021%2F12%2F26%2F17%2F31%2Fpokemon-6895600_1280.png&imgrefurl=https%3A%2F%2Fpixabay.com%2Fit%2Fimages%2Fsearch%2Fpok%25C3%25A9mon%2520vai%2F&docid=WWYqmh1yECd_qM&tbnid=sRHHBuRnPjqtSM&vet=12ahUKEwi9kqq4rvqJAxUElf0HHZBiIhUQM3oFCIABEAA..i&w=1280&h=1280&hcb=2&ved=2ahUKEwi9kqq4rvqJAxUElf0HHZBiIhUQM3oFCIABEAA"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name} \n Trainer's name is {self.pokemon_trainer} \n Trainer's id is {self.pokemon_trainer_id}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    
    def get_level(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['moves'][0]['version_group_details'][0]["level_learned_at"])
        else:
            return "Pikachu"
        
    



