import tkinter as tk
from tkinter import Label, Button
import time
from PIL import Image, ImageTk
import serial
import math
# da auswahl eines verfahrens und algoritmus eine erfahrungssache ist, und du vlcht schon eine hast, wüstest Du welches Verfahren ich auswählen soll ,
# von Maschine Learning um diese scheiben im behälter zu erkennen, zwecks platzierung auf den Tisch ? ist hier auf meiner seite. Es sollte vor allem
# so einfach wie moeglich sein und erstmnal "nur" die mitte treffen. ich wollte es erstmal so versuchen: www seite
#-------------------------- MAIN

window = tk.Tk()
localtime = time.asctime(time.localtime(time. time()))
window.title("Graphic User Interface for SCARA Robot in Python")
window.geometry("1228x550")
window.configure(background="grey91")
font10 = "{Courier New} 10 normal"
font11 = "{U.S. 101} 30 bold"
font12 = "{Al Aramco} 17"
font13 = "{Courier New} 10 bold"
font14 = "{Segoe UI} 15 bold"
font15 = "{Arial 13} bold"
font16 = "{Segoe UI} 13 bold"
myPort = serial.Serial('com8',9600)
SliderVar1 = tk.IntVar()   # SliderVar1.get() SliderVar1.set()
SliderVar2 = tk.IntVar()   # SliderVar2.get()
SliderVar3 = tk.IntVar()   # SliderVar3.get()
SliderVarZ = tk.IntVar()   # SliderVarZ.get() # Z Achse
EntryVarSpeed = tk.StringVar()
EntryVarAcceleration = tk.StringVar()
gripperValue = tk.IntVar()
myVarx = tk.IntVar()
theta1=0
def print_value2(event):
    print("Scale {}".format(SliderVar1.get()))

# MAIN draw __ config ___________#
#SliderVar1 = tk.IntVar()  # wie ich das 0 setze, oder ist automatisch
SliderVar1.set(0)#SliderVar1.set(0)
SliderVar2.set(0)# int SliderVar2 = 0
SliderVar3.set(100)# int SliderVar3 = 0
SliderVarZ.set(180)# int SliderVarZ = 180
# int j1JogValue = 0
# int j2JogValue = 0
# int j3JogValue = 0
# int zJogValue = 0
EntryVarSpeed.set(500)# int speedSlider = 500
EntryVarAcceleration.set(500)# int accelerationSlider = 500
gripperValue.set(110) # int gripperValue = 180
gripperAdd=180
positionsCounter = 0
saveStatus = 0
runStatus = 0
slider1Previous = 0
slider2Previous = 0
slider3Previous = 0
sliderzPrevious = 100
speedSliderPrevious = 500
accelerationSliderPrevious = 500
gripperValuePrevious = 100
activeIK = False
EntryVar_xP = tk.IntVar()
EntryVar_yP = tk.IntVar()
EntryVar_zP = tk.IntVar()
#xP = tk.StringVar()
#yP = tk.StringVar()
#zP = tk.StringVar()
EntryVar_xP.set(365)
EntryVar_yP.set(0)   # int yP=0;
EntryVar_zP.set(100)  # int zP=100;
floatL1 = 228 # L1 = 228mm # DoubleVar
floatL2 = 136.5 # L2 = 136.5mm
#theta1, theta2, phi, z # float, braucht man nicht für spätere Berechnung initialisieren
#String[] positions = new String[100] #braucht man nicht initialisieren
# String data #braucht man nicht initialisieren
Data=1
Data1=2

data=(b'1')
#-------------------------- IF BEDINGUNGEN
def forwardKinematics():
    print(Data)
def updateData():
    print(Data)
# println(data)                                     # ne flagge als integer intVar
saveStatus = 0 #keep savePosition variable 0 or false.See, when button SAVE pressed it makes the value 1, which indicates to store the value in the arduino code
#
# If slider moved, calculate new position of X, Y and Z with forward kinematics

SliderVar1.set(30)
if (slider1Previous != SliderVar1.get()): #.get()
    if (activeIK == False):                      # Check whether the inverseKinematics mode is active,
        theta1 = round(SliderVar1.get(), 2)
        theta2 = round(SliderVar2.get(), 2)  # Execute Forward kinematics only if inverseKinematics mode is off or false
        forwardKinematics()
        myPort.write(data)
        print(theta1)
        print("theta1")
##             theta1 = round(cp5.getController("SliderVar1").getValue()) # get the value from the slider1
#             theta2 = round(cp5.getController("SliderVar2").getValue())
#
# slider1Previous = SliderVar1  # aehnliches wie bei slider .get()

