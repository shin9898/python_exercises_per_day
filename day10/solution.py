class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score


class ScoreManager:
    def __init__(self):
        self.players_list: list[Player] = []

    def add_player(self, player: Player) -> None:
        self.players_list.append(player)

    def get_top_scorer(self) -> str:
        top_scorer = max(self.players_list, key=lambda player: player.score)
        return top_scorer.name
    
    def get_average_score(self) -> int:
        scores_list = [player.score for player in self.players_list]
        return round(sum(scores_list) / len(scores_list), 2)


if __name__ == "__main__":
    manager = ScoreManager()
    manager.add_player(Player("Alice", 95))
    manager.add_player(Player("Bob", 87))
    manager.add_player(Player("Charlie", 92))

    print(manager.get_top_scorer())  # => "Alice"
    print(manager.get_average_score())  # => 91.33