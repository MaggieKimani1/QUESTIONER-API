import datetime
all_Questions = []


class Questions():
    '''Initialize class variables the questions model needs once it starts'''

    def __init__(self):

        pass

    def create_question(self, createdOn, createdBy, meetup, topic, upvotes, downvotes, body):
        question_payload = {
            "id": len(all_Questions)+1,
            "createdOn": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
            "createdBy": createdBy,
            "meetup": meetup,
            "topic": topic,
            "upvotes": upvotes,
            "downvotes": downvotes,
            "body": body
        }
        all_Questions.append(question_payload)
        return question_payload

    def upvote(self, question_id, vote):
        '''Vote a question'''

        question = [
            question for question in all_Questions if question['id'] == id
        ]
        if not question:
            return {"status": 404,
                    "message": "Question does not exist"}
        if vote == "+":
            action = "upvoted"
            new_upvotes = question[0]["upvotes"]+1
            new_downvotes = question[0]["downvotes"]
        elif vote == "-":
            action = "downvoted"
            new_upvotes = question[0]["upvotes"]
            new_downvotes = question[0]["downvotes"]+1

        question_payload = {
            "id":  question[0]['id'],
            "createdOn": question[0]['createdOn'],
            "createdBy": question[0]['createdBy'],
            "meetup": question[0]['meetup'],
            "topic": question[0]['topic'],
            "upvotes": new_upvotes,
            "downvotes": new_downvotes

        }

        for i, question in enumerate(all_Questions):
            if question['id'] == id:
                all_Questions[i] = question_payload

        return {"Message": 'You {} question {} successfully'.format(action, id)}, 200


# question = [{
#             "question_id": len(all_Questions)+1,
#             "createdOn": datetime.datetime.now().strftime("%y-%m-%d-%H-%M"),
#             "createdBy": createdBy,
#             "meetup": meetup,
#             "topic": topic,
#             "upvotes": upvotes,
#             "downvotes": downvotes

#         }]
