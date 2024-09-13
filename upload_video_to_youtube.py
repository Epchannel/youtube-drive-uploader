from google.colab import drive
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

# Mount Google Drive để truy cập file
drive.mount('/content/drive', force_remount=True)

# Đường dẫn đến file video trên Google Drive
video_file_path = '/content/drive/MyDrive/YourFolder/your_video.mp4'  # Thay thế bằng đường dẫn đến file video của bạn

# Sử dụng access token để xác thực với API YouTube
access_token = 'YOUR_ACCESS_TOKEN'  # Thay thế bằng access_token bạn vừa nhận được

# Khởi tạo credentials từ access token
credentials = Credentials(token=access_token)

# Khởi tạo API client cho YouTube
youtube = build('youtube', 'v3', credentials=credentials)

# Cấu hình metadata cho video
request_body = {
    'snippet': {
        'categoryId': '22',  # Danh mục video: 22 là cho 'People & Blogs'
        'title': 'Tiêu đề video của bạn',
        'description': 'Mô tả video của bạn',
        'tags': ['tag1', 'tag2']
    },
    'status': {
        'privacyStatus': 'public'  # 'public', 'private', hoặc 'unlisted'
    }
}

# Tải video lên YouTube
media = MediaFileUpload(video_file_path, chunksize=-1, resumable=True, mimetype='video/*')

response = youtube.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=media
).execute()

print(f"✅ Video đã tải lên thành công. ID video: {response['id']}")
