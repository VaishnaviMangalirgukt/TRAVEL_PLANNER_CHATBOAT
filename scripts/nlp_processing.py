import os
import sys
import logging

# Completely suppress gRPC warnings
os.environ["GOOGLE_API_USE_REST"] = "true"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["GRPC_POLL_STRATEGY"] = "none"  # Disable gRPC polling strategy

# Redirect stderr (error output) to null (ignore warnings)
sys.stderr = open(os.devnull, 'w')

# Set logging level to ERROR (hides unnecessary logs)
logging.getLogger("grpc").setLevel(logging.CRITICAL)

# Add scripts directory to system path
sys.path.append("C:/Users/manga/OneDrive/Pictures/Travel_Planner_Chatbot/scripts")

from get_travel_info import get_travel_info
import re

def clean_input(user_input):
    """Cleans and preprocesses the user input."""
    user_input = user_input.lower().strip()
    user_input = re.sub(r'\s+', ' ', user_input)  # Remove extra spaces
    return user_input

def process_user_input(user_input):
    """Processes user input and fetches travel recommendations."""
    cleaned_input = clean_input(user_input)
    travel_info = get_travel_info(cleaned_input)
    return travel_info

# Run the script
if __name__ == "__main__":
    user_input = input("What kind of travel experience are you looking for? ")
    travel_info = process_user_input(user_input)
    print(f"Suggested Travel Information: {travel_info}")
