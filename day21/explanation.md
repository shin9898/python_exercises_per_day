### ✅ 解答コードレビュー：Day21

```python
def discount_calculation(products: list[dict]) -> list[str]:
    return [f"{product['name']}の割引後の価格は{round(product['price'] * (1 - product['discount'] / 100))}円です" for product in products]


if __name__ == '__main__':
    products = [
        {"name": "Tシャツ", "price": 2000, "discount": 20.0},
        {"name": "ジーンズ", "price": 5000, "discount": 10.0},
        {"name": "帽子", "price": 1500, "discount": 0.0},
    ]
    print(discount_calculation(products))
```

---

### 🧠 評価（100 点満点中）

- **Pythonic な書き方**：25 / 25（リスト内包表記を適切に使用）
- **可読性**：23 / 25（多少長い式だが明瞭）
- **型ヒント**：20 / 20（引数の型ヒントあり）
- **仕様の網羅性**：20 / 20（すべての入力に対応）
- **エラーハンドリング**：5 / 10（割引が 100%以上、またはマイナスなどへの対策がない）

**総合得点：93 / 100 点**

---

### 💡 フィードバック

- `round()`関数を使って割引価格を整数にしており、実用的です。
- 内包表記が 1 行で完結していて非常に Pythonic です。
- ただし、割引率が 100%以上やマイナスの場合のバリデーションがない点がやや心配です。

```python
# 例：バリデーション追加（任意）
if not (0 <= product['discount'] <= 100):
    raise ValueError("割引率は0〜100の範囲である必要があります")
```

---

### 📈 次のステップに向けて

- 条件分岐を用いたバリデーションチェックや、`try`-`except`を用いた例外処理も徐々に取り入れていきましょう。
- Django ではユーザー入力を受けるため、こうしたバリデーションの考え方が非常に重要になります。

引き続きがんばっていきましょう 💪
