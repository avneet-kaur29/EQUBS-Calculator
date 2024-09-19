import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
from Calculations import Calculations
def window():
    # Set up window
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setWindowTitle('EQUBS')
    win.setGeometry(50, 80, 1050, 500)

    # button functionality
    calcs = Calculations()

    lbl_diamond_density = QLabel(win)
    lbl_diamond_density.resize(500,20)

    lbl_number_density = QLabel(win)
    lbl_number_density.resize(500, 20)

    lbl_nvs_per_nd = QLabel(win)
    lbl_nvs_per_nd.resize(500, 20)

    def sectionOneClicked(self):

        try:
            lbl_diamond_density.setText("Isotope-weighted diamond density:  " + str(calcs.diamond_density(float(inp13C.text()))) + " g/cm^3")
            lbl_diamond_density.move(600, 70)

            lbl_number_density.setText("NV-doping concentration  " + str(calcs.number_density(float(inp13C.text()), float(inpNVd.text()))) + " per cm^3")
            lbl_number_density.move(600, 110)

            lbl_nvs_per_nd.setText(str(calcs.nvs_per_nd(float(inp13C.text()), float(inpNVd.text()), float(inpNDd.text()))) + " NVs per ND")
            lbl_nvs_per_nd.move(600, 150)
        except:
            lbl_diamond_density.setText("Please enter a number")
            lbl_diamond_density.move(600, 70)

            lbl_number_density.setText("")

    lbl_mass_per_nd = QLabel(win)
    lbl_mass_per_nd.resize(500, 20)

    lbl_molar_concentration = QLabel(win)
    lbl_molar_concentration.resize(500, 20)

    def sectionTwoClicked(self):
        try:
            lbl_mass_per_nd.setText("Mass per ND " + str(calcs.mass_per_nd(float(inp13C.text()), float(inpNDd.text()))) + " g")
            lbl_mass_per_nd.move(600, 270)

            lbl_molar_concentration.setText("Molar concentration " + str(calcs.molar_concentration(float(inp13C.text()), float(inpMassC.text()), float(inpNDd.text()))) + " M")
            lbl_molar_concentration.move(600, 310)
        except:
            lbl_mass_per_nd.setText("Please enter a number or enter numbers for section 1")
            lbl_mass_per_nd.move(600, 270)

    # Section One
    lblSecOne = QLabel(win)
    lblSecOne.setText("Section I")
    lblSecOne.move(50, 10)

    # Inputs:
    # % 13C
    lbl13C = QLabel(win)
    lbl13C.setText("Percentage of 13C present")
    lbl13C.move(50, 80)
    lbl13C.resize(300,20)

    inp13C = QLineEdit(win)
    inp13C.move(400, 80)

    # ND diameter
    lblNDd = QLabel(win)
    lblNDd.setText("ND Diameter (nm)")
    lblNDd.move(50, 130)
    lblNDd.resize(300,20)

    inpNDd = QLineEdit(win)
    inpNDd.move(400, 130)

    # NV density
    lblNVd = QLabel(win)
    lblNVd.setText("NV Density (ppm)")
    lblNVd.move(50, 180)
    lblNVd.resize(300,20)

    inpNVd = QLineEdit(win)
    inpNVd.move(400, 180)

    # Enter button
    btnOne = QPushButton(win)
    btnOne.move(50, 220)
    btnOne.setText("Enter")

    # When enter one is clicked
    btnOne.clicked.connect(sectionOneClicked)

    # Section Two
    lblSecTwo = QLabel(win)
    lblSecTwo.setText("Section II")
    lblSecTwo.move(50, 270)

    # Inputs
    # Mass concentration of ND suspension
    lblMassC = QLabel(win)
    lblMassC.setText("Mass Concentration of ND Suspension (mg/ml)")
    lblMassC.move(50, 320)
    lblMassC.resize(300,20)

    inpMassC = QLineEdit(win)
    inpMassC.move(400, 320)

    # Enter Button
    btnTwo = QPushButton(win)
    btnTwo.move(50, 350)
    btnTwo.setText("Enter")

    # When Enter two is clicked
    btnTwo.clicked.connect(sectionTwoClicked)

    # display and close out window
    win.show()
    sys.exit(app.exec_())

window()
