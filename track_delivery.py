def track_delivery(tracking_number):
    mock_data = {"123456789012": "In Transit", "location": "Houston, TX": "excepted_delivery": "2024-12-27"}

    
    
    #Return status if the tracking number status 
    return mock_data.get(tracking_number)