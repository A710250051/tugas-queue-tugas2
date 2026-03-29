from collections import deque

class TaskManager:
    def __init__(self):
        self.tasks = deque() # Inisialisasi deque kosong

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self):
        if not self.is_empty():
            return self.tasks.popleft() # Menghapus tugas dari depan
        else:
            return "Tidak ada tugas dalam antrian!"

    def add_urgent_task(self, task):
        self.tasks.appendleft(task) # Konversi deque ke list untuk tampilan yang lebih jelas

    def display_tasks(self):
        print(list(self.tasks))

    def is_empty(self):
        return len(self.tasks) == 0
    
if __name__ == "__main__":
    tasks = TaskManager()
    # Tambah tugas
    tasks.add_task("Kerjakan laporan")
    tasks.add_task("Meeting dengan tim")
    tasks.add_urgent_task("Bug fix urgent")
    # Tampilkan antrian
    print("Daftar Tugas:")
    tasks.display_tasks()
    # Proses tugas
    print("Tugas dikerjakan:", tasks.remove_task())
    # Tampilkan setelah diproses
    print("Daftar Tugas setelah pemrosesan:")
    tasks.display_tasks()