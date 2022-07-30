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

## handle request here

if __name__ == "__main__":
    app.run(debug=True)