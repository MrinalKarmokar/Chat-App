from django.urls import re_path

websocket_urlpatters = [
    re_path(r'ws/chat/(?P<room_id>\w+)/$', consumers.ChatRoomConsumer)
]