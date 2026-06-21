class Student:
    def __init__(self,id,name,theory_score,practive_score,project_score):
        self.__id = id
        self.__name = name
        self.__theory_score = theory_score
        self.__practive_score = practive_score
        self.__project_score = project_score
        self.__final_score = 0
        self.__academic_rank = ""

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def theory_score(self):
        return self.__theory_score

    @property
    def practive_score(self):
        return self.__practive_score

    @property
    def project_score(self):
        return self.__project_score

    @property
    def final_score(self):
        return self.__final_score

    @property
    def academic(self):
        return self.__academic_rank

    def update_theory_score(self,theory_score):
        self.__theory_score = theory_score

    def update_practive_score(self,practive_score):
        self.__practive_score = practive_score

    def update_project_score(self,project_score):
        self.__project_score = project_score

    def calculate_final_score(self):
        self.__final_score = (self.__theory_score*0.2) + (self.__practive_score*0.3) +(self.__project_score*0.5)

    def classify_academic_rank(self):
        if self.__final_score > 10 or self.__final_score < 0:
            print("Điểm không hợp lệ")
            return
        if self.__final_score < 5:
            self.__academic_rank = "Yếu"
        elif self.__final_score < 7:
            self.__academic_rank = "Trung bình"
        elif self.__final_score < 8.5:
            self.__academic_rank = "Khá"
        else:
            self.__academic_rank = "Giỏi"

class StudentManager:
    def __init__(self):
        self.students : list[Student] = []

    def add_student(self):
        while True:
            stu_id = input("Nhập mã sinh viên: ")
            if not stu_id:
                print("Không được để trống")
                continue
            else:
                break
        for stu in self.students:
            if stu.__id == stu_id:
                print("Mã sinh viên tồn tại")
                return

        while True:
            stu_name = input("Nhập họ tên: ")
            if not stu_name:
                print("Không được để trống")
            else:
                break
        stu_theory_score = float(input("Nhập điểm lý thuyết: "))
        stu_practice_score = float(input("Nhập điểm thực hành: "))
        stu_project_score = float(input("Nhập điểm đồ án: "))
        new_stu = Student(stu_id,stu_name,stu_theory_score,stu_practice_score,stu_project_score)
        new_stu.calculate_final_score()
        new_stu.classify_academic_rank()
        self.students.append(new_stu)

    def show_all(self):
        if not self.students:
            print("Không có sinh viên nào")
            return
        print(f"{'Mã SV':<7} | {'Họ tên':<20} | {'Điểm Lý Thuyết':<15} | {'Điểm Thực Hành':<15} | {'Điểm Đồ Án':<15} | {'Điểm Tổng Kết':<15} | {'Học Lực'}")
        for stu in self.students:
            print(f"{stu.id:<7} | {stu.name:<20} | {stu.theory_score:<15} | {stu.practive_score:<15} | {stu.project_score:<15} | {stu.final_score:<15} | {stu.academic}")

    def update_student(self):
        stu_id = input("Nhập mã sinh viên cần cập nhật: ")
        for stu in self.students:
            if stu.id == stu_id:
                stu_theory_score = float(input("Nhập điểm lý thuyết: "))
                stu_practice_score = float(input("Nhập điểm thực hành: "))
                stu_project_score = float(input("Nhập điểm đồ án: "))
                stu.update_theory_score(stu_theory_score)
                stu.update_practive_score(stu_practice_score)
                stu.update_project_score(stu_project_score)
                stu.calculate_final_score
                stu.classify_academic_rank
                break
        else:
            print("Không tìm thấy sinh viên cần cập nhật")

    def delete_student(self):
        stu_id = input("Nhập mã sinh viên cần cập nhật: ")
        for stu in self.students:
            if stu.id == stu_id:
                choice = input("Bạn có chắc muốn xóa sinh viên này không? (Y/N): ").lower()
                match choice:
                    case 'y':
                        self.students.remove(stu)
                        break
                    case 'n':
                        print("Hủy bỏ thao tác")
                        return
        else:
            print("Không tìm thấy sinh viên")

    def search_student(self):
        list_student = StudentManager()
        stu_name = input("Nhập tên sinh viên: ")
        for stu in self.students:
            if stu_name.lower() in stu.name.lower():
                list_student.add_student()
        list_student.show_all()
        if not list_student:
            print("Không tìm thấy sinh viên")

def menu():
    print("""
================ MENU ================
1. Hiển thị danh sách sinh viên
2. Thêm sinh viên mới
3. Cập nhật thông tin sinh viên
4. Xóa sinh viên
5. Tìm kiếm sinh viên theo tên
6. Thoát
=====================================
""")

def main():
    while True:
        menu()
        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                break
            case _:
                print("Lựa chọn không hợp lệ")