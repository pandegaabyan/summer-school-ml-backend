import flask
app = flask.Flask(__name__)

my_data = {
        "data":{
                1:{"name":"Pandega", "score":90}, 
                2:{"name":"Abyan", "score":85}
                },
        "last_id":2
        }

def get_data(id=None):
    if id == None:
        return my_data["data"]
    else:
        return my_data["data"][id]

def add_data(new_data):
    id = my_data["last_id"] + 1
    my_data["data"].update({id:new_data})
    my_data["last_id"] = id

def update_data(id, new_data):
    if id in my_data["data"].keys():
        my_data["data"].update({id:new_data})
    else:
        raise KeyError("id not exist")

def delete_data(id):
    my_data["data"].pop(id)

@app.route("/data", defaults={"id":None}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/data/<int:id>", methods=["GET", "POST", "PUT", "DELETE"])
def handle_data(id=None):
    if flask.request.method == "GET":
        try:
            response = get_data(id)
            return response
        except Exception as e:
            print(e)
            return "Error"
    elif flask.request.method == "POST" and id == None:
        try:
            new_data = flask.request.json
            add_data(new_data)
            return "Success"
        except Exception as e:
            print(e)
            return "Error"
    elif flask.request.method == "PUT" and id != None:
        try:
            new_data = flask.request.json
            update_data(id, new_data)
            return "Success"
        except Exception as e:
            print(e)
            return "Error"

    elif flask.request.method == "DELETE" and id != None:
        try:
            delete_data(id)
            return "Success"
        except Exception as e:
            print(e)
            return "Error"

if __name__ == "__main__":
    app.run(debug=True)