if (slider2Previous != SliderVar2.get()):
    if (activeIK == False): # Check whether the inverseKinematics mode is active, Executre Forward kinematics only if inverseKinematics mode is off or false
        theta1 = round(SliderVar1.get(), 2)
        theta2 = round(SliderVar2.get(), 2)
        forwardKinematics()
        myPort.write(data)
#
#
slider2Previous = SliderVar2
#
if (slider3Previous != SliderVar3.get()):
    if (activeIK == False): # Check whether the inverseKinematics mode is active, Execute Forward kinematics only if inverseKinematics mode is off or false
        theta1 = round(SliderVar1.get(), 2) #get the value from the slider1
        theta2 = round(SliderVar2.get(), 2)
        forwardKinematics()
        myPort.write(data)

slider3Previous = SliderVar3

if (sliderzPrevious != SliderVarZ):
    if (activeIK == False): # Check whether the inverseKinematics mode is active, Executre fwd kin. only if inverseKin. mode is off or false
        zP = round(SliderVarZ.get(), 2)
        myPort.write(data)
#
#
sliderzPrevious = SliderVarZ                                                  #wie acke ich das in neue variable wenn ich wert im slider ändere?
#
if (gripperValuePrevious != gripperValue):                                  # neuer Wert ist nicht gleich alter Wert?
    if (activeIK == False): # Check whether the inverseKinematics mode is active, Execute Forward kinematics only if inverseKinematics mode is off or false
        gripperAdd = round(gripperValue.get(), 0) # == ist == 0?
        gripperValue = gripperAdd + 50
        updateData() # myVarx.set(NeuerWert)
#        print(data)
        myPort.write(data)
#
gripperValuePrevious = gripperValue
activeIK = False # deactivate inverseKinematics so the above if statements can be executed the next interation
#
# #-------------------------- FUNCTIONS
#
# text just writes something onscreen analog to label bsp textSize(32); # text("word", 10, 30); # fill(0, 102, 153);
# if (positionsCounter > 0)                       # wie laasse eine variable in label anzeigen, die ich ausrechne in Tk set.TextVar
#     text(positions[positionsCounter-1], 460, 630)
#     text("Last saved position: No."+(positionsCounter-1), 460, 600)
# else
#     text("Last saved position:", 460, 600)
#     text("None", 460, 630);

#     text(positions[positionsCounter-1], 460, 630)
#     text("Last saved position: No."+(positionsCounter-1), 460, 600)
# else
#      text("Last saved position:", 460, 600)
#      text("None", 460, 630);

#
# # FORWARD KINEMATICS

# def void forwardKinematics()
#     float theta1F = theta1 * PI / 180 # degree to radians        # float variable
#     float theta2F = theta2 * PI / 180
#     xP = round(L1 * cos(theta1F) + L2 * cos(theta1F + theta2F))  # round gibts bei Tk?
#     yP = round(L1 * sin(theta1F) + L2 * sin(theta1F + theta2F))


# def void forwardKinematics()
#     float theta1F = theta1 * PI / 180 # degree to radians        # float variable
#     float theta2F = theta2 * PI / 180
#     xP = round(L1 * cos(theta1F) + L2 * cos(theta1F + theta2F))  # round gibts bei Tk?
#     yP = round(L1 * sin(theta1F) + L2 * sin(theta1F + theta2F))
#
# # INVERSE KINEMATICS
# def void inverseKinematics(float x, floaty)
#     theta2 = acos((sq(x) + sq(y) - sq(L1) - sq(L2)) / (2 * L1 * L2))
#         if (x < 0 & y < 0)
#             theta2 = (-1) * theta2
#
#     theta1 = atan(x / y) - atan((L2 * sin(theta2)) / (L1 + L2 * cos(theta2)))
#     theta2 = (-1) * theta2 * 180 / PI
#     theta1 = theta1 * 180 / PI
#
# # Angles adjustment depending in which quadrant the final tool coordinate x, y is
#         if (x >= 0 & y >= 0) # 1st quadrant
#             theta1 = 90 - theta1
#         if (x < 0 & y > 0) # 2nd quadrant
#             theta1 = 90 - theta1
#         if (x < 0 & y < 0) #3d quadrant
#             theta1 = 270 - theta1
#             phi = 270 - theta1 - theta2
#             phi = (-1) * phi
#
#         if (x > 0 & y < 0) {// 4th quadrant
#             theta1 = -90 - theta1;
#
#     if (x < 0 & y == 0) {
#         theta1 = 270 + theta1;
#
#
# # Calculate "phi" angle so gripper is parallel to the X axis
# phi = 90 + theta1 + theta2;
# phi = (-1) * phi;
#
# # Angle adjustment depending in which quadrant the final tool coordinate x, y is
x=-1
y=-1
pi=math.pi
if (x < 0 & y < 0): #3d quadrant
    pi = 270 - theta1 - theta2

