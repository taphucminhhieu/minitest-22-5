# Câu 1: Khởi động - Tính tiền thanh toán (3 điểm) 
# Viết chương trình tính tiền mua hàng cho khách.
# Yêu cầu người dùng nhập vào Đơn giá của một sản phẩm và Số lượng mua.
# Tính Tổng tiền = Đơn giá * Số lượng.
# Áp dụng logic khuyến mãi:
# Nếu Tổng tiền >= 1.000.000, giảm giá 10% trên Tổng tiền.
# Nếu Tổng tiền < 1.000.000, không giảm giá.
# In ra màn hình số tiền cuối cùng khách phải thanh toán.

price = int(input("Nhập đơn giá: "))
number = int(input("Nhập số lượng cần mua: "))

total = 0

total = price * number 

if total >= 1000000 :
    total = total *0.1
    print("Giảm giá 10% ")
elif total < 1000000 :
    print("không giảm giá")

print(f"Số tiền cần trả:{total} ")
