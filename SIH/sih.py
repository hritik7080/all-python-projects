from __future__ import print_function
import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
import auth


import io

import httplib2
from googleapiclient import discovery
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from oauth2client import tools
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
from tkinter.filedialog import askopenfile
import httplib2
# import sih_support
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Drive API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.getCredentials()

http = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http)

def listFiles(size):
    results = drive_service.files().list(pageSize=size,fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print('{0} ({1})'.format(item['name'], item['id']))


    # print('File ID: %s' % file.get('id'))

def downloadFile(file_id,filepath):
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with io.open(filepath,'wb') as f:
        fh.seek(0)
        f.write(fh.read())

def createFolder(name):
    file_metadata = {
    'name': name,
    'mimeType': 'application/vnd.google-apps.folder'
    }
    file = drive_service.files().create(body=file_metadata,fields='id').execute()
    print ('Folder ID: %s' % file.get('id'))

def searchFile(size,query):
    results = drive_service.files().list(pageSize=size,fields="nextPageToken, files(id, name, kind, mimeType)",q=query).execute()
    items = results.get('files', [])
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(item)
            print('{0} ({1})'.format(item['name'], item['id']))
# uploadFile('unnamed.jpg','unnamed.jpg','image/jpeg')
# downloadFile('1a_AaYYy2THHj_PcsOdCjbnMI7rQyd8KY','google.jpg')
# createFolder('Google')
searchFile(10,"name contains 'unnamed'")

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    # sih_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    sih_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family Tahoma -size 14 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font11 = "-family Tahoma -size 12 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font12 = "-family Tahoma -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font13 = "-family Tahoma -size 14 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font14 = "-family Tahoma -size 13 -weight normal -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family Tahoma -size 16 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1697x950+192+172")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#011007")

        self.Canvas1 = tk.Canvas(top)
        self.Canvas1.place(relx=0.006, rely=0.011, relheight=0.982
                , relwidth=0.986)
        self.Canvas1.configure(background="#011e61")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(insertbackground="black")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c9c8cc")
        self.Canvas1.configure(selectforeground="black")

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip3 = ttk.Sizegrip(self.Canvas1)
        self.TSizegrip3.place(anchor='se', relx=1.0, rely=1.0)

        self.TFrame1 = ttk.Frame(self.Canvas1)
        self.TFrame1.place(relx=0.012, rely=0.021, relheight=0.284
                , relwidth=0.296)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.0, rely=0.0, height=49, width=495)
        self.TLabel1.configure(background="#000000")
        self.TLabel1.configure(foreground="#f0f0f0")
        self.TLabel1.configure(font=font9)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(text='''Tlabel''')

        self.TEntry1 = ttk.Entry(self.TFrame1)
        self.TEntry1.place(relx=0.364, rely=0.302, relheight=0.155
                , relwidth=0.578)
        self.TEntry1.configure(font=font11)
        self.TEntry1.configure(foreground="#000000")
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")

        self.TLabel6 = ttk.Label(self.TFrame1)
        self.TLabel6.place(relx=0.02, rely=0.264, height=49, width=155)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font=font10)
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(text='''Tlabel''')

        self.TEntry2 = ttk.Entry(self.TFrame1)
        self.TEntry2.place(relx=0.364, rely=0.491, relheight=0.155
                , relwidth=0.578)
        self.TEntry2.configure(font=font11)
        self.TEntry2.configure(takefocus="")
        self.TEntry2.configure(cursor="ibeam")

        self.TLabel7 = ttk.Label(self.TFrame1)
        self.TLabel7.place(relx=0.02, rely=0.491, height=39, width=145)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font=font10)
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(text='''Tlabel''')

        self.Button1 = tk.Button(self.TFrame1)
        self.Button1.place(relx=0.364, rely=0.717, height=44, width=97)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0b0b0b")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font12)
        self.Button1.configure(foreground="#f2f2f2")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Button''')

        self.TFrame2 = ttk.Frame(self.Canvas1)
        self.TFrame2.place(relx=0.323, rely=0.021, relheight=0.284
                , relwidth=0.356)
        self.TFrame2.configure(relief='groove')
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")

        self.TFrame3 = ttk.Frame(self.Canvas1)
        self.TFrame3.place(relx=0.693, rely=0.075, relheight=0.895
                , relwidth=0.296)
        self.TFrame3.configure(relief='groove')
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief="groove")

        self.Scrolledtext1 = ScrolledText(self.Canvas1)
        self.Scrolledtext1.place(relx=0.012, rely=0.697, relheight=0.28
                , relwidth=0.67)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")

        self.TFrame4 = ttk.Frame(self.Canvas1)
        self.TFrame4.place(relx=0.012, rely=0.332, relheight=0.284
                , relwidth=0.296)
        self.TFrame4.configure(relief='groove')
        self.TFrame4.configure(borderwidth="2")
        self.TFrame4.configure(relief="groove")

        self.TLabel2 = ttk.Label(self.TFrame4)
        self.TLabel2.place(relx=0.0, rely=0.0, height=49, width=495)
        self.TLabel2.configure(background="#040404")
        self.TLabel2.configure(foreground="#f2f2f2")
        self.TLabel2.configure(font=font9)
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='center')
        self.TLabel2.configure(text='''Tlabel''')

        self.TEntry3 = ttk.Entry(self.TFrame4)
        self.TEntry3.place(relx=0.101, rely=0.453, relheight=0.192
                , relwidth=0.477)
        self.TEntry3.configure(font=font13)
        self.TEntry3.configure(takefocus="")
        self.TEntry3.configure(cursor="ibeam")

        self.Button2 = tk.Button(self.TFrame4)
        self.Button2.place(relx=0.667, rely=0.453, height=54, width=107)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#000000")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font=font12)
        self.Button2.configure(foreground="#f7f7f7")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.TFrame5 = ttk.Frame(self.Canvas1)
        self.TFrame5.place(relx=0.323, rely=0.332, relheight=0.284
                , relwidth=0.356)
        self.TFrame5.configure(relief='groove')
        self.TFrame5.configure(borderwidth="2")
        self.TFrame5.configure(relief="groove")

        self.TLabel3 = ttk.Label(self.TFrame5)
        self.TLabel3.place(relx=0.0, rely=0.0, height=49, width=595)
        self.TLabel3.configure(background="#0a0a0a")
        self.TLabel3.configure(foreground="#f3f3f3")
        self.TLabel3.configure(font=font9)
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='center')
        self.TLabel3.configure(text='''Tlabel''')

        self.Entry1 = tk.Entry(self.TFrame5)
        self.Entry1.place(relx=0.034, rely=0.302,height=40, relwidth=0.545)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=font14)
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")




        def get_file():
            file = askopenfile(mode='r', filetypes=[('PNG File', '*.png')])
            self.Button4 = tk.Button(self.TFrame5)
            self.Button4.place(relx=0.605, rely=0.264, height=174, width=217)
            self.Button4.configure(activebackground="#ececec")
            self.Button4.configure(activeforeground="#000000")
            self.Button4.configure(background="#d9d9d9")
            self.Button4.configure(disabledforeground="#a3a3a3")
            self.Button4.configure(foreground="#000000")
            self.Button4.configure(highlightbackground="#d9d9d9")
            self.Button4.configure(highlightcolor="black")
            self.Button4.configure(pady="0")
            self.Button4.configure(text='''Button1''')
            t=""
            for i in file.name[::-1]:
                if i=='/':
                    break
                t+=i
            name=t[::-1]
            print(name)

            def uploadFile(filename, filepath, mimetype):
                file_metadata = {'name': filename}
                media = MediaFileUpload(filepath, mimetype=mimetype)
                file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
                print('File ID: %s' % file.get('id'))

                self.Entry2 = tk.Entry(self.TFrame5)
                self.Entry2.place(relx=0.034, rely=0.75, height=40, relwidth=0.545)
                self.Entry2.configure(background="white")
                self.Entry2.configure(disabledforeground="#a3a3a3")
                self.Entry2.configure(font=font14)
                self.Entry2.configure(foreground="#000000")
                self.Entry2.configure(insertbackground="black")
                self.Entry2.insert(0, file.get('id'))


            self.Button5 = tk.Button(self.TFrame5)
            self.Button5.place(relx=0.3, rely=0.528, height=44, width=117)
            self.Button5.configure(activebackground="#ececec")
            self.Button5.configure(activeforeground="#000000")
            self.Button5.configure(background="#080808")
            self.Button5.configure(disabledforeground="#a3a3a3")
            self.Button5.configure(font=font12)
            self.Button5.configure(foreground="#f5f5f5")
            self.Button5.configure(highlightbackground="#d9d9d9")
            self.Button5.configure(highlightcolor="black")
            self.Button5.configure(pady="0")
            self.Button5.configure(text="Serach", command=lambda : uploadFile(name, file.name, 'image/png'))



        self.Button3 = tk.Button(self.TFrame5)
        self.Button3.place(relx=0.034, rely=0.528, height=44, width=117)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#080808")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font=font12)
        self.Button3.configure(foreground="#f5f5f5")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Browse''', command=lambda: get_file())





        self.TLabel4 = ttk.Label(self.Canvas1)
        self.TLabel4.place(relx=0.012, rely=0.643, height=49, width=1125)
        self.TLabel4.configure(background="#060606")
        self.TLabel4.configure(foreground="#f7f7f7")
        self.TLabel4.configure(font=font9)
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(text='''Tlabel''')

        self.TLabel5 = ttk.Label(self.Canvas1)
        self.TLabel5.place(relx=0.693, rely=0.021, height=49, width=495)
        self.TLabel5.configure(background="#070707")
        self.TLabel5.configure(foreground="#f4f4f4")
        self.TLabel5.configure(font=font9)
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(text='''Tlabel''')

        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.TSizegrip2 = ttk.Sizegrip(top)
        self.TSizegrip2.place(anchor='se', relx=1.0, rely=1.0)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





