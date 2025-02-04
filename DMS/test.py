from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QPushButton, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.table_widget = QTableWidget(4, 2)  # 4 rows and 2 columns
        self.table_widget.setItem(0, 0, QTableWidgetItem("Item 1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("Item 2"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("Item 3"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("Item 4"))

        self.button = QPushButton("Get Selected Item")
        self.button.clicked.connect(self.get_selected_item)

        layout = QVBoxLayout()
        layout.addWidget(self.table_widget)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def get_selected_item(self):
        selected_items = self.table_widget.selectedItems()
        if selected_items:
            for item in selected_items:
                print(f"Selected Item: {item.text()} at ({item.row()}, {item.column()})")
        else:
            print("No item selected")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()