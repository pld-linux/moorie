# TODO
# - still -O3 slips in
%define		subver	20100203
%define		rel		0.1
Summary:	HashCode Downloader
Summary(pl.UTF-8):	 Moorie to natywny klient sieci p2m Moorhunt.
Name:		moorie
Version:	0.1
Release:	0.%{subver}.%{rel}
License:	GNU GPL v3
Group:		Applications
Source0:	http://ppa.launchpad.net/moorie/ppa/ubuntu/pool/main/m/moorie/%{name}_git%{subver}-1.tar.gz
# Source0-md5:	f23ec2b6afcd52f57bd1cb14c5fbdee1
URL:		http://www.moorie.pl/
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	libmcrypt-devel
BuildRequires:	mhash-devel
BuildRequires:	openssl-devel
BuildRequires:	qt4-build
# src/libmoor/libmoorhunt.a contains ELF 32 object
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Moorie is a Moorhunt-compatible, lightweight file-sharing client for
Linux.

%prep
%setup -q -n %{name}-gir%{subver}

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DCMAKE_C_FLAGS="%{rpmcflags}" \
	-DCMAKE_LD_FLAGS="%{rpmldflags}" \
	-DCMAKE_CXX_FLAGS="%{rpmcxxflags}"  \
	-DCMAKE_SKIP_RPATH=ON \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DENABLE_GUI=ON \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/qmoorie.svgz
rm -f $RPM_BUILD_ROOT%{_datadir}/menu/qmoorie.menu

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/moorie
%attr(755,root,root) %{_bindir}/qmoorie
%attr(755,root,root) %{_libdir}/libmoor.so
%{_desktopdir}/qmoorie.desktop
%{_iconsdir}/hicolor/*/apps/qmoorie.png
%{_pixmapsdir}/qmoorie.xpm
