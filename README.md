# Introduction

This repo shows how to build an input validation loop using [Forms](https://rasa.com/docs/rasa/forms/#dynamic-form-behavior)

Click [here](https://github.com/hsm207/rasa_moodbot/tree/validaterule) for an approach using [Rules](https://rasa.com/docs/rasa/rules).

# Demo

The form will ask a user for a phone number.

All phone numbers are invalid except `110`.

If the user enters an invalid phone number more than 3 times, then the form will exit.

The form can also infer the phone number based on the value of the `mobile_number` and `fixedline_number` slots.

## Example 1

User provided a valid phone number within 3 attempts:
![](https://i.ibb.co/K65GqmX/form-valid.png)

## Example 2

User repeatedly provides an invalid phone number:

![](https://i.ibb.co/xMvKWvr/forms-fail-3-times.png)

## Example 3

Form infers the phone number and the phone number is invalid:

![](https://i.ibb.co/mDpyJ8k/forms-prefill-fail.png)

## Example 4

Form infers the phone number and the phone number is valid:

![](https://i.ibb.co/wwnjV9s/forms-prefill-successful.png)