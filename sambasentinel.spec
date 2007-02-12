Summary:	SambaSentinel - a GTK+ frontend to smbstatus
Summary(pl.UTF-8):   SambaSentinel - interfejs GTK+ do smbstatus
Name:		sambasentinel
Version:	0.1
Release:	1
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://homepage.mac.com/mattsash/fink/SambaSentinel-%{version}.tar.gz
# Source0-md5:	f9213946e051ec0491e21ae1d13de9cf
URL:		http://kling.mine.nu/sambasentinel.htm
BuildRequires:	gtk+-devel
Requires:	samba
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SambaSentinel is basically a gtk-frontend to smbstatus but it extends
it with number of useful features such as:
- Kill a specific samba-process with a simple mouse-click.
- Multi-threaded (one thread for gui and one for running
  smbstatus/updating).
- See which files a specific user is accessing.
- Mount and browse a visiting computer (with jags).

%description -l pl.UTF-8
SambaSentinel to zasadniczo interfejs GTK+ do smbstatus, ale
rozszerzający go o wiele użytecznych możliwości, takich jak:
- Zabijanie procesów samby prostym kliknięciem myszki.
- Wielowątkowość (jeden wątek dla interfejsu graficznego, jeden dla
  uruchomiania smbstatus/uaktualniania).
- Podgląd z których plików korzystają poszczególni użytkownicy.
- Montowanie i przeglądanie komputerów (z użyciem jags).

%prep
%setup -q -n SambaSentinel

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D SambaSentinel $RPM_BUILD_ROOT%{_bindir}/SambaSentinel

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%attr(755,root,root) %{_bindir}/*
