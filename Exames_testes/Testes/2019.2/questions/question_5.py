# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#euler 

a = 1
def dz(t,y,z):
    return a + t**2 + t*z
def dy(t,y,z):
    return z

def euler(t,y,z,h):
    for i in range(2): 
        z_ant = z
        y_ant = y
        t_ant = t
        t = t_ant + h
        z = z_ant + h*dz(t_ant, y_ant, z_ant)
        y = y_ant + h*dy(t_ant, y_ant, z_ant) 
        
        print(t,y)
        
euler(0,1,2,0.25)


 def rk4(t,y,z,h): 
    for i in range(2): 
        t_ant = t 
        y_ant = y 
        z_ant = z 
        t = t_ant + h 
        
        delta1_y = h*dy(t_ant, y_ant, z_ant )
        delta1_z = h*dz(t_ant, y_ant, z_ant )
        
        delta2_y = h*dy(t_ant + h/2, y_ant + delta1_y/2, z_ant + delta1_z /2 )
        delta2_z =  h*dz (t_ant + h/2, y_ant + delta1_y/2, z_ant + delta1_z /2 )
        
        delta3_y =  h*dy(t_ant + h/2, y_ant + delta2_y/2, z_ant + delta2_z /2 )
        delta3_z = h*dz(t_ant + h/2, y_ant + delta2_y/2, z_ant + delta2_z /2 )
        
        delta4_y = h*dy(t_ant + h, y_ant + delta3_y, z_ant + delta3_z )
        delta4_z = h*dz(t_ant + h, y_ant + delta3_y, z_ant + delta3_z )
        
        deltay = delta1_y/6 + delta2_y/3 + delta3_y/3 + delta4_y/6
        deltaz = delta1_z/6 + delta2_z/3 + delta3_z/3 + delta4_z/6
        
        y = deltay + y
        z = deltaz + z 
        print(t,y)
        
rk4(0,1,2,0.25)