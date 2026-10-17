import sys

from PyQt6.QtCore import QEasingCurve, Qt
from PyQt6.QtGui import QColor, QFont, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)
from PyQt6_SwitchControl import SwitchControl


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.FrontPage()
        self.DataPage()
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)
        self.setAutoFillBackground(True)
        self.stack.setAutoFillBackground(True)


    def FrontPage(self):
        page = QWidget()
        self.resize(1920, 1080)
        self.setWindowTitle("Payslip Generator")

        #title
        self.title = QLabel("[Payslip Generator]")
        font = QFont()
        font.setFamily("HYWenHei")
        font.setPointSize(40)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setContentsMargins(0,130,0,200)

        #start
        self.startbtn = QPushButton("Generate")
        self.startbtn.setToolTip("Open Template Maker")
        self.startbtn.setFont(QFont("HYWenHei", 20, QFont.Weight.Bold))
        self.startbtn.setFixedSize(200, 50)
        self.startbtn.clicked.connect(lambda: self.stack.setCurrentIndex(1))

        

        #exit
        self.exitbtn = QPushButton("EXIT")
        self.exitbtn.setToolTip("Leave Payslip Generator")
        self.exitbtn.setFont(QFont("HYWenHei", 20, QFont.Weight.Bold))
        self.exitbtn.setFixedSize(200, 50)
        self.exitbtn.clicked.connect(self.quit)

        ButtonLayout = QHBoxLayout()
        ButtonLayout.setSpacing(10)
        ButtonLayout.setContentsMargins(0, 0, 0, 0)
        ButtonLayout.addWidget(self.startbtn, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        ButtonLayout.addWidget(self.exitbtn, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        MainLayout = QVBoxLayout()
        MainLayout.setSpacing(10)  # space between every widget
        MainLayout.setContentsMargins(0, 0, 0, 0)
        MainLayout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        MainLayout.addLayout(ButtonLayout)
        

        page.setLayout(MainLayout)
        self.stack.addWidget(page)

    def quit(self):
        QApplication.quit()

    def DataPage(self):
        page = QWidget()
        layout = QVBoxLayout()

        #title
        self.title = QLabel("[TEST]")
        font = QFont()
        font.setFamily("HYWenHei")
        font.setPointSize(40)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setContentsMargins(0,100,0,150)
        back_btn = QPushButton("Back")
        back_btn.clicked.connect(lambda: self.stack.setCurrentIndex(0))

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumSize(600, 300)


        # Put your widgets inside this layout
        content = QWidget()
        content_layout = QVBoxLayout(content)

        # ============================================================
        # HEADER
        # ============================================================

        header = QFrame()
        header.setFrameShape(QFrame.Shape.Box)

        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(10, 5, 10, 5)

        company = QLabel("Demo Company Sdn Bhd")
        company.setFont(QFont("Arial", 16))

        payment = QLabel("END PAYMENT - JANUARY 2019")
        payment.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        header_layout.addWidget(company)
        header_layout.addStretch()
        header_layout.addWidget(payment)

        content_layout.addWidget(header)


        # ============================================================
        # EMPLOYEE INFORMATION
        # ============================================================

        info = QFrame()
        info.setFrameShape(QFrame.Shape.Box)

        info_layout = QGridLayout(info)
        info_layout.setContentsMargins(10, 5, 10, 5)
        info_layout.setHorizontalSpacing(15)
        info_layout.setVerticalSpacing(3)

        info_data = [
            ("EMPLOYEE NO.", "JEFF001"),
            ("NAME", "JEFFREY TOH"),
            ("IC NO.", "123456-78-9012"),
            ("DEPARTMENT", "PRO"),
            ("BASE RATE", "3,000.00"),
            ("WORKING DAYS", "31.00"),
        ]

        for row, (name, value) in enumerate(info_data):
            info_layout.addWidget(QLabel(name), row, 0)
            info_layout.addWidget(QLabel(value), row, 1)

        info_layout.addWidget(QLabel("DW"), 4, 2)
        info_layout.addWidget(QLabel("EO"), 4, 3)
        info_layout.addWidget(QLabel("LAT"), 4, 4)
        info_layout.addWidget(QLabel("TOF"), 4, 5)

        info_layout.addWidget(QLabel("31.00"), 5, 2)
        info_layout.addWidget(QLabel("6.00"), 5, 3)
        info_layout.addWidget(QLabel(".08"), 5, 4)
        info_layout.addWidget(QLabel(".08"), 5, 5)

        right_data = [
            ("POSITION", "Sale Executive"),
            ("EPF NO.", "12345677899"),
            ("SOCSO NO.", "123456789"),
            ("TAX NO.", "123456789"),
        ]

        for row, (name, value) in enumerate(right_data):
            info_layout.addWidget(QLabel(name), row, 6)
            info_layout.addWidget(QLabel(value), row, 7)

        content_layout.addWidget(info)


        # ============================================================
        # EARNINGS / DEDUCTIONS HEADER
        # ============================================================

        section_header = QFrame()
        section_header.setFrameShape(QFrame.Shape.Box)

        section_layout = QHBoxLayout(section_header)
        section_layout.setContentsMargins(0, 0, 0, 0)
        section_layout.setSpacing(0)

        earnings_title = QLabel("EARNINGS / INCOME")
        earnings_title.setContentsMargins(10, 5, 10, 5)

        deduction_title = QLabel("DEDUCTION")
        deduction_title.setContentsMargins(10, 5, 10, 5)

        section_layout.addWidget(earnings_title, 1)

        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setFrameShadow(QFrame.Shadow.Plain)
        section_layout.addWidget(divider)

        section_layout.addWidget(deduction_title, 1)

        content_layout.addWidget(section_header)


        # ============================================================
        # EARNINGS AND DEDUCTIONS
        # ============================================================

        body = QFrame()
        body.setFrameShape(QFrame.Shape.Box)

        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)


        # Earnings column
        earnings = QWidget()
        earnings_layout = QVBoxLayout(earnings)
        earnings_layout.setContentsMargins(10, 8, 10, 8)
        earnings_layout.setSpacing(5)

        earnings_data = [
            ("BASIC PAY", "3,000.00"),
            ("DAILY ATTENDANCE", "23.07"),
            ("MEAL", "93.00"),
            ("NIGHT SHIFT ALLOWANCE", "10.00"),
            ("NORMAL OT", "86.54"),
            ("REST OT", "734.44"),
        ]

        for name, amount in earnings_data:
            row = QHBoxLayout()
            row.addWidget(QLabel(name))
            row.addStretch()

            amount_label = QLabel(amount)
            amount_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            row.addWidget(amount_label)

            earnings_layout.addLayout(row)

        earnings_layout.addStretch()


        # Deductions column
        deductions = QWidget()
        deductions_layout = QVBoxLayout(deductions)
        deductions_layout.setContentsMargins(10, 8, 10, 8)
        deductions_layout.setSpacing(5)

        deduction_data = [
            ("EMPLOYEE EPF", "319.00"),
            ("EMPLOYEE SOCSO", "19.25"),
            ("EMPLOYEE EIS", "7.70"),
            ("EMPLOYEE PCB", "12.40"),
            ("EARLY OUT", "86.54"),
            ("LATENESS", "14.40"),
            ("TIME OFF", "1.15"),
        ]

        for name, amount in deduction_data:
            row = QHBoxLayout()
            row.addWidget(QLabel(name))
            row.addStretch()

            amount_label = QLabel(amount)
            amount_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            row.addWidget(amount_label)

            deductions_layout.addLayout(row)

        deductions_layout.addStretch()


        # Center divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setFrameShadow(QFrame.Shadow.Plain)

        body_layout.addWidget(earnings, 1)
        body_layout.addWidget(divider)
        body_layout.addWidget(deductions, 1)

        content_layout.addWidget(body)


        # ============================================================
        # GROSS PAY AND TOTAL DEDUCTION
        # ============================================================

        totals = QFrame()
        totals.setFrameShape(QFrame.Shape.Box)

        totals_layout = QGridLayout(totals)
        totals_layout.setContentsMargins(10, 5, 10, 5)

        gross_title = QLabel("GROSS PAY")
        gross_amount = QLabel("3,947.05")
        deduction_title = QLabel("TOTAL DEDUCTION")
        deduction_amount = QLabel("460.44")

        totals_layout.addWidget(gross_title, 0, 0)
        totals_layout.addWidget(gross_amount, 0, 1)
        totals_layout.addWidget(deduction_title, 0, 2)
        totals_layout.addWidget(deduction_amount, 0, 3)

        totals_layout.setColumnStretch(0, 1)
        totals_layout.setColumnStretch(2, 1)

        content_layout.addWidget(totals)


        # ============================================================
        # NET PAY
        # ============================================================

        net = QFrame()
        net.setFrameShape(QFrame.Shape.Box)

        net_layout = QHBoxLayout(net)
        net_layout.setContentsMargins(10, 5, 10, 5)

        net_title = QLabel("NET PAY")
        net_amount = QLabel("3,486.61")

        net_title.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        net_amount.setFont(QFont("Arial", 10, QFont.Weight.Bold))

        net_layout.addWidget(net_title)
        net_layout.addStretch()
        net_layout.addWidget(net_amount)

        content_layout.addWidget(net)


        # ============================================================
        # EMPLOYER CONTRIBUTIONS AND YTD
        # ============================================================

        bottom = QHBoxLayout()
        bottom.setSpacing(20)

        employer = QFrame()
        employer.setFrameShape(QFrame.Shape.Box)

        employer_layout = QGridLayout(employer)
        employer_layout.setContentsMargins(10, 8, 10, 8)

        employer_data = [
            ("EPF (E'YER)", "377.00"),
            ("SOCSO (E'YER)", "67.35"),
            ("EIS (E'YER)", "7.70"),
        ]

        for row, (name, amount) in enumerate(employer_data):
            employer_layout.addWidget(QLabel(name), row, 0)

            amount_label = QLabel(amount)
            amount_label.setAlignment(Qt.AlignmentFlag.AlignRight)
            employer_layout.addWidget(amount_label, row, 1)

        bottom.addWidget(employer)


        ytd = QWidget()
        ytd_layout = QGridLayout(ytd)
        ytd_layout.setContentsMargins(10, 8, 10, 8)

        ytd_data = [
            ("YTD AL", "2.50 DAYS", "[   .00]"),
            ("YTD MC", "0.00 DAYS", "[   14.00]"),
        ]

        for row, (name, days, amount) in enumerate(ytd_data):
            ytd_layout.addWidget(QLabel(name), row, 0)
            ytd_layout.addWidget(QLabel(days), row, 1)
            ytd_layout.addWidget(QLabel(amount), row, 2)

        bottom.addWidget(ytd)
        content_layout.addLayout(bottom)


        # ============================================================
        # APPROVAL SIGNATURES
        # ============================================================

        signatures = QHBoxLayout()
        signatures.setContentsMargins(20, 25, 20, 10)

        signatures.addWidget(QLabel("APPROVED BY :"))
        signatures.addStretch()
        signatures.addWidget(QLabel("RECEIVED BY :"))

        content_layout.addLayout(signatures)



        # Give the QWidget to the QScrollArea
        content_layout.addStretch()
        scroll.setWidget(content)

        layout.addWidget(self.title, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        layout.addWidget(scroll, stretch=1)
        layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignHCenter)

        page.setLayout(layout)
        self.stack.addWidget(page)
        

    

  






if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    
    form = Main()
    form.showMaximized()
    form.show()
    sys.exit(app.exec())