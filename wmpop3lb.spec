Summary:	Multi POP3 accounts mailbox checker
Summary(pl):	Monitor skrzynek pocztowych POP3
Name:		wmpop3lb
Version:	2.4.2
Release:	3
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://lbj.free.fr/wmpop3/%{name}%{version}.tar.gz
# Source0-md5:	40760d8963c25d58dea84679a390f1ac
Source1:	%{name}.desktop
Patch0:		%{name}-opt.patch
URL:		http://wmpop3lb.jourdain.org/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMPop3LB can connect to up to 6 POP3 accounts to check if there is a
new mail, get the "From:" and "Subject:" header fields of each mail
and display them in a window. Messages can be deleted directly off the
servers by selecting the mails to delete and clicking the "delete"
button. A command can be lunched for each new mail received, for each
selected message or for each server.

%description -l pl
WMPop3LB mo¿e po³±czyæ siê do 6 kont POP3 aby sprawdziæ czy znajduje
siê tam nowa poczta, pobraæ z ka¿dego listu nag³ówki "Od:" i "Tytu³:"
a nastêpnie wy¶wietliæ je w oknie. Wiadomo¶ci mog± byæ wymazane
bezpo¶rednio z serwerów poprzez wskazanie listu do wykasowania i
klikniêcie przycisku "delete". Dla ka¿dego nowego listu, wskazanej
wiadomo¶ci albo dla ka¿dego serwera mo¿e byæ uruchomiona odpowiednia
komenda.

%prep
%setup -q -n %{name}%{version}
%patch0 -p1

%build
%{__make} -C wmpop3 \
	OPT="%{rpmcflags}" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install wmpop3/wmpop3lb $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE_LOG README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/%{name}.desktop
