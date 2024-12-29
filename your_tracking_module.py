# your_tracking_module.py

import requests

def track_delivery(tracking_number):
    """
    Tracks a delivery using a mock API or external tracking service.
    
    Args:
        tracking_number (str): The tracking number provided by the user.
    
    Returns:
        dict or None: Delivery status details if tracking is successful, otherwise None.
    """
    # Simulated API endpoint (replace with an actual API URL)
    API_URL = "https://api.mocktracking.com/track"
    API_KEY = "your-api-key"  # Replace with your actual API key

    # Ensure the tracking number is valid
    if not tracking_number or len(tracking_number) < 5:
        return None  # Return None for invalid tracking numbers

    try:
        # Make a GET request to the external API with the tracking number
        response = requests.get(
            API_URL,
            params={"tracking_number": tracking_number},
            headers={"Authorization": f"Bearer {API_KEY}"}
        )

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check for errors in the API response
        if data.get("error"):
            return None

        # Return delivery status details
        return {
            "tracking_number": tracking_number,
            "status": data.get("status", "Unknown"),
            "expected_delivery": data.get("expected_delivery", "Unknown"),
            "location": data.get("current_location", "Unknown")
        }

    except requests.exceptions.RequestException as e:
        # Log the error for debugging purposes
        print(f"Error tracking delivery: {e}")
        return None
