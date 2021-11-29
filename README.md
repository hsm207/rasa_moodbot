# Introduction

This repo shows how to customize the [two stage fallback](https://rasa.com/docs/rasa/fallback-handoff/#two-stage-fallback).

There are 3 things you can customize:
* action_default_ask_affirmation
* action_default_ask_rephrase
* action_default_fallback

# Customization

The two-stage fallback behavior is:

If the confidence of the predicted intent is less then 0.95 trigger NLU fallback.

If the confidence of the predicted intent is between 0.50 and 0.95, run the normal two-stage fallback mechanism.

If the confidence of the predicted intent is less than 0.5, skipp the two-stage fallback mechanism and call `action_default_fallback`.