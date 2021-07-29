# Introduction

This repo shows that you don't have to have all your synonyms appear in your training data.

# Explanation

These are your synonyms:

``` yaml
- intent: check_balance
  examples: |
    - how much do I have on my [credit card account](account)
    - how much do I owe on my [credit account](account)
- synonym: credit
  examples: |
    - credit card account
    - credit account
    - card
```
Note that `card` is a synonym of `credit` but `card` is not annotated with as an entity `account` in any of the intent examples.

However, `card` can still be mapped to `credit`!

```
Next message:
how much do I have on my card
{
  "text": "how much do I have on my card",
  "intent": {
    "id": -705010972093115399,
    "name": "check_balance",
    "confidence": 0.9981831312179565
  },
  "entities": [
    {
      "entity": "account",
      "start": 25,
      "end": 29,
      "confidence_entity": 0.9969789981842041,
      "value": "credit",
      "extractor": "DIETClassifier",
      "processors": [
        "EntitySynonymMapper"
      ]
    }
  ],
  ```

# Notes

There are two ways to specify synonyms:

1. Method 1:
```yaml
- intent: check_balance
  examples: |
    - how much do I have on my [credit card account]{"entity": "account", "value": "credit"}
    - how much do I owe on my [credit account]{"entity": "account", "value": "credit"}
```


2. Method 2:
```yaml
- intent: check_balance
  examples: |
    - how much do I have on my [credit card account](account)
    - how much do I owe on my [credit account](account)
    
- synonym: credit
  examples: |
    - credit card account
    - credit account
```
