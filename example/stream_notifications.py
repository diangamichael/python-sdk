import elarian

# Initialize SDK
sandbox = True
api_key = 'fake_key'
elarian_service = elarian.initialize(sandbox, api_key)

# build request
req = elarian.requests.StreamNotificationRequest(app_id="fake-id")

# stream
stream = elarian_service.StreamNotifications(req)

for notification in stream:
    print(notification)
