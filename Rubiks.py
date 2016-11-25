import sys
from PyQt4 import QtGui, uic
import kociemba
import serial, time
arduino = serial.Serial('COM5', 9600, timeout=.1)
time.sleep(1)

 
qtCreatorFile = "R.ui" # Enter file here.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    c=0
    x=["FFAA00","FFFF00","00FF00","FF0000","FFFFFF","0000FF"]
    i=[1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,0,0,0,0,0,0,0,0,0]
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.done.clicked.connect(self.Done)
        self.pushButton_1.clicked.connect(self.Button_1)
        self.pushButton_2.clicked.connect(self.Button_2)
        self.pushButton_3.clicked.connect(self.Button_3)
        self.pushButton_4.clicked.connect(self.Button_4)
        self.pushButton_5.clicked.connect(self.Button_5)
        self.pushButton_6.clicked.connect(self.Button_6)
        self.pushButton_7.clicked.connect(self.Button_7)
        self.pushButton_8.clicked.connect(self.Button_8)
        self.pushButton_9.clicked.connect(self.Button_9)
        self.pushButton_10.clicked.connect(self.Button_10)
        self.pushButton_11.clicked.connect(self.Button_11)
        self.pushButton_12.clicked.connect(self.Button_12)
        self.pushButton_13.clicked.connect(self.Button_13)
        self.pushButton_14.clicked.connect(self.Button_14)
        self.pushButton_15.clicked.connect(self.Button_15)
        self.pushButton_16.clicked.connect(self.Button_16)
        self.pushButton_17.clicked.connect(self.Button_17)
        self.pushButton_18.clicked.connect(self.Button_18)
        self.pushButton_19.clicked.connect(self.Button_19)
        self.pushButton_20.clicked.connect(self.Button_20)
        self.pushButton_21.clicked.connect(self.Button_21)
        self.pushButton_22.clicked.connect(self.Button_22)
        self.pushButton_23.clicked.connect(self.Button_23)
        self.pushButton_24.clicked.connect(self.Button_24)
        self.pushButton_25.clicked.connect(self.Button_25)
        self.pushButton_26.clicked.connect(self.Button_26)
        self.pushButton_27.clicked.connect(self.Button_27)
        self.pushButton_28.clicked.connect(self.Button_28)
        self.pushButton_29.clicked.connect(self.Button_29)
        self.pushButton_30.clicked.connect(self.Button_30)
        self.pushButton_31.clicked.connect(self.Button_31)
        self.pushButton_32.clicked.connect(self.Button_32)
        self.pushButton_33.clicked.connect(self.Button_33)
        self.pushButton_34.clicked.connect(self.Button_34)
        self.pushButton_35.clicked.connect(self.Button_35)
        self.pushButton_36.clicked.connect(self.Button_36)
        self.pushButton_37.clicked.connect(self.Button_37)
        self.pushButton_38.clicked.connect(self.Button_38)
        self.pushButton_39.clicked.connect(self.Button_39)
        self.pushButton_40.clicked.connect(self.Button_40)
        self.pushButton_41.clicked.connect(self.Button_41)
        self.pushButton_42.clicked.connect(self.Button_42)
        self.pushButton_43.clicked.connect(self.Button_43)
        self.pushButton_44.clicked.connect(self.Button_44)
        self.pushButton_45.clicked.connect(self.Button_45)
        self.pushButton_46.clicked.connect(self.Button_46)
        self.pushButton_47.clicked.connect(self.Button_47)
        self.pushButton_48.clicked.connect(self.Button_48)
        self.pushButton_49.clicked.connect(self.Button_49)
        self.pushButton_50.clicked.connect(self.Button_50)
        self.pushButton_51.clicked.connect(self.Button_51)
        self.pushButton_52.clicked.connect(self.Button_52)
        self.pushButton_53.clicked.connect(self.Button_53)
        self.pushButton_54.clicked.connect(self.Button_54)


        self.pushButton_5.setStyleSheet("font-size:0px;background-color:#FFFF00;\
        border: 2px solid #000000")
        self.pushButton_14.setStyleSheet("font-size:0px;background-color:#00FF00;\
        border: 2px solid #000000")
        self.pushButton_23.setStyleSheet("font-size:0px;background-color:#FF0000;\
        border: 2px solid #000000")
        self.pushButton_32.setStyleSheet("font-size:0px;background-color:#FFFFFF;\
        border: 2px solid #000000")
        self.pushButton_41.setStyleSheet("font-size:0px;background-color:#0000FF;\
        border: 2px solid #000000")
        self.pushButton_50.setStyleSheet("font-size:0px;background-color:#FFAA00;\
        border: 2px solid #000000")
        
        
    def Button_1(self):
        self.i[0]=self.c
        self.pushButton_1.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[0]]+";\
        border: 2px solid #000000")
 

        
    def Button_2(self):
        self.i[1]=self.c
        self.pushButton_2.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[1]]+";\
        border: 2px solid #000000")
 
        
    def Button_3(self):
        self.i[2]=self.c
        self.pushButton_3.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[2]]+";\
        border: 2px solid #000000")
 
        
    def Button_4(self):
        self.i[3]=self.c
        self.pushButton_4.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[3]]+";\
        border: 2px solid #000000")
 
        
    def Button_5(self):
        self.c=1
        
    def Button_6(self):
        self.i[5]=self.c
        self.pushButton_6.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[5]]+";\
        border: 2px solid #000000")
 
        
    def Button_7(self):
        self.i[6]=self.c
        self.pushButton_7.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[6]]+";\
        border: 2px solid #000000")
 
        
    def Button_8(self):
        self.i[7]=self.c
        self.pushButton_8.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[7]]+";\
        border: 2px solid #000000")
 
        
    def Button_9(self):
        self.i[8]=self.c
        self.pushButton_9.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[8]]+";\
        border: 2px solid #000000")
 
        
    def Button_10(self):
        self.i[9]=self.c
        self.pushButton_10.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[9]]+";\
        border: 2px solid #000000")
 
        
    def Button_11(self):
        self.i[10]=self.c
        self.pushButton_11.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[10]]+";\
        border: 2px solid #000000")
 
        
    def Button_12(self):
        self.i[11]=self.c
        self.pushButton_12.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[11]]+";\
        border: 2px solid #000000")
 
        
    def Button_13(self):
        self.i[12]=self.c
        self.pushButton_13.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[12]]+";\
        border: 2px solid #000000")
 
        
    def Button_14(self):
        self.c=2
        
    def Button_15(self):
        self.i[14]=self.c
        self.pushButton_15.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[14]]+";\
        border: 2px solid #000000")
 
        
    def Button_16(self):
        self.i[15]=self.c
        self.pushButton_16.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[15]]+";\
        border: 2px solid #000000")
 
        
    def Button_17(self):
        self.i[16]=self.c
        self.pushButton_17.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[16]]+";\
        border: 2px solid #000000")
 
        
    def Button_18(self):
        self.i[17]=self.c
        self.pushButton_18.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[17]]+";\
        border: 2px solid #000000")
 
        
    def Button_19(self):
        self.i[18]=self.c
        self.pushButton_19.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[18]]+";\
        border: 2px solid #000000")
 
        
    def Button_20(self):
        self.i[19]=self.c
        self.pushButton_20.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[19]]+";\
        border: 2px solid #000000")
 
        
    def Button_21(self):
        self.i[20]=self.c
        self.pushButton_21.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[20]]+";\
        border: 2px solid #000000")
 
        
    def Button_22(self):
        self.i[21]=self.c
        self.pushButton_22.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[21]]+";\
        border: 2px solid #000000")
 
        
    def Button_23(self):
        self.c=3
        
    def Button_24(self):
        self.i[23]=self.c
        self.pushButton_24.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[23]]+";\
        border: 2px solid #000000")
 
        
    def Button_25(self):
        self.i[24]=self.c
        self.pushButton_25.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[24]]+";\
        border: 2px solid #000000")
 
        
    def Button_26(self):
        self.i[25]=self.c
        self.pushButton_26.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[25]]+";\
        border: 2px solid #000000")
 
        
    def Button_27(self):
        self.i[26]=self.c
        self.pushButton_27.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[26]]+";\
        border: 2px solid #000000")
 
        
    def Button_28(self):
        self.i[27]=self.c
        self.pushButton_28.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[27]]+";\
        border: 2px solid #000000")
 
        
    def Button_29(self):
        self.i[28]=self.c
        self.pushButton_29.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[28]]+";\
        border: 2px solid #000000")
 
        
    def Button_30(self):
        self.i[29]=self.c
        self.pushButton_30.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[29]]+";\
        border: 2px solid #000000")
 
        
    def Button_31(self):
        self.i[30]=self.c
        self.pushButton_31.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[30]]+";\
        border: 2px solid #000000")
 
        
    def Button_32(self):
        self.c=4
        
    def Button_33(self):
        self.i[32]=self.c
        self.pushButton_33.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[32]]+";\
        border: 2px solid #000000")
 
        
    def Button_34(self):
        self.i[33]=self.c
        self.pushButton_34.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[33]]+";\
        border: 2px solid #000000")
 
        
    def Button_35(self):
        self.i[34]=self.c
        self.pushButton_35.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[34]]+";\
        border: 2px solid #000000")
 
        
    def Button_36(self):
        self.i[35]=self.c
        self.pushButton_36.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[35]]+";\
        border: 2px solid #000000")
 
        
    def Button_37(self):
        self.i[36]=self.c
        self.pushButton_37.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[36]]+";\
        border: 2px solid #000000")
 
        
    def Button_38(self):
        self.i[37]=self.c
        self.pushButton_38.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[37]]+";\
        border: 2px solid #000000")
 
        
    def Button_39(self):
        self.i[38]=self.c
        self.pushButton_39.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[38]]+";\
        border: 2px solid #000000")
 
        
    def Button_40(self):
        self.i[39]=self.c
        self.pushButton_40.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[39]]+";\
        border: 2px solid #000000")
 
        
    def Button_41(self):
        self.c=5
        
    def Button_42(self):
        self.i[41]=self.c
        self.pushButton_42.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[41]]+";\
        border: 2px solid #000000")
 
        
    def Button_43(self):
        self.i[42]=self.c
        self.pushButton_43.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[42]]+";\
        border: 2px solid #000000")
 
        
    def Button_44(self):
        self.i[43]=self.c
        self.pushButton_44.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[43]]+";\
        border: 2px solid #000000")
 
        
    def Button_45(self):
        self.i[44]=self.c
        self.pushButton_45.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[44]]+";\
        border: 2px solid #000000")
 
        
    def Button_46(self):
        self.i[45]=self.c
        self.pushButton_46.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[45]]+";\
        border: 2px solid #000000")
 
        
    def Button_47(self):
        self.i[46]=self.c
        self.pushButton_47.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[46]]+";\
        border: 2px solid #000000")
 
        
    def Button_48(self):
        self.i[47]=self.c
        self.pushButton_48.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[47]]+";\
        border: 2px solid #000000")
 
        
    def Button_49(self):
        self.i[48]=self.c
        self.pushButton_49.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[48]]+";\
        border: 2px solid #000000")
 
        
    def Button_50(self):
       self.c=0
        
    def Button_51(self):
        self.i[50]=self.c
        self.pushButton_51.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[50]]+";\
        border: 2px solid #000000")
 
        
    def Button_52(self):
        self.i[51]=self.c
        self.pushButton_52.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[51]]+";\
        border: 2px solid #000000")
 
        
    def Button_53(self):
        self.i[52]=self.c
        self.pushButton_53.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[52]]+";\
        border: 2px solid #000000")
 
        
    def Button_54(self):
        self.i[53]=self.c
        self.pushButton_54.setStyleSheet("font-size:0px;background-color:#"+self.x[self.i[53]]+";\
        border: 2px solid #000000")
 

    def Done(self):
        s=["B","U","R","F","D","L"]
        cube="UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        list1 = list(cube)
        
        for j in range(0,54):
            list1[j]=s[self.i[j]]
        
        
        cube=''.join(list1)
        s=kociemba.solve(cube)
        print(s)
        
        i = 0
        s += ' '
        while(i < len(s)):
            if ( s[i+1] == ' '):
                    arduino.write(s[i].encode('utf-8'))
                    i+=2
            elif (s[i+1] == "'"):
                    arduino.write((s[i].lower()).encode('utf-8'))    
                    i+=3
            else:
                    if(s[i] == 'R'): 	arduino.write(b'1')
                    elif (s[i] == 'L'):	arduino.write(b'2')
                    elif (s[i] == 'B'):	arduino.write(b'3')
                    elif (s[i] == 'F'):	arduino.write(b'4')
                    elif (s[i] == 'U'):	arduino.write(b'5')
                    elif (s[i] == 'D'):	arduino.write(b'6')
                    i+=3
        
        sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
