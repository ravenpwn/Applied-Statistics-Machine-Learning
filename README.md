# TODO
Xử lý bộ dataset 2019: loại bỏ các cột không liên quan (vd chứa string value, cột stt, cột chứa giá trị NaN, cột chứa duy nhất 1 giá trị,...). Sau đó chuẩn hóa dữ liệu với StandardScaler, giảm độ phức tạp của data với PCA.

Cần chọn traning model thích hợp + save model (model cơ bản svm của sklearn mất khoảng 20-30p để train với bộ dữ liệu 200MB).

Có thể sẽ sử dụng các phương hướng sau để tiếp tục process data nếu model vẫn chưa thích hợp: bỏ các cột có correlation cao với các cột khác, sử dụng Anova test.
