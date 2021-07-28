# Introduction

This repo demonstrates how to build an input validation loop using [Rules](https://rasa.com/docs/rasa/rules).

For more complex use cases, consider using [Forms](https://rasa.com/docs/rasa/forms) with a [custom action to validate the extracted input](https://rasa.com/docs/rasa/forms#validating-form-input). You can break out of a form's loop by returning the [ActionExecutionRejected](https://rasa.com/docs/rasa/forms#writing-stories--rules-for-unhappy-form-paths) event in the form's validation logic.

# Demo

The bot will repeatedly ask the user for a number between 1 and 10.

It will print the number the user gave.

If the user fails to provide a valid number 3 times, then the bot will move on to something else.

![](https://i.ibb.co/xzSSjKc/demo-loop.png)
