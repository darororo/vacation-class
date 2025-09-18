import requests
import json

# --- Entity ---
class Joke:
    def __init__(self, id, type, setup, punchline):
        self.id = id
        self.type = type
        self.setup = setup
        self.punchline = punchline

    def __repr__(self):
        return f"Joke({self.id}, {self.type}, {self.setup}, {self.punchline})"


# --- Remote Repository ---
class JokeRemoteRepository:
    API_URL = "https://official-joke-api.appspot.com/random_joke"

    def get_joke(self) -> Joke:
        response = requests.get(self.API_URL)
        if response.status_code == 200:
            data = response.json()
            return Joke(**data)   # unpack dict into Joke constructor
        else:
            raise Exception(f"Error fetching joke: {response.status_code}")


# --- Local Repository ---
class JokeLocalRepository:
    def __init__(self):
        self.jokes = []

    def add_joke(self, joke: Joke):
        self.jokes.append(joke)

    def get_all_jokes(self):
        return self.jokes
    
class JokeService:
    def __init__(self, local_repo: JokeLocalRepository, remote_repo: JokeRemoteRepository):
        self.local_repo = local_repo
        self.remote_repo = remote_repo

    def fetch_and_store_joke(self) -> Joke:
        """Fetch a joke from the remote API and store it locally."""
        joke = self.remote_repo.get_joke()
        self.local_repo.add_joke(joke)
        return joke

    def get_all_local_jokes(self):
        """Return all jokes stored locally."""
        return self.local_repo.get_all_jokes()


# --- Usage ---
if __name__ == "__main__":
    local_repo = JokeLocalRepository()
    remote_repo = JokeRemoteRepository()
    service = JokeService(local_repo, remote_repo)

    # Fetch from API and save locally
    joke = service.fetch_and_store_joke()
    print("Fetched new joke:", joke)

    # Get all stored jokes
    print("Local jokes:", service.get_all_local_jokes())