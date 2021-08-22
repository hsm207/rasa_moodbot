# Introduction

This repo explains how AugmentedMemoization policy works based on [this](https://pub.towardsai.net/an-illustrated-explanation-of-how-rasas-augmentedmemoization-policy-works-da436aa20cff) Medium blog post.

# Usage

Train an augmented memoization policy on the basic stories and test it. This will fail.

```bash
rasa train core -c config_augmemo.yml -s data/stories_basic.yml && \
    rasa test core -s tests --fail-on-prediction-errors
```

Similarly, training the regular memoization policy will fail too:

```bash
rasa train core -c config_memo.yml -s data/stories_basic.yml && \
    rasa test core -s tests --fail-on-prediction-errors
```

The solution is to add a particular story to the training data:

```bash
rasa train core -c config_augmemo.yml -s data/stories_with_solution.yml && \
    rasa test core -s tests --fail-on-prediction-errors
```

But the same training set on the regular memoization policy won't work!

```bash
rasa train core -c config_memo.yml -s data/stories_with_solution.yml && \
    rasa test core -s tests --fail-on-prediction-errors -vv
```

To emphasise that the solution story must be written in a certain way:

```bash
rasa train core -c config_augmemo.yml -s data/stories_with_not_solution.yml && \
    rasa test core -s tests --fail-on-prediction-errors -vv
```

Test with regular memoization just for fun:

```bash
rasa train core -c config_memo.yml -s data/stories_with_not_solution.yml && \
    rasa test core -s tests --fail-on-prediction-errors -vv
```