if (abs(3.14) > 165):
    pi = 180 + phi
#
# theta1 = round(theta1)
# theta2 = round(theta2)
# phi = round(phi)


#SliderVar1.set(theta1)
#SliderVar1 = tk.IntVar(theta1) #getController("SliderVar1").setValue(theta1) #SliderVar1.set(0)
#getController("SliderVar2").setValue(theta2)
#getController("SliderVar3").setValue(phi)
#getController("SliderVarZ").setValue(zP)

# def void controlEvent(ControlEvent theEvent)
#     if (theEvent.isController())
#     print(theEvent.getController().getName());
#
# def global void xTextfield(String theText): #public
#     # If we enter a value into the Textfield, read the value, convert to integer, set the inverseKinematics mode active
#     xP = Integer.parseInt(theText)
#     activeIK = true
#     inverseKinematics(xP, yP) # Use inverse kinematics to calculate the J1(theta1), J2(theta2), and J3(phi) positions
#     # activeIK = false;
#     print("Test; theta1: " + theta1 + " theta2: " + theta2);
#
# def global void yTextfield(String theText)
#     yP = Integer.parseInt(theText)
#     activeIK = true
#     inverseKinematics(xP, yP)
#     # activeIK = false;
#
# def public void zTextfield(String theText)
#     zP = Integer.parseInt(theText)
#     activeIK = true
#     inverseKinematics(xP, yP)
#
#
# public void j1JogMinus()
#     intVar a = round(cp5.getController("SliderVar1").getValue())
#     a = a - j1JogValue
#     getController("SliderVar1").setValue(a)
#
# # J1 control
# def public void j1JogPlus()
#     intVar a = round(cp5.getController("SliderVar1").getValue())
#     a = a + j1JogValue
#     getController("SliderVar1").setValue(a)
#
# # J2 control
# def public void j2JogMinus()
#     intVar a = round(cp5.getController("SliderVar2").getValue());
#     a = a - j2JogValue
#     getController("SliderVar2").setValue(a)
#
# def public void j2JogPlus()
#     intVar a = round(cp5.getController("SliderVar2").getValue())
#     a = a + j2JogValue
#     getController("SliderVar2").setValue(a)
#
# # J3 control public
# def void j3JogMinus()
#     int a = round(cp5.getController("SliderVar3").getValue())
#     a = a - j3JogValue
#     getController("SliderVar3").setValue(a)
#
# def public void j3JogPlus()
#     int a = round(cp5.getController("SliderVar3").getValue())
#     a = a + j3JogValue
#     getController("SliderVar3").setValue(a)
#
# # J3 control
# def public void zJogMinus()
#     int a = round(cp5.getController("SliderVarZ").getValue())
#     a = a - zJogValue
#     getController("SliderVarZ").setValue(a)
#
# def public void zJogPlus()
#     int a = round(cp5.getController("SliderVarZ").getValue())
#     a = a + zJogValue
#     getController("SliderVarZ").setValue(a)
#
def move():
    myPort.write(data)
    print(data)
i=0
def savePosition(): #public # Save the J1, J2, J3 and Z position in the array                        ############################
    positions[i] = "J1=" + str(SliderVar1.get())
    +", J2=" + str(SliderVar2.get())
    +", J3=" + str(SliderVar3.get())
    +", Z=" + str(SliderVarZ.get())
    i+=1
#     saveStatus = 1
#     updateData()
#     myPort.write(data)
#     saveStatus = 0
#
#
# def public void run()
#     if (runStatus == 0)
#     getController("run").setCaptionLabel("STOP")
#     getController("run").setColorLabel(  # e74c3c)
#     runStatus = 1
#     else if (runStatus == 1)
#             runStatus = 0
#             getController("run").setCaptionLabel("RUN PROGRAM")
#             getController("run").setColorLabel(255)
#             updateData()
#             myPort.write(data)
# def public void updateSA()
#     myPort.write(data)
#
# def public void clearSteps()
#     saveStatus = 2 # clear all steps / program
#     updateData()
#     myPort.write(data)
#     println("Clear: " + data)
#     positionsCounter = 0
#     saveStatus = 0
#
def updateData():
    data = str(saveStatus)
    + "," + str(runStatus)
    + "," + str(SliderVar1.get())
    + "," + str(SliderVar2.get())
    + "," + str(SliderVar3.get())
    + "," + str(SliderVarZ.get())
    + "," + str(gripperValue)
    + "," + str(speedSlider)
    + "," + str(accelerationSlider)

    # Sie koennen mithilfe von F-Strings auch, there is programming ghost inside me.
    # Y = 50
    # f'{Y},{X}
    # oder f"{X},{Y}"

