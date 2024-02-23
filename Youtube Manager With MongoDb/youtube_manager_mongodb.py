# import pymongo
from pymongo import MongoClient
from bson import ObjectId

# client = pymongo.MongoClient("mongodb+srv://saptarshesinha:th7fYAiONqtYypXb@cluster0.bngzluj.mongodb.net/ytmanager")
# client = MongoClient("mongodb+srv://saptarshesinha:th7fYAiONqtYypXb@cluster0.bngzluj.mongodb.net/ytmanager") #The name after '/'is the db name i.e "ytmanager"

# or, we can initialize db as follows

client = MongoClient("mongodb+srv://saptarshesinha:th7fYAiONqtYypXb@cluster0.bngzluj.mongodb.net/", tlsAllowInvalidCertificates=True)
db = client["ytmanager"]
# db = client.ytmanger

# Not a good idea to include id and password in codefiles
# tlsAllowInvalidCertificates=True - Not a good way to handle set

video_collection = db["videos"]  # creating a collection/model

# print(video_collection)

def list_videos():
    videos = video_collection.find()
    for vid in videos:
        print(f"Id: {vid['_id']}, Name: {vid['name']} and Time: {vid['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {"name": new_name, "time": new_time}})

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to update: ")
            delete_video(video_id)
        elif choice == '5':
            break       
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()