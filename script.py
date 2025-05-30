# Импорт модуля для случайных чисел
import random


class Blackjack:
    def __init__(self):
        # Создаем колоду: 4 масти по 13 карт (2-10, JQK=10, A=11)
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(self.cards)  # Перемешиваем колоду
        self.player = []  # Карты игрока
        self.dealer = []  # Карты дилера

    def deal(self):
        # Берем последнюю карту из колоды (и удаляем ее из колоды)
        return self.cards.pop()

    def score(self, hand):
        # Считаем сумму очков
        total = sum(hand)
        # Если перебор и есть туз (11), меняем его на 1
        if total > 21 and 11 in hand:
            total -= 10  # Эквивалентно замене 11 на 1
        return total

    def play(self):
        # Начальная раздача по 2 карты
        self.player = [self.deal(), self.deal()]
        self.dealer = [self.deal(), self.deal()]

        # Ход игрока
        while True:
            current = self.score(self.player)
            print(f"Ваши карты: {self.player} ({current})")
            print(f"Дилер: {self.dealer[0]} и ?")

            if current >= 21:  # Если уже 21 или перебор
                break

            if input("Еще? (д/н): ") == 'д':
                self.player.append(self.deal())  # Добавляем карту
            else:
                break

        # Ход дилера (берет пока меньше 17)
        while self.score(self.dealer) < 17:
            self.dealer.append(self.deal())

        # Определяем результат
        player_score = self.score(self.player)
        dealer_score = self.score(self.dealer)

        print(f"\nВы: {self.player} ({player_score})")
        print(f"Дилер: {self.dealer} ({dealer_score})")

        if player_score > 21:
            print("Перебор! Вы проиграли")
        elif dealer_score > 21 or player_score > dealer_score:
            print("Вы выиграли!")
        elif player_score < dealer_score:
            print("Вы проиграли")
        else:
            print("Ничья")


# Запуск игры
if __name__ == "__main__":
    while True:
        game = Blackjack()
        game.play()
        if input("\nСыграем еще? (д/н): ") != 'д':
            break