# _______ Kopfzeile: Info Robot mit Ueberschrift und Zeit__________#
#label_b = tk.Label(text="Label B", bg="orange")
opts = { 'ipadx': 0, 'ipady': 0 , 'sticky': 'nesw' }
# #label_b.grid(row=1, column=0, columnspan=20, **opts)
#label_d.grid(row=3, column=0, rowspan=4, **opts)
# ______ Label Robot - row 0 + row 1________#
Label0 = tk.Label(text='SCARA Robot Control', background="grey91", font=font11, foreground="#091833")
Label0.grid(row=0, column=1, columnspan=120, **opts)
Label1 = Label(text=localtime, background="grey91", font=font16, fg="steel blue")
Label1.grid(row=1, column=1, columnspan=120, **opts)

Fwd_Kin = tk.Frame(window)
Fwd_Kin.grid(row=2, column=0)


Label2 = tk.Label(master=Fwd_Kin, text='Forward Kinematics:', background="grey91", font=font14, foreground="#091833")
Label2.grid(row=2, column=0, **opts)

Label3 = tk.Label(master=Fwd_Kin, text='J1:', background="grey91", font=font12, foreground="#091833")
Label3.grid(row=3, column=0, **opts)

Label4 = tk.Label(master=Fwd_Kin, text='J2:', background="grey91", font=font12, foreground="#091833")
Label4.grid(row=4, column=0, **opts)

Label5 = tk.Label(master=Fwd_Kin, text='J3:', background="grey91", font=font12, foreground="#091833")
Label5.grid(row=5, column=0, **opts)

Label6 = tk.Label(master=Fwd_Kin, text='Z', background="grey91", font=font12, foreground="#091833")
Label6.grid(row=6, column=0, **opts)

Slider1_4 = tk.Scale(master=Fwd_Kin, from_=0, to=200, orient=tk.HORIZONTAL, variable=SliderVar1, command=print_value2)# variable=myVar1, command=print_value1(myVar1))
Slider1_4.grid(row=3, column=2, **opts) #columnspan=30
Slider1_5 = tk.Scale(master=Fwd_Kin, from_=0, to=200, variable=SliderVar2, orient=tk.HORIZONTAL)# variable=myVar1, command=print_value1(myVar1))
Slider1_5.grid(row=4, column=2, **opts)
Slider1_6 = tk.Scale(master=Fwd_Kin, from_=0, to=200, variable=SliderVar3, orient=tk.HORIZONTAL)# variable=myVar1, command=print_value1(myVar1))
Slider1_6.grid(row=5, column=2, **opts)
Slider1_7 = tk.Scale(master=Fwd_Kin, from_=0, to=200, variable=SliderVarZ, orient=tk.HORIZONTAL)# variable=myVar1, command=print_value1(myVar1))
Slider1_7.grid(row=6, column=2, **opts)

# # ______ Label Robot - Sauele 2________#
Inv_Kin = tk.Frame(window)
Inv_Kin.grid(row=2, column=1)
#-------------Inversed Kinematics----------------------
Label20 = tk.Label(master=Inv_Kin, text='Inversed Kinematics:', width= 30, background="grey91", font=font14, foreground="#091833")
Label20.grid(row=2, column=0) #ipadx=5, ipady=5

entry1 = tk.Entry(master=Inv_Kin, width=4, background="grey91", textvariable=EntryVar_xP, font=font14, foreground="#091833")
entry1.grid(row=3, column=0, sticky="w")

entry2 = tk.Entry(master=Inv_Kin, width=4, background="grey91", textvariable=EntryVar_yP, font=font14, foreground="#091833")
entry2.grid(row=3, column=0, ipadx=4, sticky="n")

entry3 = tk.Entry(master=Inv_Kin, width=4, background="grey91", textvariable=EntryVar_zP, font=font14, foreground="#091833")
entry3.grid(row=3, column=0, ipadx=2, sticky="e")

Label21 = tk.Label(master=Inv_Kin, text='X:', font=font14,  foreground="#091833")
Label21.grid(row=4, column=0, sticky="w", ipadx=5, ipady=5) #ipadx=5, ipady=5
ok1_button = tk.Button(master=Inv_Kin, text="OK", font=font13)
ok1_button.grid(row=3, column=0,  padx=50, ipady=0, sticky="nw") # pack all your widgets

