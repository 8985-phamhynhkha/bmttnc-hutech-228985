from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while(1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*************MENU**************")
    print("** 1.Them Sinh Vien.                              **")
    print("** 2.Cap Nhat Thong Tin Sinh Vien.                **")
    print("** 3.Xoa Sinh Vien Boi ID.                        **")
    print("** 4.Tim Kiem Sinh Vien Theo Ten.                 **")
    print("** 5.Sap Xep Sinh VIen Theo Diem Trung Binh.      **")
    print("** 6.Sap Xep Sinh Vien Theo Ten Chuyen Nganh.     **")
    print("** 7.Hien Thi Danh Sach Sinh Vien.                **")
    print("** 0.Thoat.                                       **")
    print("*******************************")
    
    key = int(input("Nhap Tuy Chon:"))
    if key ==1:
        print("\n1. Them Sinh Vien.")
        qlsv.nhapSinhVien()
        print("\nThem Sinh Vien Thanh Cong!")
    elif key == 2:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cap Nhat Thong Tin Sinh Vien.")
            ID = int(input("Nhap ID:"))
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh Sach Sinh Vien Trong!")
    elif key == 3:
        if qlsv.soLuongSinhVien() >0:
            print("\n3. Xoa Sinh Vien.")
            ID = int(input("Nhap ID:"))
            if qlsv.deleteById(ID):
                print(f"\nSinh vien co id={ID} da bi xoa.")
            else:
                print(f"\nSinh vien co id={ID} khong ton tai.")
        else:
            print("\nDanh Sach Sinh Vien Trong!")
    elif key == 4:
        if qlsv.soLuongSinhVien() >0:
            print("\n4. Tim Kiem Sinh Vien Theo Ten.")
            name = input("Nhap ten de tim kiem:")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap Xep Sinh Vien Theo DiemTB(GPA)")
            qlsv.sortBydiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sach Sinh Vien Trong!")
    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap Xep Sinh Vien Theo Ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sach Sinh Vien Trong!")
    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien Thi Danh Sach Sinh Vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh Sach Sinh Vien Trong!")
    elif key == 0:
        print("\nBan Da Chon Thoat Chuong Trinh!")
        break
    else:
        print("\nKhong Co Chuc Nang Nay!")
        print("\nHay Chon Chuc Nang Trong Hop Menu. ")