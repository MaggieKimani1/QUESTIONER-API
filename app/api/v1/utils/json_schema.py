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
        "meetup": {type: "int"},
        "topic": {type: "string"},
        "body": {type: "string"},
        "upvotes": {type: "string"},
        "downvotes": {type: "string"},
    },
    "required": ["meetup", "topic", "body", "upvotes", "downvotes"]
}
