# Câu 2: Vận dụng - Hệ thống đăng nhập bảo mật (4 điểm) 
# Mô phỏng chức năng đăng nhập trước khi vào phần mềm. Giả sử mật khẩu đúng được lưu sẵn trong một biến là 123456.
# Sử dụng vòng lặp để yêu cầu người dùng nhập mật khẩu.
# Nếu nhập đúng, in ra "Đăng nhập thành công!" và kết thúc chương trình.
# Nếu nhập sai, in ra "Mật khẩu sai, vui lòng nhập lại!".
# Ràng buộc: Khách hàng chỉ được phép nhập sai tối đa 3 lần. Nếu quá 3 lần, in ra thông báo "Tài khoản đã bị khóa!" và buộc thoát chương trình


password_clean = "123456"
chance = 3


while chance > 0: 
    password = input("nhập mật khẩu: ")

    if password == password_clean:
        print("đăng nhâọ thành công")
        break
    else:
        chance = chance -1
    if chance > 0 :
        print("Mật khẩu sai ,vui lòng nhâọ lại")
    else :
        print("tài khoản bị khoá")








