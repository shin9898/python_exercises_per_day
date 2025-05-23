問題
あなたはとあるイベント管理システムの担当者で、参加者とその参加イベントのデータを分析しています。
以下のイベントデータと参加者データ（それぞれリスト内に辞書形式で格納されています）が与えられます。

```Python

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
```
以下の要件を満たすPythonコードを記述してください。

"Tech" カテゴリのイベントのみを抽出し、そのリストを作成する。
抽出されたTechイベントに一人でも参加者が登録しているイベントのみをさらにフィルタリングする。
ヒント: 各イベントのevent_idと、各参加者のregistered_eventsを比較して確認できます。
最終的にフィルタリングされたイベントリストから、各イベントの"name"と、そのイベントに登録している参加者の人数（num_participants）を新しい辞書のリストとして出力する。
出力リストは、num_participantsが多い順にソートし、人数が同じ場合はevent_nameの昇順でソートする。
期待する出力形式:

```Python

[
    {'event_name': 'Python Conference 2024', 'num_participants': 2},
    {'event_name': 'AI Innovation Forum', 'num_participants': 2},
    {'event_name': 'Data Science Summit', 'num_participants': 2},
    # 以下、ソートされた順に続く
]
```
※注意点：期待する出力例は、問題の条件を全て満たした場合の正確な出力とは異なる可能性があります。ご自身で正確な出力を作成してください。あくまで出力形式の参考です。

今回は、複数のリストを横断して情報を結合・集計する能力が問われます。少し難易度が上がりますが、これまでの知識を総動員すれば必ず解けます。
