# LUONG DANG – NHẠC, SÁCH, TIẾNG ANH

Trang chủ: **https://luongdang-blog.github.io**

| Mục | Thư mục | Địa chỉ |
|---|---|---|
| Trang cổng | `index.html` | / |
| Nhạc | `nhac/` | /nhac/ |
| Sách tóm tắt – phân tích | `sach/` | /sach/ |
| Học nghe và đàm thoại tiếng Anh | `tieng-anh/` | /tieng-anh/ |

Kiểu chữ, màu, thanh menu dùng chung: `assets/site.css`.
Thêm sách: đặt file bài phân tích vào `sach/` (tên không dấu, nối bằng gạch ngang), rồi thêm một dòng vào mảng `BOOKS` trong `sach/index.html`, điền `url`.

## Mục Nhạc

Nguồn bài hát: trang Notion **"NHẠC VIỆT - PHỐI KHÍ - PHỐI ÂM HAY LẠ"** (id `41c09509-f1c5-8034-8c96-e8bb4bc72b8e`).

## Cấu trúc
- `nhac/index.html` — trang nhạc (được dựng tự động, không sửa tay).
- `og.jpg` — hình xem trước khi gửi link qua Zalo/Facebook.
- `_nguon/data.tsv` — danh sách bài: `VIDEO_ID <tab> Tên bài | dòng phụ <tab> Tên kênh` (thứ tự theo Notion).
- `_nguon/template.html` — giao diện.
- `_nguon/build.py` — dựng `index.html` từ danh sách.

## Quy tắc (anh Lương đã dặn)
1. Chỉ lấy link **video** YouTube; bỏ link kênh.
2. Cùng một video dán nhiều lần → chỉ giữ một. Khác clip dù trùng tên → giữ cả hai.
3. Tên bài anh Lương tự đặt (trong `data.tsv`) được giữ nguyên, không ghi đè.
4. Trang tự xếp **theo ABC tiếng Việt** (A Ă Â B C D Đ E Ê …); loạt **"Bài Không Tên"** để riêng ở **cuối cùng**.
5. Video không đọc được tên → để trống tên, báo anh Lương đặt tên.
6. Chỉ cập nhật khi anh Lương yêu cầu (không chạy tự động).

## Cách cập nhật
1. Đọc trang Notion, so với `_nguon/data.tsv`; thêm dòng cho bài mới (tên lấy từ YouTube oEmbed), bỏ bài đã xóa.
2. Chạy: `python3 _nguon/build.py dd/mm nhac/index.html`
3. Commit và push lên nhánh `main`. Trang tự cập nhật sau 1–2 phút.
