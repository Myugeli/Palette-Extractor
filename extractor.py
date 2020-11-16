'''
Created on Nov 10, 2020

@author: myuey
'''
from PIL import Image, ImageTk
from numpy import zeros, reshape, array, vectorize, asarray, linalg
from tkinter import Tk, Button, Entry, Label, messagebox, Toplevel, LEFT, W



def gui_initiate():
    root = Tk()
    root.title("Palette Extractor by Myui")
    root.geometry('900x400')
    root.resizable(width=False, height=False)
    min_val = 1
    dim_max_val = 100
    rnd_max_val = 255
    tun_max_val = 300
    dim_val = 50
    rnd_val = 35
    tun_val = 110
    img_prev_size = 200
    tar_lbl = Label(root, text="Target Image File: ")
    tar_lbl.grid(column = 0, row = 0)
    tar_txt = Entry(root, width = 20, justify='center') 
    tar_txt.grid(column = 1, row = 0) 
    tar_img = zeros((img_prev_size, img_prev_size * 2, 3))
    tar_img_disp = ImageTk.PhotoImage(Image.fromarray(tar_img, mode = "RGB"))
    tar_prev_img = Label(root, image = tar_img_disp)
    tar_prev_img.grid(column = 4, row = 0)
    
    def tar_btn_click():
        tar_file_path = tar_txt.get()  
        if not tar_file_path:
            messagebox.showerror(title="Error", message="No filepath entered.")
        else:
            
            try:     
                tar_img = Image.open(tar_file_path)
                global tar_img_disp 
                tar_img = tar_img.resize((img_prev_size * 2, img_prev_size), Image.ANTIALIAS)
                tar_img_disp = ImageTk.PhotoImage(tar_img)
                tar_prev_img.configure(image = tar_img_disp)
            except FileNotFoundError:
                messagebox.showerror(title="Error", message="File '" + tar_file_path + "' not found.")
              
        
        
    tar_btn = Button(root, text="Set Target", command = tar_btn_click)
    tar_btn.grid(column = 2, row = 0)
    tar_prev_lbl = Label(root, text = "Target Preview: ")
    tar_prev_lbl.grid(column = 3, row = 0)

    dim_lbl = Label(root, text = "Resize To: ")
    dim_lbl.grid(column = 0, row = 1)
    dim_txt = Entry(root, width = 10, justify='center')
    dim_txt.insert(0, str(dim_val))
    dim_txt.grid(column = 1, row = 1)
    dim_lim_lbl = Label(root, text = "(" + str(min_val) + "-" + str(dim_max_val) + ")")
    dim_lim_lbl.grid(column = 2, row = 1)

    
    rnd_lbl = Label(root, text = "Round Colours To: ")
    rnd_lbl.grid(column = 0, row = 2)
    rnd_txt = Entry(root, width = 10, justify='center')
    rnd_txt.insert(0, str(rnd_val))
    rnd_txt.grid(column = 1, row = 2)
    rnd_lim_lbl = Label(root, text = "(" + str(min_val) + "-" + str(rnd_max_val) + ")")
    rnd_lim_lbl.grid(column = 2, row = 2)
    
    tun_lbl = Label(root, text = "Tuning Distance: ")
    tun_lbl.grid(column = 0, row = 3)
    tun_txt = Entry(root, width = 10, justify='center')
    tun_txt.insert(0, str(tun_val))
    tun_txt.grid(column = 1, row = 3)
    tun_lim_lbl = Label(root, text ="(" + str(min_val) + "-" + str(tun_max_val) + ")")
    tun_lim_lbl.grid(column = 2, row = 3)

    pal_file_lbl = Label(root, text = "Palette File Name:")
    pal_file_lbl.grid(column = 3, row = 5)
    
    pal_file_txt = Entry(root, width = 30, justify='center')
    pal_file_txt.insert(0, "palette.png")
    pal_file_txt.grid(column = 4, row = 5)
    
    pal_amt_lbl = Label(root, text = "Number of Colours in Palette:")
    pal_amt_lbl.grid(column = 3, row = 4)
    
    pal_num_lbl = Label(root, text = "0")
    pal_num_lbl.grid(column = 4, row = 4)
    
    pal_img = zeros((int(img_prev_size / 4), img_prev_size * 2, 3))
    pal_img_disp = ImageTk.PhotoImage(Image.fromarray(pal_img, mode = "RGB"))
    pal_prev_img = Label(root, image = pal_img_disp)
    pal_prev_img.grid(column = 4, row = 2)
    
    def inst_window():
        inst_disp = Toplevel(root)
        inst_disp.title("Instructions")
        inst_disp.geometry('900x150')
        inst_disp.focus_force()
        inst_disp.resizable(width=False, height=False)
        welc_txt = "This application will make a palette image from an input image."
        step1_txt = "Step 1: Enter target image filepath. Click 'Set Target' to make sure you have the right one. Please make sure the application and the input image are in the same folder."
        step2_txt = "Step 2: Enter resize value. The larger this is, the more colours there will be in the palette, but it will take more time to process."
        step3_txt = "Step 3: Enter rounding value. This controls colour variation. The larger this is, the less colours there will be in the palette."
        step4_txt = "Step 4: Enter tuning value. This controls how close together the palette colours will be. The larger this is, the less colours there will be in the palette."
        step5_txt = "Step 5: Click 'Preview' to preview to palette. The number of colours in it will also be displayed."
        step6_txt = "Step 6: Enter palette filename and click 'Save Palette'. The palette will be saved to the folder the application is in."
        
        welc_lbl = Label(inst_disp, text = welc_txt, justify=LEFT)
        welc_lbl.grid(sticky = W, column=0,row=0)       
        step1_lbl = Label(inst_disp, text = step1_txt, justify=LEFT)
        step1_lbl.grid(sticky = W, column=0,row=1)
        step2_lbl = Label(inst_disp, text = step2_txt, justify=LEFT)
        step2_lbl.grid(sticky = W, column=0,row=2)
        step3_lbl = Label(inst_disp, text = step3_txt, justify=LEFT)
        step3_lbl.grid(sticky = W, column=0,row=3)
        step4_lbl = Label(inst_disp, text = step4_txt, justify=LEFT)
        step4_lbl.grid(sticky = W, column=0,row=4)
        step5_lbl = Label(inst_disp, text = step5_txt, justify=LEFT)
        step5_lbl.grid(sticky = W, column=0,row=5)
        step6_lbl = Label(inst_disp, text = step6_txt, justify=LEFT)
        step6_lbl.grid(sticky = W, column=0,row=6)
        
    inst_btn = Button(root, text = "Instructions", command = inst_window)
    inst_btn.grid(column = 0, row = 7)
    
    def pal_prev_btn_click():
        img_path = tar_txt.get()
        dim = dim_txt.get()
        rnd = rnd_txt.get()
        tun = tun_txt.get()
        num_chk_flag = dim.isnumeric() and rnd.isnumeric() and tun.isnumeric()
        
        if not num_chk_flag:
            messagebox.showerror(title="Error", message="Invalid parameter values.")
        else:
            dim_rng_flag = int(dim) <= dim_max_val and int(dim) >= min_val
            rnd_rng_flag = int(rnd) <= rnd_max_val and int(rnd) >= min_val
            tun_rng_flag = int(tun) <= tun_max_val and int(tun) >= min_val
            if not (dim_rng_flag and rnd_rng_flag and tun_rng_flag):
                messagebox.showerror(title="Error", message="Parameter values out of range.")
            elif not img_path:
                messagebox.showerror(title="Error", message="No image filepath entered.")
            else:
                try:       
                    palette, num_col = create_palette(img_path, int(dim), int(rnd), int(tun))
                    global pal_img_disp
                    pal_img = palette.resize((img_prev_size * 2, int(img_prev_size / 4)))
                    pal_img_disp = ImageTk.PhotoImage(pal_img)
                    pal_prev_img.configure(image = pal_img_disp)
                    pal_num_lbl.configure(text = str(num_col))
                except FileNotFoundError:
                    messagebox.showerror(title="Error", message="File '" + img_path + "' not found.")    
    
    pal_prev_btn = Button(root, text = "Preview", command = pal_prev_btn_click)
    pal_prev_btn.grid(column = 1, row = 6)
    
    pal_prev_lbl = Label(root, text = "Palette Preview:")
    pal_prev_lbl.grid(column = 3, row = 2)
    
    def pal_save_btn_click():
        img_path = tar_txt.get()
        dim = dim_txt.get()
        rnd = rnd_txt.get()
        tun = tun_txt.get()
        pal_file_path = pal_file_txt.get()
        num_chk_flag = dim.isnumeric() and rnd.isnumeric() and tun.isnumeric()
        if not num_chk_flag:
            messagebox.showerror(title="Error", message="Invalid parameter values.")
        else:
            dim_rng_flag = int(dim) <= dim_max_val and int(dim) >= min_val
            rnd_rng_flag = int(rnd) <= rnd_max_val and int(rnd) >= min_val
            tun_rng_flag = int(tun) <= tun_max_val and int(tun) >= min_val
            if not (dim_rng_flag and rnd_rng_flag and tun_rng_flag):
                messagebox.showerror(title="Error", message="Parameter values out of range.")
            elif not img_path:
                messagebox.showerror(title="Error", message="No image filepath entered.")
            elif not pal_file_path:
                messagebox.showerror(title="Error", message="No palette filepath entered.")
            else:
                try:    
                    palette, num_col = create_palette(img_path, int(dim), int(rnd), int(tun))      
                    save_palette(palette, pal_file_path)
                except ValueError:
                    messagebox.showerror(title="Error", message="Invalid palette filepath.")
    
    pal_save_btn = Button(root, text = "Save Palette", command = pal_save_btn_click)
    pal_save_btn.grid(column = 4, row = 6)
    

    root.mainloop()

