class Node:
    def __init__(self, nim):
        self.nim = nim
        self.next = None

class SingleLinkedLisMahasiswa:
    def __init__(self):
        self.head = None

    # 1. Data di awal
    def insert_awal(self, nim):
        new_node = Node(nim)
        new_node.next = self.head
        self.head = new_node
        print(f"Data {nim} berhasil ditambahkan di AWAL.")

    # 2. Data di akhir
    def insert_akhir(self, nim):
        new_node = Node(nim)
        if not self.head:
            self.head = new_node
            print(f"Data {nim} berhasil ditambahkan sebagai data PERTAMA.")
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        print(f"Data (NIM: {nim}) berhasil ditambahkan di AKHIR.")

    # 3. Data di tengah (urut ascending)
    def insert_urut_nim(self, nim):
        new_node = Node(nim)
        if not self.head or self.head.nim > nim:
            new_node.next = self.head
            self.head = new_node
            print(f"NIM {nim} berhasil disisipkan secara berurut.")
            return
        curr = self.head
        while curr.next and curr.next.nim < nim:
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        print(f"NIM {nim} berhasil disisipkan secara teratur.")

    # 4. Hapus data berdasarkan NIM
    def delete_by_nim(self, nim):
        curr = self.head
        prev = None
        while curr and curr.nim != nim:
            prev = curr
            curr = curr.next
        if not curr:
            print(f"NIM {nim} TIDAK DITEMUKAN!")
            return
        if not prev:
            self.head = curr.next
        else:
            prev.next = curr.next
        print(f"NIM {nim} berhasil dihapus.")

    # 5. Cari data berdasarkan NIM
    def search_by_nim(self, nim):
        curr = self.head
        posisi = 1
        while curr:
            if curr.nim == nim:
                print(f"\n--- NIM Ditemukan: {curr.nim} (Berada di Node ke-{posisi}) ---\n")
                return curr
            curr = curr.next
            posisi += 1
        print(f"NIM {nim} tidak ditemukan.")
        return None

    # 6. Tampilkan semua data
    def display(self):
        if not self.head:
            print("\nData Mahasiswa Masih Kosong!\n")
            return
        print("\n" + "=" * 35)
        print("DAFTAR NIM MAHASISWA (Single LL)")
        print("=" * 35)
        curr = self.head
        while curr:
            print(f"{curr.nim} -> ", end="")
            curr = curr.next
        print("NULL\n")

def menu():
    sll = SingleLinkedLisMahasiswa()
    while True:
        print("=== MENU MANAJEMEN NIM MAHASISWA ===")
        print("1. Tambah Data diAwal")
        print("2. Tambah Data Terurut (Berdasarkan NIM)")
        print("3. Tambah Data diAkhir")
        print("4. Hapus data (Berdasarkan NIM)")
        print("5. Cari Data (Berdasarkan NIM)")
        print("6. Tampilkan Semua Data")
        print("0. Keluar")

        pilihan = input("Pilih menu (0-6): ")
        if pilihan == "1":
            nim = input("Masukkan NIM: ")
            sll.insert_awal(nim)
        elif pilihan == "2":
            nim = input("Masukkan NIM: ")
            sll.insert_urut_nim(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM: ")
            sll.insert_akhir(nim)
        elif pilihan == "4":
            nim = input("Masukkan NIM yang ingin dihapus: ")
            sll.delete_by_nim(nim)
        elif pilihan == "5":
            nim = input("Masukkan NIM yang dicari: ")
            sll.search_by_nim(nim)
        elif pilihan == "6":
            sll.display()
        elif pilihan == "0":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi!")

if __name__ == "__main__":
    menu()