import re


def tinh_tong_duong_am(chuoi):
    # Tìm tất cả các số nguyên (có thể có dấu '-' ở trước)
    cac_so = [int(x) for x in re.findall(r"-?\d+", chuoi)]

    tong_duong = sum(so for so in cac_so if so > 0)
    tong_am = sum(so for so in cac_so if so < 0)

    return tong_duong, tong_am


chuoi_nhap = input("Nhập chuỗi: ")
duong, am = tinh_tong_duong_am(chuoi_nhap)

print(f"Giá trị dương: {duong}. Giá trị âm: {am}")