def get_image(image_path, dim = 50):
    #returns np array of pixel values
    img = Image.open(image_path, "r")   
    img = img.convert("RGB")
    dim_w,dim_h = img.size
    width = dim
    height = dim
    if dim_w < dim:
        width = dim_w
    if dim_h < dim:
        height = dim_h
    img = img.resize((width,height), Image.ANTIALIAS)
    pix_values = array(list(img.getdata())).reshape((width, height, 3))
    return pix_values

def round_image(img, round_factor = 35):
    rounder = lambda t: int(t/round_factor)*round_factor
    vec_rounder = vectorize(rounder)
    img = vec_rounder(img)
    return img

def get_unique_colours(img):
    #returns list of different rgb values in the img given
    img_list = []
    shape = img.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            pix_val = tuple(img[i][j]) 
            img_list.append(pix_val)
    res = list(set(img_list))      
    return res        
def tune_colours(colour_list, tune_amt = 110):
    #Trims colour list to remove colours that are too close, defined by tune_amt value
    #tune_amt is a distance in RGB space. Defaults to 20
    res = []
    #loop through colour_list, pull an entry, and compare to entries in res list
    for in_entry in colour_list:
        entry_flag = False
        for res_entry in res:
                #calculate distance between the colours
                dist = dist_calc(in_entry, res_entry)
                entry_flag = dist < tune_amt
        if not entry_flag:
            res.append(in_entry)
    res.sort()
    return res  
