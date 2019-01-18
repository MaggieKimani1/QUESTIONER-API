meetup_schema = {
    "type": "object",
    "properties": {
        "location": {type: "string"},
        "topic": {type: "string"},
        "happeningOn": {type: "string"},
        "tags": {type: "string"},
    },
    "required": ["location", "topic", "happeningOn", "tags"]
}

question_schema = {
    "type": "object",
    "properties": {
        "topic": {type: "string"},
        "body": {type: "string"},
        "upvotes": {type: "string"},
        "downvotes": {type: "string"},
    },
    "required": ["topic", "body", "upvotes", "downvotes"]
}
