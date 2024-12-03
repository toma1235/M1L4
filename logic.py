from random import randint

import requests


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.hp = randint(200 ,400)
        self.power = randint(30 ,60)
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://static.wikia.nocookie.net/pokemon/images/0/0d/025Pikachu.png/revision/latest/scale-to-width-down/1000?cb=20181020165701&path-prefix=ru"

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
        return f"Hp = {self.hp}\nPower = {self.power}\nName = {self.name}"
        

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard): 
            chanche = randint(1,5)
            if chanche == 1:
                return  " Pokemnon wizard used a shield"
        if enemy.hp > self.power:
            self.power = randint(30, 60)
            enemy.hp -= self.power
            return f"{self.name} нанес {self.power} урона {enemy.name}"
        else:
            enemy.hp = 0
            return f" {self.name} victory against {enemy.name}"
        
class Wizard(Pokemon):
    
    def info(self):
        return f"You got a pokemon wizard with " + super().info()

    
class Fighter(Pokemon):
    
    
    
    def attack(self,enemy):
        superpower = randint(5,15)
        self.power += superpower
        result = super().attack(enemy)
        self.power -= superpower
        return result + f"\n Fighter use a super power attack:{superpower}"
    
    def info(self):
        return f"You got a pokemon fighter with " + super().info()
    
    
if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))

        
    
    
    