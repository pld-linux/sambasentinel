Summary:	SambaSentinel is basically a gtk-frontend to smbstatus
Summary(pl):	SambaSentinel to prosty interface do smbstatus
Name:		sambasentinel
Version:	0.1
Release:	1
License:	GPL v2
Group:		Networking/Tool
######		Unknown group!
######		Unknown group!
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

%description -l pl
SambaSentinel to prosty interface do smbstatus, ale rozszerzaj±cy go
kilkoma urzytecznymi dodatkami, takimi jak:
- Zabijanie procesów samby prostym klikniêciem myszki.
- Wielow±tkowo¶æ (jeden w±tek dla interfacu graficznego o jeden dla
  uruchomionych smbstatus/updating).
- Podgl±d z których plików korzystaj± poszczególni u¿ytkownicy.
- Montowanie i przegl±danie komputerów (z wyk. jags)

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
