# 🚀 Tải Video từ Google Drive lên YouTube bằng Google Colab

Chào mừng bạn đến với hướng dẫn này! 👋 Ở đây, chúng ta sẽ sử dụng Google Colab để tải video trực tiếp từ Google Drive lên YouTube bằng YouTube API. 📹

## 🔧 Yêu Cầu

- Tài khoản Google với quyền truy cập YouTube và Google Drive.
- Đã thiết lập thông tin xác thực OAuth 2.0 trên [Google Cloud Console](https://console.cloud.google.com/).
- Quyền truy cập vào Google Colab (bạn chỉ cần một tài khoản Google).

## 📝 Hướng Dẫn Chi Tiết

### 1. Thiết Lập OAuth 2.0 Credentials

1. Truy cập [Google Cloud Console](https://console.cloud.google.com/).
2. Tạo một dự án mới hoặc chọn một dự án hiện có.
3. Chuyển đến **APIs & Services > Credentials**.
4. Nhấp vào **+ CREATE CREDENTIALS** và chọn **OAuth 2.0 Client ID**.
5. Thiết lập **OAuth consent screen**:
   - Chọn **External**.
   - Điền vào các trường bắt buộc như **App Name**, **User support email**, và **Developer contact information**.
   - Nhấn **Save and Continue**.
6. Quay lại trang **Credentials**:
   - Chọn **Web application** cho loại ứng dụng.
   - Trong phần **Authorized redirect URIs**, thêm: `https://developers.google.com/oauthplayground`.
   - Nhấn **Create** và sao chép lại **Client ID** và **Client Secret**.

### 2. Sử Dụng OAuth 2.0 Playground

1. Truy cập [OAuth 2.0 Playground](https://developers.google.com/oauthplayground).
2. Ở góc trên phải, nhấp vào biểu tượng **⚙️** (Cài đặt).
   - Đánh dấu chọn **Use your own OAuth credentials**.
   - Nhập **Client ID** và **Client Secret** mà bạn đã tạo ở bước trên.
3. Trong **Step 1: Select & authorize APIs**:
   - Chọn các phạm vi:
     - `https://www.googleapis.com/auth/youtube.upload` (để tải video lên YouTube).
     - `https://www.googleapis.com/auth/drive.readonly` (để truy cập đọc file từ Google Drive).
   - Nhấp vào **Authorize APIs** và đăng nhập vào tài khoản Google của bạn.
4. Trong **Step 2**:
   - Nhấp vào **Exchange authorization code for tokens** để lấy `Access Token` và `Refresh Token`.
   - Sao chép lại `Access Token` để sử dụng trong Google Colab.

### 3. Thực Hiện Trên Google Colab

1. Tải mã Python từ tệp [`upload_video_to_youtube.py`](upload_video_to_youtube.py) trong repository này.
2. Mở một notebook mới trên [Google Colab](https://colab.research.google.com/).
3. Tải lên mã Python từ tệp đã tải và thay thế các biến cần thiết bằng thông tin của bạn.
4. Chạy mã trên Google Colab để tải video lên YouTube.

### 4. Lưu Ý

- `access_token` có thể hết hạn sau 1 giờ. Nếu gặp lỗi, hãy tạo lại `access_token`.
- Đảm bảo bạn đã thêm đúng địa chỉ email trong phần **Test Users** trong **OAuth consent screen** nếu ứng dụng chưa được chuyển sang chế độ sản xuất.

## 📂 Mã Python

Mã đầy đủ có thể được tìm thấy trong tệp [upload_video_to_youtube.py](upload_video_to_youtube.py).

## 🌟 Đóng Góp

Nếu bạn có bất kỳ đề xuất hoặc vấn đề nào, vui lòng tạo một [Issue](https://github.com/your-repo/issues) hoặc gửi pull request. Chúng tôi luôn hoan nghênh sự đóng góp của bạn! 🙌

## 📜 Bản Quyền

Phần mềm này được cung cấp theo [MIT License](LICENSE). Vui lòng xem tệp LICENSE để biết thêm thông tin.

---

Chúc bạn tải video lên YouTube thành công! 🎉
