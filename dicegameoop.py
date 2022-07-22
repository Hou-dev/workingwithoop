#WIP
import random


class Die:
    def __init__(self):
        self._value = None
    
    @property
    def value(self):
        return self._value
    
    def roll(self):
        new_value = random.randint(1,6)
        self._value = new_value
        return new_value


class Player:
    def __init__(self,die,is_computer=False):
        self._die = die
        self._is_computer = is_computer
        self._counter = 10

    @property
    def die(self):
        return self._die
    
    @property
    def is_computer(self):
        return self._is_computer 
    
    @property
    def counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1
        
    def decrement_counter(self):
        self._counter -= 1
        
    def roll_die(self):
        return self._die.roll()
    

class DiceGame:
    def __init__(self,player,computer):
        self.player = player
        self.computer = computer
        
    def play(self):
        print("++++++++++++++++++++")
        print("Welcome to Die Game")
        print("++++++++++++++++++++")
        while True:
            self.play_round()
    
    def play_round(self):
        self.print_welcome_round()
        
        player_value = self.player.roll_die()
        computer_value = self.computer.roll_die()
        
        self.show_die(player_value, computer_value)
        
        
        if player_value > computer_value:
            print("Player won the round")
            self.winner_upate(winner=self.player, loser= self.computer)
 
        elif player_value < computer_value:
            print("Computer won the round")
            self.winner_upate(winner=self.computer, loser= self.player)
            
        else:
            print("This round is a draw")
            
        self.display_counter()
 
    def print_welcome_round(self):
        print("++++++New Round++++++++")
        input("Press any key to roll")
    
    def show_die(self, player_value, computer_value):
        print(f"Your die: {player_value}")
        print(f"Computer die: {computer_value}")
        
    def winner_upate(self, winner, loser):
        winner.decrement_counter()
        loser.increment.counter()
        
    def display_counter(self):
        print(f"Player counter: {self.player.counter}")
        print(f"Computer counter: {self.computer.counter}")
        
        
player_die = Die()
computer_die = Die() 

my_player = Player(player_die, False)
computer_player = Player(computer_die, True)

game = DiceGame(my_player, computer_die)

game.play()