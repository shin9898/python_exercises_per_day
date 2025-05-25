---

### 📝 Python基礎力強化 - Day32

---

お疲れ様です！Python基礎力強化、いよいよDay32です。前回は少し難易度の高い問題でしたが、それだけに応用力が問われる内容でした。今回は、前回の反省点を踏まえつつ、同じような**データ結合、集計、フィルタリング、ソート**のスキルを確実に身につけるためのリベンジ問題です。

前回のフィードバックで提案したアプローチを参考に、ステップごとに解決していくことを意識して取り組んでみてください。

---

### 問題

あなたはとあるオンライン学習プラットフォームの運営者で、コースの受講状況と生徒の進捗データを分析しています。
以下のコースデータと受講生データ（それぞれリスト内に辞書形式で格納されています）が与えられます。
```python
courses = [
    {"course_id": "C001", "name": "Python Basics", "category": "Programming", "level": "Beginner"},
    {"course_id": "C002", "name": "Web Development with Django", "category": "Programming", "level": "Intermediate"},
    {"course_id": "C003", "name": "Data Science Fundamentals", "category": "Data Science", "level": "Beginner"},
    {"course_id": "C004", "name": "Machine Learning Advanced", "category": "Data Science", "level": "Advanced"},
    {"course_id": "C005", "name": "Cloud Computing Essentials", "category": "Cloud", "level": "Intermediate"},
]

enrollments = [
    {"student_id": "S001", "course_id": "C001", "progress": 80},
    {"student_id": "S002", "course_id": "C001", "progress": 100},
    {"student_id": "S003", "course_id": "C002", "progress": 50},
    {"student_id": "S004", "course_id": "C003", "progress": 90},
    {"student_id": "S005", "course_id": "C001", "progress": 70},
    {"student_id": "S006", "course_id": "C004", "progress": 20},
    {"student_id": "S007", "course_id": "C003", "progress": 100},
    {"student_id": "S008", "course_id": "C002", "progress": 100},
]
```

**以下の要件を満たすPythonコードを記述してください。**

1.  **"Programming" カテゴリのコースのみを抽出**し、そのリストを作成する。
2.  抽出されたProgrammingコースのうち、**一人でも受講生が登録している**コースのみをさらにフィルタリングする。
3.  フィルタリングされたコースリストから、各コースの`"name"`と、そのコースに登録している**受講生の人数**（`num_students`）を新しい辞書のリストとして出力する。
4.  出力リストは、`num_students`が**多い順**にソートし、人数が同じ場合は`course_name`の**昇順**でソートする。

**期待する出力形式:**

```python
[
    {'course_name': 'Python Basics', 'num_students': 3},
    {'course_name': 'Web Development with Django', 'num_students': 2}
]