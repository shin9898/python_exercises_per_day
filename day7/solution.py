from collections import Counter
import datetime


class Reservation:
    def __init__(self, user_name: str, event_name: str, date: str):
        self.user_name = user_name
        self.event_name = event_name
        self.date = date

    def __repr__(self):
        return f"Reservation(user_name='{self.user_name}', event_name='{self.event_name}', date='{self.date}')"


class ReservationManager(Reservation):
    def __init__(self):
        self.reservation_list = []

    def add_reservation(self, reservation: Reservation):
        self.reservation_list.append(reservation)

    def find_by_user(self, user_name: str) -> list[Reservation]:
        result = [repr(r) for r in self.reservation_list if r.user_name == user_name]
        return result
    
    def get_reservation_count_by_date(self) -> dict[str, int]:
        result = Counter(d.date for d in self.reservation_list)
        return result



if __name__ == "__main__":
    # テストデータ登録
    manager = ReservationManager()
    manager.add_reservation(Reservation("Alice", "Yoga", "2025-05-01"))
    manager.add_reservation(Reservation("Bob", "Yoga", "2025-05-01"))
    manager.add_reservation(Reservation("Charlie", "Dance", "2025-05-02"))

    # 検索・集計処理
    print(manager.find_by_user("Alice"))
    print(manager.get_reservation_count_by_date())