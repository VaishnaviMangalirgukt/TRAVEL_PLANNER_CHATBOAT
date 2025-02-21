import os

# Force REST API mode and disable gRPC
os.environ["GOOGLE_API_USE_REST"] = "true"
os.environ["PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION"] = "python"
os.environ["GRPC_POLL_STRATEGY"] = "none"

import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyD69MNQjIlhlfm8ICjzLrhRvwC4LPPkbQc")

# Initialize model
model = genai.GenerativeModel("gemini-pro")

def get_travel_info(user_input):
    """Fetch structured travel recommendations using Gemini API with more destinations, hotels, and flights."""
    prompt = f"""
    Provide a **detailed** structured travel guide for a trip to {user_input}.
    
    **Ensure you list at least 35-40 destinations**, categorized into:
    - **Top Attractions** (Famous landmarks, must-visit places)
    - **Hidden Gems** (Lesser-known but unique places)
    
    Also include:
    - Best time to visit
    - Activities
    - Estimated budget range
    - **At least 15-30 hotel recommendations** across different budget ranges:
      - **Budget (1-3 star) hotels**
      - **Mid-range (4-star) hotels**
      - **Luxury (5-star) hotels**
    - Include approximate price ranges for hotels.
    - **Flight information**:
      - Major airports near {user_input}
      - Airlines operating to {user_input}
      - Approximate airfare ranges for economy and business class
      - Best time to book flights for cheaper fares

    Format the response with bullet points and clear sections.
    """
    
    response = model.generate_content(prompt)
    
    return response.text if response else "No recommendations available."
