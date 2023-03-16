#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : can-utils
Version  : 2023.03
Release  : 7
URL      : https://github.com/linux-can/can-utils/archive/v2023.03/can-utils-2023.03.tar.gz
Source0  : https://github.com/linux-can/can-utils/archive/v2023.03/can-utils-2023.03.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: can-utils-bin = %{version}-%{release}
Requires: can-utils-license = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<p align="center">
<img src="https://github.com/linux-can/can-logos/raw/master/png/SocketCAN-logo-60dpi.png" alt="SocketCAN logo"/>
</p>

%package bin
Summary: bin components for the can-utils package.
Group: Binaries
Requires: can-utils-license = %{version}-%{release}

%description bin
bin components for the can-utils package.


%package license
Summary: license components for the can-utils package.
Group: Default

%description license
license components for the can-utils package.


%prep
%setup -q -n can-utils-2023.03
cd %{_builddir}/can-utils-2023.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1678975101
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1678975101
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/can-utils
cp %{_builddir}/can-utils-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/can-utils/9a2473b1af68a99d91b786625fcf075c2b24c35f || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/asc2log
/usr/bin/bcmserver
/usr/bin/can-calc-bit-timing
/usr/bin/canbusload
/usr/bin/candump
/usr/bin/canfdtest
/usr/bin/cangen
/usr/bin/cangw
/usr/bin/canlogserver
/usr/bin/canplayer
/usr/bin/cansend
/usr/bin/cansequence
/usr/bin/cansniffer
/usr/bin/isotpdump
/usr/bin/isotpperf
/usr/bin/isotprecv
/usr/bin/isotpsend
/usr/bin/isotpserver
/usr/bin/isotpsniffer
/usr/bin/isotptun
/usr/bin/j1939acd
/usr/bin/j1939cat
/usr/bin/j1939spy
/usr/bin/j1939sr
/usr/bin/log2asc
/usr/bin/log2long
/usr/bin/mcp251xfd-dump
/usr/bin/slcan_attach
/usr/bin/slcand
/usr/bin/slcanpty
/usr/bin/testj1939

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/can-utils/9a2473b1af68a99d91b786625fcf075c2b24c35f