def dist_calc(tup1, tup2):
    #returns space distance between two tuples with the same length
    ar1 = asarray(tup1)
    ar2 = asarray(tup2)
    dist = linalg.norm(ar1 - ar2) 
    return dist
def create_palette_img(colour_list, sq_dim = 500):
    #creates a palette image containing each colour in the list as a square of size sq_dim, dimH squares tall  
    dimH = len(colour_list)
    #create numpy array
    res_arr = zeros((sq_dim, dimH * sq_dim, 3), dtype = 'uint8')
    #loop through colour list and populate the appropriate numpy array region
    for i,colour in zip(range(len(colour_list)),colour_list):
        #create array replacement
        col_arr = zeros((sq_dim, sq_dim, 3), dtype = 'uint8')
        ind_arr = asarray(colour)
        col_arr[:] = ind_arr
        #place array replacement
        #calculate boundaries
        x_bnd1 = 0
        x_bnd2 = sq_dim
        y_bnd1 = i * sq_dim
        y_bnd2 = y_bnd1 + sq_dim
        res_arr[x_bnd1:x_bnd2,y_bnd1:y_bnd2, 0:3] = col_arr
    #write the numpy array to an image 
    res_img = Image.fromarray(res_arr, mode = "RGB")
    return res_img
def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

def save_palette(palette, palette_file = "palette.png"):
    palette.save(palette_file)
    
def create_palette(img_file, img_dim = 50, round_val = 35, tune_val = 110):
    img = get_image(img_file, img_dim)
    img = round_image(img, round_val)
    uni_colour = get_unique_colours(img)
    tune_colour = tune_colours(uni_colour, tune_val)
    palette = create_palette_img(tune_colour)
    return palette, len(tune_colour)

gui_initiate()