Label22 = tk.Label(master=Inv_Kin, text='Y:', font=font14, foreground="#091833")
Label22.grid(row=4, column=0, sticky="n", ipadx=60, ipady=0) #ipadx=5, ipady=5
ok2_button = tk.Button(master=Inv_Kin, text="OK", font=font13)
ok2_button.grid(row=3, column=0, padx=130, ipady=0, sticky="e") # pack all your widgets

Label23 = tk.Label(master=Inv_Kin, text='Z:', font=font14, foreground="#091833")
Label23.grid(row=4, column=0, sticky="e", ipadx=30, pady=0) #ipadx=5, ipady=5
ok3_button = tk.Button(master=Inv_Kin, text="OK", font=font13)
ok3_button.grid(row=3, column=0, padx=55, ipady=0, sticky="ne") # pack all your widgets

move_button = tk.Button(master=Inv_Kin, text="MOVE TO POSITION", font=font14)
move_button.grid(row=5, column=0, sticky="n") # pack all your widgets

Label24 = tk.Label(master=Inv_Kin, text='Gripper', background="grey91", font=font14, foreground="#091833")
Label24.grid(row=6, column=0, sticky="n") #ipadx=5, ipady=5


Label25 = tk.Label(master=Inv_Kin, text='close', font=font13, foreground="#091833")
Label25.grid(row=7, column=0, sticky="w") #ipadx=5, ipady=5

Slider2_1 = tk.Scale(master=Inv_Kin, from_=0, to= 200, variable=gripperValue, orient=tk.HORIZONTAL)# variable=myVar1, command=print_value1(myVar1))
Slider2_1.grid(row=7, column=0, ipadx=4, sticky="n")

Label26 = tk.Label(master=Inv_Kin, text='open', font=font13, foreground="#091833")
Label26.grid(row=7, column=0, ipadx=2, sticky="e") #ipadx=5, ipady=5

save_button = tk.Button(master=Inv_Kin, text="SAVE POS.", font=font13)
save_button.grid(row=8, column=0, sticky="w") # pack all your widgets

run_button = tk.Button(master=Inv_Kin, text="RUN PROGRAM", font=font13)
run_button.grid(row=8, column=0, sticky="e") # pack all your widgets

Label27 = tk.Label(master=Inv_Kin, text='last saved position:', font=font13, foreground="#091833")
Label27.grid(row=9, column=0, ipadx=2, sticky="w") #ipadx=5, ipady=5

clear_button = tk.Button(master=Inv_Kin, text="(CLEAR)", font=font13)
clear_button.grid(row=10, column=0, sticky="w") # pack all your widgets

update_button = tk.Button(master=Inv_Kin, text="(UPDATE)", font=font13)
update_button.grid(row=10, column=0, sticky="e") # pack all your widgets

Label28 = tk.Label(master=Inv_Kin, text='Speed', font=font13, foreground="#091833") # from_=0, to=600,
Label28.grid(row=11, column=0, sticky="w") #ipadx=5, ipady=5

Label29 = tk.Label(master=Inv_Kin, text='Acceleration', font=font13, foreground="#091833")
Label29.grid(row=11, column=0, ipadx=2, sticky="e") #ipadx=5, ipady=5

entry4 = tk.Entry(master=Inv_Kin, width=3, background="grey91", font=font14, textvariable=EntryVarSpeed, foreground="#091833")
entry4.grid(row=12, column=0, sticky="w")

entry5 = tk.Entry(master=Inv_Kin, width=3, background="grey91", font=font14, textvariable=EntryVarAcceleration, foreground="#091833")
entry5.grid(row=12, column=0, ipadx=2, sticky="e")

# BildFr = tk.Frame(window, highlightcolor="green", highlightbackground="red", highlightthickness=5, width=160, height=200)
# BildFr.grid(row=2, column=2, padx=50, pady=0, ipadx=50, ipady=50)

# car = ImageTk.PhotoImage(Image.open("Documents/car.jpg"))
# Image = Label(window, image=car)
# Image.grid(row=2, column=2)
# button_exit = Button(window, text="exit program", command=window.quit)
# button_exit.grid(row=3, column=2)
def exitAfterButtonpress(): #function call to set speed of motor
 speed_scale.config(image = car, command=window.quit) #set image to button
car = ImageTk.PhotoImage(Image.open("Documents/car.jpg"))
speed_scale = Button(window, image=car, bg="white", relief=tk.FLAT,command = exitAfterButtonpress) #set image to button
speed_scale.grid(row=2, column=2)

window.mainloop()