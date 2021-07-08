# Introduction

This repo shows how to create a custom rest channel (using a [custom connnector](https://rasa.com/docs/rasa/connectors/custom-connectors/)) that will combine an an image and its text into a single speech bubble.

# Usage

The body to send is:

```json
{
  "sender": "test_user",  
  "message": "I am sad!"
}
```

Sending it to `http://localhost:5005/webhooks/rest/webhook` gives:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/9Hkx8C2/image.png" alt="image" border="0"></a>

but sending it to `http://localhost:5005/webhooks/custom_rest/webhook` gives:

<a href="https://imgbb.com/"><img src="https://i.ibb.co/GdRtYSq/image-1.png" alt="image-1" border="0"></a>
