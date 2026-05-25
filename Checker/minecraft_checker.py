r='❌ Close'
q='✅ Clean!'
p='<Leave>'
o='<Enter>'
n='1.0'
m='white'
l='#484f58'
k='runas'
j='#da3633'
i='Consolas'
h='#1a1f2b'
g='y'
f='#06070a'
e='#1c2533'
d='#0a0d14'
c='#c9d1d9'
b='hand2'
a='#161b22'
Z='right'
Y=False
X=None
W='#8b949e'
U='#1f6feb'
T='flat'
R=''
Q='bold'
P='both'
O='❌ Error'
N='left'
L='end'
K='#0d1117'
J='#ffffff'
I='#d29922'
H='#0f1219'
G='#3fb950'
F='x'
E='Segoe UI'
D=True
B='#f85149'
import tkinter as A
from tkinter import ttk
import subprocess as S,os as C,sys,threading as M,ctypes as V
class s:
	def __init__(B):
		B.root=A.Tk();B.root.title('Minecraft Checker');B.root.geometry('1000x700');B.root.resizable(Y,Y);B.root.configure(bg=f)
		if getattr(sys,'frozen',Y):B.app_dir=C.path.dirname(sys.executable)
		else:B.app_dir=C.path.dirname(C.path.abspath(__file__))
		B.everything_path=C.path.join(B.app_dir,'Everything.exe');B.shellbag_path=C.path.join(B.app_dir,'ShellBagAnalyzerCleaner.exe');B.browserdownloadview_path=C.path.join(B.app_dir,'BrowserDownloadsView.exe');B.jumplist_path=C.path.join(B.app_dir,'JumpListView.exe');B.executedprograms_path=C.path.join(B.app_dir,'xecutedProgramsList.exe');B.prefetch_path=C.path.join(B.app_dir,'WinPrefetchView.exe');B.usbdeview_path=C.path.join(B.app_dir,'USBDeview.exe');B.userassist_path=C.path.join(B.app_dir,'UserAssistView.exe');B.root.update_idletasks();D=B.root.winfo_width();E=B.root.winfo_height();F=B.root.winfo_screenwidth()//2-D//2;G=B.root.winfo_screenheight()//2-E//2;B.root.geometry(f"{D}x{E}+{F}+{G}");B.create_widgets();B.check_files()
	def create_widgets(B):
		t='#1a2332';j='#58a6ff';S='#e94560';M=A.Canvas(B.root,bg=f,highlightthickness=0);M.pack(fill=P,expand=D);M.create_rectangle(0,0,1000,2,fill=S,outline=R);M.create_rectangle(0,697,1000,2,fill=S,outline=R);V=A.Frame(M,bg=f);V.place(x=0,y=2,width=1000,height=695);C=A.Frame(V,bg=d,width=360);C.pack(side=N,fill=g);C.pack_propagate(Y);O=A.Frame(C,bg=H);O.pack(fill=F);A.Label(O,text='⬡',font=(E,28),bg=H,fg=S).pack(pady=(15,0));A.Label(O,text='MINECHECK',font=(E,16,Q),bg=H,fg=J).pack();A.Label(O,text='tool launcher',font=(E,8),bg=H,fg='#5a6070').pack(pady=(0,12));u=A.Frame(C,bg=S,height=2);u.pack(fill=F,padx=20);A.Frame(C,bg=h,height=1).pack(fill=F,padx=20);v=A.Label(C,text='🔧 TOOLS',font=(E,9,Q),bg=d,fg=W);v.pack(anchor='w',padx=20,pady=(15,8));B.btns_frame=A.Frame(C,bg=d);B.btns_frame.pack(fill=P,expand=D,padx=15,pady=(0,10));B.create_all_buttons();X=A.Frame(C,bg=H);X.pack(fill=F,side='bottom');c=A.Frame(X,bg=H);c.pack(side=N,fill=F,padx=15,pady=8);B.status_dot=A.Label(c,text='●',font=(E,9),bg=H,fg=G);B.status_dot.pack(side=N,padx=(0,5));B.status_label=A.Label(c,text='Ready',font=(E,9),bg=H,fg=W);B.status_label.pack(side=N);e=A.Frame(X,bg=H);e.pack(side=Z,padx=15,pady=8);w=['E','S','B','J','X','P','U','A'];B.file_indicators=[]
		for x in w:k=A.Label(e,text=x,font=(E,7,Q),bg=H,fg=l);k.pack(side=N,padx=2);B.file_indicators.append(k)
		B.update_file_indicators();I=A.Frame(V,bg=K);I.pack(side=Z,fill=P,expand=D);q=A.Frame(I,bg=a);q.pack(fill=F);A.Label(q,text='📁 EVERYTHING SEARCH',font=(E,12,Q),bg=a,fg=j).pack(side=N,padx=20,pady=10);r=A.Frame(I,bg=K);r.pack(fill=P,expand=D,padx=20,pady=(10,10));B.search_text=A.Text(r,bg=K,fg=W,font=(i,10),insertbackground=m,relief=T,bd=0,wrap='word',selectbackground=U,selectforeground=J);B.search_text.pack(fill=P,expand=D);y='x-ray | celka | celestial | xray | autofish | autofarm | neat | wexide | venusfree | кфг | haruka | baritone | nursultan | britva | Ezka | nightproject | akrien | excellent | expensive | delta | hach | rassvet | newcode | moonproject | newlight | deadcode | impact | killaura | fanarme | minced | meteor | verist | fluger | nix | minced | wild | vape | doomsday | wexside | moon | monoton | dimasik | expensive | night | nightdlc | nigtix | rock | rockstar | relake';B.search_text.insert(n,y);s=A.Frame(I,bg=K);s.pack(fill=F,padx=20,pady=(0,12));L=A.Button(s,text='📋 COPY TO EVERYTHING',font=(E,9,Q),bg=t,fg=j,activebackground=U,activeforeground=J,relief=T,cursor=b,command=B.copy_search,padx=20,pady=8);L.pack(fill=F);L.bind(o,lambda e:L.configure(bg=U,fg=J));L.bind(p,lambda e:L.configure(bg=t,fg=j));A.Label(I,text='Search terms for Everything | Minecraft cheat files',font=(E,7),bg=K,fg='#30363d').pack(pady=(0,10));A.Label(C,text='v2.1 | By hero_684',font=(E,8,Q),bg=H,fg=W).place(x=15,y=5)
	def create_all_buttons(A):A.create_compact_btn(A.btns_frame,'📁 Everything','File search',U,A.open_everything);A.create_compact_btn(A.btns_frame,'🛡️ ShellBag','Registry analyzer','#7c3aed',A.open_shellbag);A.create_compact_btn(A.btns_frame,'💻 Processes','Process scanner',j,A.scan_processes);A.create_compact_btn(A.btns_frame,'📂 Recent','Recent files',I,A.check_recent);A.create_compact_btn(A.btns_frame,'🌐 Downloads','Browser history','#388bfd',A.open_browserdownloadview);A.create_compact_btn(A.btns_frame,'📋 Jump Lists','Quick access','#b8500a',A.open_jumplist);A.create_compact_btn(A.btns_frame,'⚡ Run History','Program log','#2ea043',A.open_executedprograms);A.create_compact_btn(A.btns_frame,'📋 Prefetch','Program run history','#c0392b',A.open_prefetch);A.create_compact_btn(A.btns_frame,'🔌 USB History','USB devices log','#16a085',A.open_usbdeview);A.create_compact_btn(A.btns_frame,'📝 UserAssist','Program usage log','#8e44ad',A.open_userassist)
	def create_compact_btn(D,parent,text,desc,color,cmd):C=A.Frame(parent,bg=d);C.pack(fill=F,pady=3);B=A.Button(C,text=text,font=(E,10,Q),bg=H,fg=c,activebackground=h,relief=T,bd=0,cursor=b,command=cmd,padx=12,pady=8,anchor='w',justify=N);B.pack(fill=F);B.bind(o,lambda e,b=B,c=color:b.configure(bg=h,fg=J));B.bind(p,lambda e,b=B:b.configure(bg=H,fg=c))
	def update_file_indicators(A):
		E=[A.everything_path,A.shellbag_path,A.browserdownloadview_path,A.jumplist_path,A.executedprograms_path,A.prefetch_path,A.usbdeview_path,A.userassist_path];F=[G if C.path.exists(A)else B for A in E]
		for(D,H)in enumerate(F):
			if D<len(A.file_indicators):A.file_indicators[D].configure(fg=H)
	def check_files(A):
		D={'Everything':A.everything_path,'ShellBag':A.shellbag_path,'Downloads':A.browserdownloadview_path,'JumpList':A.jumplist_path,'Executed':A.executedprograms_path,'Prefetch':A.prefetch_path,'USBDeview':A.usbdeview_path,'UserAssist':A.userassist_path};B=[A for(A,B)in D.items()if not C.path.exists(B)]
		if B:A.status_label.configure(text=f"⚠️ Missing: {", ".join(B)}",fg=I);A.status_dot.configure(fg=I)
		else:A.status_label.configure(text='All tools ready',fg=W);A.status_dot.configure(fg=G)
		A.update_file_indicators()
	def update_status(A,text,color=W):B=color;A.status_label.configure(text=text,fg=B);A.status_dot.configure(fg=B);A.root.update()
	def copy_search(A):A.root.clipboard_clear();A.root.clipboard_append(A.search_text.get(n,L).strip());A.update_status('✅ Search terms copied!',G)
	def open_everything(A):
		if not C.path.exists(A.everything_path):A.update_status('❌ Everything not found!',B);return
		A.update_status('🚀 Everything...',I)
		def E():
			try:S.Popen([A.everything_path]);A.root.after(0,lambda:A.update_status('✅ Everything',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def open_shellbag(A):
		if not C.path.exists(A.shellbag_path):A.update_status('❌ ShellBag not found!',B);return
		A.update_status('🚀 ShellBag...',I)
		def E():
			try:
				if V.windll.shell32.IsUserAnAdmin():S.Popen([A.shellbag_path],shell=D)
				else:V.windll.shell32.ShellExecuteW(X,k,A.shellbag_path,R,X,1)
				A.root.after(0,lambda:A.update_status('✅ ShellBag',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def open_browserdownloadview(A):
		if not C.path.exists(A.browserdownloadview_path):A.update_status('❌ Downloads not found!',B);return
		A.update_status('🚀 Downloads...',I)
		def E():
			try:S.Popen([A.browserdownloadview_path]);A.root.after(0,lambda:A.update_status('✅ Downloads',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def open_jumplist(A):
		if not C.path.exists(A.jumplist_path):A.update_status('❌ JumpList not found!',B);return
		A.update_status('🚀 JumpList...',I)
		def E():
			try:S.Popen([A.jumplist_path]);A.root.after(0,lambda:A.update_status('✅ JumpList',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def open_executedprograms(A):
		if not C.path.exists(A.executedprograms_path):A.update_status('❌ Run History not found!',B);return
		A.update_status('🚀 Run History...',I)
		def E():
			try:
				if V.windll.shell32.IsUserAnAdmin():C.startfile(A.executedprograms_path)
				else:V.windll.shell32.ShellExecuteW(X,k,A.executedprograms_path,R,X,1)
				A.root.after(0,lambda:A.update_status('✅ Run History',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def scan_processes(S):
		S.update_status('🔍 Processes...',I)
		def C():
			try:
				C=A.Toplevel(S.root);C.title('Processes');C.geometry('850x550');C.configure(bg=K);C.update_idletasks();f=C.winfo_screenwidth()//2-425;h=C.winfo_screenheight()//2-275;C.geometry(f"+{f}+{h}");A.Frame(C,bg=e).pack(fill=F);A.Label(C,text='📊 PROCESSES',font=(E,14,Q),bg=e,fg=J).pack(pady=10);M=A.Frame(C,bg=K);M.pack(fill=F,padx=10,pady=5);A.Label(M,text='🔍',bg=K,fg=J,font=(E,12)).pack(side=N,padx=(0,10));I=A.Entry(M,bg=a,fg=J,insertbackground=m,font=(E,10),relief=T);I.pack(side=N,fill=F,expand=D);V=A.Frame(C,bg=K);V.pack(fill=P,expand=D,padx=10,pady=10);W=A.Scrollbar(V);W.pack(side=Z,fill=g);H=A.Listbox(V,yscrollcommand=W.set,bg=a,fg=c,font=(i,9),selectbackground=U);H.pack(fill=P,expand=D);W.config(command=H.yview);k=['cheat','hack','inject','trainer','aimbot','wallhack','esp','xray','killaura','flyhack','speedhack','autoclicker','memory','debug','crack','keygen','patcher','wireshark','ollydbg','cheatengine','processhacker','celka','celestial','autofish','autofarm','wexide','venusfree','haruka','baritone','nursultan','britva','nightproject','akrien','excellent','expensive','delta','rassvet','newcode','moonproject','newlight','deadcode','impact','fanarme','minced','meteor','verist','fluger','nix','wild','vape','doomsday','wexside','moon','monoton','dimasik','nightdlc','nigtix','rock','rockstar','relake'];import psutil as n
				def X(filter_text=R):
					U='exe';T='name';Q='pid';K=filter_text;H.delete(0,L);A=[];M=[]
					for V in n.process_iter([Q,T,U]):
						try:
							F=V.info;C=F[T]
							if K and K.lower()not in C.lower():continue
							W=F[Q];N=F[U]or'N/A';X=N.lower();Z=C.lower()if C else R;O=Y;P=R
							for I in k:
								if I in Z or I in X:O=D;P=I;break
							E=f"PID:{W:6d} | {C:30s} | {N}"
							if O:E=f"⚠️ {E} [{P}]";A.append(E)
							else:M.append(f"   {E}")
						except:pass
					for J in A:H.insert(L,J);H.itemconfig(L,fg=B)
					if A:H.insert(L,'─'*85);H.itemconfig(L,fg=l)
					for J in M:H.insert(L,J);H.itemconfig(L,fg=c)
					if A:S.root.after(0,lambda:S.update_status(f"❌ Found: {len(A)}",B))
					else:S.root.after(0,lambda:S.update_status(q,G))
				I.bind('<KeyRelease>',lambda e:X(I.get()));X();d=A.Frame(C,bg=K);d.pack(fill=F,padx=10,pady=(0,10));A.Button(d,text='🔄 Refresh',bg=U,fg=J,font=(E,10),command=lambda:X(I.get()),padx=15,pady=5,relief=T,cursor=b).pack(side=N,padx=5);A.Button(d,text=r,bg=j,fg=J,font=(E,10),command=C.destroy,padx=15,pady=5,relief=T,cursor=b).pack(side=Z,padx=5)
			except:S.root.after(0,lambda:S.update_status(O,B))
		M.Thread(target=C,daemon=D).start()
	def open_prefetch(A):
		if not C.path.exists(A.prefetch_path):A.update_status('❌ Prefetch not found!',B);return
		A.update_status('🚀 Prefetch...',I)
		def E():
			try:
				if V.windll.shell32.IsUserAnAdmin():C.startfile(A.prefetch_path)
				else:V.windll.shell32.ShellExecuteW(X,k,A.prefetch_path,R,X,1)
				A.root.after(0,lambda:A.update_status('✅ Prefetch',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def open_userassist(A):
		if not C.path.exists(A.userassist_path):A.update_status('❌ UserAssist not found!',B);return
		A.update_status('🚀 UserAssist...',I)
		def E():
			try:S.Popen([A.userassist_path]);A.root.after(0,lambda:A.update_status('✅ UserAssist',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def open_usbdeview(A):
		if not C.path.exists(A.usbdeview_path):A.update_status('❌ USBDeview not found!',B);return
		A.update_status('🚀 USBDeview...',I)
		def E():
			try:S.Popen([A.usbdeview_path]);A.root.after(0,lambda:A.update_status('✅ USBDeview',G))
			except:A.root.after(0,lambda:A.update_status(O,B))
		M.Thread(target=E,daemon=D).start()
	def check_recent(N):
		N.update_status('🔍 Recent...',I)
		def H():
			try:
				W=C.path.join(C.environ['APPDATA'],'Microsoft\\Windows\\Recent');H=A.Toplevel(N.root);H.title('Recent Files');H.geometry('700x500');H.configure(bg=K);H.update_idletasks();X=H.winfo_screenwidth()//2-350;Y=H.winfo_screenheight()//2-250;H.geometry(f"+{X}+{Y}");A.Frame(H,bg=e).pack(fill=F);A.Label(H,text='📂 RECENT FILES',font=(E,14,Q),bg=e,fg=J).pack(pady=10);M=A.Frame(H,bg=K);M.pack(fill=P,expand=D,padx=10,pady=10);R=A.Scrollbar(M);R.pack(side=Z,fill=g);I=A.Listbox(M,yscrollcommand=R.set,bg=a,fg=c,font=(i,10),selectbackground=U);I.pack(fill=P,expand=D);R.config(command=I.yview);d=['.exe','.bat','.cmd','.ps1','.vbs','.jar','.dll','.msi']
				if C.path.exists(W):
					f=C.listdir(W);S=0
					for V in f:
						h=C.path.splitext(V)[1].lower()
						if h in d:I.insert(L,f"⚠️ {V}");I.itemconfig(L,fg=B);S+=1
						else:I.insert(L,f"   {V}")
					if S>0:N.root.after(0,lambda:N.update_status(f"❌ Found: {S}",B))
					else:N.root.after(0,lambda:N.update_status(q,G))
				A.Button(H,text=r,bg=j,fg=J,font=(E,10),command=H.destroy,padx=15,pady=5,relief=T,cursor=b).pack(pady=10)
			except:N.root.after(0,lambda:N.update_status(O,B))
		M.Thread(target=H,daemon=D).start()
	def run(A):A.root.mainloop()
if __name__=='__main__':t=s();t.run()