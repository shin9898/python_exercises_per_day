from collections import defaultdict

def filter_events(events: list[dict]) -> list[dict]:
    return list(filter(lambda event: "Tech" in event['category'], events))


def event_attendee_count(filtered_events: list[dict], participants: list[dict]) -> list[dict]:
    summary = defaultdict(lambda: {'num_participants': 0})
    for event in filtered_events:
        event_id = event['event_id']
        event_name = event['name']
        for participant in participants:
            registered_events = participant['registered_events']
            if event_id in registered_events:
                summary[event_name]['num_participants'] += 1
    return sorted(summary, key=lambda e: (e['num_participants'], e['event_id']))





if __name__ == '__main__':
    events = [
        {"event_id": "E001", "name": "Python Conference 2024", "category": "Tech", "date": "2024-07-10"},
        {"event_id": "E002", "name": "Data Science Summit", "category": "Tech", "date": "2024-08-05"},
        {"event_id": "E003", "name": "Marketing World Expo", "category": "Business", "date": "2024-09-01"},
        {"event_id": "E004", "name": "AI Innovation Forum", "category": "Tech", "date": "2024-07-20"},
        {"event_id": "E005", "name": "Product Design Workshop", "category": "Design", "date": "2024-08-15"},
    ]

    participants = [
        {"participant_id": "P001", "name": "Alice", "email": "alice@example.com", "registered_events": ["E001", "E004"]},
        {"participant_id": "P002", "name": "Bob", "email": "bob@example.com", "registered_events": ["E001", "E002"]},
        {"participant_id": "P003", "name": "Charlie", "email": "charlie@example.com", "registered_events": ["E003"]},
        {"participant_id": "P004", "name": "David", "email": "david@example.com", "registered_events": ["E002", "E005"]},
        {"participant_id": "P005", "name": "Eve", "email": "eve@example.com", "registered_events": ["E004"]},
    ]

    filtered_events = filter_events(events)
    print(event_attendee_count(filtered_events, participants))